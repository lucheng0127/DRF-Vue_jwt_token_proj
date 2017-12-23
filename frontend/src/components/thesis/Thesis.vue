<template>
  <div id="thesis">
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <BreadcrumbItem>所有毕设</BreadcrumbItem>
        <BreadcrumbItem><router-link to="/import">导入毕设</router-link></BreadcrumbItem>
        <BreadcrumbItem></BreadcrumbItem>
      </Breadcrumb>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
        <Table class="thesis-list-table" height="500" :columns="columns" :data="thesisData"></Table>
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
  import {getThesisList} from '../../api/thesis'
  import router from '../../router/index'
  export default {
    name: 'thesis',
    data () {
      return {
        columns: [
          {
            title: '论文题目',
            key: 'title'
          },
          {
            title: '学生姓名',
            key: 'stu_name'
          },
          {
            title: '学生学号',
            key: 'stu_num'
          },
          {
            title: '指导老师',
            key: 'instructor'
          },
          {
            title: '专业',
            key: 'subject'
          },
          {
            title: '毕业年份',
            key: 'graduation_year'
          },
          {
            title: '操作',
            key: 'action',
            width: 150,
            align: 'center',
            render: (h, params) => {
              return h('div', [
                h('Button', {
                  props: {
                    type: 'primary',
                    size: 'small'
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: () => {
                      router.push('/thesis/' + params.row.id)
                    }
                  }
                }, '详情'),
                h('Button', {
                  props: {
                    type: 'error',
                    size: 'small'
                  },
                  on: {
                    click: () => {
                      this.remove(params.index)
                    }
                  }
                }, '删除')
              ])
            }
          }
        ],
        thesisData: []
      }
    },
    created: function () {
      getThesisList(this)
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
</style>
