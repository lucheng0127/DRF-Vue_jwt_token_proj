const AUTH_HEADER = { 'Authorization': 'JWT ' + sessionStorage.getItem('auth-token') }
const THESIS_URL = '/thesis.json'

export function getThesisList (context) {
  context.$axios.get(THESIS_URL, {headers: AUTH_HEADER})
    .then(function (response) {
      context.thesisData = response.data.results
      console.log(response.data.results)
    })
    .catch(function (error) {
      console.log(error)
    })
}
