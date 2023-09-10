
const knex = require('knex')

// const db = knex({
//     client: 'pg',
//     connection: {
//       host : 'localhost',
//       port : 5432,  // if there's 2 db, second one will be 5433 and so on
//       user : 'postgres',
//       password : 'veampti0312',
//       database : 'dvdrental' //example
//     }
//   });

//   db.select('customer_id', 'first_name', 'last_name').from('customer')
//   .then(rows=> {
//     console.log(rows);
//   })
//   .catch(err => {
//     console.log(err);
//   });

/// for cloud DB
const db = knex({
    client: 'pg',
    connection: {
      host : 'lucky.db.elephantsql.com',
      port : 5432,  // if there's 2 db, second one will be 5433 and so on
      user : 'csckshjz',
      password : 'W7M7NAkDjY9wxo6VFGToACQBl9wuTVgz',
      database : 'csckshjz' //example
    }
  });
//   db.select('id', 'name', 'price').from('products')
// db('products').select('id','name', 'price')// runs as SELECTALL from this table
// .where({ id:1 })
//     .then(rows=> {
//       console.log(rows);
//     })
//     .catch(err => {
//       console.log(err);
//     });

// db('products')
// .insert([
//     {
//         name: 'icar', price: 1000
//     }
// ])
// .then(rows=> {
// console.log(rows);
//         })
//         .catch(err => {
//           console.log(err);
//         });

// db('products')
// .insert([
//     {
//         name: 'ichair', price: 1100
//     }
// ], ['id', 'name'])
// .then(rows=> {
// console.log(rows);
//         })
//         .catch(err => {
//           console.log(err);
//         });

// db('products')
// .where({ id:1 })
// .update({name:'iphone14'}, ['name'])
//     .then(rows=> {
//       console.log(rows);
//     })
//     .catch(err => {
//       console.log(err);
//     });

    // db('products')
    // .select('id','name', 'price')
    // .orderBy('name')
    //     .then(rows=> {
    //       console.log(rows);
    //     })
    //     .catch(err => {
    //       console.log(err);
    //     });

//    db.raw('select id, name, price from products where id > ?', [3])
//         .then(rows=> {
//           console.log(rows.rows);
//         })
//         .catch(err => {
//           console.log(err);
//         });

// const register = async () => {
//     const trx = await db.transaction();
//     try {
//         const user = await db('myusers').insert({
//             username: 'ola',
//             email : 'ola@mail.com'

//         },
//         ['username', 'email'])
//         .transacting(trx);
//         console.log('user=>', user);
//         const hashpwd = await db('hashpwd')
//         .insert({
//             username:user[0].username,
//             password: 'somepass'
//         }, ['password', 'username'])
//         .transacting(trx);
//         console.log('hashpwd=>', hashpwd)
//         await trx.commit();
//     }
//     catch (error) {
//         trx.rollback()
//     }
    
//     }
// register();

const register = async () => {
    const trx = await db.transaction();
    try {
      const user = await db("myusers")
        .insert(
          {
            username: "bbb",
            email: "bbb@gmail.com",
          },
          ["username", "email"]
        )
        .transacting(trx);
  
      console.log("user=>", user);
  
      const hashpwd = await db("hashpwd")
        .insert(
          {
            username: user[0].username,
            password: "123456",
          },
          ["password", "username"]
        )
        .transacting(trx);
  
      console.log("hashpwd=>", hashpwd);
  
      await trx.rollback();
      // await trx.commit();
    } catch (error) {
      await trx.rollback();
    }
  };
  register();