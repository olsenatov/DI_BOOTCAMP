import React from "react";
import User from "./components/User";

class AppClass extends React.Component {
    constructor() {
        super();
        this.state = {
            txt: 'Hello',
            users: []
        };
        console.log('constructor');
    }

    getData = async () => {
        try {
          const res = await fetch('https://jsonplaceholder.typicode.com/users');
          const data = await res.json();
         console.log(data);
         this.setState({users:data})
        } catch(error) {
          console.log('err=>', error);
        }
    }
    handleChange = (e) => {
        console.log(e.target.value);
        this.setState({txt:e.target.value})
    };

    componentDidMount = () => {
        console.log('ComponentDidMount');
        this.getData()
    };

    render() {
        console.log('render');
        return (
            <div>
                <h1>App Class Component</h1>
                <h2>{this.state.txt}</h2>
                <input onChange={this.handleChange} />
                <button onClick={this.getData}>Get users!</button>
                <div>
                    {
                        this.state.users.map(item=> {
                            return <User info={item} />
                        })
                    }
                </div>
            </div>
        )
    }
}

export default AppClass