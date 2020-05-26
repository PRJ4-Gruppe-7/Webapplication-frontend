<template>
  <div id="app">
    <Header id="header" v-on:goto-settings="goto_settings"/>
    <SettingsWindow class="content" id="page2" v-on:selected-theme="changeTheme"/>
    <HeatmapWindow class="content" id="page1"/>
  </div>
</template>

<script>

import Header from './components/Header.vue'
import HeatmapWindow from './components/HeatmapWindow.vue'
import SettingsWindow from './components/SettingsWindow.vue'


export default {
  name: 'App',
  components: {
    SettingsWindow,
    HeatmapWindow,
    Header
  },
  data() { return {
      theme: 'dark_theme'
  };
  },
  mounted() {
    if (localStorage.theme) {
      console.log(localStorage.theme)
      this.theme = localStorage.theme;
      this.changeTheme(this.theme);
    }
    //this.changeTheme(this.theme);

  },
  methods: {
    goto_settings: function() {
      var page1 = document.getElementById("page1");
      var page2 = document.getElementById("page2");

      console.log(page2.style.marginLeft)
      if (page2.style.marginLeft != "0px")
      {
        page1.style.transitionDelay = "0s";
        page2.style.transitionDelay = "0.2s";
        page2.style.marginLeft = 0;
        page1.style.right = 100 + "vw";
      } else {
        page1.style.transitionDelay = "0.2s";
        page2.style.transitionDelay = "0s";
        page2.style.marginLeft = 100 + "vw";
        page1.style.right = 0;
      }
    },
    changeTheme: function(theme) {
      console.log(theme);
      document.getElementsByTagName("BODY")[0].className = theme;
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap');

* {
  -webkit-user-select: none;  /* Chrome all / Safari all */
  -moz-user-select: none;     /* Firefox all */
  -ms-user-select: none;      /* IE 10+ */
  user-select: none;          /* Likely future */
  overflow: hidden; /* Hide scrollbars */
  margin: 0px;
  padding: 0px;
}

#app {
  width: 100vw;
  height: 100vh;
  background-color: #514e5d;
  display: grid;
  grid-gap: 20px;
  grid-template-rows: 100px auto;
  grid-template-areas:
    "Header"
    "Content";
}

#header {
  grid-area: Header;
}

.content {
  grid-area: Content;
}

#page1 {
  position: relative;
  transition: 1s;
  right: 0;
}

#page2 {
  transition: 1s;
  margin-left: 100vw;
}


/* Light Theme */

.light_theme #app {
  background-color: white;
}


</style>
