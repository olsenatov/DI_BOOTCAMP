const express = require('express');

const dotenv = require('dotenv');
dotenv.config();
const app = express();

app.use(express.json());
const PORT = 5002;

const { fetchPosts } = require('./data/dataService.js');


app.get('/posts', async (req, res) => {
    try {
      const posts = await fetchPosts();
      res.json(posts);
    } catch (error) {
      res.status(500).json({ error: 'Internal server error' });
    }
  });
  
  module.exports = { fetchPosts };
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
  }); 
