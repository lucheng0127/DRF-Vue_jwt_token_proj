import {getAuthHeader} from './thesis'
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

export function materialUpload (context, data) {
  context.$axios({
    method: 'post',
    headers: getAuthHeader(),
    url: MATERIAL_URL,
    data: data
  })
    .then(function (response) {
      context.msg = '上传成功！'
      console.log(response)
    })
    .catch(function (error) {
      console.log(error)
    })
}
