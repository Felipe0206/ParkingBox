import React from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import { Login } from "./components/Login/Login";
import { HomeLogin } from "./components/layout/home-Login/HomeLogin";

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/login" component={Login}></Route>
        <Route path="/homeLogin" component={HomeLogin}></Route>
      </Switch>
    </Router>
  );
}

export default App;
