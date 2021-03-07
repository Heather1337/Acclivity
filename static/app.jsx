// const Router = ReactRouterDOM.BrowserRouter;
// const { useHistory, useParams, Redirect, Switch, Prompt, Link, Route } = ReactRouterDOM;

function App() {
    const [user, setUser] = React.useState(undefined)

    React.useEffect(() => {
      const currentuser = JSON.parse(localStorage.getItem('user'));
      setUser(currentuser)
    },[]);


    return (

      <Router>

             {/* <TopNav user={user} setUser={setUser}/> */}
              {/* <Dashboard/> */}
              {/* <TopNav user={user} setUser={setUser}/> */}
              {/* <Dashboard/> */}
              {/* <StocksContainer user={user} setUser={setUser}/> */}
              {/* <Dashboard/> */}
              {/* <StocksContainer user={user} setUser={setUser}/> */}

          <Switch>
                  <Route path="/">
                      <Dashboard/>
                      <StocksContainer user={user} setUser={setUser}/>
                  </Route>


                  <Route path='/signup'>
                       <Signup setUser={setUser} user={user}/>
                   </Route>

                   {/* <Route path='/login'>
                       <Login user={user} setUser={setUser}/>
                   </Route>

                   <Route path="/">
                       <LandingPage user={user} />
                   </Route> */}

           </Switch>

            {/* <Footer/> */}

      </Router>

    );
}

ReactDOM.render(<App />, document.getElementById('app'));