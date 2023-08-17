import logo from './logo.svg';
import './App.css';
import Plugins from './components/Plugins';
import image from './assets/dewan.jpeg'
import { useState,useEffect } from 'react';

function App() {

  const [showPlugins, setShowPlugins] = useState(false)


  const pluginHandler = () => {
    setShowPlugins(true)
  }

  const cancelHandler = () => {
    setShowPlugins(false)
  }

  // useEffect(() => {
  //   fetch('http://127.0.0.1:8000/')
  //     .then(response => response.json())
  //     .then(data => setMessage(data.message))
  //     .catch(error => console.error(error));
  // }, []);

  return (
    <div className="button-screen-container">
      <div className="App">
        <img src={image} className='expanded-image' />

      </div>
  
      <div>
        <div className='container'>
          <button onClick={pluginHandler} className='button'>Show Plugins</button>
        </div>
        {showPlugins && <Plugins oncancel={cancelHandler} />}

      </div>

    </div>
  );
}

export default App;
