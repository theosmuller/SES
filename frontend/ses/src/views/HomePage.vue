<template>
  <div class = "container">
    <div><ClassList :classes="[1,2,3]"/></div>
    <div><Grid :columns="columns"/></div>
  </div>
  </template>
  
  <script>
  import Class from '../components/Class.vue';
  import ClassList from '../components/ClassList.vue';
  import Grid from '../components/Grid.vue';
  export default {
    components: {
        Class,
        ClassList,
        Grid,
    },
    data(){
  return{
    columns: [{
      id: 1,
      header: 'Monday',
      rows: [{
        id: 1,
        content: 'Class 1'
      },
    { id:2,
    content: 'Class 2'
    }]}, // Add a comma here
    {
      id: 2,
      header: 'Tuesday',
      rows: [{
        id: 1,
        content: 'Class 1'
      },
    { id:2,
      content: 'Class 2'
    }]}]
  }
}
  };
  </script>

  <style scoped>
  .container {
    display: flex;
    flex-direction: row;
    justify-content: left;
    align-items: center;
    height: 100vh;
    width: 100vw;
    background-color: #0e0720;
    background-size: repeat;
    background-position: center;
    color:white
  }

  .container > div {
    margin: 10px;
  }
  .grid{
    flex-basis: 30%;
  }
  </style>
  