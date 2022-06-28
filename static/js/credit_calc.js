//month Rangenin deyismesi
let output1 = document.getElementById("month");
let slider1 = document.getElementById("range1").oninput = function () {
    let value1 = (this.value - this.min)
    output1.innerHTML = value1;
};

//amount Rangenin deyismesi
let output2 = document.getElementById("amount");
let slider2 = document.getElementById("range2").oninput = function () {
    let value2 = (this.value - this.min)
    output2.innerHTML = value2;
};

//percent Rangenin deyismesi
let output3 = document.getElementById("percent");
let slider3 = document.getElementById("range3").oninput = function () {
    let value3 = (this.value - this.min)
    output3.innerHTML = value3;
};


$(document).ready(function () {
    let month;
    let amount;
    let percent;
    let total_amount;
    let percent_amount;
    let monthly_payment;

    //yekun ve qazanci hesablama funksiyasi
    function yekun(month, amount, percent) {
        // console.log(month, amount, percent)
        yekun_mebleg = parseInt(amount + amount * month * percent * 30 / 365 / 100);
        $('#percent_amount').text(yekun_mebleg - amount);
        $('#total_amount').text(yekun_mebleg);
        $('#monthly_payment').text((yekun_mebleg / month).toFixed(2));
    };

    //default values
    function defaultvalues() {
        month = parseInt($('#month').text());
        amount = parseInt($('#amount').text());
        percent = parseFloat($('#percent').text());
        total_amount = parseFloat($('#total_amount').text());
        percent_amount = parseFloat($('#percent_amount').text());
        monthly_payment = parseFloat($('#monthly_payment').text());
    };
    defaultvalues();

    if ($('#creditCalculator').click()) {
        $('#range1').on('change', function () {
            month = parseInt($('#month').text());
            yekun(month, amount, percent);
        });
        $('#range2').on('change', function () {
            amount = parseInt($('#amount').text());
            yekun(month, amount, percent);
        });
        $('#range3').on('change', function () {
            percent = parseFloat($('#percent').text());
            yekun(month, amount, percent);
        });
    };

});
