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
        <h3>批量导入毕业设计数据</h3>
        <b>通信工程：</b>CE<br/><b>信息与计算科学：</b>IS<br>
        [学生姓名1],[学生学号1],[专业1],[毕业年份1],[论文题目1]<br>
        [学生姓名2],[学生学号2],[专业2],[毕业年份2],[论文题目2]<br>
        <p class="notify-msg">逗号为英文状态下逗号','</p>
        <Alert type="warning" show-icon>总数据{{all_data}}条</Alert>
        <Alert type="success" show-icon>成功{{good_data}}条</Alert>
        <Alert type="error" show-icon>失败{{bad_data}}条</Alert>
        <!--<Input v-model="thesisData" type="textarea" :rows="10" placeholder="鲁成,20140154004,CE,2018,学院材料收集系统"></Input>-->
        <textarea class="thesis-text" v-model="thesisData" rows="10" placeholder="鲁成,20140154004,CE,2018,学院材料收集系统"></textarea>
        <Button type="primary" shape="circle" icon="ios-download-outline" v-on:click="submitData">导入</Button>
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
  import {importThesis} from '../../api/thesis'
  export default {
    name: 'import-thesis',
    data () {
      return {
        good_data: 0,
        bad_data: 0,
        thesisData: ''
      }
    },
    computed: {
      all_data: function () {
        return this.good_data + this.bad_data
      }
    },
    methods: {
      submitData () {
        const data = {
          data: this.thesisData
        }
        importThesis(this, data)
      }
    }
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
  .layout-content-main button{
    float: right;
    margin-top: 5px;
  }
  .notify-msg{
    color: red;
  }
  .thesis-text{
    width: 100%;
  }
</style>
