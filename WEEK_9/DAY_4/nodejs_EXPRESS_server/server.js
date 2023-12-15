const express = require('express');
const dotenv = require('dotenv');
dotenv.config();

const cors = require('cors')

const app = express();

const { u_router } = require('./routes/users.router.js');

const { p_router } = require("./routes/products.router.js");

const { products } = require('./config/db.js');
// const PORT = 3001 from .env


app.use(express.urlencoded({extended:true}));
app.use(express.json());

app.listen(process.env.PORT, () => {
    console.log(`run on port ${process.env.PORT}`);
});

app.use('/api/products/', p_router);
app.use('/api/users/', u_router);

app.use(cors());
app.use(logger);
app.use('/api/users/', auth);