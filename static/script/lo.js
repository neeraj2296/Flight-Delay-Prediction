function onClickedPredictdelay() {
    console.log("Predicted delay button clicked");
    var MONTH = document.getElementById("uimonth");
    var DAY = document.getElementById("uiday");
    var DAY_OF_WEEK = document.getElementById("uiday_of_week");
    var AIRLINE = document.getElementById("uiAirline");
    var ORIGIN_AIRPORT = document.getElementById("uiorigin_airport");
    var DESTINATION_AIRPORT = document.getElementById("uidestination_airport");
    var SCHEDULED_TIME = document.getElementById("uischeduled_time");
    var DISTANCE = document.getElementById("uidistance");
    var ARRIVAL_DELAY = document.getElementById("uiarrival_delay");
    var Scheduled_dep_hour = document.getElementById("uischeduled_dep_hour");
    var Scheduled_dep_min = document.getElementById("uischeduled_dep_min");
    var Scheduled_arr_hour = document.getElementById("uischeduled_arr_hour");
    var Scheduled_arr_min = document.getElementById("uischeduled_arr_min");
    var estdelay = document.getElementById("uipredicteddelay");
  
    // var url = ""; 
  
    var url = "http://127.0.0.1:5000/predict";
  
    $.post(url, {
        MONTH: parseFloat(MONTH.value),
        DAY: parseFloat(DAY.value),
        DAY_OF_WEEK: DAY_OF_WEEK.value,
        AIRLINE: AIRLINE.value,
        ORIGIN_AIRPORT: ORIGIN_AIRPORT.value,
        DESTINATION_AIRPORT: DESTINATION_AIRPORT.value,
        SCHEDULED_TIME: parseFloat(SCHEDULED_TIME.value),
        DISTANCE: parseFloat(DISTANCE.value),
        ARRIVAL_DELAY: parseFloat(ARRIVAL_DELAY.value),
        Scheduled_dep_hour: parseFloat(Scheduled_dep_hour.value),
        Scheduled_dep_min: parseFloat(Scheduled_dep_min.value),
        Scheduled_arr_hour: parseFloat(Scheduled_arr_hour.value),
        Scheduled_arr_min: parseFloat(Scheduled_arr_min.value)    
    },function(data, status) {
        console.log(data.estimated_delay);
        estdelay.innerHTML = "<h2>" + data.estimated_delay.toString() + "mins</h2>";
        console.log(status);
    });
  }
function onPageLoad() {
    console.log( "document loaded" );
    // var url = "http://127.0.0.1:5000/get_Origin_airport"; 
    var url = "http://127.0.0.1:5000/origin";
    $.get(url,function(data, status) {
        console.log("got response for get_Origin_airport request");
        if(data) {
            var Origin_airport = data.ORIGIN_AIRPORT;
            var uiorigin_airport = document.getElementById("uiorigin_airport");
            $('#uiorigin_airport').empty();
            for(var i in Origin_airport) {
                var opt = new Option(Origin_airport[i]);
                $('#uiorigin_airport').append(opt);
            }
        }
    });
}

{
    console.log( "document loaded" );
    // var url = ""; 
    var url = "http://127.0.0.1:5000/destination";
    $.get(url,function(data, status) {
        console.log("got response for get_Destination_airport request");
        if(data) {
            var Destination_airport = data.ORIGIN_AIRPORT;
            var uidestination_airport = document.getElementById("uidestination_airport");
            $('#uidestination_airport').empty();
            for(var i in Destination_airport) {
                var opt = new Option(Destination_airport[i]);
                $('#uidestination_airport').append(opt);
            }
        }
    });
}

{
    console.log( "document loaded" );
    // var url = "http://127.0.0.1:5000/get_AIRLINE";
    var url = "http://127.0.0.1:5000/airline";    
    $.get(url,function(data, status) {
        console.log("got response for get_AIRLINE request");
        if(data) {
            var Airline = data.AIRLINE;
            var uiAirline = document.getElementById("uiAirline");
            $('#uiAirline').empty();
            for(var i in Airline) {
                var opt = new Option(Airline[i]);
                $('#uiAirline').append(opt);
            
            }
        }
    });
}


  
window.onload = onPageLoad;
