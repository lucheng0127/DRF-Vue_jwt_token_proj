<template>
  <div id="thesis-detail">
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <BreadcrumbItem>{{data.title}}</BreadcrumbItem>
      </Breadcrumb>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
        <div class="content-top">

        </div>
        <div class="content-body">
          <div class="content-body-left">
            材料上传统计
          </div>
          <div class="content-body-right">
            <h3 class="timeline-title">最近上传</h3>
            <Timeline>
              <TimelineItem v-for="item in timeLineData" v-bind:key="item.filename_cn">
                <p class="time">{{item.last_update_time}}</p>
                <p class="content">{{item.filename_cn}}</p>
              </TimelineItem>
            </Timeline>
          </div>
        </div>
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'thesis-detail',
    created: function () {
      console.log(this.$route.params.thesis_id)
    },
    data () {
      return {
        data: {},
        thesis_log_data: [],
        timeLineData: [
          {
            filename_cn: '材料名字1',
            last_update_time: '2017-11-22T03:36:30.498937Z'
          },
          {
            filename_cn: '材料名字2',
            last_update_time: '2017-11-22T03:36:30.498937Z'
          }
        ]
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
  }
</style>
