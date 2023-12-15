import logo from './logo.svg';
import './App.css';

import users from "./data.json";
import User from './components/User';
import { v4 as uuidv4 } from 'uuid';
import Button from '@mui/material/Button';
import 'tachyons';

function App() {  
 
  return (
    <div >
      <header>
    {
      users.map((item) => {
        return <User info={item} key={uuidv4()}/>
      })
    }
     </header>
     <div>
     <Button variant="contained">Contained</Button>
     </div>
    </div>
  );
}

export default App;
