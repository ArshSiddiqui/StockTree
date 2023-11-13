<script>
    // Country Details
    export let name = "country-name";
    export let unemployment_rate = 0;
    export let gdp = 0;
    export let inflation_rate = 0;
    export let population = 0;

</script>

<div id="stock_details">
    <table>
        <thead>
            <tr>
                <th colspan="4">{name}</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>Unemployment Rate</th>
                <th>{unemployment_rate}%</th>
                <th>GDP</th>
                <th>{gdp}</th>
            </tr>
            <tr>
                <th>inflation Rate</th>
                <th>{inflation_rate}%</th>
                <th>population</th>
                <th>{population}</th>
            </tr>
        </tbody>
    </table> 
</div>