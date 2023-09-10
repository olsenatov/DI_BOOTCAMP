const express = require('express');
const app = express();

const port = 3000;

const data = [
    { id: 1, title: 'First Blog Post', content: 'This is the content of the first blog post.' },
    { id: 2, title: 'Second Blog Post', content: 'This is the content of the second blog post.' },
  ];

app.use(express.json());

//get all
app.get('/posts', (req, res) => {
    res.json(data);
  });

// get one by id
app.get('/posts/:id', (req, res) => {
    const id = req.params.id;
    const post = data.find((item)=> item.id == id);
    if (!post) return res.status(404).json({msg: "Post not found"})
    res.json(post)
});

//POST
app.post('/posts', (req, res) => {
  const { title, content } = req.body;
  const newPost = {
      id: data.length +1,
      title,
      content
  }
  data.push(newPost);
  res.status(201).json(newPost);
});
//put
app.put("/posts/:id", (req, res) => {
  console.log('requests received');
  const { id } = req.params;
  const { title, content } = req.body;
  const index = data.findIndex((item) => item.id == id);
  data[index] = {
  ...data[index], 
  title, 
  content
  }
  res.json(data);

  });

//delete
app.delete("/posts/:id", (req, res) => {
  const { id } = req.params;
  const index = data.findIndex((item) => item.id == id);
  if (index === -1) return res.status(404).json({ msg: "not found" }) ;
  data.splice(index, 1) ;
  res.json(data);
  });

// errors 
app.use((req, res) => {
  res.status(404).json({ error: 'Route not found' });
});

app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).json({ error: 'Internal server error' });
});


//run

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});