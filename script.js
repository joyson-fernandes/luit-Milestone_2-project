function sendPageVisit() {
    const apiUrl = 'https://o0aph4ei5g.execute-api.us-east-1.amazonaws.com/prod/metrics';
    const data = {
        page: window.location.pathname
    };
    fetch(apiUrl, {
        method: 'POST',        headers: {
            'Content-Type': 'application/json'
        },        body: JSON.stringify(data)
    })
    .then(response => response.json())    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

window.onload = sendPageVisit;
