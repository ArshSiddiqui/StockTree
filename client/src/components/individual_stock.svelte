<script>
    // Stock Details
    export let name = "stock-name";
    export let price = "price";
    export let open = "open";
    export let ask = "ask";
    export let day_range = "day-range";
    export let volume = "volume";
    export let company_name = "company-name";
    export let financial_market = "financial-market";
    export let bid = "bid";
</script>

<div id="stock_details">
    <table>
        <thead>
            <tr>
                <th colspan="2">{name} - {company_name}</th>
                <!-- <th>{company_name}</th> -->
                <th colspan="2">{financial_market}</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>Price</th>
                <th>{price}</th>
                <th>Open</th>
                <th>{open}</th>
            </tr>
            <tr>
                <th>Ask</th>
                <th>{ask}</th>
                <th>Day Range</th>
                <th>{day_range}</th>
            </tr>
            <tr>
                <th>Volume</th>
                <th>{volume}</th>
                <th>Bid</th>
                <th>{bid}</th>
            </tr>
        </tbody>
    </table> 
</div>