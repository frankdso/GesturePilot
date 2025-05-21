import { useState, useEffect } from 'react';

function App() {
  const [logs, setLogs] = useState<string[]>([]);

  const startGesturePilot = () => {
    window.electron.ipcRenderer.send('start-gesturepilot');
    setLogs(logs => [...logs, '🚀 Started GesturePilot...']);
  };

  const stopGesturePilot = () => {
    window.electron.ipcRenderer.send('stop-gesturepilot');
    setLogs(logs => [...logs, '🛑 Stopped GesturePilot...']);
  };

  useEffect(() => {
    window.electron.ipcRenderer.on('gesture-log', (msg: string) => {
      setLogs(logs => [...logs, msg]);
    });
  }, []);

  return (
    <div className="relative w-full h-screen bg-gradient-to-br from-black via-gray-900 to-black overflow-hidden flex items-center justify-center">
      {/* Pulsing Background Bubble */}
      <div className="absolute top-0 left-0 w-full h-full bg-[radial-gradient(circle_at_30%_30%,#9333ea_20%,transparent_40%)] opacity-10 animate-pulse" />

      {/* Centered Content */}
      <div className="relative z-10 flex flex-col items-center justify-center text-center px-4">
        <h1 className="text-6xl font-extrabold text-purple-400 mb-10 flex items-center gap-3">
          <span>🎯</span>
          <span>GesturePilot</span>
        </h1>

        <div className="flex space-x-6">
          <button
            onClick={startGesturePilot}
            className="px-8 py-4 bg-purple-600 hover:bg-purple-700 rounded-xl text-lg font-bold transition duration-300 shadow-lg"
          >
            Let’s Start
          </button>
          <button
            onClick={stopGesturePilot}
            className="px-8 py-4 bg-red-600 hover:bg-red-700 rounded-xl text-lg font-bold transition duration-300 shadow-lg"
          >
            Stop
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
