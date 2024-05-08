function Predict() {
    var size = document.getElementById('size').value;
    var bedrooms = document.getElementById('bedrooms').value;
    var show = document.getElementById('predicted_price'); 

  

    var data = {
        "size":size,
        "bedrooms":bedrooms
    };

    fetch('https://65.0.61.158/predict',{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        show.innerText = 'Predicted price $' + data.predicted_price;
    })
}
