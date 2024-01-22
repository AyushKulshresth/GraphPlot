function loadJson(selector) {
    return JSON.parse(document.querySelector(selector).getAttribute("data"));
}

window.onload = function(){
    var jsonData = loadJson("#my-data");

    // console.log(jsonData);

    var data = [];

    for (let i = 0; i<jsonData.length; i++){
        jsonData[i]["type"] = "bar";
        jsonData[i]["name"] = "All Matches";
        data.push(jsonData[i]);
    }

    // console.log(data);

    var layout = {
        title: 'Number of Matches played per Season',
        font:{
          family: 'Raleway, sans-serif'
        },
        showlegend: true,
        xaxis: {
          tickangle: -90
        },
        yaxis: {
          zeroline: false,
          gridwidth: 2
        },
        bargap :0.5,
        width: 1000,
        height: 600
      };

    ele = document.getElementById("graph");

    Plotly.newPlot(ele, data, layout);
}
