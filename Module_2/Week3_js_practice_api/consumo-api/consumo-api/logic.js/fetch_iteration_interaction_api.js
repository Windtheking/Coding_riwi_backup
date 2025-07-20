/**
 * fetchCharacter
 * 
 * Función que se encarga de consumir la API con fetch
 * @param {string} API_URL 
 */
export async function fetchCharacter(API_URL) {
    try {
        const response = await fetch(API_URL);
        if(!response.ok) {
            throw new Error("Error al consumir la API");
        }
        return await response.json()
    } catch (error) {
        console.log(error + "hola") 
    }
        
}
