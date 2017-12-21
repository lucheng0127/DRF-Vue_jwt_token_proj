const THESIS_URL = '/thesis.json'
const IMPORT_THESIS_URL = '/thesis/'

export function getAuthHeader () {
  return { 'Authorization': 'JWT ' + sessionStorage.getItem('auth-token') }
}

export function getThesisList (context) {
  context.$axios.get(THESIS_URL, {headers: getAuthHeader()})
    .then(function (response) {
      context.thesisData = response.data
      console.log(response.data)
    })
    .catch(function (error) {
      console.log(error)
    })
}

export function importThesis (context, data) {
  console.log(data)
  context.$axios({
    method: 'post',
    headers: getAuthHeader(),
    url: IMPORT_THESIS_URL,
    data: data
  })
    .then(function (response) {
      console.log(response)
      context.good_data = response.data.success
      context.bad_data = response.data.failed
    })
    .catch(function (error) {
      console.log(error)
    })
}
