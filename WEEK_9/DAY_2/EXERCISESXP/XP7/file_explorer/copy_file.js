const fs = require('fs');

const filePathSource = 'source.txt';

const filePathDest = 'destination.txt';

fs.readFile(filePathSource, 'utf8', (err, data) => {
    if (err) {
        console.error('error reading source txt', err);
        return;
    }
    fs.writeFile(filePathDest, data, 'utf8', (err) => {
        if (err) {
            console.error('error writing to the file', err);
            return;
    }
    console.log('text copied!')
});

});

