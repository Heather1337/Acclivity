"use strict";

//Container for all stock components on page
function Dashboard() {

    const [payouts, setPayouts] = React.useState({QuarterlyPayout: 0, MonthlyPayout:0, OtherPayout:0, AnnualPayout:0, spent:0});
    const [portfolioRisk, setPortfolioRisk] = React.useState('None');
    const [sectorsOccupied, setSectorsOccupied] = React.useState(['test1','test2','test2']);


    React.useEffect(() =>{
        fetch('/api/get-all-payouts')
        .then(response => response.json())
        .then(data => {
            console.log('here',data)
            // setPayouts(data)
        });
    }, []);

    React.useEffect(() =>{
        fetch('/api/get-profile-info')
        .then(response => response.json())
        .then(data => {
            console.log('here',data)
            setProfileRisk(data)
            setSectorsOccupied(data)

        });
    }, []);


    return (
        <Row id="user-dashboard">

        <Col>

            <p>
            Quarterly Payouts: {payouts.QuarterlyPayout}
            <br/>
            Monthly Payouts: {payouts.MonthlyPayout}
            <br/>
            Other Payouts: {payouts.OtherPayout}
            <br/>
            Total Annual payout: <p className="green">{payouts.AnnualPayout}</p>
            <p>
            Total Spent: <p>className="red">{payouts.spent}</p>
            </p>
            </p>

        </Col>

        <Col>
            <p>
                Profile risk level:<p className={portfolioRisk === 'High'?  "red" : "green"}>{portfolioRisk} </p>
                <br/>
                Sectors Occupied: {sectorsOccupied}
            </p>
        </Col>

        </Row>
    )

}