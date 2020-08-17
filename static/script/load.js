function onPageLoad() {

    console.log( "document loaded" );
    // var url = "http://127.0.0.1:5000/get_AIRLINE";
    var url = " https://us-flight-delay-predicter.herokuapp.com/airline";    
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
    var url = " https://us-flight-delay-predicter.herokuapp.com/origin";
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
    var url = " https://us-flight-delay-predicter.herokuapp.com/destination";
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
