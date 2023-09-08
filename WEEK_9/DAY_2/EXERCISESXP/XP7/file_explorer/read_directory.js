const fs = require('fs');

const dirPath = './'

fs.readdir(dirPath, (err, files) => {
    if(err) {
        console.log('error reading directory', err);
        return;
    }
    console.log('Files in directory: ');
    files.forEach((file) => {
        console.log(file)
    })    
});