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


  // Registration / Add User Function


  function register(username, firstname, lastname, email, pass1, pass2) {
    const url = base_url+'add-user/';
    const data = {
      username: username,
      first_name: firstname,
      last_name: lastname,
      email: email,
      password1: pass1,
      password2: pass2
    };  
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    };
    fetch(url, options)
      .then(response => {
        if (response.ok) {
          return response.json();
        }
        throw new Error('Network Response Was Not Ok.');
      })
      .then(data => {
        console.log(`User Created Successfully With ID: ${data.user_id}`);
        alert(`User Created Successfully With ID: ${data.user_id}`);
      })
      .catch(error => {
        console.error('There Was A Problem Creating the User:', error);
        alert('There Was A Problem Creating the User:', error);
      });
  }