<template>
    <div>
        Batiment B

        <p>Choisissez les horaires de disponibilité des machines </p>
		<v-toolbar >

			<v-overflow-btn
			  :items="dropdown_edit"
			  editable
			  label="Horaire de début"
			  hide-details
			  class="pa-5"
			  overflow
			></v-overflow-btn>

			<v-divider
			  class="mr-5"
			  vertical
			></v-divider>
			<v-overflow-btn
			  :items="dropdown_edit"
			  editable
			  label="Horaire de fin"
			  hide-details
			  class="pa-5"
			  overflow
			></v-overflow-btn>
		  </v-toolbar>
        
		<p></p>
        <v-btn color="info"
        @click="showMachines()"
        >Show Machines</v-btn>
        <div id="welcomeDiv"  style="display:none;" class="answer_list" > WELCOME</div>
    
    </div>
</template>

<script>
import router from "../../../index.js";
import axios from 'axios';
import B from '@/components/pages/batiments/B.vue'
export default {
  name: "B",
  //el: '#example-1',
  /*mounted() {
    return axios.get('http://127.0.0.1:8000/machine/info/blabla/db',{headers: {'Access-Control-Allow-Credentials': true}})
    },*/
      data () {
      return {
        dropdown_edit: [
          { text: '10' },
          { text: '11' },
          { text: '12' },
          { text: '13' },
          { text: '14' },
		  { text: '15' },
		  { text: '16' },
		  { text: '17' },
		  { text: '18' },
		  { text: '19' },
		  { text: '20' },
		  { text: '21' },
		  { text: '22' },
		  { text: '12' }
        ]
      
      }
	  },
    //template: '<div>{{ message }}</div>',
    methods: {
      showMachines : function (){
      
       //this.$set(message, "hello")    
       document.getElementById('welcomeDiv').style.display = "block";
       document.getElementById('example').value = "thiago";
       axios.get('http://127.0.0.1:5000/machine/blabla',
       {headers: {'Access-Control-Allow-Credentials': true}})
       .then(function (response) {
          //console.log(response);
          alert(response);
        })
        .catch(function (error) {
          //console.log(error);
          alert(error);
        });
       //this.push({message: 'new message'});
        //alert(test);
      }
  }
}
</script>