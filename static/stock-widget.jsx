"use strict";

const handleStockClick = (e) => {
    const stock_id = e.target.id;
    const user_id = 0;
    const payload = {'stock_id': stock_id, 'user_id': user_id};

    if(e.target.innerText === "+") {
        console.log("ADDED DIVIDEND");
        fetch('/api/add-user-stock', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        })
        .then(resp => resp.json())
        .then()
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

    let risk = '-';
    if(stock.ratio < .35) risk = 'Low';
    if(stock.ratio > .35 && stock.ratio < .55) risk = 'Average';
    if(stock.ratio > .55) risk = 'High';

    return (
        <tr className={risk}>
            <td>{stock.symbol}</td>
            <td>{stock.name}</td>
            <td>{stock.price}</td>
            <td>{stock.ratio}</td>
            <td>{stock.dividend_amount}</td>
            <td>{stock.dividend_yield}</td>
            <td>{stock.payout_schedule}</td>
            <td>{stock.quantity}</td>
            <td>
                <Row className="buttons-row">
                    <p id={stock.id} size="sm" className="stock-button"  onClick={(e)=>handleStockClick(e)}>+</p>
                    <p id={stock.id} size="sm" className="stock-button"  onClick={(e)=>handleStockClick(e)}>-</p>
                </Row>
            </td>
        </tr>
    );
}

//Container for all stock components on page
const StocksContainer = () => {
    const [stocks, setStocks] = React.useState([]);
    const [userStocks, setUserStocks] = React.useState({});
    const stocksArr = [];
    const sectors = {};

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
                                id={stock.id}
                                quantity={quantity}
                                ratio={stock.payout_ratio}
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
            <Col>
            <Row className="center"><p>{keysArr[i]}</p></Row>
            <Col className="table-col">
            <Table size="sm" className="sector-table overflow-hidden" responsive="True">
                <thead>
                    <th>Symbol</th>
                    <th>Company</th>
                    <th>Price</th>
                    <th>Ratio</th>
                    <th>Dividend</th>
                    <th>Yield</th>
                    <th>Schedule</th>
                    <th>Quantity</th>
                </thead>
                <tbody>
                    {sectors[keysArr[i]]}
                </tbody>
            </Table>
            </Col>
            </Col>
            <Col className="table-container">
            <Row className="center"><p>{keysArr[i + 1]}</p></Row>
            <Col className="table-col">
            <Table size="sm" className="sector-table overflow-hidden">
                <thead>
                    <th>Symbol</th>
                    <th>Company</th>
                    <th>Price</th>
                    <th>Interval</th>
                    <th>Dividend</th>
                    <th>Yield</th>
                    <th>Schedule</th>
                    <th>Quantity</th>
                </thead>
                <tbody>
                    {sectors[keysArr[i+1]]}
                </tbody>
            </Table>
            </Col>
            </Col>
        </Row>
        );
    }

    return (
        <Col>
        <Container>{stocksArr}</Container>
        </Col>
    )

}