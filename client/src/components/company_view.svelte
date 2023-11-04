<script>
    import IndividualStock from "./individual_stock.svelte";

    export let companyName = "company-name";

    // Company Details
    let ceo = "ceo-name";
    let industry = "industry-name";
    let abbreviation = "abbreviation";

</script>

<div id="company-header">
    <h2>{companyName}</h2>

    <div id="company-details">
        <h3>CEO: {ceo}</h3>
        <h3>Industry: {industry}</h3>
        <h3>Primary Stock Abbreviation: {abbreviation}</h3>
    </div>

    <svelte:component this={IndividualStock}></svelte:component>
</div>
