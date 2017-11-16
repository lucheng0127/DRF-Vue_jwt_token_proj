<template>
  <div id="app">
    <v-login></v-login>
  </div>
</template>

<script>
  import login from './components/login/login.vue'

  export default {
    name: 'app',
    components: {
      'v-login': login
    }
  }
</script>

<style>
</style>
