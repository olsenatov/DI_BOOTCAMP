const aboutRouter = express.Router();
const { aboutDB } = require('../config/db.js');


aboutRouter.get('/', (req, res) =>{
  res.json(aboutDB);
});


aboutRouter.put("/:id", (req, res) => { 
  const { id } = req.params;
  const { firstkey,
    secondkey,
    etckey  } = req.body;
  const index = aboutDB.findIndex((item) => item.id == id);
  aboutDB[index] = {
  ...aboutDB[index], 
  firstkey,
  secondkey,
  etckey 
  }
  res.json(aboutDB);
});

aboutRouter.delete("/:id", (req, res) => {
    const { id } = req.params;
    const index = aboutDB.findIndex((item) => item.id == id);
    if (index === -1) return res.status(404).json({ msg: "Smth not found" }) ;
    aboutDB.splice (index, 1) ;
    res.json(aboutDB);
  });


module.exports = { aboutRouter }