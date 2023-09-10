// const { users } = require('../config/db.js');

// const getAllusers = (req, res) =>{
//     res.json(users);
// }

// const getUser = (req, res) => {
//     const id = req.params.id;
//     const user = users.find((item)=> item.id == id);
//     if (!user) return res.status(404).json({msg: "User not found"})
//     res.json(user)
// }

// const addNewUser = users.post('/:id', (req, res) => {
//     const { name, email} = req.body;
//     const newUser = {
//         id: users.length +1,
//         name,
//         email
//     }
// })

// products.push(newProduct);
// res.json(products);


// module.exports = {
//     getAllusers,
//     getUser
// }

