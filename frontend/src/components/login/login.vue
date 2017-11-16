<template>
  <div class="login">
    <el-row type="flex" class="row-bg">
      <el-col :span="6">
        <div class="login-content">
          <el-form label-width="100px">
            <el-form-item>
              <el-alert type="error" v-if="errors">
                {{ errors }}
              </el-alert>
              <el-alert type="success" v-if="info">
                {{ info }}
              </el-alert>
            </el-form-item>
            <el-form-item label="账号">
              <el-input v-model="username"></el-input>
            </el-form-item>
            <el-form-item label="密码">
              <el-input type="password" v-model="password"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button round v-on:click="formSubmit">登录</el-button>
            </el-form-item>
          </el-form>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: 'login',

  data() {
    return {
      errors: null,
      info: null,
    }
  },

  methods: {
    formSubmit: function () {
      if (this.username == null || this.username == undefined || this.username == '') {
        this.errors = '请输入账号！'
      } else if (this.password == null || this.password == undefined || this.password == '') {
        this.errors = '请输入密码！'
      } else if (this.password.length < 8 || this.password.length > 20) {
        this.errors = '密码长度为8到20位'
      } else {
        console.log(this.username);
        console.log(this.password);
        console.log(sessionStorage);
        this.loginUser(this.username, this.password);
        this.errors = null;
      }
    },

    loginUser: function (username, password) {
      this.$axios.post('http://127.0.0.1:8000/api-token-auth/', {
        username: username,
        password: password
      })
        .then(function (response) {
          sessionStorage.setItem('auth-token', response.data.token);
          this.info = '登录成功！';
        }.bind(this))
        .catch(function (error) {
          this.errors = '用户名或密码错误！';
          console.log(error);
        }.bind(this))
    },

  },

  }
</script>

<style>

</style>
