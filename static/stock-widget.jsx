"use strict";

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
            <Col><p>Divident</p></Col>
            <Col><p>Dividend Yield</p></Col>
            <Col><p>Payout Schedule</p></Col>
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