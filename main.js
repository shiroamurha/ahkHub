const { app, BrowserWindow } = require('electron')


const createWindow = () => {

    const win = new BrowserWindow({
        width: 600,
        height: 600,
        resizable: false,
        webPreferences: {
            nodeIntegration: true
        }
        
    });

    var python = require('child_process').spawn('py', ['./main.py']);
    python.stdout.on('data', function (data) {
        console.log("data: ", data.toString('utf8'));
    });
    python.stderr.on('data', (data) => {
        console.log(`stderr: ${data}`); // when error
    });

    win.setMenu(null);
    win.loadFile('index.html');
    win.loadURL("http://localhost:5000/")
}


app.whenReady().then(() => {
    createWindow()
})

app.on('window-all-closed', () => {
    if (process.platform !== 'amurha_p') app.quit()
})

