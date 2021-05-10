function Route_setting() {
    window.open("/map/Enter_Route_Title", "a", "width=700, height=432, location=no, toolbars=no, menubar=no")
};

function Go_To_Station() {
    window.open("/main/Station", "_self")
};

function Station_Setting() {
    window.open("/map/Enter_Station_Title", "a", "width=700, height=432, location=no, toolbars=no, menubar=no")
};

function Go_To_Route() {
    window.open("/main/Route", "_self")
};


function Show_Map(target, route_or_station) {
    const form = document.createElement('form');
    window.open("", "new_window", "width=700, height=432, location=no, toolbars=no, menubar=no")
    form.method = 'POST';
    form.action = "/map/Show_Worker_Map";
    form.target = "new_window";

    const hiddenField = document.createElement('input');
    hiddenField.type = 'hidden';
    if (route_or_station == "0")
        hiddenField.name = "route_title";
    else
        hiddenField.name = "station_title";
    hiddenField.value = target;
    form.appendChild(hiddenField);

    const hiddenField2 = document.createElement('input');
    hiddenField2.type = 'hidden';
    hiddenField2.name = "flag";
    hiddenField2.value = route_or_station;
    form.appendChild(hiddenField2);

    document.body.appendChild(form);
    form.submit();
}

function OnloadImg(url) {
    var img = new Image();
    img.src = url;
    var img_width = img.width;
    var win_width = img.width;
    var height = img.height;
    var OpenWindow = window.open('', '_blank', "width=700, height=432, location=no, toolbars=no, menubar=no");
    OpenWindow.document.write("<style>body{margin:0px;}</style><img src='" + url + "' width='300'>");
}