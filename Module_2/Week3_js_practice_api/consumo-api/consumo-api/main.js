import { buildCharacter } from "./logic.js/characterbuidl.js";
import { fetchCharacter } from "./logic.js/fetch_iteration_interaction_api.js";


// Se define el PATCH de la API
const API_URL = 'https://rickandmortyapi.com/api/character';

// Ejecuto el llamado de la función que desencadena el fetch
const data = await fetchCharacter(API_URL);
buildCharacter(data.results)
// axiosCharacter(API_URL)


const theBody = document.querySelector('body')
const theHeader = document.createElement('header')
theHeader.className = "a_big_header"
theHeader.textContent = "hola mundo"
theBody.append(theHeader)



