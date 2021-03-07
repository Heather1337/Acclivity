"use strict";

//Build each individual stock node
const Stocks = (stock) => {

    return (

        <Row>
            <Col><p>{stock.symbol}</p></Col>
            <Col><p>{stock.name}</p></Col>
            <Col><p>{stock.price}</p></Col>
            <Col><p>{stock.interval}</p></Col>
            <Col><p>{stock.dividend_amount}</p></Col>
            <Col><p>{stock.dividend_yield}</p></Col>
            <Col><p>{stock.payout_schedule}</p></Col>
            <Col><p>{stock.sector}</p></Col>
        </Row>

    );
}

//Container for all stock components on page
const StocksContainer = () => {

    const [stocks, setStocks] = React.useState([]);
    const stocksArr = [];

    React.useEffect(() =>{
        fetch('/api/get-all-stocks')
        .then(response => response.json())
        .then(data => {
            setStocks(data)
        });
    }, []);

    for(const stock of stocks) {
        console.log(stock)
        stocksArr.push(
            <Stocks
            symbol={stock.symbol}
            name={stock.name}
            sector={stock.sector}
            dividend_yield={stock.dividend_yield}
            dividend_amount={stock.dividend_amount}
            payout_schedule={stock.payout_schedule}
            price={stock.stock_price}
            interval={stock.payout_ratio}
            />
        );
    }

    return (
        <Col>
        <h3>Financial</h3>
        <Row>
            <Col><p>Symbol</p></Col>
            <Col><p>Name</p></Col>
            <Col><p>Sector</p></Col>
            <Col><p>Price</p></Col>
            <Col><p>Interval</p></Col>
            <Col><p>Dividend Amount</p></Col>
            <Col><p>Divident Yield</p></Col>
            <Col><p>Payout Schedule</p></Col>
        </Row>
        <Container>{stocksArr}</Container>
        </Col>
    )

}