// import { info } = './modules/app.js'; //for ecmascript 6 syntax (need to change type in)
const { info } = require('./modules/app.js') // for commonjs syntax
var slugify = require('slugify')

info().then((data)=> console.log(data))

const slug = slugify('some string')
console.log(slug)