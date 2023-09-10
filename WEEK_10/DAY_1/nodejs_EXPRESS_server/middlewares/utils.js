const logger = (req, res, next) => {
    console.log('urs=>', req.url);
    console.log('method=>', req.method);
    console.log('params=>', req.params);
    console.log('query=>', req.query);
    console.log('body=>', req.body); 
    next()
  }
  
  const auth = (req, res, next) => {
    const user = req.query.user;
    if(user == 'admin'){
      next()
    }
    else{
      res.status(401).send('Unauthorized')
    }
  };

  module.exports = { logger, auth };