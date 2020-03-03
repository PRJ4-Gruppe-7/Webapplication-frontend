<template>
  <div id="HeatmapInfo">
    <h2 id="name_h2">{{room.name}}</h2>
    <hr id="Title_underline" />
  </div>
</template>

<script>
export default {
  name: 'HeatmapInfo',
  props: {
    room: Object
  }
}
</script>


<style scoped>
#Title_underline {
  border: 1px solid #3282b8;
}


#name_h2 {
  text-align: center;
  font-size: 40px;
  font-family: 'Open Sans';
  font-weight: 700;
  color: #3282b8;
}


</style>
