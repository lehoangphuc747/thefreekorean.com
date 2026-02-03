---
name: Korean Vocabulary Builder
description: Create and format Korean vocabulary documentation with etymology analysis, grammatical structure breakdowns, and bilingual explanations. Use when (1) Creating Korean vocabulary files or lessons, (2) Explaining Korean word etymology (Sino-Korean/loanwords/native Korean), (3) Breaking down grammatical expressions and usage patterns, (4) Formatting Korean-Vietnamese vocabulary tables, (5) User mentions 'từ vựng', 'vocabulary', 'Korean words', 'bài học', 'lesson', or needs help with Korean language documentation.
---

# Korean Vocabulary Builder Skill

Kỹ năng chuyên biệt để tạo file từ vựng tiếng Hàn có cấu trúc rõ ràng, giải thích chi tiết nguồn gốc từ, và các biểu hiện thường dùng.

## Nguyên Tắc Cốt Lõi (Core Principles)

### ⚠️ QUY TẮC TUYỆT ĐỐI #1: Phân Biệt Từ Gốc vs Biểu Hiện

**KHÔNG BAO GIỜ nhầm lẫn 2 format:**

1. **Từ Gốc** (phân tích từ nguyên) → Phân tích **TỪ NGUYÊN**
   - Hán Việt: `**도착**: Đáo trước.<br>**도 (Đáo)**: đến<br>**착 (Trước)**: dính vào/tới nơi<br>→ Nghĩa: Đến nơi, tới đích.<br><br>Cấu trúc thường gặp: **Địa điểm N에 도착하다** → Đến địa điểm N`
   - Từ mượn: `Từ mượn tiếng Anh "bus".`
   - Thuần Hàn: `Động từ thuần Hàn.<br><br>Cấu trúc thường gặp: **N을/를 타다** → Đi bằng phương tiện N`

2. **Biểu Hiện** (phân tích cấu trúc) → Phân tích **CẤU TRÚC (3 BƯỚC)**
   - Format: `**출발하다**: xuất phát<br><br>Cấu trúc: **N에서 출발하다**.<br>Cấu trúc này có nghĩa là: **Xuất phát từ địa điểm N.**<br><br>Trong câu **집에서 출발하다** có nghĩa là: **Xuất phát từ nhà.**`

### 🚫 QUY TẮC TUYỆT ĐỐI (Absolute Rules)

1. **KHÔNG BAO GIỜ dùng phiên âm Latinh** trong cột Giải thích
   - ❌ SAI: "Orae (오래)", "Gil (길)", "Xa (차)"
   - ✅ ĐÚNG: "**오래**: lâu", "**길**: đường", "**차**: xe"

2. **KHÔNG IN ĐẬM** trong các cột "Tiếng Hàn", "Phiên âm", "Tiếng Việt".
   - Chỉ in đậm trong cột "Giải thích" để nhấn mạnh các thành phần quan trọng.

3. **MỖI TỪ LÀ MỘT CÁ THỂ ĐỘC LẬP**
   - Người học phải hiểu được từ chỉ bằng cách đọc hàng đó
   - Không được giả định họ đã đọc hàng trước
   - Phải nhắc lại nghĩa của từng thành phần ngay cả khi đã giải thích ở trên

4. **KHÔNG dùng công thức ngữ pháp khô khan**
   - ❌ SAI: "Noun + 에서 + 내리다"
   - ✅ ĐÚNG: "Cấu trúc: **N에서 내리다**.<br>Cấu trúc này có nghĩa là: **Xuống từ phương tiện (giao thông) N.**"

## Cấu Trúc File Từ Vựng (Vocabulary File Structure)

### Bảng Từ Vựng Chuẩn

```markdown
| Tiếng Hàn | Phiên âm | Tiếng Việt | Loại từ | Giải thích | Ví dụ | Nghĩa ví dụ | Collocation | Synonym | Antonym |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
```

**Các cột:**
- **Tiếng Hàn**: Từ gốc hoặc biểu hiện (KHÔNG in đậm)
- **Phiên âm**: 
  - Âm Hán Việt (nếu là từ Hán Việt)
  - Gốc tiếng Anh/Pháp (nếu là từ mượn)
  - Để trống (nếu là từ thuần Hàn)
  - KHÔNG in đậm
- **Tiếng Việt**: Nghĩa tiếng Việt (KHÔNG in đậm)
- **Giải thích**: Phân tích chi tiết (xem phần dưới) - CHỈ cột này mới có in đậm

## Cách Viết Giải Thích (Explanation Guidelines)

### ⚠️ PHÂN BIỆT RÕ 2 LOẠI

**QUY TẮC TUYỆT ĐỐI:**
- **Từ Gốc** → Phân tích **TỪ NGUYÊN** (từng chữ Hán, nguồn gốc)
- **Biểu Hiện** → Phân tích **CẤU TRÚC (3 BƯỚC)** (cách dùng, ngữ pháp)
- **KHÔNG BAO GIỜ** dùng format phân tích cấu trúc cho từ gốc
- **KHÔNG BAO GIỜ** dùng format phân tích từ nguyên cho biểu hiện

---

### A. Từ Gốc - Phân Tích Từ Nguyên

#### 1. Từ Hán Việt (Sino-Korean Words)

**Format:**
```
**[Từ]**: [Hán Việt].
**[Chữ 1] ([Hán 1])**: [giải thích nghĩa]
**[Chữ 2] ([Hán 2])**: [giải thích nghĩa]
→ Nghĩa: [tổng hợp]
<br><br>
Cấu trúc thường gặp: [nếu có]
```

**Ví dụ:**
```markdown
|到着하다 | đáo trước | đến nơi | Động từ | **도착**: Đáo trước.<br>**도 (Đáo)**: đến<br>**착 (Trước)**: dính vào/tới nơi<br>→ Nghĩa: Đến nơi, tới đích.<br><br>Cấu trúc thường gặp: **Địa điểm N에 도착하다**<br>→ Đến địa điểm N |
```

**Ví dụ có nhiều cấu trúc:**
```markdown
| 출발하다 | xuất phát | xuất phát | Động từ | **출발**: Xuất phát.<br>**출 (Xuất)**: ra khỏi<br>**발 (Phát)**: rời đi<br>→ Nghĩa: Bắt đầu đi, rời khỏi điểm xuất phát.<br><br>Cấu trúc thường gặp:<br> 1. **Địa điểm N에서 출발하다** → Xuất phát từ N<br>2. **Địa điểm N(으)로 출발하다** → Xuất phát hướng về N |
```

#### 2. Từ Mượn (Loanwords)

**Format:**
```
Từ mượn tiếng [Anh/Pháp/Việt] "[gốc]".
```

**Ví dụ:**
```markdown
| 버스 | bus | xe buýt | Danh từ | Từ mượn tiếng Anh "bus". |
```

#### 3. Từ Thuần Hàn (Pure Korean Words)

**Format:**
```
Động từ thuần Hàn.<br><br>Cấu trúc thường gặp: **[Cấu trúc]**<br>→ [Nghĩa]
```

**Ví dụ:**
```markdown
| 타다 | | lên, đi (phương tiện giao thông) | Động từ | Động từ thuần Hàn.<br><br>Cấu trúc thường gặp: **Phương tiện N을/를 타다**<br>→ Đi bằng phương tiện N |
```

#### 4. Động Từ Ghép (Compound Verbs)

**Format:**
```
**[Phần 1]**: nghĩa + **[Phần 2]**: nghĩa
→ Nghĩa: [tổng hợp]
```

**Ví dụ:**
```markdown
| 갈아타다 | | đổi (phương tiện giao thông) | Động từ | **갈아**: thay/đổi + **타다**: đi xe.<br>→ Nghĩa: Chuyển từ xe này sang xe khác.<br><br>Cấu trúc thường gặp: **Phương tiện N(으)로 갈아타다**<br>→ Chuyển sang phương tiện N |
```

### B. Biểu Hiện - Phân Tích Cấu Trúc (3 BƯỚC)

**⚠️ Lưu ý:** Chỉ dùng format này khi là **BIỂU HIỆN** (cụm từ/cấu trúc), không phải từ gốc.

**Format bắt buộc (Nguyên tắc 3 bước):**
1. **Động từ chính**: `**[Động từ]**: [nghĩa]`
2. **Phân tích cấu trúc**: `Cấu trúc: **[Cấu trúc]**.<br>Cấu trúc này có nghĩa là: **[Giải thích nghĩa cấu trúc]**.`
3. **Ý nghĩa trong ví dụ**: `Trong câu **[Biểu hiện cụ thể]** có nghĩa là: **[Nghĩa trong câu đó]**.`

**Phân tách:** Dùng `<br><br>` sau bước 1 và bên bước 3 (trước "Trong câu").

**Ví dụ:**
```markdown
| 버스를 타다 | | đi xe buýt | Danh từ + Động từ | **타다**: lên, đi (phương tiện giao thông)<br><br>Cấu trúc: **N을/를 타다**.<br>Cấu trúc này có nghĩa là: **Đi bằng phương tiện (giao thông) N.**<br><br>Trong câu **버스를 타다** có nghĩa là: **Đi bằng xe buýt.** |
```

**Nguyên tắc:**
1. **In đậm** phần "**[Động từ]: nghĩa**" ở đầu.
2. **In đậm** phần cấu trúc: "**N... [Động từ]**".
3. **In đậm** phần nghĩa trong các câu giải thích.
4. KHÔNG in đậm cột "Tiếng Hàn".

---

## Phân Biệt Từ Đồng Nghĩa (Differentiating Similar Words)

Khi có từ có nghĩa tiếng Việt giống/gần nhau, **BẮT BUỘC** phải có phần **"Phân biệt:"**

**Format:**
```
**[Từ]**: [Nghĩa chính]
**Phân biệt:** Dùng cho [bối cảnh cụ thể]
```

**Ví dụ: 사용하다 vs 이용하다**

| Từ | Nghĩa | Phân biệt | Ví dụ |
|----|-------|-----------|-------|
| 사용하다 | sử dụng | **Đồ vật hữu hình** (cầm/chạm vào) | 컴퓨터를 사용하다, 휴대폰을 사용하다 |
| 이용하다 | sử dụng | **Dịch vụ/hệ thống** | 버스를 이용하다, 도서관을 이용하다 |

---

## Quy Trình Tạo File Từ Vựng (Workflow)

### Bước 1: Phân Loại Từ Vựng

Nhóm từ vựng theo chủ đề logic:
- Danh từ (xe cộ, địa điểm, đồ vật...)
- Động từ & Tính từ
- Từ nghi vấn
- Từ vựng mở rộng

### Bước 2: Sắp Xếp Thứ Tự

### ⚠️ QUY TẮC TUYỆT ĐỐI #2: Nhóm Biểu Hiện Với Từ Gốc

**LUÔN LUÔN** đặt biểu hiện **NGAY SAU** từ gốc của nó:

✅ **ĐÚNG:**
```
넣다 (từ gốc)
가방에 넣다 (biểu hiện đơn giản)
가방에 휴대폰을 넣다 (biểu hiện cụ thể)
커피에 설탕을 넣다 (biểu hiện khác)
꺼내다 (từ gốc antonym)
가방에서 꺼내다
```

❌ **SAI:** Đặt tất cả biểu hiện ở cuối file

**Trong mỗi nhóm:**
- Từ gốc chính → Biểu hiện đơn giản → Biểu hiện phức tạp
- Nếu có antonym, đặt sau hết biểu hiện của từ đầu tiên
- Sắp theo **logic** (ví dụ: hành trình đi lại): xuất phát → lên xe → đổi xe → xuống xe → đến nơi

### Bước 3: Viết Giải Thích

**Checklist cho TỪ GỐC:**
- [ ] Đã phân tích **TỪ NGUYÊN** (từng chữ Hán, nguồn gốc)?
- [ ] Phân tích Hán Việt (nếu có)?
- [ ] Ghi nguồn gốc (nếu là từ mượn)?
- [ ] Dùng `<br>` để ngắt dòng?
- [ ] Có "→ Nghĩa: [tổng hợp]" ở cuối?
- [ ] KHÔNG có phiên âm Latinh?
- [ ] Cột "Tiếng Hàn", "Phiên âm", "Tiếng Việt" KHÔNG in đậm?
- [ ] 🔴 Nếu có từ đồng nghĩa, đã thêm phần "**Phân biệt:**"?
- [ ] 🔴 Cột "Tiếng Hàn" và "Ví dụ" KHÔNG chứa tiếng Việt?

**Checklist cho BIỂU HIỆN:**
- [ ] 🔴 Đã đặt **NGAY SAU** từ gốc (không đặt ở cuối file)?
- [ ] Đã phân tích **CẤU TRÚC (3 BƯỚC)**?
- [ ] Đã **in đậm** phần "**[Động từ]: nghĩa**" ở đầu?
- [ ] Có `<br><br>` sau phần động từ, sau cấu trúc, sau giải thích cấu trúc?
- [ ] Có "Cấu trúc: **N...**" rõ ràng?
- [ ] Có "Cấu trúc này có nghĩa là: **[...]**" và đã **in đậm** phần nghĩa?
- [ ] Có "Trong câu **[biểu hiện]** có nghĩa là: **[...]**" và đã **in đậm** phần nghĩa?
- [ ] Cột "Tiếng Hàn", "Phiên âm", "Tiếng Việt" KHÔNG in đậm?
- [ ] 🔴 Cột "Tiếng Hàn" và "Ví dụ" KHÔNG chứa tiếng Việt?

---

## Ví Dụ Hoàn Chỉnh (Complete Example)

```markdown
## 1. Phương tiện giao thông

| Tiếng Hàn | Phiên âm | Tiếng Việt | Loại từ | Giải thích | Ví dụ | Nghĩa ví dụ | Collocation | Synonym | Antonym |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 도착하다 | đáo trước | đến nơi | Động từ | **도착**: Đáo trước.<br>**도 (Đáo)**: đến<br>**착 (Trước)**: dính vào/tới nơi<br>→ Nghĩa: Đến nơi, tới đích.<br><br>Cấu trúc thường gặp: **Địa điểm N에 도착하다**<br>→ Đến địa điểm N | 비행기가 공항에 **도착했어요**. | Máy bay đã **đến** sân bay. | 정시에 도착하다 (đến đúng giờ) | | 출발하다 |
| 공항에 도착하다 | | đến sân bay | Danh từ + Động từ | **도착하다**: đến nơi<br><br>Cấu trúc: **N에 도착하다**.<br>Cấu trúc này có nghĩa là: **Đến địa điểm N.**<br><br>Trong câu **공항에 도착하다** có nghĩa là: **Đến sân bay.** | 2시에 **공항에 도착할** 거예요. | Tôi sẽ **đến sân bay** lúc 2 giờ. | | | |
| 타다 | | lên, đi (phương tiện giao thông) | Động từ | Động từ thuần Hàn.<br><br>Cấu trúc thường gặp: **Phương tiện N을/를 타다**<br>→ Đi bằng phương tiện N | 버스를 **타요**. | Tôi **lên** xe buýt. | | 승차하다 | 내리다 |
| 버스를 타다 | | đi xe buýt | Danh từ + Động từ | **타다**: lên, đi (phương tiện giao thông)<br><br>Cấu trúc: **N을/를 타다**.<br>Cấu trúc này có nghĩa là: **Đi bằng phương tiện (giao thông) N.**<br><br>Trong câu **버스를 타다** có nghĩa là: **Đi bằng xe buýt.** | 학교 갈 때 **버스를 타요**. | Khi đi học tôi **đi xe buýt**. | | | |
```

## Lỗi Thường Gặp & Cách Sửa (Common Mistakes)

| Lỗi | Sai | Đúng |
|-----|-----|------|
| Dùng Latinh | "Orae (오래): lâu" | "**오래**: lâu" |
| In đậm cột Tiếng Hàn/Tiếng Việt | \| **도착하다** \| đáo trước \| **đến nơi** \| | \| 도착하다 \| đáo trước \| đến nơi \| |
| In đậm dư thừa | "Cấu trúc: **N từ N**" | "Cấu trúc: **N에서**." |
| Thiếu 3 bước biểu hiện | Chỉ viết nghĩa cấu trúc | Phải đủ: Động từ -> Cấu trúc -> Ý nghĩa trong ví dụ |
| Thiếu `<br><br>` | "**타다**: lên<br>Cấu trúc: ..." | "**타다**: lên<br><br>Cấu trúc: ..." |

## Lỗi Nghiêm Trọng Cần Tránh (Critical Pitfalls)

### 1. Tiếng Việt Lẫn Vào Tiếng Hàn

| Lỗi | Sai | Đúng |
|-----|-----|------|
| Danh từ | `가방에 túi을 넣다` | `가방에 핸드폰을 넣다` |
| Động từ | `부모님은 con을 걱정하세요` | `부모님은 자식을 걱정하세요` |
| Ví dụ | `xe를 조심하세요` | `차를 조심하세요` |

**Nguyên nhân:** Copy/paste từ phần tiếng Việt mà không sửa lại

### 2. Biểu Hiện Đặt Sai Vị Trí

❌ Thêm tất cả biểu hiện mới xuống cuối file
✅ Ngay khi thêm biểu hiện, đặt LUÔN sau từ gốc

### 3. Từ Đồng Nghĩa Không Phân Biệt

❌ 사용하다 và 이용하다 đều dịch "sử dụng" nhưng không giải thích khác biệt
✅ Luôn thêm phần "**Phân biệt:**" khi có từ gần nghĩa

---

## Ghi Chú Bổ Sung

- Skill này sẽ được tối ưu dần theo phản hồi của người dùng
- Ưu tiên tính tự chứa đựng (self-contained) hơn là tính ngắn gọn
- Giải thích chi tiết > Giản lược
- 📁 Xem thêm: `examples/` folder để tham khảo mẫu thực tế
