import React, { useEffect } from 'react'
import { Titulo } from "../Titulo";
import { FormInput } from "../FormInput";
import { Buscar } from "../Buscar";
import { TextArea } from "../TextArea";
import { Button } from "../Button";
import { TableVentas } from '../table/TableVentas';
import { Formik, Form, Field, ErrorMessage } from "formik";
import { Navigate, useNavigate } from 'react-router-dom';
import swal from 'sweetalert';

/* constuyendo() */






export const Ventas = () => {
  const navigate = useNavigate()
  let documentoCliente, idProducto, producto, cantidad;
  useEffect(() => {
    
  }, []);

  const construyendo = (e) => {
    swal({
      title: "Modúlo Ventas en construcción",
      text: "El modúlo ventas está en proceso de desarrollo",
      icon: "info",
      buttons: "ok",
      closeOnClickOutside: false,
      closeOnEsc: false,
      
    }).then((value) => {
      if (value) {
        navigate('/');
       
      }
    })
  }
  return (
    <>
      <section className="registro-venta m-4 d-flex flex-column justify-content-center">
        
        <TableVentas
          textoColumna1={"Descripcion"}
          textoColumna2={"Placa"}
          textoColumna3={"Entrada"}
          textoColumna4={"Salida"}
          textoColumna5={"Tiempo"}
          textoColumna6={"Pagos"}
        />

      </section >
    </>
  )
}
