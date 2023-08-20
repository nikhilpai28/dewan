import React, { useEffect } from 'react';
import './Softwares.css';
import './PluginItem.css'
import './PluginsList.css'
import { useState } from 'react';

const Softwares = (props) => {

    const [message, setMessage] = useState('');
    const [currentVersion, setCurrentVersion] = useState('')
    const [newVersion, setNewVersion] = useState('')
    const [required,setRequired] = useState(false)



    const checkValues = currentVersion === newVersion
    
    const pluginButtonHandler = () => {
        fetch('http://127.0.0.1:8000/')
            .then(response => response.json())
            .then(data => setMessage(data.message))
            .catch(error => console.error(error));
    }

    useEffect(() => {
        fetch('http://localhost:8000/get_versions')
            .then(response => response.json())
            .then(data => {
                setCurrentVersion(data[0]);
                setNewVersion(data[1])
            })

        fetch('http://localhost:8000/store') 

        setRequired(currentVersion === newVersion)
    }, [])

    const installHandler = () => {
        console.log("debug")
        fetch("http://localhost:8000/install")
    }
    return (
        <div className='main'>
            <table className='table'>
                <tr>
                    <th>Software</th>
                    <th>Current Version</th>
                    <th>New Version</th>
                    <th>Install</th>
                </tr>
                <tr>
                    <td>Python</td>
                    <td>{currentVersion}</td>
                    <td>{newVersion}</td>
                    {required && (<td><button onClick={installHandler}>Install</button></td>)}
                </tr>
            </table>
        </div>
    );
};

export default Softwares;
