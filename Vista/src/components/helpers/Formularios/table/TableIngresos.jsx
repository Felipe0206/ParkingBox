import React from "react";
import axios from "axios";
import { useEffect, useState } from "react";
import { Titulo } from "../Titulo";
import { Buscar } from "../Buscar";
import { Link, useNavigate } from "react-router-dom";


const URI = '../../../../assets/Datos/Datos.json';

export const TableIngresos = ({ textoColumna1, textoColumna2, textoColumna3, textoColumna4, textoColumna5, textoColumna6, tdId }) => {
  const navigate = useNavigate()
  const [ingreso, setIngreso] = useState([]);

  useEffect(() => {
    getIngresos();
  }, [])

  const getIngresos = async () => {
    const res = await axios.get(URI)
    setIngreso(res.data)
    navigate('/ingresos')

  }

  const deleteIngresos = async (id) => {
    await axios.delete(`${URI}/${id}`);
    getIngresos();
  }

  const [idIngreso, setIdIngreso] = useState('');
  const [idCliente, setIdCliente] = useState('');
  const [placa, setPlaca] = useState('');
  const [fechaIngreso, setFechaIngreso] = useState('');
  const [horaIngreso, setHoraIngreso] = useState('');
  const [horasTotales, setHorasTotales] = useState('');
  const [id, setId] = useState('')
  const [trBody, setTrBody] = useState({ display: "" })
  const [trById, setTrById] = useState({ display: "none" })

 const buscarPorId = async (e) => {
    e.preventDefault()
    console.log(id)
    
    /* console.log(res) */
    try {
      let res = await axios.get(URI + '/' + id)
      setIdIngreso(res.data.idIngreso)
      setIdCliente(res.data.idCliente);
      setPlaca(res.data.placaMoto)
      setFechaIngreso(res.data.fechaIngreso)
      setHoraIngreso(res.data.horaIngreso)
      setHorasTotales(res.data.horasTotales)
      setTrBody({ display: "none" })
      setTrById({ display: "" })
    } catch (error) {
      swal({
        title: "Dato no encontrado",
        text: "El dato ingresado no se encuentra en la base de datos",
        icon: "error",
        button: "ok"
      });
    }


  }

  const confirmacion = (id) => {
    swal({
      title: "Eliminar",
      text: "¿Estás seguro de eliminar este ingreso?",
      icon: "warning",
      buttons: ["No", "Sí"],
      dangerMode: true
    }).then((value) => {
      if (value) {
        deleteIngresos(id);
        swal({
          title: "Confirmación Eliminación",
          text: "¡Cliente eliminado correctamente!",
          icon: "success",

        });
        regresar();
      }
    });
  };

  const pulsarBuscar = (e) => {
    setId(e.target.value)

  }

  const regresar = () => {
    setTrBody({ display: "" })
    setTrById({ display: "none" })
  }


  return (
    <>

      <section className="seccion-buscar d-flex mt-4 ">
        <Titulo textTitulo={"Listado Ingresos: "} tittle={'me-4'} />
        <section className="d-flex">
          <button className="btn botones-2" onClick={getIngresos
          }><img
              className="iconos-botones-cargar"
              src={"../../../../../src/assets/icons/girar.png"}
              alt=""
              width="40px "
              height="40px"
            /></button>
          <Buscar inputbuscar={"input-buscar fst-italic"}
            search={'Ingrese placa, documento'}
            button={'ms-3'}
            onSubmit={buscarPorId}
            onChange={pulsarBuscar}
          />
        </section>


      </section>
      <section className="tabla-registros d-flex justify-content-center align-items-start ">
        <table id="tabla">
          <thead>
            <tr>
              <td className="td-principal" id={tdId}>{textoColumna1}</td>
              <td className="td-principal" id={tdId}>{textoColumna2}</td>
              <td className="td-principal" id={tdId}>{textoColumna3}</td>
              <td className="td-principal" id={tdId}>{textoColumna4}</td>
              <td className="td-principal" id={tdId}>{textoColumna5}</td>
              <td className="td-principal" id={tdId}>{textoColumna6}</td>
            </tr>
          </thead>
          <tbody style={trBody}>
            {ingreso.map((ingres) => (
              <tr key={ingres.idIngreso}>
                <td>{ingres.idCliente}</td>
                <td>{ingres.placaMoto}</td>
                <td>{ingres.fechaIngreso}</td>
                <td>{ingres.horaIngreso}</td>
                <td>{ingres.horasTotales}</td>
                <td className="td-accion">
                  <Link to={"editarIngresos/" + ingres.idIngreso}>
                    <button className="btn botones">
                    Marcar Salida
                    </button>
                  </Link>
                  <button className="btn botones"
                    onClick={() => { confirmacion(ingres.placaMoto) }}>
                    Entrada
                  </button>

                  <button className="btn botones"
                    onClick={() => { confirmacion(ingres.placaMoto) }}>
                    Salida Fact
                  </button>
                </td>

              </tr>
            )

            )}

          </tbody>
          <tbody style={trById}>
            <tr key={idIngreso}>
              <td>{idCliente}</td>
              <td>{placa}</td>
              <td>{fechaIngreso}</td>
              <td>{horaIngreso}</td>
              <td>{horasTotales}</td>
              <td>
                <Link to={"editarIngresos/" + idIngreso}>
                  <button className="btn botones">
                    <img className="iconos-botones"
                      src={"../../../../../src/assets/icons/Editar.png"}
                      alt=""
                      width="40px "
                      height="40px"
                    />
                  </button>
                </Link>
                <button className="btn botones"
                  onClick={() => {
                    confirmacion(idIngreso)

                  }}>

                  <img
                    className="iconos-botones"
                    src={"../../../../../src/assets/icons/Eliminar.png"}
                    alt=""
                    width="40px "
                    height="40px" />
                </button>

                <button className="btn botones" onClick={regresar}>
                  {" "}
                  <img
                    className="iconos-botones"
                    src={"../../../../../src/assets/icons/regreso.png"}
                    alt=""
                    width="40px "
                    height="40px"
                  />
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </section>
    </>
  );
};