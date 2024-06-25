import React from "react";
import { BarraInferiorIconos } from "./BarraInferiorIconos";
import moment from "moment/moment";

export const Inicio = () => {
  return (
    <section className="header d-flex flex-column">
      <section className="encabezado d-flex flex-column justify-content-center align-items-center">
        <section className="titulo-inicio">
          <h2>BIENVENIDO A PARKINGBOX</h2>
        </section>
      </section>
      <section className="time" style={{ marginBottom: '5%' }}>
        <h1>{moment().format('MMMM Do YYYY, h:mm a')}</h1>

       <br /><br /><br /><br /><br /><br />

        <div className="container mt-5">
          <p className="h3 font-weight-bold text-primary">La dirección de PARKINGBOX es:</p>
          <p className="h3 font-weight-bold text-secondary">El número de Bahías de PARKINGBOX es:</p>
        </div>

        
      </section>
      <BarraInferiorIconos />
    </section>
  );
};
