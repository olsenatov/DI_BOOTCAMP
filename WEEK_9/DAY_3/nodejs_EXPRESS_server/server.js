const express = require('express');
const dotenv = require('dotenv');
dotenv.config();
const app = express();

const { products } = require('./config/db.js');
// const PORT = 3001

app.use(express.urlencoded({extended:true}));
app.use(express.json());

app.listen(process.env.PORT, () => {
    console.log(`run on port ${process.env.PORT}`);
});

// CREATE
app.get('/api/products', (req, res) => {
    // res.send(products)
    res.json(products)
});

// // CRUD get all query string /?name=smth 
app.get('/api/products/search', (req, res) => { 
const productName = req.query.name;
  const filteredProducts = products.filter((item) => {
    return item.name.toLowerCase().includes(productName.toLowerCase());
  });

  if (filteredProducts.length === 0) {
    return res.status(200).json({ msg: "no matched to your search" });
  }
  res.status(200).json(filteredProducts);

});

// // CRUD get one 
app.get('/api/products/:id', (req, res) => {
    // res.send(products)
    const id = req.params.id;
    // console.log("params =>", params)
    const product = products.find((item)=> item.id == id);
    if (!product) return res.status(404).json({msg: "Product not found"})
    res.json(product)
});

// MAKE CHANGES - POST new
app.post('/api/products/:id', (req, res) => {
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
app.put ("/api/products/:id", (req, res) => {
   
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
app.delete("/api/products/:id", (req, res) => {
        const { id } = req.params;
        const index = products.findIndex((item) => item.id == id);
        if (index === -1) return res.status (404). json ({ msg: "not found" }) ;
        products.splice (index, 1) ;
        res.json(products);
        });