import { loginUser } from "../script.supabase";

const form = document.querySelector('form')

form.addEventListener('submit', async function(event){
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    await loginUser(email, password);

})