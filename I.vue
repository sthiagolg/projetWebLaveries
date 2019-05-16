<template>
    <div>
        <h1>Bâtiment I</h1>
		<p></p>

        <h2>Choisissez les horaires de disponibilité des machines </h2>
		<p></p>
		<v-toolbar >
			<v-overflow-btn
			  :items="date"
			  editable
			  label="Date"
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
			<v-divider
			  class="mr-5"
			  vertical
			></v-divider>
			<v-btn color="info"
				@click="verifierDisponibilite()"
			>Show Machines</v-btn>			
		  </v-toolbar>
        
		<p></p>
        <v-btn large color="info"
        @click="showMachines('I')"
        >Show Machines available now</v-btn>
				<br><br><br>
				<h2 id="machines"></h2>
    </div>
</template>

<script>
import router from "../../../index.js";
import axios from 'axios';
import I from '@/components/pages/batiments/I.vue'
export default {
  name: "I",
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
        ],
		date: [
          { text: "Aujourd'hui" },
          { text: 'Demain' },
          { text: 'Apès-demain' }
        ]	
      }
	  },
    //template: '<div>{{ message }}</div>',
    methods: {
      showMachines : function (batiment){
      var date = new Date();
					//var minutes = date.getMinutes();
					var hour = date.getHours();
					var minutes = date.getMinutes();
       //this.$set(message, "hello")    
       
       //document.getElementById('example').value = "thiago";
       axios.get('http://127.0.0.1:8000/machine/info/'+batiment+'/db',
       {headers: {'Access-Control-Allow-Credentials': true}})
       .then(function (response) {
          //console.log(response);
					//alert(response.data["seche"]);
					document.getElementById('machines').innerHTML = hour+"h"+minutes+": Il y a "+response.data["lave"]+" laves linges et "+ response.data["seche"]+" sèches linges disponibles maintenant au "+batiment;
        })
        .catch(function (error) {
          //console.log(error);
          alert(error);
        });
       //this.push({message: 'new message'});
        //alert(test);
      },
			verifierDisponibilite: function(){
					alert("Cette fonctionalité est indisponible pour l'instant");

			}
  }
}
</script>