async function getData() {
    const searchInput = document.getElementById("search"); 
    const city = searchInput.value.trim(); // Get the value and remove extra spaces

    if (!city) {
        alert("Please enter a city name!");
        return;
    }
    
    try {
        const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=8f0dfbae67a42f2745a6fea2bd772c49&units=metric`);
        const data = await response.json(); 
        console.log(data); 
        document.getElementById("temp").innerHTML = data.main.temp + "°C";
        document.getElementById("ws").innerHTML = data.main.sea_level ? data.main.sea_level + " m" : "N/A";
        document.getElementById("hmdty").innerHTML = data.main.humidity + "%";
    } catch (err) {
        console.error("Error fetching weather data:", err);
        alert("Failed to fetch weather data. Please try again.");
    }
}

// Add event listener for Enter key on the input field
const ssearchInput = document.getElementById("search");
ssearchInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        getData();
    }
});
