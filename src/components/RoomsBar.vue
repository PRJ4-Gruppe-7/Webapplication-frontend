<template>
  <div id="RoomsBar">
    <ul id="Rooms">
      <li v-for="room in rooms" :key="room.name">
        {{ room.name }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HeatmapWindow',
  props: {
    rooms: {
      type: Array,
      required: true
    }
  }
}
</script>


<style scoped>
#Rooms li {
  font-size: 40px;
  font-family: 'Open Sans';
  font-weight: 700;
  color: #514e5d;
  font-size: 40px;
  background-color: #1b262c;
  margin-top: 30px;
  padding-left: 10px;
}

#Rooms {
  margin-top: 20%;
}


/* Light Theme */

.light_theme #Rooms li {
  color: #b1b1b1;
  background-color: #ebebeb;
}

</style>
