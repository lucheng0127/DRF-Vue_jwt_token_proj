const THESIS_URL = '/thesis.json'
const IMPORT_THESIS_URL = '/thesis/'

export function getAuthHeader () {
  return { 'Authorization': 'JWT ' + sessionStorage.getItem('auth-token') }
}

export function getThesisList (context) {
  context.$axios.get(THESIS_URL, {headers: getAuthHeader()})
    .then(function (response) {
      context.thesisData = response.data
    })
    .catch(function (error) {
      console.log(error)
    })
}

export function importThesis (context, data) {
  context.$axios({
    method: 'post',
    headers: getAuthHeader(),
    url: IMPORT_THESIS_URL,
    data: data
  })
    .then(function (response) {
      context.good_data = response.data.success
      context.bad_data = response.data.failed
    })
    .catch(function (error) {
      console.log(error)
    })
}

export function getThesisDetail (context, id) {
  context.$axios({
    method: 'get',
    headers: getAuthHeader(),
    url: IMPORT_THESIS_URL + id + '.json'
  })
    .then(function (response) {
      context.data = response.data
    })
    .catch(function (error) {
      console.log(error)
    })
}

export function getThesisLog (context, id) {
  context.$axios({
    method: 'get',
    headers: getAuthHeader(),
    url: IMPORT_THESIS_URL + id + '/thesis_log/'
  })
    .then(function (response) {
      context.thesis_log_data = response.data.data
    })
    .catch(function (error) {
      console.log(error)
    })
}
