
// 3. App.js - use state of txt and an input to chage this txt state
// 4. Text.js - get the txt as a props, and render it on the page
// */
// import React from 'react'
import { useEffect, useState } from 'react'



const Text = (props) => {
    const [ users, setUsers ] = useState([]);
// class Text extends React.Component{
    useEffect(() => {
        if (props.txt === 'Olga') getData(); console.log("this is my name: ", props.txt);
      },[props.txt]);

const getData = async () => {
        try {
          const res = await fetch('https://jsonplaceholder.typicode.com/users');
          const data = await res.json();
         console.log(data);
         setUsers(data);
        } catch(error) {
          console.log('err=>', error);
        }
};    
    return (
        <div>
 <h2>Text Component</h2>
 {users.map((item, i) => {
    return <div key={i}>{item.name}</div>
})}
        </div>
    )   
}

export default Text