function myFunction() {
    console.log("Megnyomtál!");
}

function adatFetcheles(adat) {
    fetch(adat)
        .then(response => response.json())
        .then((data) => {
            const recept = JSON.parse(data);
            document.getElementById("recept-nev").innerHTML = recept.nev;
        })
        .catch((err) => console.log(err));
}