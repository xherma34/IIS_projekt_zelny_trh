import './App.css';

import { BrowserRouter as Routes, Router, Route, Link, Switch } from 'react-router-dom' 
import PrivateRoute from './utils/PrivateRoute'
import { AuthProvider } from './context/AuthContext'
import ReactDOM from "react-dom";

import HomePage from './pages/HomePage'
import LoginPage from './pages/LoginPage'
import RegisterPage from './pages/RegisterPage'
import CatalogPage from './pages/CatalogPage'
import CropPage from './pages/CropPage'
import AdminPage from './pages/AdminPage' //Added
import UserInfo from './pages/UserInfoPage' //Added
import SuggestionPage from './pages/SuggestionPage' //Added
import AdminChangeUser from './pages/AdminChangeUser'; //Added

import Header from './components/Header'
import Footer from './components/Footer'

import axios from 'axios';

// axios.defaults.xsrfCookieName = 'csrftoken'
// axios.defaults.xsrfHeaderName = 'X-CSRFToken'

function App() {
  return (
    <div className="App">
       <Routes>
        <AuthProvider>
          <Header />
          <Route component={HomePage} exact path="/"/>
          <Route component={LoginPage} path="/login"/>
          <Route component={RegisterPage} path="/register"/>
          <Route component={CatalogPage} path="/catalog"/>
          <Route component={CropPage} path="/crop"/>
          <Route component={AdminPage} path="/admin"/>
          <Route component={UserInfo} path="/userinfo"/>
          <Route component={SuggestionPage} path="/suggestion"/>
          <Route component={AdminChangeUser} path="/changeuser/:id"/>
          <Footer/>
        </AuthProvider>
      </Routes>
      <p>Here is our react website</p>  
      
    </div> //Added line
  ); 
} 

export default App;
