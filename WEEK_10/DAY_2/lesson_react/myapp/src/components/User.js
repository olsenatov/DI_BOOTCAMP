import './User.css'

const User = (props) => {
    const { info } = props
    return(
        <div className='dib pa3 ma3 tc bg-light-green grow br3'>
            <img src={`https://robohash.org/${info.id}?size=150x150`}/>
            <h2>{info.name}</h2>
            <p>{info.email}</p>
            <p>{info.username}</p>
        </div>
    )
}

export default User