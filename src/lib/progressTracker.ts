/**
 * Progress Tracking Utility
 * 
 * Quản lý tiến trình làm bài TOPIK:
 * - Lưu đáp án đã chọn
 * - Kiểm tra đúng/sai
 * - Tính toán thống kê
 * - Lưu vào server (nếu đã đăng nhập) và localStorage (backup)
 */

export interface QuestionProgress {
  selectedAnswer: number;
  isCorrect: boolean;
  timestamp: number;
}

export interface ExerciseProgress {
  [questionId: string]: QuestionProgress;
}

export interface ProgressStats {
  totalQuestions: number;
  answered: number;
  correct: number;
  wrong: number;
  accuracy: number;
}

class ProgressTracker {
  private exerciseSlug: string;
  private progress: ExerciseProgress = {};
  private isLoggedIn: boolean = false;

  constructor(exerciseSlug: string) {
    this.exerciseSlug = exerciseSlug;
    this.loadFromLocalStorage();
  }

  /**
   * Khởi tạo - kiểm tra đăng nhập và tải progress
   */
  async init(): Promise<void> {
    // Kiểm tra đăng nhập bằng Firebase Auth
    try {
      const { getAuth } = await import("firebase/auth");
      const auth = getAuth();
      this.isLoggedIn = !!auth.currentUser;
    } catch {
      this.isLoggedIn = false;
    }

    // Nếu đã đăng nhập, tải progress từ server
    if (this.isLoggedIn) {
      await this.loadFromServer();
    }
  }

  /**
   * Lưu progress vào localStorage
   */
  private saveToLocalStorage(): void {
    try {
      const key = `topik_progress_${this.exerciseSlug}`;
      localStorage.setItem(key, JSON.stringify(this.progress));
    } catch (error) {
      console.error("Error saving to localStorage:", error);
    }
  }

  /**
   * Tải progress từ localStorage
   */
  private loadFromLocalStorage(): void {
    try {
      const key = `topik_progress_${this.exerciseSlug}`;
      const data = localStorage.getItem(key);
      if (data) {
        this.progress = JSON.parse(data);
      }
    } catch (error) {
      console.error("Error loading from localStorage:", error);
    }
  }

  /**
   * Tải progress từ server
   */
  private async loadFromServer(): Promise<void> {
    try {
      const response = await fetch(`/api/progress/load?slug=${this.exerciseSlug}`);
      if (response.ok) {
        const data = await response.json();
        if (data.progress) {
          // Merge server progress với local progress (server priority)
          this.progress = { ...this.progress, ...data.progress };
        }
      }
    } catch (error) {
      console.error("Error loading from server:", error);
    }
  }

  /**
   * Lưu progress lên server
   */
  private async saveToServer(questionId: number, selectedAnswer: number, isCorrect: boolean): Promise<void> {
    if (!this.isLoggedIn) return;

    try {
      await fetch("/api/progress/save", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          exerciseSlug: this.exerciseSlug,
          questionId,
          selectedAnswer,
          isCorrect,
        }),
      });
    } catch (error) {
      console.error("Error saving to server:", error);
    }
  }

  /**
   * Lưu đáp án đã chọn
   */
  async saveAnswer(questionId: number, selectedAnswer: number, correctAnswer: number): Promise<void> {
    const isCorrect = selectedAnswer === correctAnswer;
    
    this.progress[questionId] = {
      selectedAnswer,
      isCorrect,
      timestamp: Date.now(),
    };

    // Lưu vào localStorage
    this.saveToLocalStorage();

    // Lưu lên server (nếu đã đăng nhập)
    await this.saveToServer(questionId, selectedAnswer, isCorrect);
  }

  /**
   * Lấy tiến trình của một câu hỏi
   */
  getQuestionProgress(questionId: number): QuestionProgress | null {
    return this.progress[questionId] || null;
  }

  /**
   * Lấy tất cả tiến trình
   */
  getAllProgress(): ExerciseProgress {
    return { ...this.progress };
  }

  /**
   * Tính toán thống kê
   */
  getStats(totalQuestions: number): ProgressStats {
    const answered = Object.keys(this.progress).length;
    const correct = Object.values(this.progress).filter(p => p.isCorrect).length;
    const wrong = answered - correct;
    const accuracy = answered > 0 ? Math.round((correct / answered) * 100) : 0;

    return {
      totalQuestions,
      answered,
      correct,
      wrong,
      accuracy,
    };
  }

  /**
   * Xóa tất cả tiến trình
   */
  clearProgress(): void {
    this.progress = {};
    this.saveToLocalStorage();
  }

  /**
   * Lấy danh sách câu trả lời sai
   */
  getWrongQuestions(): number[] {
    return Object.entries(this.progress)
      .filter(([_, p]) => !p.isCorrect)
      .map(([id]) => parseInt(id));
  }

  /**
   * Lấy danh sách câu đã bookmark (localStorage)
   */
  getBookmarks(): number[] {
    try {
      const key = `topik_bookmarks_${this.exerciseSlug}`;
      const data = localStorage.getItem(key);
      return data ? JSON.parse(data) : [];
    } catch {
      return [];
    }
  }

  /**
   * Toggle bookmark
   */
  toggleBookmark(questionId: number): boolean {
    const bookmarks = this.getBookmarks();
    const index = bookmarks.indexOf(questionId);
    
    if (index === -1) {
      bookmarks.push(questionId);
    } else {
      bookmarks.splice(index, 1);
    }

    try {
      const key = `topik_bookmarks_${this.exerciseSlug}`;
      localStorage.setItem(key, JSON.stringify(bookmarks));
    } catch (error) {
      console.error("Error saving bookmark:", error);
    }

    return index === -1; // Trả về true nếu đã bookmark
  }
}

export default ProgressTracker;
