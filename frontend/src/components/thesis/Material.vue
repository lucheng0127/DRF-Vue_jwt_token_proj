<template>
  <div id="material">
    <div class="main">
      <div class="layout-content">
        <div class="layout-content-top">
          <h2>请选择要上传的材料:</h2>
          <Select v-model="material_name" style="width:200px">
            <Option v-for="item in materials" :value="item.value" :key="item.value">{{ item.filename }}</Option>
          </Select>
          <p class="upload-info">请先选择要上传的材料</p>
        </div>
        <div class="layout-content-body">
          <form enctype="multipart/form-data">
            <div class="dropbox">
              <input type="file" :disabled="material_selected" class="input-file" v-on:change="fileUpload($event.target.files)">
              <p>
                将文件退拽至此开始上传<br> 或者点击预览
              </p>
            </div>
          </form>
          <p v-if="msg">{{msg}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import {getMaterialsChoices, materialUpload} from '../../api/materials'
  export default {
    data () {
      return {
        materials: {},
        material_name: '',
        msg: ''
      }
    },
    computed: {
      material_selected () {
        return this.material_name === ''
      }
    },
    created: function () {
      getMaterialsChoices(this)
    },
    methods: {
      fileUpload: function (fileData) {
        console.log(fileData)
        const data = {
          thesis_id: this.$route.params.thesis_id,
          material: this.material_name,
          my_file: fileData
        }
        console.log(data)
        materialUpload(this, data)
      }
    }
  }
</script>

<style>

</style>
