<template>
  <div id="import-thesis">
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <BreadcrumbItem><router-link to="/thesis">所有毕设</router-link></BreadcrumbItem>
        <BreadcrumbItem>导入毕设</BreadcrumbItem>
        <BreadcrumbItem></BreadcrumbItem>
      </Breadcrumb>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
        Import Thesis Page
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'import-thesis'
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
</style>
