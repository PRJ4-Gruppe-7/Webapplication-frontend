<template>
  <div class="HeatWin">
    <RoomsBar id="NavBar" v-bind:rooms="Rooms"/>
    <div id="HeatmapBox">
      <HeatmapInfo id="HeatmapInfo" v-bind:room="currentRoom"/>
      <HeatmapViewer id="HeatmapViewer"/>
    </div>
  </div>
</template>

<script>
import HeatmapViewer from './HeatmapViewer.vue'
import HeatmapInfo from './HeatmapInfo.vue'
import RoomsBar from './RoomsBar.vue'

export default {
  name: 'HeatmapWindow',
  components: {
    HeatmapViewer,
    HeatmapInfo,
    RoomsBar
  },
  data: function () {
    return {
      currentRoom: {name: "009-S"},
      Rooms: [{name: "009-S"}, {name:  "003B-S"}]
    }
  }
}
</script>



<style scoped>
.HeatWin {
  display: grid;
  grid-column-gap: 30px;
  grid-template-columns: 200px auto;
  grid-template-areas:
    "navbar heatmap";
}

#NavBar {
  height: 95%;
  grid-area: navbar;
  margin-left: 20px;
}

#HeatmapBox {
  background-color: #1b262c;
  height: 95%;
  grid-area: heatmap;
  grid-gap: 30px;
  margin-right: 20px;
  -webkit-box-shadow: 10px 10px 11px -1px rgba(57,59,77,1);
  -moz-box-shadow: 10px 10px 11px -1px rgba(57,59,77,1);
  box-shadow: 10px 10px 11px -1px rgba(57,59,77,1);

  display: grid;
  grid-template-columns: 250px auto;
  grid-template-areas:
    "statistics heatmap";
}

#HeatmapInfo {
  margin: 30px;
  margin-right: 0px;
  grid-area: statistics;
}

#HeatmapViewer {
  margin: 30px;
  margin-left: 0px;
  grid-area: heatmap;
  -webkit-box-shadow: inset 2px -2px 39px -4px rgba(0,0,0,0.27);
  -moz-box-shadow: inset 2px -2px 39px -4px rgba(0,0,0,0.27);
  box-shadow: inset 2px -2px 39px -4px rgba(0,0,0,0.27);

}


/* Light Theme */

.light_theme #HeatmapBox {
  background-color: #ebebeb;
  -webkit-box-shadow: 10px 10px 11px -1px rgba(57,59,77,0.2);
  -moz-box-shadow: 10px 10px 11px -1px rgba(57,59,77,0.2);
  box-shadow: 10px 10px 11px -1px rgba(57,59,77,0.2);
}

.light_theme #HeatmapViewer {
  -webkit-box-shadow: inset 2px -2px 39px -4px rgba(0,0,0,0.27);
  -moz-box-shadow: inset 2px -2px 39px -4px rgba(0,0,0,0.27);
  box-shadow: inset 2px -2px 39px -4px rgba(0,0,0,0.27);
}


</style>
