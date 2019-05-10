<template>
    <div>
        Page des Laveries

        <p>I can put whatever I want here </p>
        <v-btn color="info" @click="redirectTo('B')">B</v-btn>
        
        
        <v-btn color="info">D</v-btn>
        <v-btn color="info">E</v-btn>
        <v-btn color="info">F</v-btn>
        <v-btn color="info">G/J</v-btn>
        <v-btn color="info">H</v-btn>
        <v-btn color="info">I</v-btn>
    </div>
</template>

<script>
import router from "../../index.js";
export default {
  name: "Laveries",
  /*mounted() {
    this.checkLoggedIn();
  },*/
  methods: {
      redirectTo : function (key){
      
       router.push("/laveries/"+key)
      
      }
  }
}
</script>
