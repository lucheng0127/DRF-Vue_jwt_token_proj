<template>
  <div id="thesis-list">
    <el-table :data="data" stripe style="width: 100%">
      <el-table-column
        prop="instructor"
        label="指导老师">
      </el-table-column>
      <el-table-column
        prop="stu_name"
        label="学生姓名">
      </el-table-column>
      <el-table-column
        prop="stu_num"
        label="学号">
      </el-table-column>
      <el-table-column
        prop="graduation_year"
        label="毕业年份">
      </el-table-column>
      <el-table-column
        prop="subject"
        label="专业">
      </el-table-column>
      <el-table-column
        prop="title"
        label="论文题目">
      </el-table-column>
      <el-table-column
        fixed="right"
        label="操作"
        width="100">
        <template slot-scope="scope">
          <el-button type="text" size="small">
            <i class="el-icon-edit">编辑</i>
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
  export default {
    name: 'thesisList',

    data() {
      return {
        data: [],
      }
    },

    created: function () {
      this.$axios.get('/thesis.json', {
        headers: { 'Authorization': 'JWT ' + sessionStorage.getItem('auth-token') }
      })
        .then(function (response) {
          this.data = response.data.results;
          console.log(response.data.results);
        }.bind(this))
        .catch(function (error) {
          console.log(error);
        }.bind(this))
    },

  }
</script>

<style>

</style>
