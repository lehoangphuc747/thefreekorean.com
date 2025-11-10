const fs = require('fs');
const path = require('path');

try {
  const filePath = './src/content/topik/on-luyen/on-luyen-001/reading-dang-1-고객센터.json';
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  
  let count = 0;
  const grammars = [];
  const issues = [];
  
  // Kiểm tra cấu trúc
  if (!data.categories) {
    issues.push('❌ Thiếu trường "categories"');
  } else {
    data.categories.forEach((cat, catIdx) => {
      if (!cat.functionalGroups) {
        issues.push(`❌ Category ${catIdx + 1} thiếu "functionalGroups"`);
      } else {
        cat.functionalGroups.forEach((group, groupIdx) => {
          if (!group.sections) {
            issues.push(`❌ Group ${groupIdx + 1} trong category ${catIdx + 1} thiếu "sections"`);
          } else {
            group.sections.forEach((section, secIdx) => {
              count++;
              grammars.push({
                title: section.title,
                note: section.note,
                itemCount: section.items ? section.items.length : 0,
                category: cat.categoryTitle,
                group: group.groupTitle
              });
              
              // Kiểm tra mỗi section có items không
              if (!section.items || section.items.length === 0) {
                issues.push(`⚠️  Section "${section.title}" không có items`);
              } else if (section.items.length !== 5) {
                issues.push(`⚠️  Section "${section.title}" có ${section.items.length} items (nên có 5)`);
              }
              
              // Kiểm tra mỗi item có prompt và answer không
              section.items?.forEach((item, itemIdx) => {
                if (!item.prompt) {
                  issues.push(`❌ Section "${section.title}", item ${itemIdx + 1} thiếu "prompt"`);
                }
                if (!item.answer) {
                  issues.push(`❌ Section "${section.title}", item ${itemIdx + 1} thiếu "answer"`);
                }
              });
            });
          }
        });
      }
    });
  }
  
  console.log('═══════════════════════════════════════════════════════');
  console.log('📊 KẾT QUẢ KIỂM TRA JSON');
  console.log('═══════════════════════════════════════════════════════\n');
  
  console.log(`✅ Tổng số ngữ pháp: ${count}`);
  console.log(`📝 Mong đợi: 30 ngữ pháp\n`);
  
  if (count === 30) {
    console.log('✅ Đủ 30 ngữ pháp!\n');
  } else {
    console.log(`⚠️  Thiếu ${30 - count} ngữ pháp\n`);
  }
  
  console.log('═══════════════════════════════════════════════════════');
  console.log('📋 DANH SÁCH NGỮ PHÁP THEO NHÓM');
  console.log('═══════════════════════════════════════════════════════\n');
  
  let currentCategory = '';
  let currentGroup = '';
  let grammarNum = 1;
  
  grammars.forEach(grammar => {
    if (grammar.category !== currentCategory) {
      currentCategory = grammar.category;
      console.log(`\n📁 ${currentCategory}`);
    }
    if (grammar.group !== currentGroup) {
      currentGroup = grammar.group;
      console.log(`\n  🔹 ${currentGroup}`);
    }
    console.log(`    ${grammarNum}. ${grammar.title} (${grammar.note}) - ${grammar.itemCount} items`);
    grammarNum++;
  });
  
  console.log('\n═══════════════════════════════════════════════════════');
  console.log('🔍 PHÁT HIỆN VẤN ĐỀ');
  console.log('═══════════════════════════════════════════════════════\n');
  
  if (issues.length === 0) {
    console.log('✅ Không có vấn đề nào được phát hiện!');
  } else {
    issues.forEach(issue => console.log(issue));
  }
  
  console.log('\n═══════════════════════════════════════════════════════');
  console.log(`✅ Cú pháp JSON: Hợp lệ`);
  console.log(`✅ Cấu trúc dữ liệu: ${issues.length === 0 ? 'Hợp lệ' : 'Có vấn đề'}`);
  console.log('═══════════════════════════════════════════════════════\n');
  
} catch (error) {
  console.error('❌ Lỗi:', error.message);
  process.exit(1);
}

