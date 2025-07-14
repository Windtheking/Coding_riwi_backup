let productSet = new Set()
let productMap = new Map()
const products ={
    1: {id:"1" , name:"Laptop"},
    2:  {id:"2" , name:"Mouse"},
    3: {id:"3" , name:"Keyboard"}
}




console.log(`Object products ${products}`)
// for (const product of products){
//     console.log(`Id: ${id} name: ${this.name}`)
// }

    
for (const key in products){
    productSet.add(products)
    productMap.set(key, products)
    console.log(productSet)
    console.log(productMap)
}


// products.forEach(product => {
//     console.log(`este es una prueba de productos: ${product.name}`)
   
// });