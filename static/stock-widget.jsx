"use strict";

//Build each individual stock node
const Stocks = (stock) => {

    return (

        <Row>
            <Col sm={1}><p>{stock.symbol}</p></Col>
            <Col sm={1}><p>{stock.name}</p></Col>
            <Col sm={1}><p>{stock.price}</p></Col>
            <Col sm={1}><p>{stock.interval}</p></Col>
            <Col sm={1}><p>{stock.dividend_amount}</p></Col>
            <Col sm={1}><p>{stock.dividend_yield}</p></Col>
            <Col sm={1}><p>{stock.payout_schedule}</p></Col>
            <Col sm={1}><p>{stock.sector}</p></Col>
        </Row>

    );
}

//Container for all stock components on page
const StocksContainer = () => {

    const [stocks, setStocks] = React.useState([]);
    const stocksArr = [];
    const sectors = {};

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
                                name={stock.name}
                                sector={stock.sector}
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
        // stocksArr.push(
        //     <Stocks
        //     symbol={stock.symbol}
        //     name={stock.name}
        //     sector={stock.sector}
        //     dividend_yield={stock.dividend_yield}
        //     dividend_amount={stock.dividend_amount}
        //     payout_schedule={stock.payout_schedule}
        //     price={stock.stock_price}
        //     interval={stock.payout_ratio}
        //     />
        // );

        for(const sector in sectors) {
            stocksArr.push(
            <Row className={"sector"}>
                <Row><p>{sector}</p></Row>
                <Row>{sectors[sector]}</Row>
            </Row>
            );
        }
    }

    return (
        <Col>
        <h3>Financial</h3>
        <Container>{stocksArr}</Container>
        </Col>
    )

}