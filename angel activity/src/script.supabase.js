const URL = "https://qmcvwjhihwuoepzcprmv.supabase.co/rest/v1/users?email=eq.{email}"
const API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFtY3Z3amhpaHd1b2VwemNwcm12Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MjcxMzIyNywiZXhwIjoyMDY4Mjg5MjI3fQ.wHepnufDopMGzpVrk86-q4oN8W27rEmuNdmSJyE7Xos"


export async function registerUser(email, password, confirmPassword) {
    if (password !== confirmPassword){
        alert('Las contraseñas no coinciden');
        return false;
    };

    const endpoint = URL + '?email=eq' + email;

    const headers = {
        apikey: API_KEY,
        Authorization: 'Bearer ' + API_KEY,
        'Content-type' : 'application/json'
    };

    const responseCheck = await fetch(endpoint, {headers: headers});
    const dataCheck  = await responseCheck.json();

    if (dataCheck && dataCheck.length > 0){
        alert('El correo ya esta registrado');
        return false;
    }

    const urlRegister = URL;

    const body = JSON.stringify({email: email, password: password})

    const responseRegister = await fetch(urlRegister, {
        method: 'POST',
        headers: headers,
        body: body
    })

    if (!responseRegister.ok){
        alert('Error al resgistrarse usuario');
        return false;
    }

    alert('Usuario registrado correctamente');
    return true;

}

export async function loginUser(email,password){
    const endpoint = URL + '?email=eq' + email;

    const headers = {
        apikey: API_KEY,
        Authorization: 'Bearer ' + API_KEY,
        'Content-type' : 'application/json'
    };

    const response = await fetch(endpoint, {headers: headers});

    const data = await response.json();

    if (data || data.length === 0){
        alert('Usuario no encontrado')
        return false;
    }

    if (data[0].password !== password){
        alert('Contraseña incorrecta, perteene a ' + data[0].usuario);
        return false
    }

    alert('BIenvenido!!')
    return true;

}