import logo from './logo.svg';
import { useEffect, useState } from 'react';
import jwt_decode from "jwt-decode";
import './App.css';
import React from 'react';
import Navbar from './components/Navbar';
import Navbar2 from './components/Navbar';
import { BrowserRouter as Router, Routes, Route, Navigate}
    from 'react-router-dom';
import About from './components/pages/about';
import Home from './components/pages/home';
import SecretPage from './components/pages/secret_page';
import List_documents from './components/pages/list_documents';
import { Link } from 'react-router-dom';

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
    google.accounts.id.disableAutoSelect();
    window.location.href = "/";
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

  }, []);

  
  // If we have no user : sign in button
  // If we have a user : show logout button

  return (
    <div className="App">
      <Router>
        { Object.keys(user).length === 0 &&
          <Navbar/>
        }    
        <Routes>
          <Route
            path="/"
            element=
            {
              Object.keys(user).length !== 0 ? (
                <Navigate to="/secret_page" />
              ) : (<Home />)
            }
          />
          <Route path="/about" element={<About />} />
          <Route path="/secret_page" element={<SecretPage />} />
        </Routes>
      </Router>

      { Object.keys(user).length !== 0 &&
        <div className="user-info">
          <img src={user.picture} alt="User Profile" />
          <div>
            <h3>Hi, {user.name}</h3>
            <button onClick={(e) => handleSignOut(e)}>Sign Out</button>
          </div>
        </div>
      }
      
      <div id="signInDiv"></div>
    </div>
  );
}

export default App;
