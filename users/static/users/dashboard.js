const form = document.getElementById("chart-form");
const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
const chartType = document.getElementById("id_chart");
const start = document.getElementById("id_start");
const last = document.getElementById("id_last");

const chartBlock = document.getElementById("show-chart");

const renderGraph = (response) => {
    chart = response["chart"];
    average = response["average"];
    stdDeviation = response["std_deviation"];
    minimum = response["minimum"];
    maximum = response["maximum"];
    // img_src = data:image/png;base64, {{ chart|safe}}
    // img = `<img src="data:image/png;base64,` + `{{ ${chart}|safe}}">`;
    chartBlock.src = "data:image/png;base64," + chart;
    document.getElementById("button-panel").classList.remove("d-none");
    document.getElementById("average").textContent = average.toFixed(2);
    document.getElementById("std-deviation").textContent =
        stdDeviation.toFixed(2);
    document.getElementById("minimum").textContent = minimum.toFixed(2);
    document.getElementById("maximum").textContent = maximum.toFixed(2);
};

form.addEventListener("submit", (e) => {
    e.preventDefault();
    // console.log(chartType.value);
    // console.log(start.value);
    // console.log(last.value);
    const formdata = new FormData();
    formdata.append("csrfmiddlewaretoken", csrf);
    formdata.append("chartType", chartType.value);
    formdata.append("start", start.value);
    formdata.append("last", last.value);

    $.ajax({
        type: "POST",
        url: "/dashboard-chart/",
        data: formdata,
        success: function (response) {
            // console.log(response["chart"]);
            renderGraph(response);
        },
        error: function (error) {
            console.log("error");
        },
        processData: false,
        contentType: false,
    });
});
