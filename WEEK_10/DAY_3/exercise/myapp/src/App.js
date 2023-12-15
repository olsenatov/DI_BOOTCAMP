import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from 'react';
import Text from './components/Text';

function App() {
  const [txt, setText] = useState('');

  // useEffect(() => {
  //   console.log('');
  // },[]);

  // useEffect(() => {
  //   if (txt != 'a') console.log(txt);
  //   console.log('');
  // },[txt]);

  // useEffect(() => {
  //   if (txt === 'Olga') console.log(txt);
  //   console.log('');
  // },[txt]);

  return (
    <>
    <input type='text' onChange={(e) => {
      setText(e.target.value)
      }} />
   <Text txt = {txt}/>
   </>
  );
}

export default App;
