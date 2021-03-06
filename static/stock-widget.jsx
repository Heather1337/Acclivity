function Stocks({user}) {

    const [stocks, setStocks] = React.useState([]);

    React.useEffect(() =>{
        let user_id = user.user_id;
        let data = {user_id};
        fetch('/api/get-all-stocks',
        {method:"POST", body: JSON.stringify(data),headers: { 'Content-Type': 'application/json'}})
        .then(response => response.json())
        .then(data => setProductInfo(data));
    }, []);

    return (

      <React.Fragment>
      </React.Fragment>

    );
}