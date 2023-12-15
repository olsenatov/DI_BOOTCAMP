const smthRouter = express.Router();
const { smthDB } = require('../config/db.js');


smthRouter.get('/', (req, res) =>{
  res.json(smthDB);
});

 smthRouter.get('/:id', (req, res) => {
  const id = req.params.id;
  const smth = smthDB.find((item)=> item.id == id);
  if (!smth) return res.status(404).json({msg: "Smth not found"})
  res.json(smth)
});

smthRouter.post('/', (req, res) => {
  const { firstkey, secondkey, etckey} = req.body;
  const newSmth = {
      id: smthDB.length +1,
      firstkey,
      secondkey,
      etckey
  }
  smthDB.push(newSmth);
res.json(smthDB);
});

 smthRouter.put("/:id", (req, res) => { 
  const { id } = req.params;
  const { firstkey,
    secondkey,
    etckey  } = req.body;
  const index = smthDB.findIndex((item) => item.id == id);
  smthDB[index] = {
  ...smthDB[index], 
  firstkey,
  secondkey,
  etckey 
  }
  res.json(smthDB);
});

smthRouter.delete("/:id", (req, res) => {
    const { id } = req.params;
    const index = smthDB.findIndex((item) => item.id == id);
    if (index === -1) return res.status(404).json({ msg: "Smth not found" }) ;
    smthDB.splice (index, 1) ;
    res.json(smthDB);
  });


module.exports = { smthRouter }