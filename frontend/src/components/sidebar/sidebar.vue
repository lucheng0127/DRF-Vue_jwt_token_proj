<template>
  <div id="sidebar">
    <el-aside width="200px" style="background-color: rgba(201,246,239,0.09)">
      <el-menu :default-openeds="['1', '3']">
        <el-submenu index="1">
          <template slot="title"><i class="el-icon-message"></i>通知</template>
          <el-menu-item-group>
            <el-menu-item index="1-1">发布通知</el-menu-item>
            <el-menu-item index="1-2">最新通知</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title"><i class="el-icon-menu"></i>毕业论文</template>
          <el-menu-item-group>
            <el-menu-item index="2-1">导入学生论文</el-menu-item>
            <el-menu-item index="2-2">我的论文</el-menu-item>
            <el-menu-item index="2-3">学院论文</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-submenu index="3">
          <template slot="title"><i class="el-icon-setting"></i>设置</template>
          <el-menu-item-group>
            <el-menu-item index="3-1">个人资料</el-menu-item>
            <el-menu-item index="3-2">添加用户</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
      </el-menu>
    </el-aside>
  </div>
</template>

<script>
  export default {
    name: 'sidebar',

  }
</script>

<style>

</style>
