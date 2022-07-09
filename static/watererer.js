function update_moisture() {
    let ws = new WebSocket("ws://" + window.location.host + "/read_live")
    ws.onmessage = function (event) {
    document.getElementById('moisture').innerText = event.data;
    }

}


window.onload = update_moisture();

// TODO: properly close websockets