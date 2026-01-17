const tg = window.Telegram.WebApp;
tg.ready();

function sendOrder() {
    tg.sendData("buyurtma");
    tg.close();
}
