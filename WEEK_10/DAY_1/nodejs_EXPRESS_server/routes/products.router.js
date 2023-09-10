const express = require('express');

const p_router = express.Router();

module.exports = { p_router };

const { products } = require('../config/db.js');
const { getAllProducts, searchProduct } = require('../controllers/products.controller.js');

const logger = requre("../controllers/products.controller.js")

// CREATE
p_router.get('/', logger, getAllProducts);

// // CRUD get all query string /?name=smth 
p_router.get('/search', searchProduct)

// // CRUD get one 
p_router.get('/:id', (req, res) => {
    // res.send(products)
    const id = req.params.id;
    // console.log("params =>", params)
    const product = products.find((item)=> item.id == id);
    if (!product) return res.status(404).json({msg: "Product not found"})
    res.json(product)
});

// MAKE CHANGES - POST new
p_router.post('/:id', (req, res) => {
    const { name, price} = req.body;
    const newProduct = {
        id: products.length +1,
        name,
        price
    }
products.push(newProduct);
res.json(products);


})

// MAKE CHANGES - PUT correct or change existing
p_router.put ("/:id", (req, res) => {
   
    const { id } = req.params;
 
    const { name, price } = reg.body;
  
    const index = products.findIndex((item) => item.id == id);
    products [index] = {
    ...products [index], 
    name: name, 
    price: price
    }
    res.json (products);

    });
// MAKE CHANGES - DELETE 
p_router.delete("/:id", (req, res) => {
        const { id } = req.params;
        const index = products.findIndex((item) => item.id == id);
        if (index === -1) return res.status (404). json ({ msg: "not found" }) ;
        products.splice (index, 1) ;
        res.json(products);
        });


module.exports = { p_router };