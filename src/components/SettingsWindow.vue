<template>
  <div class="SettingsWin">
    <div id="SettingsBox">
      <h1>Settings</h1>
      <div class="setting_item" id="theme">
        <a class="setting_text">Theme</a>
        <DropDownBar id="theme_drop" v-bind:items="theme_items" v-bind:selectedIndex="0" />
      </div>

      <div class="setting_item"  id="gradMin">
        <a class="setting_text">Gradient Color Minimum</a>
      </div>

      <div class="setting_item"  id="gradMax">
        <a class="setting_text">Gradient Color Maximum</a>
      </div>
    </div>
  </div>
</template>

<script>
import DropDownBar from './DropDownBar.vue'

export default {
  name: 'SettingsWindow',
  components: {
    DropDownBar
  },
  data: function() {
    return {
      theme_items: ["Dark Theme", "Light Theme"]
    }
  }
}
</script>



<style scoped>
.SettingsWin {

}

h1 {
  text-align: center;
  font-size: 50px;
  font-family: 'Open Sans';
  font-weight: 700;
  color: #514e5d;
  grid-area: title;
}

.setting_item {
  font-size: 28px;
  font-family: 'Open Sans';
  font-weight: 700;
}

.setting_text {
  color: #3282b8;
  margin-left: 40px;
}

#theme_drop {
  width: 100%;
  color: #1b262c;
  background-color: #514e5d;
  margin-left: 0px;
}

#SettingsBox {
  min-width: 400px;
  max-width: 40%;
  background-color: #1b262c;
  height: 95%;
  margin-right: auto;
  margin-left: auto;
  -webkit-box-shadow: 10px 10px 11px -1px rgba(57,59,77,1);
  -moz-box-shadow: 10px 10px 11px -1px rgba(57,59,77,1);
  box-shadow: 10px 10px 11px -1px rgba(57,59,77,1);

  display: grid;
  grid-template-rows: 120px;
  grid-template-areas:
    "title"
    "theme"
    "gradMin"
    "gradMax";
}



</style>
