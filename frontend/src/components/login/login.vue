<template>
  <div class="login">
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
        <el-form-item style="margin-bottom: 0">
          <el-button round v-on:click="formSubmit">登录</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
  import ElHeader from "../../../node_modules/element-ui/packages/header/src/main.vue";
  import ElMain from "../../../node_modules/element-ui/packages/main/src/main.vue";

  export default {
    components: {
      ElMain,
      ElHeader},
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
        this.loginUser(this.username, this.password);
        this.errors = null;
      }
    },

    loginUser: function (username, password) {
      this.$axios.post('/api-token-auth/', {
        username: username,
        password: password
      })
        .then(function (response) {
          sessionStorage.setItem('auth-token', response.data.token);
          this.info = '登录成功！';
          this.$router.replace('/thesis-list');
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
  .login {
    margin: 0 auto;
    background-image: url("../../common/img/bg.jpg");
    padding-bottom: 180px;
    padding-top: 220px;
  }

  .login-content {
    width: 380px;
    margin: 0 auto;
  }

  .el-form-item label {
    color: #ecf5ff;
  }

  .el-form-item input {
    background: transparent;
    color: #ecf5ff;
  }

  .el-form-item button {
    background: transparent;
    color: #ecf5ff;
  }

</style>
