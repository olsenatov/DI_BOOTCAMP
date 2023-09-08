const { products } = require("../config/db.js");
const { p_router } = require("../routes/products.router.js");

const getAllProducts = p_router.get('/', (req, res) => {
    // res.send(products)
    res.json(products)
});

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