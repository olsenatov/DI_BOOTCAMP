const { fileWrite, fileRead } = require('./fileManager.js');

console.log(fileRead('Hello_World.txt'));

fileWrite('Bye_world.txt', 'writing to the file...');
