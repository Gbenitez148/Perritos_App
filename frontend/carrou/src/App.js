import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Jumbotron from './components/Jumbotron';
import Carousel from './components/Carousel';
/*import Formu from './components/Formu';*/
import Navbar from './components/Navbar'
import Entregas from './components/Entregas';

// ampliar la imagen del carro container flex
function App() {
  return (
    <div className="App">

      <Navbar/>
      <Carousel/>
      <Jumbotron/>
      <Entregas/>


      

     
     
    
  
    </div>
  );
}

export default App;
