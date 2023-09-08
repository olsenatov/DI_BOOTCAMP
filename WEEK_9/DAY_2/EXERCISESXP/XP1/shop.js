const products = require('./products');

console.log(products);

function findPrByName(productName) {
    const foundProduct = products.find(product => product.name === productName);
    if (foundProduct) {
        console.log('product found: ', foundProduct) ;
    }else {
        console.log('not found');

        }
        }; 

findPrByName('dress');
findPrByName('skirt');