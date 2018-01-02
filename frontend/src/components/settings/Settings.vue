<template>
  <div id="settings">
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <BreadcrumbItem>设置</BreadcrumbItem>
      </Breadcrumb>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
        <div class="setting-body">
          <img src="../../assets/img/logo.png">
          <h2>重置登录密码</h2>
          <div class="passwd-reset">
            <p>密码：</p>
            <Input class="passwd-input" type="password" v-model="password" />
            <div>
              <p>再次输入：</p>
              <Input class="passwd-input2" type="password" v-model="password2">
              <Button slot="append" icon="ios-refresh" v-on:click="passwdResetCheck">重置</Button>
              </Input>
            </div>
            <p class="setting-notify-msg" v-show="msg">{{msg}}</p>
          </div>
        </div>
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
  import {setPasswd} from '../../api/setPasswd'
  export default {
    name: 'settings',
    data () {
      return {
        password: '',
        password2: '',
        msg: ''
      }
    },
    methods: {
      passwdResetCheck: function () {
        if (this.password !== this.password2) {
          this.msg = '两次输入密码不一致！'
        } else if (this.password.length < 8 | this.password.length > 15) {
          this.msg = '密码应为8~15位！'
        } else {
          let data = {
            'password': this.password
          }
          setPasswd(this, data)
        }
      }
    }
  }
</script>

<style>
  .layout-breadcrumb{
    padding: 10px 15px 0;
    height: 31px;
  }
  .layout-content{
    height: calc(100% - 160px);
    position: absolute;
    width: calc(100% - 28px);
    margin: 15px;
    overflow: hidden;
    background: #fff;
    border-radius: 4px;
  }
  .layout-content-main{
    height: 100%;
    padding: 10px;
  }
  .setting-body{
    text-align: left;
    float: left;
  }
  .passwd-input{
    width: 225px;
  }
  .passwd-input2{
    width: 300px;
    float: left;
  }
  .setting-notify-msg{
    color: red;
    float: left;
    line-height: 32px;
    margin-left: 30px;
  }
  .passwd-reset{
    margin-top: 30px;
  }
</style>
