import React from 'react';
import imagen4 from './../assets/images/4.png';
import imagen5 from './../assets/images/5.png';
import imagen6 from './../assets/images/6.png';



function FormularioContainer()
{  
  return(
<div class="container">

<div class="form">
  <div class="contact-info">
    <h3 class="title">Contacto</h3>
    <p class="text">
    </p>

    <div class="info">
      <div class="information">
        <img src={imagen5} class="icon" alt="" />
        <p>Avenida Siempreviva 742</p>
      </div>
      <div class="information">
        <img src={imagen4} class="icon" alt="" />
        <p>Perritos@patitas.com</p>
      </div>
      <div class="information">
        <img src={imagen6} class="icon" alt="" />
        <p>123-456-789</p>
      </div>
    </div>

    <div class="social-media">
      <p></p>
      <div class="social-icons">
      </div>
    </div>
  </div>

  <div class="contact-form">
    <span class="circle one"></span>
    <span class="circle two"></span>

    <form action="index.html" autocomplete="off">
      <h3 class="title">Contacto</h3>
      <div class="input-container">
        <input type="text" name="Nombre" class="input" />
        <label for=""></label>
        <span>Nombre</span>
      </div>
      <div class="input-container">
        <input type="email" name="email" class="input" />
        <label for=""></label>
        <span>Email</span>
      </div>
      <div class="input-container">
        <input type="tel" name="phone" class="input" />
        <label for=""></label>
        <span>Telefono</span>
      </div>
      <div class="input-container textarea">
        <textarea name="message" class="input"></textarea>
        <label for=""></label>
        <span>Mensaje</span> 
      </div>
      <input type="submit" value="Enviar" class="boton" />
    </form>
  </div>
</div>
</div>)

}
;



export default FormularioContainer;