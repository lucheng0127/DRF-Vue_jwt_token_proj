<template>
  <div id="home">
    <div class="layout" :class="{'layout-hide-text': spanLeft < 5}">
      <Row type="flex">
        <Col :span="spanLeft" class="layout-menu-left">
        <Menu active-name="1" theme="dark" width="auto">
          <div class="layout-logo-left">
            <h1>DGS</h1>
          </div>
          <MenuItem name="1">
            <Icon type="information-circled" :size="iconSize"></Icon>
            <router-link to="/notify"><span class="layout-text">最新通知</span></router-link>
          </MenuItem>
          <MenuItem name="2">
            <Icon type="ios-keypad" :size="iconSize"></Icon>
            <router-link to="/thesis"><span class="layout-text">论文材料</span></router-link>
          </MenuItem>
          <MenuItem name="3">
            <Icon type="gear-a" :size="iconSize"></Icon>
            <router-link to="/settings"><span class="layout-text">个人设置</span></router-link>
          </MenuItem>
        </Menu>
        </Col>
        <Col :span="spanRight" style="height: -webkit-fill-available;">
        <div class="layout-header">
          <Button type="text" @click="toggleClick">
            <Icon type="navicon" size="32"></Icon>
          </Button>
          <Button class="logout" type="primary" shape="circle" icon="log-out" size="small" v-on:click="logout">注销</Button>
        </div>
        <router-view/>
        <div class="layout-copy">
          &copy; 2017 lucheng | <Icon type="email" /> lc960127@gmail.com
        </div>
        </Col>
      </Row>
    </div>
  </div>
</template>

<script>
  import {logout} from '../../api/auth'
  export default {
    name: 'home',
    data () {
      return {
        spanLeft: 5,
        spanRight: 19
      }
    },
    computed: {
      iconSize () {
        return this.spanLeft === 5 ? 14 : 24
      }
    },
    methods: {
      toggleClick () {
        if (this.spanLeft === 5) {
          this.spanLeft = 2
          this.spanRight = 22
        } else {
          this.spanLeft = 5
          this.spanRight = 19
        }
      },
      logout () {
        logout()
      }
    }
  }
</script>

<style>
  .layout{
    border: 1px solid #d7dde4;
    background: #f5f7f9;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
  }
  .layout-copy{
    text-align: center;
    padding: 10px 0 20px;
    color: rgba(8, 5, 6, 0.85);
    height: 48px;
    width: 100%;
    position: absolute;
    bottom: 0;
  }
  .layout-menu-left{
    background: #464c5b;
  }
  .layout-header{
    height: 60px;
    background: #fff;
    box-shadow: 0 1px 1px rgba(0,0,0,.1);
  }
  .layout-logo-left{
    width: 90%;
    height: 30px;
    border-radius: 3px;
    margin: 15px auto;
    color: dodgerblue;
    text-align: center;
    line-height: 42px;
  }
  .layout-ceiling-main a{
    color: #9ba7b5;
  }
  .layout-hide-text .layout-text{
    display: none;
  }
  .layout-text{
    color: #c6c8cd;
  }
  .logout{
    float: right;
    margin-top: 10px;
    margin-right: 30px;
  }
</style>
