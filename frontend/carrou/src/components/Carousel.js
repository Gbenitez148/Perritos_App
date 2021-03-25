import React,{ useEffect, useState } from 'react';
import Carousel from 'react-bootstrap/Carousel'
import  { carrouselService } from '../services/carrousel.service'
import Container from 'react-bootstrap/Container'

/*console.log(json)*/
function App() {

    const [imgObjeto,setImgObjeto]= useState([]);
    useEffect(() => {

        const getData=() => {
            carrouselService.getImg().then((json) => {
                setImgObjeto(json.data);

            });
        };
        getData(); /*Para ejecutar la funcion*/ 

    }, []);
  return (
    <Container fluid className="mt-5 p-0" id="carcont">
        <h2 id="home"/>
      <Carousel>
          {imgObjeto && imgObjeto.length > 0 && 
          imgObjeto.map((imagenPerro) => (
            <Carousel.Item interval={2000}>
            <img
                className="d-block w-100"
                src={imagenPerro.foto}
                alt="First slide" 
         />
            <Carousel.Caption>
                <p><h2>{imagenPerro.titulo}</h2>{imagenPerro.pie_de_pagina}</p>
            </Carousel.Caption>
        </Carousel.Item>
          ))}
        
      </Carousel>
      </Container>
  );
}
export default App;