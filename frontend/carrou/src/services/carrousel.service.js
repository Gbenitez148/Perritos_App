import axios from 'axios'
import {generalConstants} from '../constants/general.constants'
export const carrouselService={
    /*Acá van todos los  Servicios/API*/
    getImg
    
};

function getImg() {
    const requestOptions ={
        headers:{
            "Content-Type": "application/json"

        }
    };
    return axios.get(`${generalConstants.API_URL}carrousel/`, requestOptions);
}
