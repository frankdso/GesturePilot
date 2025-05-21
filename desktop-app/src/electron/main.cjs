const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let mainWindow;
let pythonBackend = null; // ✅ Add this line

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1024,
    height: 768,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      enableRemoteModule: false,
      nodeIntegration: false
    },
  });

  // mainWindow.loadURL('http://localhost:5173'); // Dev server
  const isDev = !app.isPackaged;

  if (isDev) {
    mainWindow.loadURL('http://localhost:5173');
  } else {
    mainWindow.loadFile(path.join(app.getAppPath(), 'dist', 'index.html'));
  }

}

app.whenReady().then(() => {
  createWindow();

ipcMain.on('start-gesturepilot', () => {
  if (!pythonBackend) {
    const pythonPath = path.join(process.resourcesPath, 'python-runtime', 'python.exe');
    const scriptPath = path.join(process.resourcesPath, 'backend', 'main.py');

    console.log("Launching GesturePilot with:");
    console.log("Python Path →", pythonPath);
    console.log("Script Path →", scriptPath);
    console.log("Exists?", require('fs').existsSync(pythonPath), require('fs').existsSync(scriptPath));
      

    pythonBackend = spawn(pythonPath, [scriptPath], {
      cwd: path.join(process.resourcesPath, 'python-runtime'),
    });

    pythonBackend.stdout.on('data', (data) => {
      console.log(`[PYTHON STDOUT]: ${data}`);
      mainWindow.webContents.send('gesture-log', `[PY] ${data.toString()}`);
    });

    pythonBackend.stderr.on('data', (data) => {
      console.error(`[PYTHON STDERR]: ${data}`);
      mainWindow.webContents.send('gesture-log', `[ERR] ${data.toString()}`);
    });

    pythonBackend.on('exit', () => {
      mainWindow.webContents.send('gesture-log', '🛑 GesturePilot stopped.');
      pythonBackend = null;
    });
  }
});


  ipcMain.on('stop-gesturepilot', () => {
    if (pythonBackend) {
      pythonBackend.kill();
      pythonBackend = null;
    }
  });

  app.on('before-quit', () => {
    if (pythonBackend) pythonBackend.kill();
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
