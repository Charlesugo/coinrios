var ngn = document.getElementById("id_NGN");
var usd = document.getElementById("id_USD");
var volume = document.getElementById("id_volume");

var ethereumPrice = document.getElementById("ethereumPrice").value;
var getNumbersAlone = ethereumPrice.substr(4);
// convert to float number
var ethPrice = parseFloat(getNumbersAlone);

ngn.setAttribute('placeholder', "Amount In Nigerian Naira");
//ngn.setAttribute('min', '1');
usd.setAttribute('placeholder', "Amount In United States Dollars");
volume.setAttribute('readonly', 'true');
volume.setAttribute('placeholder', 'Ethereum Volume');

// this is for converting from ngn to usd
ngn.onkeyup = function() {
    var ngnBuyRate = ethPrice;
    var ngnValue = ngn.value / ngnBuyRate;
    usd.value = ngnValue.toFixed(2);
    // for the volume -- we are going to use the api key to get the actual amount of these coins
    //  ngnPrice or usdPrice / actual amount
    var volumeFormula = parseFloat(ngn.value) / ethPrice;
    volume.value = volumeFormula;
}
//    // this is for converting from usd to ngn
usd.onkeyup = function() {
    var ngnBuyRate = ethPrice;
    var usdValue = usd.value * ngnBuyRate;
    ngn.value = usdValue.toFixed(2);
    // for the volume -- we are going to use the api key to get the actual amount of these coins
    //  ngnPrice or usdPrice / actual amount
    var volumeFormula2 = parseFloat(ngn.value) / ethPrice;
    volume.value = volumeFormula2;
}