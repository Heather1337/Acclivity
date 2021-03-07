"use strict";

const handleStockClick = (e) => {
    const stock_id = e.target.id;
    const user_id = localStorage.id;
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
        //Call Patch request to update the amount of stocks for this user
    }
    else if(e.target.innerText === "-") {
        console.log("SUBTRACTED DIVIDEND");
        fetch('/api/remove-user-stock', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        })
        .then(resp => resp.json())
        .then(data => console.log('Removed stock to user account', data))
        //Call Patch request to update the amount of stocks for this user
    }
}

//Build each individual stock node
const Stocks = (stock) => {

    return (
        <Container className="stock-container">
            <Row>
                <Col><p>{stock.symbol}</p></Col>
                <Col><p>{stock.name}</p></Col>
                <Col><p>{stock.price}</p></Col>
                <Col><p>{stock.interval}</p></Col>
                <Col><p>{stock.dividend_amount}</p></Col>
                <Col><p>{stock.dividend_yield}</p></Col>
                <Col><p>{stock.payout_schedule}</p></Col>
                <Col>
                    <Button id={stock.symbol} size="sm" variant="outline-info" onClick={(e)=>handleStockClick(e)}>+</Button>
                    <Button id={stock.symbol} size="sm" variant="outline-info" onClick={(e)=>handleStockClick(e)}>-</Button>
                </Col>
            </Row>
        </Container>
    );
}

//Container for all stock components on page
const StocksContainer = () => {

    const [stocks, setStocks] = React.useState([]);
    const stocksArr = [];
    const sectors = {};

    const headers = <Row>
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
        });
    }, []);

    for(const stock of stocks) {
        const stockNode =  <Stocks
                                symbol={stock.symbol}
                                name={stock.company_name}
                                dividend_yield={stock.dividend_yield}
                                dividend_amount={stock.dividend_amount}
                                payout_schedule={stock.payout_schedule}
                                price={stock.stock_price}
                                interval={stock.payout_ratio}
                            />
        if(!sectors[stock.sector]) {
            sectors[stock.sector] = [stockNode]
        }
        else {
            sectors[stock.sector].push(stockNode)
        }
    }

    for(const sector in sectors) {
        console.log('sector: ', sectors)
        stocksArr.push(
        <Row className={"sector"}>
            <Col>
            <Row className="sector-title"><p>{sector}</p></Row>
            <Row>{headers}</Row>
            <Container>{sectors[sector]}</Container>
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