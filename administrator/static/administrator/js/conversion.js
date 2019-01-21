var ngn = document.getElementById("id_NGN");
var usd = document.getElementById("id_USD");
var volume = document.getElementById("id_volume");
var btcDollarPrice = document.getElementById("btcDollarPrice");
var btcNGNPrice = document.getElementById("btcNGNPrice");

var btcPrice = document.getElementById("btcPrice").value;
var getNumbersAlone = btcPrice.substr(4);
var bitPrice = parseFloat(getNumbersAlone);

ngn.setAttribute('placeholder', "Amount In Nigerian Naira");
usd.setAttribute('placeholder', "Amount In United States Dollars");
volume.setAttribute('readonly', 'true');
volume.setAttribute('placeholder', 'Bitcoin Volume');

// this is for converting from ngn to usd
ngn.onkeyup = function() {
    var ngnBuyRate = bitPrice;
    var ngnValue = ngn.value / ngnBuyRate;
    usd.value = ngnValue.toFixed(2);
    // for the volume
    var volumeFormula = parseFloat(ngn.value) / parseFloat(btcNGNPrice.value);
    volume.value = volumeFormula;

}
// this is for converting from usd to ngn
usd.onkeyup = function() {
    var ngnBuyRate = bitPrice;
    var usdValue = usd.value * ngnBuyRate;
    ngn.value = usdValue.toFixed(2);
    // for the volume
    var volumeFormula2 = parseFloat(usd.value) / parseFloat(btcDollarPrice.value);
    volume.value = volumeFormula2;

}