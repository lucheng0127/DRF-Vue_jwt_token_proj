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
        data: [{
          user: 'lucheng',
          username_cn: '鲁成',
          role: '学生'
        }],
      }
    },

    created: function () {
      this.$axios.get('/user-info.json')
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
