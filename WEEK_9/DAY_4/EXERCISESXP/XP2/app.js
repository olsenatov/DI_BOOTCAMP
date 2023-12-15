const express = require('express');
const app = express();
const todo_router = require('./routes/todos.router.js');
app.use(express.json());
const logger = require('./middlewares/utils.js');
// app.use('/todos', todo_router);

const PORT = 3000;

app.use(logger);

app.use('/todos', todo_router);
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
  }); 
