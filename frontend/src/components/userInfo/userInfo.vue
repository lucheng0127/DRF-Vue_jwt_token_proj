<template>
  <div id="user-info">
    <el-table
      :data="data"
      stripe
      style="width: 100%">
      <el-table-column
        prop="user"
        label="账号"
        width="180">
      </el-table-column>
      <el-table-column
        prop="username_cn"
        label="姓名"
        width="180">
      </el-table-column>
      <el-table-column
        prop="role"
        label="角色">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
  export default {
    name: 'userInfo',

    data() {
      return {
        data: [],
      }
    },

    created: function () {
      console.log(sessionStorage);
      this.$axios.get('/user-info.json', {
        headers: { 'Authorization': 'JWT ' + sessionStorage.getItem('auth-token') }
      })
        .then(function (response) {
          this.data = response.data.results;
        }.bind(this))
        .catch(function (error) {
          console.log(error);
        }.bind(this))
    },

  }
</script>

<style>
</style>
