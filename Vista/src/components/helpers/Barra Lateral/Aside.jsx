import React from 'react'
import { Logo } from './Logo'
import { MenuItem } from './MenuItem'
/* import img from '../../../../src/assets/icons/icon-cliente.png' */

export const Aside = () => {
    return (
        <aside className='barra-lateral d-flex flex-column align-items-center gap-1' id=''>
            <Logo />
            <MenuItem to='home/' src={'../../../../src/assets/icons/icon-inicio.png'} classImg={'icon-inicio'} itemText={'Inicio'} />
            <MenuItem to='home/clientes' src={'../../../../src/assets/icons/icon-cliente.png'} itemText={'Registro Usuarios'} />
            <MenuItem to='homeproductos' src={'../../../../src/assets/icons/icon-producto.png'} itemText={'Reg Tipos-Tarifas'} />
            <MenuItem to='home/ingresos' src={'../../../../src/assets/icons/icon-ingreso.png'} itemText={'Registro Ingresos'} />
            <MenuItem to='home/ventas' src={'../../../../src/assets/icons/icon-venta.png'} classImg={'icon-venta'} itemText={'Reportes Parking'} />
        </aside>
    )
}
