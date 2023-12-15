const Hello = (props) => {
    const { name, email } = props;
    return (
        <> <h1>
            Hello {name} {email}!</h1>
        </>
    )
}
export default Hello;