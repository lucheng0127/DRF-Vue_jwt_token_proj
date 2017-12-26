<template>
  <div id="thesis-detail">
    <div class="layout-breadcrumb">
      <div class="nav-left">
        <Breadcrumb>
          <BreadcrumbItem class="thesis-title">{{data.title}}</BreadcrumbItem>
        </Breadcrumb>
      </div>
      <div class="nav-right">
        <Button class="logout" type="primary" shape="circle" icon="ios-cloud-upload" size="small" v-on:click="to_file_upload">上传材料</Button>
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
                <p class="time">{{item.last_update_time}}</p>
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
  import {getThesisDetail, getThesisLog, getTopLogs} from '../../api/thesis'
  import router from '../../router/index'
  export default {
    name: 'thesis-detail',
    created: function () {
//      console.log(this.$route.params.thesis_id)
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
            key: 'last_update_time'
          },
          {
            title: '下载',
            key: 'action',
            fixed: 'right',
            width: 60,
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
                      console.log('下载文件,id为' + params.row.id)
                    }
                  }
                }, '下载')
              ])
            }
          }
        ]
      }
    },
    methods: {
      to_file_upload: function () {
        router.push('/material/' + this.$route.params.thesis_id)
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
