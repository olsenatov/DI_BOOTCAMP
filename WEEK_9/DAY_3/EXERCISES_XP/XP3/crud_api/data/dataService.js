const axios = require('axios')


async function fetchPosts() {
    try {
      const response = await axios.get('https://jsonplaceholder.typicode.com/posts');
      return response.data;
    } catch (error) {
      throw error;
    }
  }
  
  module.exports = { fetchPosts };
