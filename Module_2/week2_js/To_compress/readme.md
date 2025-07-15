# **Data Gestion**
-------
#### This program is designedfor the completion of the module 3 week 2 for JS and to do the demostration of the proper use for " for...of ", " for...in " and " forEach "
-------
In this program there is presence of java script code for the iteration for the data of an object (product) with the various loop methods (for methods)

for it's proper use please do check if you have the propper extension to run the code and also the methods in the code interpreter like VS code if not use a browser console for the excecution of the code, have in mind, some features that work in VS code don't work in the browser console

### ***Requierements for the proper code excecution***
- VS code Java Script interpreter
- Acces to VS code or browser console



```javascript
for (const id in products){
    console.log(`Product ID: ${id}, Details:`, products[id])
}

for (const product of productSet){
    console.log(`Unique product: `, product)
}

// productMap iteration
productMap.forEach((products, key) => {
    console.log(`Category: ${key}, Product: ${products} `);
});
```
This ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
is the proper way of using the for method as exposed in the preview