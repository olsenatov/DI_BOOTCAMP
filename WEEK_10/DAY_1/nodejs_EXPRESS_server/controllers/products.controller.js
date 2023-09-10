const { products } = require("../config/db.js");
const { p_router } = require("../routes/products.router.js");
const { modelGetAll } = require('../models/product.model.js');


const getAllProducts = (req, res) => {
    modelGetAll()
    .then((data) => {
      res.json(data);
    })
    .catch((err) => {
      console.log(err);
      res.status(404).json({msg: 'not found'});
   });
  }

  const getProduct = async (req, res) => {
    try {
      const id = req.params.is;
      const data = await modelGetbyId(id);
      res.json(data)
    } catch (error) {
      console.log(error);
      res.status(404).json({msg: 'not found'});
    }
  }

  const searchProductNew = async (req, res) => {
    try {
      const data = await modelSearchProduct(req.query.name)
      res.json(data)
    } catch (error) {
      console.log(error);
      res.status(404).json({msg: error.name}); 
    }
  }

  const createProduct = async (req, res) => {
    const { name, price } = req.body;
    try {
      const data = await modelInsertProduct(req.body);
      res.json(data);
    } catch (error) {
      console.log(error);
      res.status(404).json({msg: error.name}); 
    }
  }

  const updateProduct = async (req, res) => {
    const { id } = req.params;
    const { name, price } = req.body;
    try {
      const data = await modelUpdateProduct(req.body, id);
      res.json(data);
    } catch (error) {
      console.log(error);
      res.status(404).json({msg: error.name}); 
    }
  }

  const deleteProduct = async (req, res) => {
  const { id } = req.params;  
  try {
    const data = await modelDeleteProduct(id);
    res.json(data);
  } catch (error) {
    console.log(error);
    res.status(404).json({msg: error.name}); 
  }
}



const searchProduct = p_router.get('/search', (req, res) => { 
    const productName = req.query.name;
      const filteredProducts = products.filter((item) => {
        return item.name.toLowerCase().includes(productName.toLowerCase());
      });
    
      if (filteredProducts.length === 0) {
        return res.status(200).json({ msg: "no matched to your search" });
      }
      res.status(200).json(filteredProducts);
    
    });

module.exports = { getAllProducts, searchProduct };