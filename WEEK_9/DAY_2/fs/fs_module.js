const fs = require('fs')

// const data = fs.readFileSync('user.json', 'utf-8');
// console.log(data);

//async
// const data = fs.readFile('user.json', 'utf-8', (err, data)=>{
//     if(err) return console.log(err);
//     console.lof(data);
// });
// fs.writeFile('info', 'bla bla bla bla override', (err)=>{
//     if (err) return console.log(err)
// });
// console.log(data)

let rr = [{username: 'aaa', pass: 123456 }]

fs.writeFile('info', JSON.stringify(rr), (err)=>{
    if (err) return console.log(err)
});

