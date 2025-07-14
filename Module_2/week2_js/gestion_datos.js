
// Declaration of object and elements in div
const products ={
    1: {id:"1" , name:"Laptop" , price: 1500},
    2:  {id:"2" , name:"Mouse", price: 25},
    3: {id:"3" , name:"Keyboard", price: 50}
}



// Program initialization
console.log(`\nObject products`, products)

// Object conversion to a set
const productSet = new Set(Object.values(products).map(products => products.name))
console.log("\nUnique products Set", productSet)

// Map creation for categorizing products
const productMap = new Map([
    ["Electronics", "Laptop"],
    ["Accesories", "Mouse, Keyboard"]
])
console.log("Products and categories Map", productMap)


// Product object iteration with for...in and for...of
for (const id in products){
    console.log(`\nProduct ID: ${id}, Details:`, products[id])
}

for (const product of productSet){
    console.log(`\nUnique product: `, product)
}

// productMap iteration
productMap.forEach((products, key) => {
    console.log(`\nCategory: ${key}, Product(s): ${products} `);
})

// Validations and testing
console.log("\nData gestion, testing complete");
console.log("Products list(Object)", products);
console.log("Products list(Set)", productSet);
console.log("Products list(Map)", productMap);

