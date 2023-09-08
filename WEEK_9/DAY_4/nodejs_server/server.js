const http = require('http');

const server = http.createServer((req, res) =>{
    console.log('getting your request');
    res.end('hello my first node server');
});

server.listen(5000, () =>{
    console.log('run on port 5000');
});