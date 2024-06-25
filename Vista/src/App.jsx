import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomeLogin from './components/layout/home-Login/HomeLogin';
import Login from './components/Login/Login';

function App() {
  return (
    
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/home/*" element={<HomeLogin />} />
      </Routes>
   
  );
}

export default App;
