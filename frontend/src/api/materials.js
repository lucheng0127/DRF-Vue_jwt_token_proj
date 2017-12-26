const MATERIAL_URL = '/materials/'

export function getMaterialsChoices (context) {
  context.$axios({
    method: 'get',
    url: MATERIAL_URL
  })
    .then(function (response) {
      context.materials = response.data
    })
    .catch(function (error) {
      console.log(error)
    })
}
