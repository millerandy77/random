<template>
  <nav class="navbar">
    <nav class="right-side">
    <router-link to="/">Home</router-link>
    <router-link to="/news">News</router-link>
    <router-link to="/contact">Contact</router-link>
    </nav>
    <nav>
      <router-link class="active" to="/about">About</router-link>
    </nav>

  </nav>
  
  <router-view/>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  nav.navbar{
    display: flex;
    justify-content: space-between;
    background-color: #333;
  }

  nav.right-side{
    display: flex;
  }

  .active{
    background-color: #04AA6D;
    
  }

  nav a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
  }

  a:hover:not(.active) {
    background-color: #111;
  }

</style>
