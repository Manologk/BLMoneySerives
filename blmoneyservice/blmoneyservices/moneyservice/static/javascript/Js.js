const left = document.getElementById("leftInput");
var right = document.getElementById("rightInput");


var total_amount, commission;
var percentage_1 = 0.06;
var percentage_2 = 0.08;

var usd_rub_buying = 60;
var usd_rub_selling = 59;
var zmw_usd_buying = 17;
var zmw_usd_selling = 16.5;


function rub2kwacha(amount, usd_rub_buying, zmw_usd_selling){
    let x = amount / usd_rub_buying;
    let y = x * zmw_usd_selling;

    var percentage_1 = 0.06;
    var percentage_2 = 0.08;

    if (x <= 200){
        commission = y * percentage_2;
    }
    else{
        commission = y * percentage_1;
    }
    total_amount = y + commission;

    return {'amount': roundToTwo(total_amount), 'commission': roundToTwo(commission)}
}


function roundToTwo(num) {
    return +(Math.round(num + "e+2")  + "e-2");
}

function double(x){
    return x * 2;
}


left.addEventListener("input", () =>{
    console.log(double(left.value));
    // document.getElementById("rightInput").value = double(left.value);
    amount = rub2kwacha(left.value, 60, 16.5)
    right.value = amount['amount'];
})

function ani(){
    document.getElementById("img").classList.add('classname');
}




