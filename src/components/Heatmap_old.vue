<template>
    <div id="heatmapContainerWrapper">
        <div id="heatmapContainer">
        </div>
    </div>
</template>

<script>

import * as h337 from 'heatmap.js';
import heatmapdata_json from '../data/heat.json'
// import heatmapdata_json from '../data/heatmapdata.json'

export default {
  name: 'Heatmap',
  data: function() {
    return {
      heatmapdata: heatmapdata_json,
      heatmap: "",
      radius: 70,
      config: {
        gradient: {
          // enter n keys between 0 and 1 here
          // for gradient color customization
          '.3': '#3282b8',
          '.7': '#A14F47',
          '.90': '#CCE248',
          '.95': 'white'
        },
        maxOpacity: 1,
        minOpacity: 0
      }
    }
  },
  mounted: function () {
    this.heatmap = h337.create(Object.assign({
      container: document.getElementById("heatmapContainer")
    }, this.config));

    /* This is a hotfix */
    this.adaptMap();
    this.adaptMap();
    this.adaptMap();
  },
  methods: {
    onResize : function () {
      this.scaleHeatmap();
    },
    scaleHeatmap : function () {
      console.log("scale");
      var canvas = document.getElementsByClassName("heatmap-canvas");
      canvas[0].style.width = canvas[0].parentNode.parentNode.clientWidth + "px";
      canvas[0].style.height = canvas[0].parentNode.parentNode.clientHeight + "px";

    },
    adaptMap: function() {
      var heatmapdiv = document.getElementById("heatmapContainer");
      console.log(heatmapdiv);

      var max_x = Math.max.apply(Math, this.heatmapdata.map(function(o) { return o.x; }));
      console.log(max_x);

      var factor = heatmapdiv.clientWidth / max_x;
      console.log(factor);

      var dataobj = this.heatmapdata;
      console.log(dataobj);

      dataobj.forEach((item) => {
        item.x = item.x * factor;
        item.y = item.y * factor;
        item.radius = this.radius;
      });

      var data = {
        max: 20.0,
        min: 0,
        data: dataobj
      };
      console.log(data);

      this.heatmap.setData(data);

    }
  }
}


</script>

<style scoped>

#heatmapContainer {
  position: absolute;
  width: 100%;
  height: 100%;
}


</style>
