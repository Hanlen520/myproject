<template>
  <div id="app">

    <router-view/>
    <router-view>UpdateUrl</router-view>
    <router-view>Url</router-view>
    <router-view v-if="isRouterAlive"/>
  </div>
</template>

<script>

  export default {
    name: 'App',
    data(){
      return{
        isRouterAlive: true
      }
    },
    provide(){
      return{
      reload1: this.reload
    }
    },
    methods:{
      reload(){
        this.isRouterAlive = false;
        this.$nextTick(function () {
          this.isRouterAlive = true
        })
      }
    }

  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
