function onPageload(){
    console.log("page loaded");
    var url="http://127.0.0.1:5000/dummy";
    $.get(url);
}
function onClickPredict(){
    console.log("iris data prediction");
    var sl=document.getElementById("sepal_length");
    var sw=document.getElementById("sepal_width");
    var pl=document.getElementById("petal_length");
    var pw=document.getElementById("petal_width");
    var pred=document.getElementById('prediction');
    console.log(sl.value,pw.value);
    var url="http://127.0.0.1:5000/predict";

    $.post(url,{
        sepal_length: sl.value,
        sepal_width: sw.value,
        petal_length: pl.value,
        petal_width: pw.value
    },function(data,status){
        console.log(data.prediction);
        pred.innerHTML="<h2>"+data.prediction.toString()+"</h2>"
        console.log(status)

    });
}

window.onload=onPageload;