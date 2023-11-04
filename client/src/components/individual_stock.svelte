<script>
    // Stock Details
    let name = "stock-name";
    let price = "price";
    let open = "open";
    let ask = "ask";
    let day_range = "day-range";
    let volume = "volume";
    let company_name = "company-name";
    let financial_market = "financial-market";
</script>

<div id="stock_details">
    <table>
        <thead>
            <tr>
                <th></th>
                <th>{name}</th>
                <th>{company_name}</th>
                <th colspan="2">{financial_market}</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>Price</th>
                <th>{price}</th>
                <th>Open</th>
                <th>{open}</th>
                <th>Ask</th>
                <th>{ask}</th>
            </tr>
            <tr>
                <th>Day Range</th>
                <th>{day_range}</th>
                <th>Volume</th>
                <th>{volume}</th>
            </tr>
        </tbody>
    </table> 
</div>