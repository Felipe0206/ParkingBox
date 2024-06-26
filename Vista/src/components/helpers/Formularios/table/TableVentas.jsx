import React from "react";
import axios from "axios";
import { useEffect, useState } from "react";
import { Titulo } from "../Titulo";
import { Buscar } from "../Buscar";
const URI = 'http://localhost:3100/ventas';

export const TableVentas = ({
    textoColumna1,
    textoColumna2,
    textoColumna3,
    textoColumna4,
    textoColumna5,
    textoColumna6,
    tdId
}) => {

    const [ventas, setVentas] = useState([]);
    const getVentas = async () => {
        const res = await axios.get(URI)
        setVentas(res.data)
    }
    const deleteVentas = async (id) => {
        await axios.delete(`${URI}/${id}`);
        getVentas();
    }
    useEffect(() => {
        getVentas();
    }, [])
    return (
        <>

            <section className="seccion-buscar d-flex mt-4">
                <Titulo textTitulo={"Reporte de Ventas "} tittle={'me-4'} />
                <h2>Total :</h2>
                <section className=" d-flex">
                <button className="btn botones-2" onClick={getVentas
                }><img
                        className="iconos-botones-cargar"
                        src={"../../../../../src/assets/icons/girar.png"}
                        alt=""
                        width="40px "
                        height="40px"
                    /></button>
                <Buscar
                    inputbuscar={"input-buscar fst-italic"}
                    search={'Documento cliente'} />
                </section>
                
            </section>
            <section className="tabla-registros d-flex justify-content-center align-items-start ">
                <table className="" id="tabla">
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
                    <tbody>
                        {ventas.map((venta) => (
                            <tr key={venta.idVenta}>
                                <td>{ }</td>
                                <td>{ }</td>
                                <td>{venta.fechaVenta}</td>
                                <td>{ }</td>
                                <td>{ }</td>
                                <td className="td-accion">
                                    <section className="botones">
                                        <img
                                            className="iconos-botones"
                                            src={"../../../../../src/assets/icons/Editar.png"}
                                            alt=""
                                            width="40px "
                                            height="40px"
                                        />
                                        <img
                                            className="iconos-botones"
                                            src={"../../../../../src/assets/icons/Eliminar.png"}
                                            alt=""
                                            width="40px "
                                            height="40px" />



                                    </section>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </section>
        </>
    );
};