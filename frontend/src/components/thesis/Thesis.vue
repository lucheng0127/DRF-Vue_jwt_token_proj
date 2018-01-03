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
      <div class="filter-bar">
        <Input class="filter-input" v-model="filterList.stuName" placeholder="学生姓名"/>
        <Input class="filter-input" v-model="filterList.stuNum" placeholder="学号"/>
        <Input class="filter-input" v-model="filterList.stuSubj" placeholder="专业"/>
        <Input class="filter-input" v-model="filterList.gYear" placeholder="毕业年份"/>
        <Button type="primary" v-on:click="filterData">查找</Button>
      </div>
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
        filterList: {
          stuName: '',
          stuNum: '',
          stuSubj: '',
          gYear: ''
        },
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
            key: 'subject',
            filters: [
              {
                label: '通信工程',
                value: '通信工程'
              },
              {
                label: '信息与计算科学',
                value: '信息与计算科学'
              }
            ],
            filterMultiple: false,
            filterMethod (value, row) {
              return row.subject === value
            }
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
    },
    methods: {
      filterData: function () {
        let stuNameStr = '?stu_name='
        let stuNumStr = '&stu_num='
        let stuSubjStr = '&stu_subj='
        let gYearStr = '&graduation_year='
        if (this.filterList.stuName !== '') {
          stuNameStr = stuNameStr + this.filterList.stuName
        }
        if (this.filterList.stuNum !== '') {
          stuNumStr = stuNumStr + this.filterList.stuNum
        }
        if (this.filterList.stuSubj !== '') {
          if (this.filterList.stuSubj === '通信工程' || this.filterList.stuSubj === 'CE') {
            stuSubjStr = stuSubjStr + 'CE'
          } else if (this.filterList.stuSubj === '信息与计算科学' || this.filterList.stuSubj === 'CE') {
            stuSubjStr = stuSubjStr + 'IS'
          }
        }
        if (this.filterList.gYear !== '') {
          gYearStr = gYearStr + this.filterList.gYear
        }
        let str = stuNameStr + stuNumStr + stuSubjStr + gYearStr
        getThesisList(this, str)
        this.filterList.stuName = ''
        this.filterList.stuNum = ''
        this.filterList.stuSubj = ''
        this.filterList.gYear = ''
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
  .filter-input{
    width: 22%;
  }
  .filter-bar{
    padding-left: 10px;
    padding-top: 5px;
  }
</style>
