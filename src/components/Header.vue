<template>
  <header>
    <div id="logo">
      <img id="logo_png"   src="../img/logo.png"/>
    </div>
    <div id="bar">
      <a id="Title">FRUiT FLY</a>
      <div id="settings-container" @click="$emit('goto-settings')">
        <svg id="settings" enable-background="new 0 0 512 512" height="512" viewBox="0 0 512 512" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m464.866 192.8h-10.87c-3.531-11.05-7.986-21.784-13.323-32.097l7.698-7.698c18.665-18.645 18.165-48.525.006-66.665l-22.711-22.71c-18.129-18.153-48.015-18.679-66.665-.007l-7.704 7.704c-10.313-5.336-21.048-9.792-32.097-13.323v-10.871c0-25.989-21.144-47.133-47.134-47.133h-32.133c-25.989 0-47.133 21.144-47.133 47.133v10.871c-11.049 3.53-21.784 7.986-32.097 13.323l-7.697-7.697c-18.613-18.635-48.498-18.198-66.664-.006l-22.713 22.711c-18.152 18.132-18.677 48.014-.006 66.665l7.704 7.704c-5.337 10.313-9.792 21.046-13.323 32.097h-10.87c-25.989-.001-47.134 21.143-47.134 47.132v32.134c0 25.989 21.145 47.133 47.134 47.133h10.87c3.531 11.05 7.986 21.784 13.323 32.097l-7.698 7.698c-18.665 18.645-18.165 48.525-.006 66.665l22.711 22.71c18.129 18.153 48.015 18.679 66.665.007l7.704-7.704c10.313 5.336 21.048 9.792 32.097 13.323v10.871c0 25.989 21.145 47.133 47.134 47.133h32.133c25.989 0 47.134-21.144 47.134-47.133v-10.871c11.049-3.53 21.784-7.986 32.097-13.323l7.697 7.697c18.613 18.635 48.497 18.198 66.664.006l22.713-22.712c18.152-18.132 18.677-48.014.006-66.665l-7.704-7.704c5.337-10.313 9.792-21.046 13.323-32.097h10.87c25.989 0 47.134-21.144 47.134-47.133v-32.134c-.001-25.987-21.146-47.131-47.135-47.131zm-208.866 174.6c-61.427 0-111.4-49.974-111.4-111.4s49.973-111.4 111.4-111.4 111.4 49.974 111.4 111.4-49.973 111.4-111.4 111.4z"/></svg>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header'
}
</script>


<style scoped>
header {
  display: grid;
  grid-template-columns: 200px auto;
  grid-template-areas:
    "logo bar";
}



#settings {
  display: block;
  float: right;
  margin-top: 25px;
  margin-right: 30px;
  width: 50px;
  height: 50px;
  fill: #3282b8;
  transition: 0.3s;
  cursor: pointer;
}

#settings:hover {
  fill: white;
}


#logo {
  height: 100%;
  background-color: #323441;
  grid-area: logo;
}

#logo_png {
  margin-top: 10%;
  height: 60%;
  margin-left: auto;
  margin-right: auto;
  display: block;
}

#Title {
  margin-right: 30px;
  margin-left: 30px;
  display: inline-block;
  font-size: 70px;
  font-family: 'Open Sans';
  font-weight: 700;
  color: #fab32e;
  opacity: 0.7;
}

#settings-container {
  float: right;
  display: inline-block;
}

#bar {
  background-color: #1b262c;
  height: 100%;
  width: 100%;
  grid-area: bar;
}


/* Light Theme */

.light_theme #settings {
  fill: white;
}

.light_theme #settings:hover {
  fill: white;
}


.light_theme #logo {
  background-color: #bde5f0;
}

.light_theme #bar {
  background-color: #d7d7d7;
}
</style>
