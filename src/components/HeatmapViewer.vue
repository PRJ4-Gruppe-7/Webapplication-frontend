<template>
  <div id="HeatmapViewer" @mouseover="mouseStatus(true)" @mouseleave="mouseStatus(false)">
    <div v-drag style="absolute" id="map">

      <Heatmap ref="Heatmapdiv" id="heatmap"/>
      <div id="Topography"/>
    </div>
  </div>
</template>

<script>
import drag from '@branu-jp/v-drag'
import Heatmap from './Heatmap.vue'

export default {
  name: 'HeatmapViewer',
  components: {
    Heatmap
  },
  directives: {
    drag,
  },
  data: function () {
    return {
      mouseOverHeatmap: false
    }
  },
  mounted: function() {
    new ResizeObserver(this.ResizeObserved).observe(document.getElementById("map"));
  },
  methods: {
    mouseStatus: function(bool) {
      this.mouseOverHeatmap = bool;
      if (bool == true)
      {
        document.addEventListener('wheel', this.onScroll);
      } else
      {
        document.removeEventListener('wheel', this.onScroll);
      }
    },
    ResizeObserved : function () {
      this.$refs.Heatmapdiv.onResize();
    },
    onScroll : function (event) {
        var add = 10;
        if (event.deltaY < 0) add = -add;

        var map = document.getElementById("map");
        map.style.height = (map.offsetHeight + add) + "px";
        map.style.width = (map.offsetHeight + add) + "px";
      }
  }
}
</script>


<style scoped>

#HeatmapViewer {
  clip-path: inset(0 0 0 0);
}

#map {
  clip-path: inset(-5px -4px -2px -2px);
  display: grid;
  grid-template-areas: "map";
  width: 500px;
  height: 500px;
  position: absolute;
  align-items: center;
  cursor: pointer;
}

#Topography {
  grid-area: map;
  box-shadow: inset 0px 0px 0px 2px #3282b8;
  width: 100%;
  height: 100%;
}

#heatmap {
  grid-area: map;
  width: 100%;
  height: 100%;
}


/* Light Theme */

.light_theme #Topography {
  box-shadow: inset 0px 0px 0px 2px #bde5f0;
}


</style>
