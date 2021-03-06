"use strict";

//Build each individual stock node
function Stocks(stock) {

    return (

      <React.Fragment>
          <Row>
              <Col><p>{stock.symbol}</p></Col>
              <Col><p>{stock.name}</p></Col>
              <Col><p>{stock.price}</p></Col>
              <Col><p>{stock.interval}</p></Col>
          </Row>
      </React.Fragment>

    );
}

//Container for all stock components on page
function StocksContainer() {

    // const [stocks, setStocks] = React.useState([test]);
    const test = {
        'symbol': 'AAPL',
        'name': 'Apple',
        'price': 300,
        'interval': 4
    }
    const stocksArr = [];
    const stocks = [test]

    // React.useEffect(() =>{
    //     let user_id = user.user_id;
    //     let data = {user_id};
    //     fetch('/api/get-all-stocks')
    //     .then(response => response.json())
    //     .then(data => setStocks(data));
    // }, []);

    for(const stock of stocks) {
        console.log(stocks)
        stocksArr.push(
            <Stocks
            symbol={stock.symbol}
            name={stock.name}
            // sector={stock.sector}
            // dividend_yield={stock.dividend_yield}
            // dividend_amount={stock.dividend_amount}
            // payout_schedule={stock.payout_schedule}
            price={stock.price}
            interval={stock.payout_ratio}
            // date_added={stock.date_added}
            // date_modified={stock.date_modified}
            />
        );
    }

    return (
        <Col>
        {stocksArr}
        </Col>
    )

}