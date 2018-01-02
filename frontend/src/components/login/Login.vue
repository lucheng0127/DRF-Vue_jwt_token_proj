<template>
  <div id="login">
    <div class="login-page">
      <div class="login-content">
        <div class="login-form">
          <div class="login-title">
            <img src="../../assets/img/logo.png">
          </div>
          <div class="login-item">
            <Icon type="person" size="23" />
            <input type="text" placeholder=" 用户名" v-model="username" />
            <p class="error-msg" v-if="usernameMsg">
              {{ usernameMsg }}<Icon type="close-circled" />
            </p>
          </div>
          <div class="login-item">
            <Icon type="locked" size="23" />
            <input type="password" placeholder=" 密码" v-model="passwd" />
            <p class="error-msg" v-if="passwdMsg">
              {{ passwdMsg }}<Icon type="close-circled" />
            </p>
          </div>
          <div class="login-item">
            <Button type="ghost" shape="circle" v-on:click="formSubmit">登 录</button>
          </div>
        </div>
      </div>
      <div class="login-copy">
        &copy; 2017 lucheng | <Icon type="email" /> lc960127@gmail.com
      </div>
    </div>
  </div>
</template>

<script>
  import {login} from '../../api/auth'

  export default {
    data () {
      return {
        usernameMsg: '',
        passwdMsg: '',
        username: '',
        passwd: ''
      }
    },
    methods: {
      formSubmit: function () {
        console.log('验证数据正确性')
        if (this.username === '') {
          this.usernameMsg = '请输入用户名！'
        }
        if (this.passwd.length < 8 || this.passwd.length > 15) {
          this.passwdMsg = '密码应为8~15位！'
        }
        const authData = {
          username: this.username,
          password: this.passwd
        }
        login(this, authData, '/')
      }
    }
  }
</script>

<style>
  .login-page{
    border: 1px solid #d7dde4;
    background: #f5f7f9;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
  }
  .login-content{
    background-image: url('../../assets/img/bg.jpg');
    height: -webkit-fill-available;
  }
  .login-copy{
    text-align: center;
    padding: 10px 0 20px;
    color: #FFFFFF;
    margin-top: -40px;
    height: 40px;
  }
  .login-form{
    color: #FFFFFF;
    width: 350px;
    margin: 0 auto;
    padding-top: 80px;
  }
  .login-title{
    font-size: 2.5em;
    text-align: center;
    margin-bottom: 20px;
  }
  .login-item{
    width: 100%;
    min-height: 100px;
  }
  .login-item i{
    line-height: 40px;
  }
  .login-item input{
    color: #FFFFFF;
    width: 90%;
    float: right;
    height: 40px;
    font-size: 22px;
    background: transparent;
    border: None;
    border-bottom: 1px solid #ffffff;
  }
  .error-msg{
    color: red;
    margin-bottom: 10px;
    text-align: center;
  }
  .error-msg i{
    margin-left: 10px;
  }
  .login-form button{
    color: #FFFFFF;
    margin-top: 8px;
    margin-left: 135.5px;
    font-size: 20px;
  }
</style>
