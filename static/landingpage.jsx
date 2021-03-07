function LandingPage() {

    return (

        <React.Fragment>

        <Row id="landing-page-row">

            <Col id='landing-page-logo-column'>
                    <img id="logo"
                    src="static/img/landing-logo.png"
                    className="d-inline-block align-top"
                    alt="Logo"/>

                <Button><Link to="/signup">Signup</Link></Button>
                <Button><Link to="/login">Login</Link></Button>
                
            </Col>

        
        </Row>


        </React.Fragment>
        
    );
}