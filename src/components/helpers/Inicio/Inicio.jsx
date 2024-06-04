import React from "react";
import { BarraInferiorIconos } from "./BarraInferiorIconos";
import moment from "moment/moment";
import { Formik, Form, Field, ErrorMessage } from "formik";
import { FormInput2 } from "../Formularios/FormInput2";

export const Inicio = () => {
  let fecha = new Date()
  let hora =  fecha.toLocaleTimeString('en-US');
  return (
    <section className="header d-flex flex-column">
      <section className="encabezado d-flex flex-column justify-content-center align-items-center ">
       
        <section className="titulo-inicio"><h1>BIENVENIDO A PARKINGBOX</h1></section>
        
      </section>
      <section className="time" style={{ marginBottom: '5%' }}>
      <h1> {moment().format('MMMM Do YYYY, h:mm a')}</h1>
  

      <form>
  <div class="mb-3">
    <label for="correo" class="form-label">Correo:</label>
    <input type="email" class="form-control" id="correo" aria-describedby="emailHelp"></input>
  </div>
  <div class="mb-3">
    <label for="contraseña" class="form-label">Contraseña:</label>
    <input type="password" class="form-control" id="contraseña"></input>
  </div>
  <div class="text-center">
    <button type="submit" class="btn btn-primary mb-3   col-12">Iniciar sesión</button>
    <br />
    <a href="#" class="btn btn-link">Recuperar Contraseña</a>
  </div>
</form>



      
        
      </section>
      <BarraInferiorIconos/>


    </section>
  );
};