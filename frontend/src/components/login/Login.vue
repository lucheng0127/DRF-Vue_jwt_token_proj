<template>
  <div id="login">
    <div class="layout">
      <div class="layout-content">
        <Row>
          <Col span="6" offset="9">
            <div class="login-form">
              <div class="login-form-title">
                <h1>Welcome to DGS</h1>
              </div>
              <Form :model="loginForm" :rules="ruleForm">
                <FormItem prop="user">
                  <Input type="text" v-model="loginForm.user" placeholder="用户名">
                    <Icon class="ivu-icon ivu-icon-person" slot="prepend"></Icon>
                  </Input>
                </FormItem>
                <FormItem prop="password">
                  <Input type="password" v-model="loginForm.password" placeholder="密码">
                    <Icon class="ivu-icon ivu-icon-locked" slot="prepend"></Icon>
                  </Input>
                </FormItem>
                <FormItem>
                  <Button type="ghost" @click="handleSubmit('loginForm')">登录</Button>
                </FormItem>
                <FormItem>
                  <div class="layout-copy">
                    &copy; 2017 lucheng | <Icon type="email" /> lc960127@gmail.com
                  </div>
                </FormItem>
              </Form>
            </div>
          </Col>
        </Row>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        loginForm: {
          user: '',
          password: ''
        },
        ruleForm: {
          user: [
            { required: true, message: '请输入用户名', trigger: 'blur' }
          ],
          password: [
            { required: true, message: '请输入密码', trigger: 'blur' },
            { type: 'string', min: 8, max: 15, message: '密码应8到15位', trigger: 'blur' }
          ]
        }
      }
    },
    methods: {
      handleSubmit () {
        this.$Message.error('错误信息!')
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
  .layout-content{
    background-image: url('../../assets/img/bg.jpg');
    height: -webkit-fill-available;
  }
  .layout-copy{
    text-align: center;
    padding: 10px 0 20px;
    color: #FFFFFF;
    margin-top: 40px;
  }
  .layout-ceiling-main a{
    color: #9ba7b5;
  }
  .login-form-title{
    text-align: center;
    margin-bottom: 40px;
  }
  .login-form{
    color: #FFFFFF;
    margin-top: 200px;
  }
  .login-form input{
    color: #FFFFFF;
    background: transparent;
  }
  .login-form button{
    color: #FFFFFF;
  }
</style>
