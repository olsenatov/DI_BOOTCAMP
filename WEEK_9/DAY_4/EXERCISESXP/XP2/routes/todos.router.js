const express = require('express');
const todo_router = express.Router();

const logger = require("../middlewares/utils.js");

const { getAllToDo, addToDo, changeToDo, deleteToDo} = require('../controllers/todos.controller.js')


todo_router.get('/' , logger, getAllToDo);
todo_router.post('/', logger, addToDo);
todo_router.put('/:id', logger, changeToDo);
todo_router.delete('/:id', logger, deleteToDo);

// todo_router.use(logger.logger)



module.exports =  todo_router 