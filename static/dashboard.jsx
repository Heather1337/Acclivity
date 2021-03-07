"use strict";

//Container for all stock components on page
function Dashboard(props) {

    const [payouts, setPayouts] = React.useState({QuarterlyPayout: 0, triannualPayout:0, OtherPayout:0, AnnualPayout:0, spent:0});
    const [portfolioRisk, setPortfolioRisk] = React.useState('None');
    const [sectorsOccupied, setSectorsOccupied] = React.useState([]);
    const stocks = props.dashboardRefresher
    console.log(stocks)


    React.useEffect(() =>{
        let user_id = props.user? props.user.id:'0'
        let data = {user_id}
        fetch('/api/get-all-payouts',
        {method: "POST",  body: JSON.stringify(data),  headers: {'Content-Type': 'application/json'}})
        .then(response => response.json())
        .then(data => {
            // console.log('here',data)
            console.log(props)
            setPayouts(data)
        });
    },[stocks]);

    React.useEffect(() =>{
        let user_id = props.user? props.user.id:'0'
        let data = {user_id}
        fetch('/api/get-profile-info',
        {method: "POST",  body: JSON.stringify(data),  headers: {'Content-Type': 'application/json'}})
        .then(response => response.json())
        .then(data => {
            // console.log('here',data)
            setPortfolioRisk(data['PortfolioRisk'])
            setSectorsOccupied(data['Industries'])
        });
    },[stocks]);



    return (
        <Row id="user-dashboard">

        <Col>

            <Table size="sm">
                <tbody>
                    <tr>
                    <td>Quarterly Income:</td>
                    <td>{payouts.QuarterlyPayout}</td>
                    <td></td>
                    </tr>
                    <tr>
                    <td>Triannual Income:</td>
                    <td>{payouts.triannualPayout}</td>
                    <td></td>
                    </tr>
                    <tr>
                    <td>Other Income:</td>
                    <td>{payouts.OtherPayout}</td>
                    </tr>
                    <tr>
                    <td>Total Annual Income:</td>
                    <td className="green">{payouts.AnnualPayout}</td>
                    <td>Total Spent:</td>
                    <td></td>
                    <td className="red">{payouts.spent}</td>
                    </tr>
                </tbody>
            </Table>

        </Col>

        <Col>

            <Table size="sm">
                    <tbody>
                        <tr>
                        <td>Portfolio Risk:</td>
                        <td className={portfolioRisk === 'High'?  "red" : "green"}>{portfolioRisk}</td>
                        <td></td>
                        </tr>
                        <tr>
                        <td>Sectors Occupied:</td>
                        <td>{sectorsOccupied}</td>
                        <td></td>
                        </tr>
                    </tbody>
            </Table>

        </Col>

        </Row>
    )

}