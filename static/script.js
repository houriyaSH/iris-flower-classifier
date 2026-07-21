function predict() {

    let sepalLength = document.getElementById("sepalLength").value;
    let sepalWidth = document.getElementById("sepalWidth").value;
    let petalLength = document.getElementById("petalLength").value;
    let petalWidth = document.getElementById("petalWidth").value;


    // Check empty inputs
    if (
        sepalLength === "" ||
        sepalWidth === "" ||
        petalLength === "" ||
        petalWidth === ""
    ) {
        document.getElementById("result").innerHTML =
            "Please fill all fields";

        return;
    }


    // Check numbers
    if (
        isNaN(sepalLength) ||
        isNaN(sepalWidth) ||
        isNaN(petalLength) ||
        isNaN(petalWidth)
    ) {
        document.getElementById("result").innerHTML =
            "Please enter numbers only";

        return;
    }


    let data = {

        sepal_length: Number(sepalLength),
        sepal_width: Number(sepalWidth),
        petal_length: Number(petalLength),
        petal_width: Number(petalWidth)

    };


    fetch("/predict", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(data)

    })


    .then(response => response.json())


    .then(result => {


        if (result.prediction) {

            document.getElementById("result").innerHTML =
                "Prediction: " + result.prediction;

        }

        else if (result.error) {

            document.getElementById("result").innerHTML =
                result.error;

        }

    })


    .catch(error => {

        document.getElementById("result").innerHTML =
            "Something went wrong";

        console.log(error);

    });

}



function resetForm() {


    document.getElementById("sepalLength").value = "";

    document.getElementById("sepalWidth").value = "";

    document.getElementById("petalLength").value = "";

    document.getElementById("petalWidth").value = "";


    document.getElementById("result").innerHTML = "";

}