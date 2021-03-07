function Signup({setUser}) {


  const [email, setEmail] = React.useState('')
  const [password, setPassword] = React.useState('')
  const [fname, setFname] = React.useState('')
  const [lname, setLname] = React.useState('')
  const history = useHistory();

  function handleSubmit(evt){
    evt.preventDefault()
    let data = {email:email, password:password, fname:fname, lname:lname}
    console.log(data)
    fetch('/api/signup',
    {method: "POST",  body: JSON.stringify(data),  headers: {'Content-Type': 'application/json'}} )
    .then(response => response.json())
    .then(data => {
    if (data == 'account created'){
      alert('account created, please login')
      history.push('/login');
    }else{
      alert('invalid email or password')
    }
    });
  }

    return (

        <React.Fragment>
            
            <Row className="login-signup-row">
                <Form id='signupform' onSubmit={handleSubmit}>
                <Form.Group controlId="formBasicfname">
                    <Form.Control type="text"
                                    name="fname"
                                    placeholder="First"
                                    value={fname}
                                    onChange={e => setFname(e.target.value)}></Form.Control>
                    </Form.Group>
                    <Form.Group controlId="formBasiclname">
                        <Form.Control type="text"
                        name="lname"
                        placeholder="Last"
                        value={lname}
                        onChange={e => setLname(e.target.value)}></Form.Control>
                    </Form.Group>
                    <Form.Group controlId="formBasicemail">
                        <Form.Control type="email"
                                    name="email"
                                    placeholder="email"
                                    value={email}
                                    onChange={e => setEmail(e.target.value)}></Form.Control>
                        </Form.Group>
                    <Form.Group controlId="formSignupPassword">
                        <Form.Control type="password"
                                    name="password"
                                    placeholder="password"
                                    value={password}
                                    onChange={e => setPassword(e.target.value)}></Form.Control>
                    </Form.Group>
                    <Button id='register-button'
                            variant="primary"
                            type="submit">
                            Register
                    </Button>
                </Form>
            </Row>
        </React.Fragment>
    )

};