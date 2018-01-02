<template>
  <div id="notify">
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <BreadcrumbItem>最新通知</BreadcrumbItem>
      </Breadcrumb>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
          通知页面
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'notify'
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
  .logo-bar img{
    width: 100px;
  }
</style>
