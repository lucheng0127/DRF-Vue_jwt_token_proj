const LOGIN_URL = 'http://127.0.0.1:8000/api-token-api/'

export default {
  user: {
    authenticated: false
  },
  checkAuth () {
    const jwt = sessionStorage.getItem('api-toke')
    if (jwt) {
      this.user.authenticated = true
    } else {
      this.user.authenticated = false
    }
  },
  getAuthHeader () {
    return {
      'Authorization': 'JWT ' + sessionStorage.getItem('api-token')
    }
  },
  logout () {
    sessionStorage.removeItem('api-token')
    this.user.authenticated = false
  },
  login (context, creds, redirect) {
    context.$axios.post(LOGIN_URL, creds)
      .then(response => console.log(response.data))
      .catch(e => console.data)
  }
}
