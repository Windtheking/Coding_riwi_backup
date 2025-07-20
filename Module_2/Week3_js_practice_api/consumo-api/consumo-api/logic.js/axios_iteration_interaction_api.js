async function axiosCharacter(API_URL) {
    try {
        const response = await axios(API_URL);
        console.log(response);
        return response;
    } catch (error) {
        console.log("Hay un error en la API")
    }
}