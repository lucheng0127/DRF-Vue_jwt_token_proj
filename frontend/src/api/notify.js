import {getAuthHeader} from './thesis'
const NOTIFY_URL = '/notify/'

export function getNotify (context) {
  context.$axios({
    method: 'get',
    headers: getAuthHeader(),
    url: NOTIFY_URL
  })
    .then(function (response) {
      if (response.data.length) {
        context.notify = response.data[0]
      }
    })
    .catch(function (error) {
      console.log(error)
    })
}

export function newNotify (context, data) {
  context.$axios({
    method: 'post',
    headers: getAuthHeader(),
    url: NOTIFY_URL,
    data: data
  })
    .then(function (response) {
      console.log(response.data)
      context.$Message.info('发布成功！')
      getNotify(context)
    })
    .catch(function (error) {
      console.log(error)
      context.$Message.error('只有管理员和领导可以发布通知！\n并且通知内不能含有特殊字符！')
    })
}
