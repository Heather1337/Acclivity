function LandingPage() {

    return (

        <React.Fragment>

        <Row className="landing-page-row">

            <Col id='landing-page'>
                    <img id="logo"
                    src="static/img/logo.png"
                    className="d-inline-block align-top"
                    alt="Logo"/>
            </Col>

            <Col>

                <Button>Login</Button>
                <Button>Signup</Button>
                
            </Col>

        
        </Row>


        </React.Fragment>
        
    );
}