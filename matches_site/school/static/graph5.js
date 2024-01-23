function loadJson(selector) {
    return JSON.parse(document.querySelector(selector).getAttribute("data"));
}

window.onload = function(){
    var jsonData = loadJson("#my-data");

    var data = [];

    for (let x in jsonData){
        var temp = {};
        temp["name"] = x;
        temp["type"] = "bar";
        temp["x"] = [];
        temp["y"] = [];
        for(let j=0; j<jsonData[x].length; j++)
        {
            temp["x"].push(jsonData[x][j]["district"]);
            temp["y"].push(jsonData[x][j]["cCount"]);
        }
        // if (x === 'Mumbai Indians'){
        //     console.log("adfvb")
        //     temp['name'] = 'draw'; 
        // }
        data.push(temp);
    }

    // console.log(data);

    var layout = {
        barmode: 'stack',
        title: 'Number of languages per district',
        font:{
          family: 'Raleway, sans-serif'
        },
        showlegend: true,
        xaxis: {
          tickangle: -30
        },
        yaxis: {
          zeroline: false,
          gridwidth: 2
        },
        bargap :0.5,
        width: 1200,
        height: 700
      };

    ele = document.getElementById("graph");

    Plotly.newPlot(ele, data, layout);
}