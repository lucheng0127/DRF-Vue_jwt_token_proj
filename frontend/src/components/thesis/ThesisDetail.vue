<template>
  <div id="thesis-detail">
    <div class="layout-breadcrumb">
      <div class="nav-left">
        <Breadcrumb>
          <BreadcrumbItem class="thesis-title">{{data.title}}</BreadcrumbItem>
        </Breadcrumb>
      </div>
      <div class="nav-right">
        <Button class="logout" type="primary" shape="circle" icon="ios-cloud-download" size="small" v-on:click="download_file">打包材料</Button>
      </div>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
        <div class="content-top">

        </div>
        <div class="content-body">
          <div class="content-body-left">
            <Table height="500" :columns="thesisLogColumns" :data="thesis_log_data"></Table>
          </div>
          <div class="content-body-right">
            <Card>
              <p slot="title">基本信息：</p>
              <p><b>论文题目：</b>{{data.title}}</p>
              <p><b>指导老师：</b>{{data.instructor}}</p>
              <p><b>学生：</b>{{data.stu_name}}</p>
            </Card>
            <h3 class="timeline-title">最近上传</h3>
            <Timeline>
              <TimelineItem v-for="item in timeLineData" v-bind:key="item.filename_cn">
                <p class="time">{{item.last_upload_time}}</p>
                <p class="content">{{item.filename_cn}}</p>
              </TimelineItem>
            </Timeline>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import {getThesisDetail, getThesisLog, getTopLogs, getAuthHeader} from '../../api/thesis'
  import axios from 'axios'
  const MATERIAL_URL = '/materials/'
  const DOWNLOAD_URL = '/get_material/'
  export default {
    name: 'thesis-detail',
    created: function () {
      getThesisDetail(this, this.$route.params.thesis_id)
      getThesisLog(this, this.$route.params.thesis_id)
      getTopLogs(this, this.$route.params.thesis_id)
    },
    data () {
      return {
        data: {},
        thesis_log_data: [],
        timeLineData: [],
        thesisLogColumns: [
          {
            title: '材料',
            key: 'filename_cn'
          },
          {
            title: '上传次数',
            key: 'upload_times'
          },
          {
            title: '最近上传时间',
            key: 'last_upload_time'
          },
          {
            title: '操作',
            key: 'action',
            fixed: 'right',
            width: 80,
            render: (h, params) => {
              return h('div', [
                h('A', {
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: () => {
                      if (params.row.pk !== '') {
                        console.log('下载文件,id为' + params.row.pk)
                        let filename = ''
                        let data = {'thesis_log_id': params.row.pk}
                        axios({
                          method: 'post',
                          headers: getAuthHeader(),
                          url: DOWNLOAD_URL,
                          data: data
                        })
                          .then(function (response) {
                            filename = response.data.filename
                          })
                          .catch(function (error) {
                            console.log(error)
                          })
                        axios({
                          method: 'get',
                          headers: getAuthHeader(),
                          url: DOWNLOAD_URL + '?thesis_log_id=' + params.row.pk
                        })
                          .then(function (response) {
                            let blob = new Blob([response.data], { type: 'application/force-download' })
                            let link = document.createElement('a')
                            link.href = window.URL.createObjectURL(blob)
                            link.download = filename
                            link.click()
                          })
                          .catch(function (error) {
                            console.log(error)
                          })
                      }
                    }
                  }
                }, '下载'),
                h('Upload', {
                  props: {
                    action: MATERIAL_URL,
                    headers: {'Authorization': 'JWT ' + sessionStorage.getItem('auth-token')},
                    name: 'my_file',
                    data: {
                      'thesis_id': this.$route.params.thesis_id,
                      'material': params.row.material
                    }
                  },
                  style: {
                    width: '25px',
                    marginRight: '5px',
                    float: 'left',
                    color: '#2d8cf0'
                  },
                  on: {
                    click: () => {
                      console.log('上传文件,id为' + params.row.id)
                    }
                  }
                }, '上传')
              ])
            }
          }
        ]
      }
    },
    methods: {
      download_file: function () {
        console.log('打包下载材料')
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
  .content-body-left{
    width: 70%;
    float: left;
  }
  .content-body-right{
    width: 30%;
    float: left;
  }
  .timeline-title{
    margin-bottom: 20px;
    margin-top: 30px;
  }
  .thesis-title{
    font-weight: 800;
  }
  .nav-left{
    width: 85%;
    float: left;
  }
  .nav-right{
    width: 15%;
    float: left;
  }
  .nav-right button{
    margin-top: 0px;
    margin-right: 17px;
  }
</style>
