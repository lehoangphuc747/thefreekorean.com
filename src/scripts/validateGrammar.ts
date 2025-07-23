import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

interface GrammarFrontmatter {
  title?: string;
  date?: string;
  category?: string;
  subcategory?: string;
  type?: string;
  level?: string;
  grammarPattern?: string;
  meaning?: string;
  cover?: string;
  description?: string;
  tags?: string[];
  examples?: number;
  exercises?: number;
  difficulty?: string;
  estimatedTime?: string;
  relatedGrammar?: string[];
  prerequisites?: string[];
}

interface ValidationResult {
  filePath: string;
  isValid: boolean;
  errors: string[];
  warnings: string[];
  frontmatter: GrammarFrontmatter;
  stats: {
    wordCount: number;
    hasExamples: boolean;
    hasExercises: boolean;
    hasPronunciation: boolean;
  };
}

interface ValidationSummary {
  totalFiles: number;
  validFiles: number;
  invalidFiles: number;
  totalErrors: number;
  totalWarnings: number;
  results: ValidationResult[];
}

class GrammarValidator {
  private grammarDir: string;
  private requiredFields: (keyof GrammarFrontmatter)[] = [
    'title',
    'date', 
    'category',
    'type',
    'level',
    'grammarPattern',
    'meaning',
    'description',
  ];
  
  private optionalFields: (keyof GrammarFrontmatter)[] = [
    'subcategory',
    'cover',
    'tags',
    'examples',
    'exercises',
    'difficulty',
    'estimatedTime',
    'relatedGrammar',
    'prerequisites',
  ];

  constructor() {
    // Use process.cwd() to get current working directory
    this.grammarDir = path.join(process.cwd(), 'src', 'documents', 'grammar');
  }

  async validateAllGrammarFiles(): Promise<ValidationSummary> {
    console.log(`📁 Checking grammar directory: ${this.grammarDir}`);
    
    if (!fs.existsSync(this.grammarDir)) {
      console.error(`❌ Grammar directory not found: ${this.grammarDir}`);
      return {
        totalFiles: 0,
        validFiles: 0,
        invalidFiles: 0,
        totalErrors: 1,
        totalWarnings: 0,
        results: []
      };
    }

    const files = fs.readdirSync(this.grammarDir)
      .filter(file => file.endsWith('.mdx'))
      .map(file => path.join(this.grammarDir, file));

    console.log(`📄 Found ${files.length} MDX files`);
    files.forEach(file => console.log(`  - ${path.basename(file)}`));

    const results: ValidationResult[] = [];
    
    for (const filePath of files) {
      const result = await this.validateGrammarFile(filePath);
      results.push(result);
    }

    const summary: ValidationSummary = {
      totalFiles: results.length,
      validFiles: results.filter(r => r.isValid).length,
      invalidFiles: results.filter(r => !r.isValid).length,
      totalErrors: results.reduce((sum, r) => sum + r.errors.length, 0),
      totalWarnings: results.reduce((sum, r) => sum + r.warnings.length, 0),
      results
    };

    return summary;
  }

  async validateGrammarFile(filePath: string): Promise<ValidationResult> {
    const content = fs.readFileSync(filePath, 'utf-8');
    const fileName = path.basename(filePath);
    
    const result: ValidationResult = {
      filePath,
      isValid: true,
      errors: [],
      warnings: [],
      frontmatter: {},
      stats: {
        wordCount: 0,
        hasExamples: false,
        hasExercises: false,
        hasPronunciation: false,
      }
    };

    try {
      // Extract frontmatter - handle Windows line endings
      const frontmatterMatch = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
      if (!frontmatterMatch) {
        result.errors.push('No frontmatter found');
        result.isValid = false;
        return result;
      }

      // Parse frontmatter (simple YAML parsing)
      const frontmatterText = frontmatterMatch[1];
      const frontmatter = this.parseFrontmatter(frontmatterText);
      result.frontmatter = frontmatter;

      // Validate required fields
      for (const field of this.requiredFields) {
        if (!frontmatter[field]) {
          result.errors.push(`Missing required field: ${field}`);
          result.isValid = false;
        }
      }

      // Validate field types and values
      if (frontmatter.level && !['Beginner', 'Intermediate', 'Advanced'].includes(frontmatter.level)) {
        result.errors.push(`Invalid level: ${frontmatter.level}. Must be Beginner, Intermediate, or Advanced`);
        result.isValid = false;
      }

      if (frontmatter.type && !['Grammar'].includes(frontmatter.type)) {
        result.warnings.push(`Unusual type: ${frontmatter.type}. Expected: Grammar`);
      }

      if (frontmatter.examples && typeof frontmatter.examples !== 'number') {
        result.errors.push('examples field must be a number');
        result.isValid = false;
      }

      if (frontmatter.exercises && typeof frontmatter.exercises !== 'number') {
        result.errors.push('exercises field must be a number');
        result.isValid = false;
      }

      // Validate content structure
      const bodyContent = content.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, '');
      this.validateContentStructure(bodyContent, result);

      // Calculate statistics
      result.stats.wordCount = this.countWords(bodyContent);
      result.stats.hasExamples = /ExampleSection|examples=\{/.test(content);
      result.stats.hasExercises = /PracticeSection|exercises=\{/.test(content);
      result.stats.hasPronunciation = /PronunciationGuide/.test(content);

      // Quality warnings
      if (result.stats.wordCount < 500) {
        result.warnings.push('Content seems too short (< 500 words)');
      }

      if (!result.stats.hasExamples) {
        result.warnings.push('No ExampleSection component found');
      }

      if (!result.stats.hasExercises) {
        result.warnings.push('No PracticeSection component found');
      }

      if (!result.stats.hasPronunciation) {
        result.warnings.push('No PronunciationGuide component found');
      }

    } catch (error) {
      result.errors.push(`Parsing error: ${error.message}`);
      result.isValid = false;
    }

    return result;
  }

  private parseFrontmatter(frontmatterText: string): GrammarFrontmatter {
    const frontmatter: GrammarFrontmatter = {};
    const lines = frontmatterText.split(/\r?\n/);

    for (const line of lines) {
      const trimmedLine = line.trim();
      if (!trimmedLine || trimmedLine.startsWith('#')) continue;
      
      const colonIndex = trimmedLine.indexOf(':');
      if (colonIndex === -1) continue;
      
      const key = trimmedLine.substring(0, colonIndex).trim();
      const value = trimmedLine.substring(colonIndex + 1).trim();
      
      if (!value) continue;
      
      // Handle different value types
      if (value.startsWith('[') && value.endsWith(']')) {
        // Array
        const arrayContent = value.slice(1, -1).trim();
        if (arrayContent) {
          frontmatter[key] = arrayContent.split(',').map(s => s.trim().replace(/^["']|["']$/g, ''));
        } else {
          frontmatter[key] = [];
        }
      } else if (value === 'true' || value === 'false') {
        // Boolean
        frontmatter[key] = value === 'true';
      } else if (/^\d+$/.test(value)) {
        // Number
        frontmatter[key] = parseInt(value, 10);
      } else {
        // String (remove quotes)
        frontmatter[key] = value.replace(/^["']|["']$/g, '');
      }
    }

    return frontmatter;
  }

  private validateContentStructure(content: string, result: ValidationResult): void {
    // Check for required sections
    const requiredSections = [
      '## 📝 Ý nghĩa',
      '## 📚 Cấu trúc ngữ pháp',
    ];

    for (const section of requiredSections) {
      if (!content.includes(section)) {
        result.warnings.push(`Missing recommended section: ${section}`);
      }
    }

    // Check for import statements
    const requiredImports = [
      'ExampleSection',
      'PracticeSection', 
      'PronunciationGuide'
    ];

    for (const importName of requiredImports) {
      if (!content.includes(importName)) {
        result.warnings.push(`Missing import: ${importName}`);
      }
    }

    // Check for MDX syntax errors (basic)
    const mdxComponents = content.match(/<\w+[^>]*>/g) || [];
    for (const component of mdxComponents) {
      if (!component.includes('/>') && !content.includes(component.replace('<', '</'))) {
        result.warnings.push(`Potentially unclosed component: ${component}`);
      }
    }
  }

  private countWords(content: string): number {
    // Remove MDX components and count Korean/Vietnamese/English words
    const cleanContent = content
      .replace(/<[^>]*>/g, '') // Remove HTML/MDX tags
      .replace(/```[\s\S]*?```/g, '') // Remove code blocks
      .replace(/`[^`]*`/g, '') // Remove inline code
      .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1'); // Replace links with text

    const words = cleanContent
      .split(/\s+/)
      .filter(word => word.length > 0 && !/^[^\w가-힣À-ỹ]/.test(word));

    return words.length;
  }

  generateReport(summary: ValidationSummary): string {
    let report = '# Grammar Content Validation Report\n\n';
    
    report += `## Summary\n`;
    report += `- **Total Files**: ${summary.totalFiles}\n`;
    report += `- **Valid Files**: ${summary.validFiles} (${Math.round((summary.validFiles / summary.totalFiles) * 100)}%)\n`;
    report += `- **Invalid Files**: ${summary.invalidFiles}\n`;
    report += `- **Total Errors**: ${summary.totalErrors}\n`;
    report += `- **Total Warnings**: ${summary.totalWarnings}\n\n`;

    if (summary.invalidFiles > 0) {
      report += `## Files with Errors\n\n`;
      for (const result of summary.results.filter(r => !r.isValid)) {
        report += `### ${path.basename(result.filePath)}\n`;
        for (const error of result.errors) {
          report += `- ❌ ${error}\n`;
        }
        report += '\n';
      }
    }

    if (summary.totalWarnings > 0) {
      report += `## Files with Warnings\n\n`;
      for (const result of summary.results.filter(r => r.warnings.length > 0)) {
        report += `### ${path.basename(result.filePath)}\n`;
        for (const warning of result.warnings) {
          report += `- ⚠️ ${warning}\n`;
        }
        report += '\n';
      }
    }

    report += `## Statistics\n\n`;
    report += `| File | Words | Examples | Exercises | Pronunciation |\n`;
    report += `|------|-------|----------|-----------|---------------|\n`;
    
    for (const result of summary.results) {
      const fileName = path.basename(result.filePath);
      const { stats } = result;
      report += `| ${fileName} | ${stats.wordCount} | ${stats.hasExamples ? '✅' : '❌'} | ${stats.hasExercises ? '✅' : '❌'} | ${stats.hasPronunciation ? '✅' : '❌'} |\n`;
    }

    return report;
  }

  async run(): Promise<void> {
    console.log('🔍 Starting grammar content validation...\n');
    
    const summary = await this.validateAllGrammarFiles();
    const report = this.generateReport(summary);
    
    // Write report to file
    const reportPath = path.join(process.cwd(), 'grammar-validation-report.md');
    fs.writeFileSync(reportPath, report);
    
    console.log(`📊 Validation complete!`);
    console.log(`📄 Report saved to: ${reportPath}`);
    console.log(`✅ Valid files: ${summary.validFiles}/${summary.totalFiles}`);
    
    if (summary.invalidFiles > 0) {
      console.log(`❌ Invalid files: ${summary.invalidFiles}`);
      console.log(`🔧 Please check the report for details.`);
      process.exit(1);
    }
    
    if (summary.totalWarnings > 0) {
      console.log(`⚠️ Warnings: ${summary.totalWarnings}`);
      console.log(`💡 Consider addressing warnings for better quality.`);
    }
  }
}

// Export for use as module
export { GrammarValidator };

// Run if executed directly
if (process.argv[1].includes('validateGrammar')) {
  const validator = new GrammarValidator();
  validator.run().catch(console.error);
}
