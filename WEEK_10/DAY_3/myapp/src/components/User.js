import './User.css'
import React from 'react'


class User extends React.Component{
    
    render(){
        const { info } =this.props
        return(
        <div className='dib pa3 ma3 tc bg-light-green grow br3'>
        <img src={`https://robohash.org/${info.id}?size=150x150`}/>
        <h2>{info.name}</h2>
        <p>{info.email}</p>
         <p>{info.username}</p>
        </div>
                )

    }
}

// const User = (props) => {
//   
//    
// }

export default User