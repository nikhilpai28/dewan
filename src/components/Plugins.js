import React from 'react';
import './Plugins.css';
import './PluginItem.css'
import './PluginsList.css'
import { useState } from 'react';

const Plugins = (props) => {

    const [message, setMessage] = useState('');

    const onCancelHandler = () => {
        props.oncancel()
    }

    const pluginButtonHandler = () => {
        fetch('http://127.0.0.1:8000/')
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(error => console.error(error));
    }


    return (
        <ul className='plugins-list'>
            <li className="plugin-item">
                <div className="plugin-item__description"><h2>Plugin 1</h2></div>
                <button className="plugin-item__price" onClick={pluginButtonHandler}>Click here</button>
                {message}
            </li>
            <li className="plugin-item">
                <div className="plugin-item__description"><h2>Plugin 2</h2></div>
                <button className="plugin-item__price" onClick={pluginButtonHandler}>Click here</button>
                {message}
            </li>
            <li className="plugin-item">
                <div className="plugin-item__description"><h2>Plugin 3</h2></div>
                <button className="plugin-item__price" onClick={pluginButtonHandler}>Click here</button>
                {message}
            </li>
            <li className="plugin-item">
                <div className="plugin-item__description"><h2>Plugin 4</h2></div>
                <button className="plugin-item__price" onClick={pluginButtonHandler}>Click here</button>
                {message}
            </li>
            <div className='container'>
                <button className='button' onClick={onCancelHandler}>Hide Plugins</button>
            </div>
        </ul>
    );
};

export default Plugins;
