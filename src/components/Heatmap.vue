<template>
    <div id="heatmapContainerWrapper">
      <svg id="svg_container" height="100%" width="100%" preserveAspectRatio="none">
        <!--
        <polygon points="0,0 100,0 100,50 70,50 70,70 100,70 100,100 0,100" style="fill:lime;stroke:purple;stroke-width:1" />
        -->
      </svg>

      <div id="heatmapContainer">
      </div>

    </div>
</template>

<script>

import * as h337 from 'heatmap.js';

export default {
  name: 'Heatmap',
  data: function() {
    return {
      heatmapdata: null,
      heatmap: "",
      radius: 0.8,
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

    var _this = this;

    this.getJSONAsync().then( function(result) {
      _this.heatmapdata = result.data



      _this.heatmap = h337.create(Object.assign({
        container: document.getElementById("heatmapContainer"),
      }, _this.config));


      _this.make_svg_topography(_this.heatmapdata);

      _this.adaptMap();

    }).catch(err =>
    {
      var error_text = document.createElement("a");
      error_text.textContent = err;
      error_text.style.fontSize = "40px"
      error_text.style.fontFamily = "Open Sans"
      error_text.style.fontWeight = "700"
      error_text.style.color = "red"
      document.getElementById("heatmapContainer").appendChild(error_text)

    });

  },
  methods: {
    onResize : function () {
      console.log("scale");
      var canvas = document.getElementsByClassName("heatmap-canvas");
      canvas[0].style.width = canvas[0].parentNode.parentNode.clientWidth + "px";
      canvas[0].style.height = canvas[0].parentNode.parentNode.clientHeight + "px";
    },
    getJSONAsync : async function(){

        const axios = require('axios');

        // The await keyword saves us from having to write a .then() block.
        let json = await axios.get('https://localhost:44306/Heatmap');

        // The result of the GET request is available in the json variable.
        // We return it just like in a regular synchronous function.
        return json;
    },
    make_svg_topography : function (heatmapdata) {
      console.log("making svg")
      var width = 0.05
      // Get the container
      var svg_container = document.getElementById("svg_container")
      var heatmap_container = document.getElementById("heatmapContainer")

      // Finding maximum values to determine viewBox size
      var max_x = Math.max.apply(Math, heatmapdata.map(function(o) { return o.x; }));
      var max_y = Math.max.apply(Math, heatmapdata.map(function(o) { return o.y; }));
      console.log(max_x, max_y)

      svg_container.setAttribute("viewBox","0 0 " + max_x + " " + max_y);

      // Create general shape
      var pointData = this.GetPointData(this.heatmapdata)
      var pointString = this.createPointString(pointData)
      var polygon_container = document.createElementNS('http://www.w3.org/2000/svg','polygon');
      polygon_container.setAttribute("points", pointString);
      polygon_container.setAttribute("style", "fill:none;stroke:purple;stroke-width:" + width);

      //Create clippath
      var polygonString = this.createPolygonString(pointData)
      heatmap_container.style.clipPath = polygonString
      console.log(polygonString)

      // Extract negative space
      /*
      var polygon_negative_container = document.createElementNS('http://www.w3.org/2000/svg','polygon');
      polygon_negative_container.setAttribute("points","1,1 2,1 2,2 1,2");
      // Get current color of background
      var bg_color = window.getComputedStyle(document.getElementById("HeatmapBox")).backgroundColor
      polygon_negative_container.setAttribute("style", `fill:${bg_color};stroke:purple;stroke-width:${width}`);
      */


      svg_container.appendChild(polygon_container)
      //svg_container.appendChild(polygon_negative_container)
    },
    GetPointData : function(heatmapdata) {
      // Pass each line and find corners
      var corners = []

      heatmapdata.forEach(iterate);

      function iterate(coord) {
        console.log(`for the coordinate: ${coord.x},${coord.y}`)
        var gapright, gapleft, gapup, gapdown,
        norightneighbour, noleftneighbour,
        noupneighbour, nodownneighbour = false


        // Check if gap right
        if (!heatmapdata.some(e => e.y === coord.y && e.x === coord.x + 1)) {
          gapright = true
          console.log("Gap right")
        }

        // Check if gap left
        if (!heatmapdata.some(e => e.y === coord.y && e.x === coord.x - 1)) {
          gapleft = true
          console.log("Gap left")
        }

        // Check if gap down
        if (!heatmapdata.some(e => e.y === coord.y - 1 && e.x === coord.x)) {
          gapdown = true
          console.log("Gap down")
        }

        // Check if gap up
        if (!heatmapdata.some(e => e.y === coord.y + 1 && e.x === coord.x)) {
          gapup = true
          console.log("Gap up")
        }

        // Check if right neigbour doesnt continue
        if ((gapup && heatmapdata.some(e =>  (e.y === coord.y + 1 && e.x === coord.x + 1)))
            ||
            (gapdown && heatmapdata.some(e =>  (e.y === coord.y - 1 && e.x === coord.x + 1))))
            {
          norightneighbour = true
          console.log("Right neighbour doesnt continue")
        }



        // Check if left neigbour doesnt continue
        if ((gapup && heatmapdata.some(e =>  (e.y === coord.y + 1 && e.x === coord.x - 1)))
            ||
            (gapdown && heatmapdata.some(e =>  (e.y === coord.y - 1 && e.x === coord.x - 1))))
            {
          noleftneighbour = true
          console.log("Left neighbour doesnt continue")
        }

        // Check if down neigbour doesnt continue
        if ((gapright && heatmapdata.some(e =>  (e.y === coord.y - 1 && e.x === coord.x + 1)))
            ||
            (gapleft && heatmapdata.some(e =>  (e.y === coord.y - 1 && e.x === coord.x - 1))))
            {
          nodownneighbour = true
          console.log("Down neighbour doesnt continue")
        }

        // Check if up neigbour doesnt continue
        if ((gapright && heatmapdata.some(e =>  (e.y === coord.y + 1 && e.x === coord.x + 1)))
            ||
            (gapleft && heatmapdata.some(e =>  (e.y === coord.y + 1 && e.x === coord.x - 1))))
            {
          nodownneighbour = true
          console.log("Up neighbour doesnt continue")
        }

        // Data collected time to write rules:
        if ((gapup && gapleft) || (gapup && gapright) || (gapdown && gapleft) || (gapdown && gapright)) corners.push([coord.x,coord.y])
        if (norightneighbour) corners.push([coord.x + 1, coord.y])
        if (noleftneighbour) corners.push([coord.x - 1, coord.y])
        if (nodownneighbour) corners.push([coord.x, coord.y + 1])
        if (noupneighbour) corners.push([coord.x, coord.y - 1])

        console.log(noupneighbour, nodownneighbour, noleftneighbour, norightneighbour)

      }
      corners = this.multiDimensionalUnique(corners)

      this.Sort(corners);



      return corners;

    },
    createPointString : function(corners)  {
      // Create point string
      var output = ""
      corners.forEach(stringIT);

      function stringIT(coord)
      {
        output += `${coord[0]},${coord[1]} `

      }
      console.log(output)
      return output
    },
    createPolygonString : function(corners)  {
      // Create polygon string
      var max_x = Math.max.apply(Math, this.heatmapdata.map(function(o) { return o.x; }));
      var max_y = Math.max.apply(Math, this.heatmapdata.map(function(o) { return o.y; }));
      var output = ""
      corners.forEach(stringIT);

      function stringIT(coord)
      {
        output += `${coord[0]/max_x*100}% ${coord[1]/max_y*100}%, `

      }
      console.log(output)
      return `polygon(${output.slice(0,-2)})`
    },

    multiDimensionalUnique : function(arr)  {

      // Found on StackOverflow: https://stackoverflow.com/questions/20339466/how-to-remove-duplicates-from-multidimensional-array
      var uniques = [];
      var itemsFound = {};
      for(var i = 0, l = arr.length; i < l; i++) {
          var stringified = JSON.stringify(arr[i]);
          if(itemsFound[stringified]) { continue; }
          uniques.push(arr[i]);
          itemsFound[stringified] = true;
      }
      return uniques;
    },
    Sort : function(arr) {
      for (var i = 1; i < arr.length; i++) {
        if (arr[i-1][0] != arr[i][0] && arr[i-1][1] != arr[i][1])
        {

          console.log("Mistake" + arr[i]);
          if (arr[i+1] != undefined)
          {
            [arr[i+1], arr[i]] = [arr[i], arr[i+1]];
          }


        }
      }
    },
    adaptMap: function() {
      var heatmapdiv = document.getElementById("heatmapContainer");
      console.log(heatmapdiv);

      var max_x = Math.max.apply(Math, this.heatmapdata.map(function(o) { return o.x; }));
      console.log(max_x);

      var factor = heatmapdiv.clientWidth / max_x;
      console.log(factor);

      var dataobj = this.heatmapdata;

      var max_value = Math.max.apply(Math, this.heatmapdata.map(function(o) { return o.value; }));

      dataobj.forEach((item) => {
        item.x = item.x * factor;
        item.y = item.y * factor;
        item.radius = this.radius * factor;
        item.value = (item.value / max_value) + 1 // Normalize
      });




      var data = {
        max: 2.0,
        min: 1.0,
        data: dataobj
      };

      this.heatmap.setData(data);
      console.log(dataobj);
      console.log(this.heatmap.getData());

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

#svg_container {
  top: 0;
  position: absolute;

}


</style>
