import React from 'react'
import {Navbar, Nav, Form, FormControl} from 'react-bootstrap';



function Navibar() {
  return (
    <div>
      <>
      
  <Navbar fixed="top" bg="dark" variant="dark" >
    <Navbar.Brand href="#home">Perritolandia</Navbar.Brand>
    <Nav className="mr-auto">
      <Nav.Link href="#home">Carrousel</Nav.Link>
      <Nav.Link href="#QS">Quienes somos</Nav.Link>
      <Nav.Link href="#Entregas">Entregas</Nav.Link>
    </Nav>
    <Form inline>
  
      
    </Form>
  </Navbar>
</>
    </div>
  )
}

export default Navibar
