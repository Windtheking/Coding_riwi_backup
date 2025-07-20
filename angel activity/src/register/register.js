import { registerUser } from "../script.supabase.js";


const form = document.querySelector('form')

form.addEventListener("submit", async function(event){
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm-password").value;
    // console.log(email)
    // console.log(password)
    // console.log(confirmPassword)
    await registerUser(email, password, confirmPassword)
})
