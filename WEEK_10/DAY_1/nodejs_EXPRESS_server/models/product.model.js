const {db} = require('../config/db.js');

const modelGetAll = () => {
    return db('products')
    .select('id', 'name', 'price')
    .orderBy('name');
}
const modelGetbyId = (id) => {
    return db('products').select('id', 'name', 'price').where({id});
};

const modelSearchProduct = (name) => {
    return db('products')
    .select('id', 'name', 'price')
    .whereILike('name', `${name}%`)
}
const modelInsertProduct = ({name, price}) => {
    return db('products').insert({name, price}, ['id', 'name', 'price']);
    
};


const modelUpdateProduct = ({name, price}, id) => {
    return db('products').update({name, price},['id', 'name', 'price'] ).where({id})
}

const modelDeleteProduct = (id) => {
    return db('products')
    .where({id})
    .del()
    .returning(['id', 'name', 'price'])
}
module.exports = { modelGetAll,modelGetbyId }


