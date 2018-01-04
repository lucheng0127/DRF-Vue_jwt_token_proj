<template>
  <div id="notify">
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <BreadcrumbItem>最新通知</BreadcrumbItem>
      </Breadcrumb>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
        <div class="dgs-notify">
          <div class="notify-logo-bar">
            <img src="../../assets/img/logo.png">
          </div>
          <div class="notify-left-bar">
            <Card>
              <p slot="title">最新通知</p>
              <h2 class="notify-title">{{notify.title}}</h2>
              <p class="notify-post-date">{{notify.created_date}}</p>
              <br/>
              <p class="notify-body">{{notify.body}}</p>
              <b><p class="notify-remark">{{notify.remark}}</p></b>
            </Card>
          </div>
          <div class="notify-right-bar">
            <Card>
              <p slot="title">发布通知</p>
              <Input v-model="postNotify.title" placeholder="标题" />
              <Input class="notify-right-bar-body" v-model="postNotify.body" type="textarea" :rows="5" placeholder="内容" />
              <Input v-model="postNotify.remark" placeholder="备注" />
              <Button class="notify-right-bar-submit" type="primary" v-on:click="submitNotify" icon="android-create">发布</Button>
            </Card>
          </div>
        </div>
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
  import {getNotify, newNotify} from '../../api/notify'
  export default {
    name: 'notify',
    data () {
      return {
        notify: {},
        postNotify: {
          title: '',
          body: '',
          remark: ''
        }
      }
    },
    created: function () {
      getNotify(this)
    },
    methods: {
      submitNotify: function () {
        if (this.postNotify.title === '') {
          this.$Message.warning('标题不能为空！')
        } else if (this.postNotify.body === '') {
          this.$Message.warning('内容不能为空！')
        } else {
          let data = {
            title: this.postNotify.title,
            body: this.postNotify.body,
            remark: this.postNotify.remark
          }
          console.log(data)
          newNotify(this, data)
        }
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
  .logo-bar img{
    width: 100px;
  }
  .notify-logo-bar{
    text-align: center;
  }
  .notify-left-bar{
    width: 50%;
    float: left;
  }
  .notify-right-bar{
    width: 50%;
    float: left;
  }
  .notify-post-date{
    float: right;
    color: rgba(38, 107, 255, 0.75);
  }
  .notify-body{
    padding: 10px;
  }
  .notify-remark{
    margin-top: 10px;
  }
  .notify-right-bar-body{
    margin-top: 10px;
    margin-bottom: 10px;
  }
  .notify-right-bar-submit{
    margin-top: 20px;
  }
</style>
