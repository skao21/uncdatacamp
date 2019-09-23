// from data.js
var ufoData = data;

// assigning variables
    // select the submit button
var submit = d3.select("#filter-btn");
    //select the body
var tbody = d3.select("tbody");

function sighting(sightingData) {
    tbody.html("");
    sightingData.forEach((record) => {
        var row = tbody.append("tr");
        Object.entries(record).forEach(([key, value]) => {
        var cell = tbody.append("td");
        cell.text(value);
    });
})};

//  Initial output
sighting(ufoData);

// take the input from the user and filter the data (submit was assigned above)
submit.on("click", function() {

    // Prevent the page from refreshing
    d3.event.preventDefault();

    // Get the value property of the input element
    var values = d3.select("#datetime").property("value");
  
    // filter the data table to match user's input
    var filteredData = ufoData.filter(sightingRows => sightingRows.datetime === values);
    
    // displayed filtered data
    sighting(filteredData);
});
