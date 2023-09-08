const { userInfo } = require('./users.js');

// userInfo.then((data)=> console.log(data)); 

// const info = async() => {
//     const data = await userInfo();
//     console.log(data);

// }
(async () => {
    const data = await userInfo();
    //     console.log(data);
})

// self-awoke function