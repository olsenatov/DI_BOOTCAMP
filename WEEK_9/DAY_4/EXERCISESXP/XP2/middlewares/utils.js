const logger = (req, res, next) => {
    console.log('urs=>', req.url);
    console.log('method=>', req.method);
    console.log('params=>', req.params);
    console.log('query=>', req.query);
    console.log('body=>', req.body); 
    next()
  }
  
module.exports = logger