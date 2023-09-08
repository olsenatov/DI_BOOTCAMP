const fs = require('fs');

function fileRead(filePath){
    fs.readFile(filePath, 'utf-8', function (err, data) {
    if (err) {
        console.error(err)
        return
    }
    });
}

function fileWrite(filePath, content){
    fs.writeFile(filePath, content, 'utf8', function (err) {
    if (err) {
        console.error(err)
        return
    }
    });
}

module.exports = { fileRead, fileWrite };