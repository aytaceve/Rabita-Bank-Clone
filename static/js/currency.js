// Currency Functions on index.html
let convert_rate = document.getElementById('convert_rate');
let convert_result = document.getElementById('convert_result');
let convert_from = document.getElementById('convert_from');
let convert_to = document.getElementById('convert_to');
let buyAndSell = document.getElementById('buy-sell');
let cashAndCard = document.getElementById('cash-card');
let buyingRates = document.querySelectorAll('.buyingRates li');
let sellingRates = document.querySelectorAll('.sellingRates li');
let buyByCashCurrencyList = [];
let sellByCashCurrencyList = [];
let buyByCardCurrencyList = [];
let sellByCardCurrencyList = [];

// Functions to show exchange rates' list
$(document).ready(function(){
    for (let i = 0; i< sellingRates.length; i++){
        let y = (parseFloat(sellingRates[i].textContent) * 97/100).toFixed(4);
        buyByCashCurrencyList.push(y);
        buyingRates[i].querySelector('p').innerHTML = y;
    };
    for (let i = 0; i< sellingRates.length; i++){
        sellByCashCurrencyList.push((parseFloat(sellingRates[i].textContent)).toFixed(4));
        sellingRates[i].querySelector('p').innerHTML = sellByCashCurrencyList[i];
    };
    for (let i = 0; i< sellingRates.length; i++){
        let y = (parseFloat(sellingRates[i].textContent) * 96/100).toFixed(4);
        buyByCardCurrencyList.push(y);
        buyingRates[i].querySelector('p').innerHTML = y;
        };
    for (let i = 0; i< sellingRates.length; i++){
        let y = (parseFloat(sellingRates[i].textContent) * 99/100).toFixed(4);
        sellByCardCurrencyList.push(y);
        sellingRates[i].querySelector('p').innerHTML = y;
        };      
});

// Functions for 'Nağd' vs 'Nağdsız' options 
function cashVsCard(x){
    if(x == 'Nağd'){
        for (let i = 0; i< buyByCashCurrencyList.length; i++){
            buyingRates[i].querySelector('p').innerHTML = buyByCashCurrencyList[i];
    };
        for (let i = 0; i< sellByCashCurrencyList.length; i++){
            sellingRates[i].querySelector('p').innerHTML = sellByCashCurrencyList[i];
    };
   }else if(x == 'Nağdsız'){
        for (let i = 0; i< buyByCardCurrencyList.length; i++){
            buyingRates[i].querySelector('p').innerHTML = buyByCardCurrencyList[i];
    };
        for (let i = 0; i< sellByCardCurrencyList.length; i++){
            sellingRates[i].querySelector('p').innerHTML = sellByCardCurrencyList[i];
    };
   }
   y = convert_rate.value;
    changeResult(y);
};
// Functions for 'Alış' vs 'Satış' options 
function buyVsSell(){
   y = convert_rate.value;
    changeResult(y);
};

// Functions to disable selected currency option
function changeCurrency1(){
    let x = convert_from.selectedIndex;
    for(let i=0; i < convert_to.options.length; i++){
        if (i == x){
           convert_to.options[i].setAttribute('disabled', 'disabled');
        }else{
            convert_to.options[i].removeAttribute('disabled');
        }
    } 
    y = convert_rate.value;
    changeResult(y);
}
function changeCurrency2(){
    let x = convert_to.selectedIndex;
    for(let i=0; i < convert_from.options.length; i++){
        if (i == x){
           convert_from.options[i].setAttribute('disabled', 'disabled');
        }else{
            convert_from.options[i].removeAttribute('disabled');
        }
    } 
    y = convert_rate.value;
    changeResult(y);
}

// Function to change input value
convert_rate.addEventListener('input', function () {
    convert_rate.value = this.value;
});

// Function to get currency values
convert_to.addEventListener('select', function(){
    convert_to.value =  this.value;
    changeResult(this.value);
})

convert_from.addEventListener('select', function(){
    convert_from.value = this.value;
    changeResult(this.value);
})


// Function to change result amount
function changeResult(x){
    if(buyAndSell.value == 'Alış' && cashAndCard.value == 'Nağd'){
        if(convert_from.value == 'azn' && convert_to.value == 'gbp' ){
            result =( x / buyByCashCurrencyList[0]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'azn' && convert_to.value == 'eur' ){
            result = (x / buyByCashCurrencyList[1]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'azn' && convert_to.value == 'usd' ){
            result = (x / buyByCashCurrencyList[2]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'gbp' && convert_to.value == 'azn' ){
            result = (x * buyByCashCurrencyList[0]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'eur' && convert_to.value == 'azn' ){
            result = (x * buyByCashCurrencyList[1]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'usd' && convert_to.value == 'azn' ){
            result = (x * buyByCashCurrencyList[2]).toFixed(4);
            convert_result.value = result;
        }
        else{
            convert_result.value = '';
        }
    }
    else if (buyAndSell.value == 'Satış' && cashAndCard.value == 'Nağd'){
        if(convert_from.value == 'azn' && convert_to.value == 'gbp' ){
            result =( x / sellByCashCurrencyList[0]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'azn' && convert_to.value == 'eur' ){
            result = (x / sellByCashCurrencyList[1]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'azn' && convert_to.value == 'usd' ){
            result = (x / sellByCashCurrencyList[2]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'gbp' && convert_to.value == 'azn' ){
            result = (x * sellByCashCurrencyList[0]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'eur' && convert_to.value == 'azn' ){
            result = (x * sellByCashCurrencyList[1]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'usd' && convert_to.value == 'azn' ){
            result = (x * sellByCashCurrencyList[2]).toFixed(4);
            convert_result.value = result;
        }
        else{
            convert_result.value = '';
        }
    }else if (buyAndSell.value == 'Alış' && cashAndCard.value == 'Nağdsız'){
        if(convert_from.value == 'azn' && convert_to.value == 'gbp' ){
            result =( x / buyByCardCurrencyList[0]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'azn' && convert_to.value == 'eur' ){
            result = (x / buyByCardCurrencyList[1]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'azn' && convert_to.value == 'usd' ){
            result = (x / buyByCardCurrencyList[2]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'gbp' && convert_to.value == 'azn' ){
            result = (x * buyByCardCurrencyList[0]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'eur' && convert_to.value == 'azn' ){
            result = (x * buyByCardCurrencyList[1]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'usd' && convert_to.value == 'azn' ){
            result = (x * buyByCardCurrencyList[2]).toFixed(4);
            convert_result.value = result;
        }
        else{
            convert_result.value = '';
        }
    }else if (buyAndSell.value == 'Satış' && cashAndCard.value == 'Nağdsız'){
        if(convert_from.value == 'azn' && convert_to.value == 'gbp' ){
            result =( x / sellByCardCurrencyList[0]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'azn' && convert_to.value == 'eur' ){
            result = (x / sellByCardCurrencyList[1]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'azn' && convert_to.value == 'usd' ){
            result = (x / sellByCardCurrencyList[2]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'gbp' && convert_to.value == 'azn' ){
            result = (x * sellByCardCurrencyList[0]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'eur' && convert_to.value == 'azn' ){
            result = (x * sellByCardCurrencyList[1]).toFixed(4);
            convert_result.value = result;
        }
        else if(convert_from.value == 'usd' && convert_to.value == 'azn' ){
            result = (x * sellByCardCurrencyList[2]).toFixed(4);
            convert_result.value = result;
        }
        else{
            convert_result.value = '';
        }
    }
}
