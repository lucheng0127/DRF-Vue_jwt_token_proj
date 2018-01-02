import {getAuthHeader, getUserId} from './thesis'

const SETPASSWD_URL = '/users/'

export function setPasswd (context, data) {
  let userID = getUserId()
  let uri = SETPASSWD_URL + userID + '/set_passwd/'
  context.$axios({
    method: 'post',
    headers: getAuthHeader(),
    url: uri,
    data: data
  })
    .then(function (response) {
      context.msg = response.data.msg
    })
    .catch(function (error) {
      console.log(error)
      context.msg = '只有本人和管理员可以修改密码!'
    })
}
