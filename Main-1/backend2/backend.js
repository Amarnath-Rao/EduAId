const express = require('express');
const multer = require('multer');
const cors=require('cors')
const path = require('path');
const { spawn } = require('child_process');
const { error } = require('console');

const app = express();
const port = 3000;
app.use(cors())
// Set up storage using multer
const storage = multer.memoryStorage(); // Store the file data in memory
const upload = multer({ storage: storage });


app.post('/upload', upload.single('file'), (req, res) => {

  
  // Spawn a child process to call the Python script

  const path1= '../python2/keywords.py'
  const pythonScriptPath = path1;
  const pythonProcess = spawn('python', [pythonScriptPath]);
  // Send the file data to the Python script via stdin
  
  // Listen for data from the Python script
  let result = '';

  
  pythonProcess.stdout.on('data', (data) => {
   // let num = data;
    console.log(data.toString())
    //for(let i=0;i<num;i++){
    result+=data.toString();
  });
  // pythonProcess.stdout.end();
  

});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
