function DATE(){
    var DATE = document.getElementById("uiDATE").value;
    var year = "'"+DATE+"'";

    var date = new Date(year);
   
    var weekday = date.getDay()+1;

    var DAY = date.getDate();

    var MONTH = date.getMonth()+1;

    var calend =new Array(weekday, DAY, MONTH);
 
    return calend;
}

function SCHEDULED_DEPARTURE(){
    var DEPARTURE = document.getElementById("uiDEPARTURE").value;

    var dhour = DEPARTURE.slice(0, 2);

    var dmin = DEPARTURE.slice(3,5);

    var DEPART = parseInt(dhour.concat(dmin));
 
    return DEPART;
}

function STIME(){
    var TIME = document.getElementById("uiTIME").value;

    var ahour = TIME.slice(0,2);

    var amin = TIME.slice(3,5);

    var STIME = parseInt(ahour.concat(amin));

    return STIME;
}


function onClickedPredictdelay(){
    console.log("Predicted delay clicked");
    var MONTH = parseInt(DATE()[2]);
    console.log(MONTH);
    var DAY = DATE()[1];
    console.log(DAY);
    var DAY_OF_WEEK = DATE()[0];
    console.log(DAY_OF_WEEK);
    var AIRLINE = document.getElementById("uiAIRLINE");
    console.log(AIRLINE.value);
    var ORIGIN = document.getElementById("uiORIGIN");
    console.log(ORIGIN.value);
    var DESTIN = document.getElementById("uiDESTIN");
    console.log(DESTIN.value);
    var Scheduled_departure = SCHEDULED_DEPARTURE();
    console.log(Scheduled_departure);
    var Scheduled_Time = STIME();
    console.log(Scheduled_Time);
    var Arrival_delay = document.getElementById('uiARRIVAL_DELAY');
    console.log(Arrival_delay.value);
    var estdelay = document.getElementById('uipredict');
    console.log(estdelay);
    var url = "http://127.0.0.1:5000/predict";
    var dat = {
        MONTH: 11,//MONTH.value,
        DAY: 5,//DAY,
        DAY_OF_WEEK: 6,//DAY_OF_WEEK,
        AIRLINE: AIRLINE,
        ORIGIN_AIRPORT: ORIGIN,
        DESTINATION_AIRPORT: DESTIN,
        SCHEDULED_DEPARTURE: 1850,//Scheduled_departure,
        SCHEDULED_TIME: 1855,//Scheduled_Time,
        ARRIVAL_DELAY: -44,//Arrival_delay
        }
    console.log(typeof(dat));
    console.log(typeof(JSON.parse(dat)));
    // sleep(1000*60)
    $.post(url,JSON.stringify(dat)),
        function(data, status)  {
            console.log(data.est_delay);
            estdelay.innerHTML = "<h2>Your Flight might depart" + data.est_delay + " mins </h2>";
            console.log(status);
        };


}


function onPageLoad() {

    console.log( "document loaded" );
    // var url = "http://127.0.0.1:5000/get_AIRLINE";
    var url = " https://us-flight-delay-predictor.herokuapp.com/airline";    
    $.get(url,function(data, status) {
        console.log("got response for get_AIRLINE request");
        if(data) {
            var AIRLINE = data.AIRLINE;
            var uiAIRLINE = document.getElementById("uiAIRLINE");
            $('#uiAIRLINE').empty();
            for(var i in AIRLINE) {
                var opt = new Option(AIRLINE[i]);
                $('#uiAIRLINE').append(opt);
            
            }
        }
    });
    console.log( "document loaded" );
    // var url = ""; 
    var url = " https://us-flight-delay-predictor.herokuapp.com/origin";
    $.get(url,function(data, status) {
        console.log("got response for get_Destination_airport request");
        if(data) {
            var ORIGIN = data.ORIGIN;
            var uiORIGIN = document.getElementById("uiORIGIN");
            $('#uiORIGIN').empty();
            for(var i in ORIGIN) {
                var opt = new Option(ORIGIN[i]);
                $('#uiORIGIN').append(opt);
            }
        }
    });
    console.log( "document loaded" );
    // var url = ""; 
    var url = " https://us-flight-delay-predictor.herokuapp.com/destination";
    $.get(url,function(data, status) {
        console.log("got response for get_Destination_airport request");
        if(data) {
            var DESTIN = data.DESTIN;
            var uiDESTIN = document.getElementById("uiDESTIN");
            $('#uiDESTIN').empty();
            for(var i in DESTIN) {
                var opt = new Option(DESTIN[i]);
                
                $('#uiDESTIN').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;
