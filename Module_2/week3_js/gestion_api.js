fetch("http://localhost:3000/productos")
    .then(response => response.json())
    .then(productos => {
        const products = document.getElementById("listproducts")
        productos.forEach(producto => {
            const listElement = document.createElement("li")
            listElement.textContent = `${producto.name} - $${producto.price}`
            products.appendChild(listElement)
        });
    })
    .catch(error => console.error("Error al obtener los datos:", error))
