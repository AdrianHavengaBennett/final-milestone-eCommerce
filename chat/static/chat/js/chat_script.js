const roomName = JSON.parse(document.getElementById('room-name').textContent);

var loc = window.location
var wsStart = 'ws://'
if (loc.protocol == 'https:') {
    wsStart = 'wss://'
}

const chatSocket = new WebSocket(
    wsStart
    + loc.host
    + '/ws/chat/'
    + roomName
    + '/'
);

var textarea = document.getElementById('chat-log');
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.querySelector('#chat-log').value += (data.message + '\n');
    textarea.scrollTop = textarea.scrollHeight;
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

var elem = document.getElementById('chat-message-input');
window.onload = function () {
    elem.scrollIntoView();
    elem.focus();
}

document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
};
