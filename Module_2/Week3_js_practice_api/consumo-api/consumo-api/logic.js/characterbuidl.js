/**
 * fetchCharacter
 * 
 * Función que se encarga de consumir la API con axios
 * @param {object} characters 
 */
export function buildCharacter(characters) {
    const build = document.getElementById("character-render")
    characters.forEach(element => {
        let divContainer = document.createElement("div")
        
        let name = document.createElement("h2")
        name.textContent = element.name
        
        let characterPic = document.createElement("img")
        characterPic.setAttribute("src", element.image)
        
        divContainer.append(name, characterPic)
        build.append(divContainer)

    });   
}