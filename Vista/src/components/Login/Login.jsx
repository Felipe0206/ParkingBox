import React, { useState } from "react";
import { Link } from "react-router-dom";

const Login = ({ onLogin }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    // Lógica simulada de autenticación exitosa
    onLogin(true); // Llama a la función onLogin para indicar que el usuario ha iniciado sesión
  };

  return (
    <div className="d-flex justify-content-center align-items-center vw-100 vh-100">
      <div className="container-fluid">
        <div className="row justify-content-center">
          <div className="col-sm-10 col-md-8 col-lg-6 col-xl-4">
            <form className="p-4 border rounded bg-light shadow-sm" onSubmit={handleSubmit}>
              <div className="mb-3">
                <label htmlFor="email" className="form-label">
                  Correo electrónico:
                </label>
                <input
                  type="email"
                  className="form-control"
                  id="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="password" className="form-label">
                  Contraseña:
                </label>
                <input
                  type="password"
                  className="form-control"
                  id="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
              </div>
              <Link to="/home/home/" relative="path">
              <button type="submit" className="btn btn-primary col-12">
                Iniciar sesión
                
              </button></Link>
              
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
