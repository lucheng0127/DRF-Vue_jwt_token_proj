const LOGIN_URL = '/api-token-auth/'

export default {
  user: {
    authenticated: false
  },
  checkAuth () {
    var jwt = sessionStorage.getItem('auth-toke')
    if (jwt) {
      this.user.authenticated = true
    } else {
      this.user.authenticated = false
    }
  },
  getAuthHeader () {
    return {
      'Authorization': 'JWT ' + sessionStorage.getItem('auth-token')
    }
  },
  logout () {
    sessionStorage.removeItem('auth-token')
    this.user.authenticated = false
  },
  login (context, creds, redirect) {
    context.$axios.post(LOGIN_URL, creds)
      .then(response => console.log(response.data))
      .catch(e => console.data)
  }
}
