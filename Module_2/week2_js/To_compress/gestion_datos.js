
let mainInBody = document.createElement("main")
let newDiv = document.createElement("div")
let lineSpace = document.createElement("br")
const mylist = document.getElementById("Mylist")
const secondList = document.getElementById("Mylist2")
const thirdList = document.getElementById("Mylist3")
// const divInBody = document.createElement("section")

// Declaration of object and elements in div
const products ={
    1: {id:"1" , name:"Laptop" , price: 1500},
    2:  {id:"2" , name:"Mouse", price: 25},
    3: {id:"3" , name:"Keyboard", price: 50}
}


// Program Html content insertion
document.body.appendChild(mainInBody)
newDiv.textContent = 'Object products'
newDiv.className = "Div1";
mainInBody.appendChild(newDiv)

// Program initialization
mylist.textContent = 'Object data gestion'

// Object conversion to a set
const productSet = new Set(Object.values(products).map(products => products.name))
console.log(`Unique products Set ${productSet}`)

// Map creation for categorizing products
const productMap = new Map([
    ["Electronics", "Laptop"],
    ["Accesories", "Mouse, Keyboard"]
])
console.log("Products and categories Map", productMap)


// every "document.createElement" is used to create new elements to inert information with appendchild
let pCointainer = document.createElement('p')
// every "textConent" variable is used to add to a created element the content needed
pCointainer.textContent = 'This is the Map array'
// every "className" variable is to asign a class to the created element 
pCointainer.className = "Ptext1"
// every "appendChild" is used to add created elements to others
mylist.appendChild(pCointainer)

// Product object iteration with for...in and for...of
for (const id in products){
    console.log("Funciona 1");
    let newlistItem = document.createElement('li')
    let theforid = products[id]
    newlistItem.textContent = `Product ID: ${id}, Details: Name ->${theforid.name}, Price: $${theforid.price}` 
    mylist.appendChild(newlistItem)
}

// productSet iteration
for (const product of productSet) {
    console.log("Funciona 2");
    let newlistItem = document.createElement('li');
    newlistItem.textContent = `Unique product: ${product}`;
    secondList.appendChild(newlistItem);
}


// productMap iteration
productMap.forEach((products, key) => {
    let newlistItem = document.createElement('li')
    newlistItem.textContent = `Category: ${key}  |  Product(s): ${products}`
    thirdList.appendChild(newlistItem)
})

// Validations and testing

let newdiv1 = document.createElement("div")
newdiv1.className = "Div2";
newdiv1.textContent = "Data gestion, testing complete (for more information, check the console of the web)";
mainInBody.appendChild(newdiv1)
console.log("Products list(Set)", productSet);
console.log("Products list(Map)", productMap);

