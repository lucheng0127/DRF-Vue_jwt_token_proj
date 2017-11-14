<template>
  <div class="user-info">
    <h2>用户信息：</h2>
    <ul v-if="users && users.count">
      <li v-for="user in users.results">
        {{ user.nickname }}-{{ user.username_cn }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'user-info',
  data () {
    return {
      users: [],
    }
  },

  created () {
    this.$axios.get('http://127.0.0.1:8000/user-info.json/')
    .then(function (response) {
      console.log(response);
      this.users = response.data;
    }.bind(this))
    .catch(function (error) {
      console.log(error);
    });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
