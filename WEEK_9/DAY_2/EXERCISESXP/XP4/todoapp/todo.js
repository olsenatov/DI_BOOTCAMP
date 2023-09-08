
class TodoList {
    constructor() {
      this.tasks = [];
    }
  
    addTask(task) {
      this.tasks.push({ task, completed: false });
    }
  
    markTaskAsComplete(taskIndex) {
      if (taskIndex >= 0 && taskIndex < this.tasks.length) {
        this.tasks[taskIndex].completed = true;
      }
    }
        listTasks() {
      return this.tasks.map((task, index) => {
        const status = task.completed ? '[x]' : '[ ]';
        return `${index + 1}. ${status} ${task.task}`;
      }).join('\n');
    }
  };
  

  export default TodoList;