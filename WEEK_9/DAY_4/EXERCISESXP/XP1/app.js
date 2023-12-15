const express = require('express');
const app = express();
const smthRouter = require('./routes/index.router.js');
const aboutRouter = require('./routes/about.router.js');

app.use('/', smthRouter);
app.use('/about', aboutRouter)

const PORT = 3000;


app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
  }); 
