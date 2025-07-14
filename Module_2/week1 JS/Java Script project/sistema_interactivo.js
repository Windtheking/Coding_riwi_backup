//Variable declaration 
let name = prompt("Insert name ")
let age = prompt("Insert age ")

//Convesion of values to integer if posible
age = parseInt(age);

//Conditional to evaluate  if it is not a number, if so tell the usser it is not a number
if (isNaN(age)){
    document.getElementById("Main_square").innerHTML = `<p>Usser ${name} Inserted invalid value (${age}). Please insert valid value</p>`;
}
//Conditional to evaluate the age and from that select an outcome
else{

    //outcome A. Invalid age: An age bellow 0 was inserted
    if (age < 0){
            document.getElementById("Main_square").innerHTML = `<p>Usser ${name} inserted a Invalid age (${age}). Please ${name} insert a valid age</p>`;
    } 
    //outcome B. Underage age: An age bellow 18 was inserted hence you are a minor
    else if(age >= 18){
        document.getElementById("Main_square").innerHTML = `<p>Usser ${name} You are ${age} years old hence you are an adult</p>`;
    } 
    //outcome C. Adult age: An age over 18 was inserted hence you are an adult
    else if(age < 18 && age > -1){
        document.getElementById("Main_square").innerHTML = `<p>Usser ${name} You are ${age} years old hence you are not an adult</p>`;
    }
}

//timer to reload the DOM so the process can be done again without the need of the usser to restart the page
setTimeout(() => {
  location.reload();
}, 8000);