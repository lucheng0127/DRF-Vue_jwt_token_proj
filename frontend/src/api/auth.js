import router from '../router/index'

const LOGIN_URL = '/api-token-auth/'

export function login (context, creds, redirect) {
  context.$axios.post(LOGIN_URL, creds)
    .then(function (response) {
      sessionStorage.setItem('auth-token', response.data.token)
      router.push('/')
    })
    .catch(function (error) {
      console.log(error)
      context.usernameMsg = '用户名或者密码错误！'
    })
}

export function logout () {
  sessionStorage.removeItem('auth-token')
  router.push('login')
}
