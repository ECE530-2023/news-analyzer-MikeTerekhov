import logo from './logo.svg';
import { useEffect, useState } from 'react';
import jwt_decode from "jwt-decode";
import './App.css';
import React from 'react';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Routes, Route}
    from 'react-router-dom';
import About from './components/pages/about';
import Home from './components/pages/home';

function App() {
  const [ user, setUser ] = useState({});

  function handleCallbackResponse(response){
    console.log("Encoded JWT ID token: " + response.credential);
    var userObject = jwt_decode(response.credential);
    console.log(userObject);
    setUser(userObject);
    document.getElementById("signInDiv").hidden = true;
  }

  function handleSignOut(event){
    setUser({});
    document.getElementById("signInDiv").hidden = false;
  }

  useEffect(() => {
    /* global google */
    google.accounts.id.initialize({
      client_id : "1084845137503-uppgp698bga93em102f069qq6r0vsq4s.apps.googleusercontent.com",
      callback : handleCallbackResponse
    });

    google.accounts.id.renderButton(
      document.getElementById("signInDiv"),
      { theme : "outline", size : "large"}
    );

    google.accounts.id.prompt();

  }, [])
  // If we have no user : sign in button
  // If we have a user : show logout button

  return (
    <div className="App">

    <Router>
      <Navbar />
      <Routes>
        <Route exact path='/home' element={<Home />} />
        <Route path='/about' element={<About/>} />
      </Routes>
    </Router>

     <div id = "signInDiv"></div>
     { Object.keys(user).length != 0 &&
        <button onClick = { (e) => handleSignOut(e)}>Sign Out</button>
     }
     { user &&
     <div>
      <img src = {user.picture}></img>
      <h3>{user.name}</h3>
    </div>
     }
    </div>
  );
}

export default App;
