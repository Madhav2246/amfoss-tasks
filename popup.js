document.getElementById("searchButton").addEventListener("click", () => {
  const locationInput = document.getElementById("locationInput").value;
  if (locationInput) {
    fetchWeather(locationInput);
  }
});

function fetchWeather(location) {
  
  const apiKey = "6d2cfe94b13df6d6bc4c99763aa23df3";
  const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey}&units=metric`;

  fetch(apiUrl)
    .then((response) => response.json())
    .then((data) => {
      const weatherInfo = document.getElementById("weatherInfo");
      weatherInfo.innerHTML = `
        <h3>Weather in ${data.name}, ${data.sys.country}</h3>
        <p>${data.weather[0].description}</p>
        <p>Temperature: ${data.main.temp}°C</p>
        <p>Humidity: ${data.main.humidity}%</p>
      `;
    })
    .catch((error) => {
      console.error(error);
      const weatherInfo = document.getElementById("weatherInfo");
      weatherInfo.innerHTML = "<p>Weather data not available.</p>";
    });
}

