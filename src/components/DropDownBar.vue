<template>
  <div id="dropBar" @click="click">
    <ul id="dropBarContent">
      <li id="text">{{items[selectedIndex]}}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'DropDownBar',
  props: {
    items: {
      type: Array,
      required: true
    },
    selectedIndex: {
      type: Number,
      default: 0
    },
    backgroundColor: String
  },
  data: function () {
    return {
      isOpen: false,
      dropBarContent: ""
    }
  },
  methods: {
    click: function(event) {
      if (!this.isOpen)
      {
        this.dropBarContent = document.getElementById("dropBarContent");

        this.items.forEach((item, i) => {
          if (this.selectedIndex != i)
          {
            var list = document.createElement("LI");
            var textnode = document.createTextNode(item);
            list.append(textnode);
            this.dropBarContent.append(list);
          }
        });

        this.isOpen = true;

      } else {

        this.close(event.toElement.innerHTML);
      }
    },
    close: function(newSelected) {
      this.selectedIndex = this.items.indexOf(newSelected);
      console.log(this.selectedIndex);
      var list = document.createElement("LI");
      var textnode = document.createTextNode(newSelected);
      list.append(textnode);
      this.dropBarContent.textContent = '';
      this.dropBarContent.append(list);

      this.isOpen = false;
    }
  }
}
</script>


<style scoped>
a{
  -webkit-user-select: none;  /* Chrome all / Safari all */
  -moz-user-select: none;     /* Firefox all */
  -ms-user-select: none;      /* IE 10+ */
  user-select: none;          /* Likely future */
}


</style>

<style>
#dropBarContent li {
  padding-left: 40px;
}
#dropBarContent li:hover {
  background-color: #354954;
}
</style>
