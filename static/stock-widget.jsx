"use strict";

const handleStockClick = (e) => {
    const stock_id = e.target.id;
    const user_id = 0;
    const payload = {'stock_id': stock_id, 'user_id': user_id}

    if(e.target.innerText === "+") {
        console.log("ADDED DIVIDEND");
        fetch('/api/add-user-stock', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        })
        .then(resp => resp.json())
        .then(data => console.log('Added stock to user account', data))
    }
    else if(e.target.innerText === "-") {
        console.log("SUBTRACTED DIVIDEND");
        fetch('/api/remove_user_stock', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        })
        .then(resp => resp.json())
        .then(data => console.log('Removed stock to user account', data))
    }
}

//Get all stocks belonging to a User
const getUserStocks = (setUserStocks) => {
    const payload = {'user_id': 0}
    console.log('calling get Usr Stocks!!!!')
    fetch('/api/get-user-stocks', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
    })
    .then(resp => resp.json())
    .then(data => {
        console.log('data returned from user stocks fetch', data)
        setUserStocks(data)
    })
}
//===========================================================================================================//
//Build each individual stock node
const Stocks = (stock) => {

    return (
        <tr>
            <td>{stock.symbol}</td>
            <td>{stock.name}</td>
            <td>{stock.price}</td>
            <td>{stock.interval}</td>
            <td>{stock.dividend_amount}</td>
            <td>{stock.dividend_yield}</td>
            <td>{stock.payout_schedule}</td>
            <td>{stock.quantity}</td>
        </tr>
        // <Container className="stock-container">
        //     <Row>
        //         <Col><p>{stock.symbol}</p></Col>
        //         <Col><p>{stock.name}</p></Col>
        //         <Col><p>{stock.price}</p></Col>
        //         <Col><p>{stock.interval}</p></Col>
        //         <Col><p>{stock.dividend_amount}</p></Col>
        //         <Col><p>{stock.dividend_yield}</p></Col>
        //         <Col><p>{stock.payout_schedule}</p></Col>
        //         <Col><p>{stock.quantity}</p></Col>
        //         <Col>
        //             <Button id={stock.id} size="sm" variant="outline-info" onClick={(e)=>handleStockClick(e)}>+</Button>
        //             <Button id={stock.id} size="sm" variant="outline-info" onClick={(e)=>handleStockClick(e)}>-</Button>
        //         </Col>
        //     </Row>
        // </Container>
    );
}

//Container for all stock components on page
const StocksContainer = () => {
    const handleStockClick = (e) => {
        const stock_id = e.target.id;
        const user_id = 0;
        const payload = {'stock_id': stock_id, 'user_id': user_id}
    
        if(e.target.innerText === "+") {
            console.log("ADDED DIVIDEND");
            fetch('/api/add-user-stock', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            })
            .then(resp => resp.json())
            .then(getUserStocks(setUserStocks))
        }
        else if(e.target.innerText === "-") {
            console.log("SUBTRACTED DIVIDEND");
            fetch('/api/remove_user_stock', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            })
            .then(resp => resp.json())
            .then(getUserStocks(setUserStocks))
        }
    }

    const [stocks, setStocks] = React.useState([]);
    const [userStocks, setUserStocks] = React.useState({});
    const stocksArr = [];
    const sectors = {};
    const headers = <Row id = "symbol-space">
            <Col><p>Symbol</p></Col>
            <Col><p>Stock Name</p></Col>
            <Col><p>Current Price</p></Col>
            <Col><p>Interval</p></Col>
            <Col><p>Dividend</p></Col>
            <Col><p>Dividend Yield</p></Col>
            <Col><p>Payout Schedule</p></Col>
            <Col><p>Quantity</p></Col>
        </Row>

    React.useEffect(() =>{
        fetch('/api/get-all-stocks')
        .then(response => response.json())
        .then(data => {
            setStocks(data)
        })
        .then(getUserStocks(setUserStocks))
    }, []);

    for(const stock of stocks) {
        let quantity = userStocks[stock.id] ?  userStocks[stock.id] : 0;
        const stockNode =  <Stocks
                                symbol={stock.symbol}
                                name={stock.company_name}
                                dividend_yield={stock.dividend_yield}
                                dividend_amount={stock.dividend_amount}
                                payout_schedule={stock.payout_schedule}
                                price={stock.stock_price}
                                interval={stock.payout_ratio}
                                id={stock.id}
                                quantity={quantity}
                            />
        if(!sectors[stock.sector]) {
            sectors[stock.sector] = [stockNode]
        }
        else {
            sectors[stock.sector].push(stockNode)
        }
    }

    const keysArr = Object.keys(sectors);
    for(var i = 0; i < keysArr.length; i+=2) {
        console.log('sector: ', sectors)
        stocksArr.push(
        <Row>
            <Col >
            <Table size="sm" className="sector-table">
                <thead>
                    <th>Symbol</th>
                    <th>Stock Name</th>
                    <th>Current Price</th>
                    <th>Interval</th>
                    <th>Dividend</th>
                    <th>Dividend Yield</th>
                    <th>Payout Schedule</th>
                    <th>Quantity</th>
                </thead>
                <tbody>
                    {sectors[keysArr[i]]}
                </tbody>
            </Table>
            </Col>
            <Col >
            <Table size="sm" className="sector-table">
                <thead>
                    <th>Symbol</th>
                    <th>Stock Name</th>
                    <th>Current Price</th>
                    <th>Interval</th>
                    <th>Dividend</th>
                    <th>Dividend Yield</th>
                    <th>Payout Schedule</th>
                    <th>Quantity</th>
                </thead>
                <tbody>
                    {sectors[keysArr[i+1]]}
                </tbody>
            </Table>
            </Col>
        </Row>
        // <Row className={"sector"}>
        //     <Col>
        //     <Row className="sector-title"><p>{sector}</p></Row>
        //     <Row>{headers}</Row>
        //     <Container>{sectors[sector]}</Container>
        //     </Col>
        // </Row>
        );
    }

    return (
        <Col>
        <Container>{stocksArr}</Container>
        </Col>
    )

}