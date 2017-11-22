<template>
  <div id="app">
    <el-container>
      <el-header>
        <div class="logo-content">
          <img src="./common/img/logo.png"/>
        </div>
        <el-button type="danger" round v-on:click="logoutUser">logout</el-button>
      </el-header>
      <el-container>
        <v-sidebar v-if="can_show!=undefined && can_show!=null && can_show!=''"></v-sidebar>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
      <el-footer>
        <p>&copy; 2017 lucheng  |  lc960127@gmail.com  |  LC_WeChat_0127</p>
      </el-footer>
    </el-container>
    <!--<v-login></v-login>-->
  </div>
</template>

<script>
  import ElHeader from "../node_modules/element-ui/packages/header/src/main.vue";
  import ElMain from "../node_modules/element-ui/packages/main/src/main.vue";
  import ElFooter from "../node_modules/element-ui/packages/footer/src/main.vue";
  import ElAside from "../node_modules/element-ui/packages/aside/src/main.vue";
  import ElContainer from "../node_modules/element-ui/packages/container/src/main.vue";
  import sidebar from './components/sidebar/sidebar.vue'

  export default {
    components: {
      ElContainer,
      ElAside,
      ElFooter,
      ElMain,
      ElHeader,
      'v-sidebar': sidebar,
    },
    name: 'app',

    data() {
      return {
        can_show: sessionStorage.getItem('auth-token'),
      }
    },

    created: function () {
      if (sessionStorage.getItem('auth-token') == null || sessionStorage.getItem('auth-token') == undefined || sessionStorage.getItem('auth-token') == '') {
        console.log('用户未登录');
        this.$router.replace('/login');
      } else {
        console.log('用户已登录');
        this.$router.replace('/thesis-list');
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
  #app{
    height: 100%;
  }

  .el-container {
    margin: 0;
  }

  .el-header {
    background-color: #cdd6d0;
    color: #333;
    line-height: 60px;
    margin: 0;
    text-align: right;
    font-size: 12px;
  }

  .el-main {
    min-height: 560px;
  }

  .el-footer {
    background-color: #cdd6d0;
    color: #333;
    line-height: 60px;
    margin-top: -60px;
    text-align: center;
  }

  .el-footer p {
    margin: 0;
  }

  .el-main {
    margin-bottom:60px;
    padding: 0;
  }

  .logo-content {
    float: left;
  }

  .logo-content img {
    width: 60px;
  }
</style>
