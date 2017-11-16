<template>
  <div id="app">
    <el-row :gutter="20">
      <el-col :span="20">
        <div>
          <p><router-link to="/user-info">User Info</router-link></p>
        </div>
      </el-col>
      <el-col :span="4">
        <div>
          <el-button type="danger" round v-on:click="logoutUser">logout</el-button>
        </div>
      </el-col>
    </el-row>
    <router-view></router-view>
    <!--<v-login></v-login>-->
  </div>
</template>

<script>
  import login from './components/login/login.vue'

  export default {
    name: 'app',
    components: {
      'v-login': login
    },

    created: function () {
      if (sessionStorage.getItem('auth-token') == null || sessionStorage.getItem('auth-token') == undefined || sessionStorage.getItem('auth-token') == '') {
        console.log('用户未登录');
        this.$router.replace('/login');
      } else {
        console.log('用户已登录');
      }
    },

    methods: {
      logoutUser: function () {
        if (sessionStorage.getItem('auth-token') != null || sessionStorage.getItem('auth-token') != undefined || sessionStorage.getItem('auth-token') != '') {
          sessionStorage.clear('auth-token');
          this.$router.replace('/login');
        }
      }
    },
  }
</script>

<style>
</style>
