var base_url = "/api/";
let tokens = {};

// Login function

function login(email, password) {
    return new Promise((resolve, reject) => {
      fetch(base_url+'token/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          email: email,
          password: password
        })
      })
      .then(response => response.json())
      .then(data => {
        const refresh_token = data.refresh;
        const access_token = data.access;
        tokens = { refresh_token, access_token }; // store tokens in the 'tokens' object
        resolve(tokens);
        resolve(tokens);
        window.location.href = 'home';
      })
      .catch(error => reject(error));
    });
  }
  