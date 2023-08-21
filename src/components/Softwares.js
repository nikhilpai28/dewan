import React, { useEffect } from 'react';
import './Softwares.css';
import './PluginItem.css'
import './PluginsList.css'
import { useState } from 'react';
import constClass from '../Constants';

const Softwares = (props) => {

    const [currentVersion, setCurrentVersion] = useState('')
    const [newVersion, setNewVersion] = useState('')


    useEffect(() => {
        console.log("debug")
        fetch(constClass.GET_VERSIONS)
            .then(response => response.json())
            .then(data => {
                setCurrentVersion(data[0]);
                setNewVersion(data[1])
            })

        fetch(constClass.STORE)

    }, [])

    const installHandler = () => {
        console.log("debug")
        fetch(constClass.INSTALL)
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
                    
                    {currentVersion === newVersion ? (<p>Already updated to the latest version!</p>):
                    (<td><button onClick={installHandler}>Install</button></td>)}
                </tr>
            </table>
        </div>
    );
};

export default Softwares;
