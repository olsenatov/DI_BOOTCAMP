
import TodoList from './todo.js';

const myTodoList = new TodoList();

myTodoList.addTask('Buy books');
myTodoList.addTask('A meeting');

console.log(myTodoList.listTasks());

myTodoList.markTaskAsComplete(0);

console.log(myTodoList.listTasks());