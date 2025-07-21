const trigger = document.getElementById("form1")
const trigger2 = document.getElementById("form2")
const trigger3 = document.getElementById("form3")


/**
 * fetch GET (R of the CRUD, Read) method to avoid problems and to renderize
 * data with the DOM manipulation also to see if the json db has
 * the information inserted by the POST method
 */
fetch("http://localhost:3000/Inventory")
.then(response =>  {        
    if (!response.ok)
        throw Error("network response was not ok")
    
    return response.json()})

    // Iteration and renderizing of the database information
    .then(Inventory => {
        console.log(Inventory);
        // consts for Id identification
        const products = document.getElementById("tableHead")
        const productsData = document.getElementById("tableData")
        const productsData2 = document.getElementById("tableData2")
        Inventory.forEach(singleProduct => {
            // creation of the elements to add the information
            const listElement = document.createElement("th")
            const listElement2 = document.createElement("td")
            const listElement3 = document.createElement("td")
            //obtaining information from the form to renderize
            listElement.textContent = `${singleProduct.name}`
            listElement2.textContent = `$${singleProduct.price}`
            listElement3.textContent = `${singleProduct.id}`
            //adding variables to renderize the information designated
            products.appendChild(listElement)
            productsData.appendChild(listElement2)
            productsData2.appendChild(listElement3)

        });
        
    })
    .catch(error => console.error("Error al obtener los datos:", error))


/**
 * Fetch POST (C of the CRUD, Create) method to 
 * uppload to the json database the information needed
 * using the Id inside and the id of the form itself 
 * to localize and obtain the data inserted
 */
trigger.addEventListener("submit", (event) =>{
    // prevrents reload
    event.preventDefault()
    const newProduct = document.getElementById("Product_name").value;
    const newPrice = Number(document.getElementById("Product_price").value);

    // fetch protocol
    fetch("http://localhost:3000/Inventory",{
        method: "POST",  
        // information to insert into the Data Base
        body: JSON.stringify({
            "name":newProduct,
            "price":newPrice
        })
    });
    if (!response.ok)
        throw Error("network response was not ok")
        return false
});




/**
 * Fetch PUT (U of the CRUD, Update) Method to update 
 * the json database element using the information 
 * given by the previous form 
 */
trigger2.addEventListener("submit", (event) => {
    event.preventDefault()
    const productId = document.getElementById("Product_id").value;
    const updated = {
        "id": `${productId}`,
        "name": document.getElementById("Update_Product_name").value,
        "price": Number(document.getElementById("Update_Product_price").value)
    };

    fetch(`http://localhost:3000/Inventory/${productId}`, {
        method: 'PUT',
        body: JSON.stringify(updated),
    });
    if (!response.ok)
        throw Error("network response was not ok")
        return false
});


/**
 * Fetch DELETE (D of the CRUD, Delete) Method to delete the json database element
 * using the information given by the previous form using the value given from the 3rd
 * form
 */
trigger3.addEventListener("submit", (event) => {
    event.preventDefault()
    const productIdForDeletion = document.getElementById("Input_for_deletion").value

    fetch(`http://localhost:3000/Inventory/${productIdForDeletion}`,{
        method: 'DELETE',  
    });
    if (!response.ok)
        throw Error("network response was not ok")
        return false
});