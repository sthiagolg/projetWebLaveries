<template>
    <div>
        Page des Laveries

        <h1 >Choisissez le bâtiment que vous souhaitez</h1>
		<v-container>
				<v-btn large color="info" @click="redirectTo('B')">B </v-btn>
		
				<v-btn large color="info" @click="redirectTo('D')">D</v-btn>
				<v-btn large color="info" @click="redirectTo('E')">E</v-btn>

				<v-btn large  color="info" @click="redirectTo('F')" >F</v-btn>

				<v-btn large color="info" @click="redirectTo('G')">G/J</v-btn>

				<v-btn large  color="info" @click="redirectTo('H')">H</v-btn>

				<v-btn large color="info" @click="redirectTo('I')">I</v-btn>
		
		
		
			<v-img :src="require('../../assets/plan.jpg')" />
	</v-container>
		  
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



<style>
  .p  {
    font-size: 4em;
  }
</style>
