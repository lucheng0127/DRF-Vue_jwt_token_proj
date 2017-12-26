<template>
  <div id="material">
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <BreadcrumbItem>材料上传</BreadcrumbItem>
      </Breadcrumb>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
        <ul>
          <li v-for="item in materials">
            {{item}}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
  import {getMaterialsChoices} from '../../api/materials'
  export default {
    data () {
      return {
        materials: {}
      }
    },
    created: function () {
      getMaterialsChoices(this)
    }
  }
</script>

<style>

</style>
