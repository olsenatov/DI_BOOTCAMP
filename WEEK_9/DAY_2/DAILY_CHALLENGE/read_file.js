import fs from 'fs';



function readAndDisplay() {
    fs.readFile('./files/file_data.txt', 'utf8', (err, data) => {
         if (err) {
        console.error('error reading source txt', err);
        return;
    }
    console.log('this is from file_data: ', data);
});
};

export default readAndDisplay