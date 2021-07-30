const form = document.getElementById("chart-form");
const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
const chartType = document.getElementById("id_chart");
const start = document.getElementById("id_start");
const last = document.getElementById("id_last");

form.addEventListener("submit", (e) => {
    e.preventDefault();
    // console.log(chartType.value);
    // console.log(start.value);
    // console.log(last.value);
    const formdata = new FormData();
    formdata.append("csrfmiddlewaretoken", csrf);
    formdata.append("chartType", chartType);
    formdata.append("start", start);
    formdata.append("last", last);

    $.ajax({
        type: "POST",
        url: "",
        data: formdata,
        success: function (response) {
            console.log("success");
        },
        error: function (error) {
            console.log("error");
        },
        processData: false,
        contentType: false,
    });
});
