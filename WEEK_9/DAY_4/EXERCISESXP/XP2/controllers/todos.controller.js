// const { todo_router } = require( "../routes/todos.router.js");
const { response } = require('express');
const fs = require('fs');


const readData = async(req,res)=>{
  const response= await fs.readFileSync('./data/todos.json', 'utf-8')
 
   res.json(response)
}
const writeData = async (task)=>{
  data = await fs.readFileSync('./data/todos.json', 'utf-8')
  data.push(task)
  fs.writeFileSync(task, './data/todos.json')
}
const getAllToDo =  (req, res)  => {
  const todos = readData()
    res.json(todos);
  };
  
  
  const addToDo = (req, res) => {
    
    const todos = readData()
    console.log(todos)
    const { task } = req.body;
    const newTask = {
      id: todos.length + 1,
      task,
    };
    writeData(newTask)
    data = readData()
    res.status(201).json(data);
  };
  
  
   const changeToDo =  (req, res) => { 
    const { id } = req.params;
    const { task } = req.body;
    const index = todos.findIndex((item) => item.id == id);
    todos[index] = {
    ...todos[index], 
    task
    }
    res.json(todos);
  };
  
  const deleteToDo = (req, res) => {
      const { id } = req.params;
      const index = todos.findIndex((item) => item.id == id);
      if (index === -1) return res.status(404).json({ msg: "Task not found" }) ;
      todos.splice(index, 1) ;
      res.json(todos);
    };

module.exports = { getAllToDo, addToDo, changeToDo, deleteToDo }
