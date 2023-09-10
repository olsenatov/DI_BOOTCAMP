const express = require('express');

const dotenv = require('dotenv');
dotenv.config();
const app = express();

app.use(express.json());
const PORT = 5001;

const data = [
    { id: 1, title: 'Harry Potter', author: 'JKR', publishedYear: 1999 },
    { id: 2, title: 'The Lord of the Rings', author: 'Tolkien', publishedYear: 1955 },
    { id: 3, title: 'His Dark Materials', author: 'Pullman', publishedYear: 1995 }
,
  ];

//get all
app.get('/api/books', (req, res) => {
    res.json(data);
  });


// get one by id
app.get('/api/books/:id', (req, res) => {
    const id = req.params.id;
    const book = data.find((item)=> item.id == id);
    if (!book) return res.status(404).json({msg: "Book not found"});
    res.status(200).json(book) 
});

app.post('/api/books', (req, res) => {
    const { title, author, publishedYear } = req.body;
    const newBook = {
        id: data.length +1,
        title,
        author, 
        publishedYear
    }
    data.push(newBook);
    res.status(201).json(newBook);
  });

  app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
  }); 