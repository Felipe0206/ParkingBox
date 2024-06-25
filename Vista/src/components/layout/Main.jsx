import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { Inicio } from '../helpers/Inicio/Inicio';
import { Clientes } from '../helpers/Formularios/Clientes/Clientes';
import { Ingresos } from '../helpers/Formularios/Ingresos/Ingresos';
import { Productos } from '../helpers/Formularios/Productos/Productos';
import { Ventas } from '../helpers/Formularios/Ventas/Ventas';
import { PaginaError404 } from '../helpers/Error/PaginaError404';
import { EditarCliente } from '../helpers/Formularios/Clientes/EditarCliente';
import { EditarProducto } from '../helpers/Formularios/Productos/EditarProducto';
import { EditarIngreso } from '../helpers/Formularios/Ingresos/EditarIngreso';

export const Main = () => {
  return (
    <main className="" id="">
      <Routes>
        <Route path="/home/*" element={<Inicio />} />
        <Route path="/home/clientes/*" element={<Clientes />} />
        <Route path="/home/clientes/editarCliente/:id" element={<EditarCliente />} />
        <Route path="/home/productos/*" element={<Productos />} />
        <Route path="/home/productos/editarProducto/:id" element={<EditarProducto />} />
        <Route path="/home/ingresos/*" element={<Ingresos />} />
        <Route path="/home/ingresos/editarIngresos/:id" element={<EditarIngreso />} />
        <Route path="/home/ventas/*" element={<Ventas />} />
        <Route path="/home/*" element={<PaginaError404 />} />
      </Routes>
    </main>
  );
};

export default Main;