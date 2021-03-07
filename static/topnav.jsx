function TopNav({user, setUser}) {

    const history = useHistory();

    // function handleSubmit(evt) {
    //     evt.preventDefault();
    //     localStorage.removeItem('user');
    //     setUser({fname: "", id: 0, sumbission_status:'false'});
    //     history.push('/');
    // };

    return (

        <React.Fragment>
            <Navbar
                scrolling="true"
                expand="sm"
                fixed='top'
                id='topnav'>
                    <Link>
                    OH HERRO
                    </Link>
                {/* <Navbar.Brand>
                    <Link to='/'id='shoppies'>
                    <img id="logo"
                        src="https://www.nydailynews.com/resizer/Ee9izZJ1zk1aij0aZ0lwemFgLoQ=/800x553/top/cloudfront-us-east-1.images.arcpublishing.com/tronc/LGGTNSKXKRH6LM53TFE4VDJIYI.jpg"
                        className="d-inline-block align-top"
                        alt="Logo"/>
                    </Link> */}
                {/* </Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="mr-auto">
                            {user?'':<Nav.Link to="/signup">Login | Signup</Nav.Link>}
                            {user?
                                <NavDropdown title= {user.fname} id="basic-nav-dropdown">
                                    <NavDropdown.Item><Button onClick={handleSubmit} variant="light">Logout</Button></NavDropdown.Item>
                                </NavDropdown>:''}
                        </Nav>
                    </Navbar.Collapse> */}
            </Navbar>
        </React.Fragment>
    );
}