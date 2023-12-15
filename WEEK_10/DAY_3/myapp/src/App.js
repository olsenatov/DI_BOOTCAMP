import logo from './logo.svg';
import './App.css';

// import users from "./data.json";
import { useState } from 'react';
import User from './components/User';
import { v4 as uuidv4 } from 'uuid';
import Button from '@mui/material/Button';
import 'tachyons';

function App() {  
const [state, setState] = useState();
const [users, setUsers] = useState([]);
const [txt, setText] = useState('Heloooooo hooks');  //hooks



//  const users = [];

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
 const handleChange = (e) => {
  console.log(e.target.value);
 }
  return (
    <>
    <h2>{txt}</h2>
    <input type='text' onChange={(e) => handleChange(e)} />
     <button onClick={()=> getData()}>Get users!</button>
   
    <div >
  
    {
      users.map((item) => {
        return <User info={item} key={uuidv4()}/>
      })
    }
    </div>
    </>
  );
}

export default App;


