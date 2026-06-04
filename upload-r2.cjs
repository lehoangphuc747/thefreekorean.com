const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const DIRECTORY = path.join(__dirname, 'public', 'downloads', 'topik');
const BUCKET_NAME = 'ankivn-media';
const R2_PREFIX = 'topik/';

// Function to recursively find all mp3 and pdf files
function findMediaFiles(dir, fileList = []) {
  if (!fs.existsSync(dir)) return fileList;
  
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const filePath = path.join(dir, file);
    if (fs.statSync(filePath).isDirectory()) {
      findMediaFiles(filePath, fileList);
    } else {
      if (filePath.endsWith('.mp3') || filePath.endsWith('.pdf')) {
        fileList.push(filePath);
      }
    }
  }
  return fileList;
}

const allFiles = findMediaFiles(DIRECTORY);
console.log(`Found ${allFiles.length} media files (.mp3, .pdf) to upload.`);

let successCount = 0;
let errorCount = 0;

for (let i = 0; i < allFiles.length; i++) {
  const filePath = allFiles[i];
  const fileName = path.basename(filePath);
  // Remove spaces and special chars in filename if needed, but keeping it as is for now
  // Key format: topik/filename.mp3
  const r2Key = `${R2_PREFIX}${fileName}`;
  
  console.log(`[${i + 1}/${allFiles.length}] Uploading ${fileName} to ${r2Key}...`);
  
  try {
    // We quote paths to handle spaces in folder names like "TOPIK I"
    const command = `npx wrangler r2 object put "${BUCKET_NAME}/${r2Key}" --file "${filePath}"`;
    execSync(command, { stdio: 'ignore' });
    successCount++;
  } catch (err) {
    console.error(`❌ Failed to upload ${fileName}`);
    errorCount++;
  }
}

console.log(`\n🎉 Upload Summary:`);
console.log(`Total: ${allFiles.length}`);
console.log(`Success: ${successCount}`);
console.log(`Errors: ${errorCount}`);
