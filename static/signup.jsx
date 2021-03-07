function Signup({setUser}) {

    return (

        <React.Fragment>
            
            <Row className="login-signup-row">
            <Col id='login-column'>
                <Login setUser={setUser}/>
            </Col>
            <Col id='signup-column'>
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
            </Col>
            </Row>
        </React.Fragment>
    )

};