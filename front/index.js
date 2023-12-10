const url = 'http://127.0.0.1:8000/clients/'

function send_request(method, url, body = null) {
    return fetch(url).then(response => {
        return response.text()
    })
}

send_request('GET', url)
.then(data => console.log(data))
.catch(err => console.log(err))