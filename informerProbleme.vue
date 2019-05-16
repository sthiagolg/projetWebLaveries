
<template>
  <v-card
    class="mx-auto"
    max-width="500"
  >

    <v-card-title class="title font-weight-regular justify-space-between">
      <span>{{ currentTitle }}</span>
      <v-avatar
        color="primary lighten-2"
        class="subheading white--text"
        size="24"
        v-text="step"
      ></v-avatar>
    </v-card-title>

    <v-window v-model="step">
      <v-window-item :value="1">
        <v-card-text>
          <v-text-field
            label="Nom"
             type="Nom"
             id="name"
          ></v-text-field>
        </v-card-text>
      </v-window-item>
      <v-window-item :value="2">
        <v-card-text>
          <v-text-field
            label="Bâtiment"
            type="Bâtiment"
            id="batiment"
          ></v-text-field>
          <v-text-field
            label="numéro de machine"
            type="numéro de machine"
            id="machine"
          ></v-text-field>
          <span class="caption grey--text text--darken-1">
            Merci d'entrer le bâtiment et la numéro de machine
          </span>
        </v-card-text>
      </v-window-item>

      <v-window-item :value="3">
        <div class="pa-3 text-xs-center">
		<p><br><textarea id="description" name="description" rows="10" cols="50"></textarea></p>
          <span class="caption grey--text"> Merci de préciser le problème</span>
        </div>
      </v-window-item>
    </v-window>

    <v-divider></v-divider>

    <v-card-actions>
      <v-btn
        :disabled="step === 1"
        flat
        @click='step--'
      >
        Back
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn
        :disabled="step === 3"
        color="primary"
        depressed
        @click='step++'
      >
        Next
      </v-btn>
      <v-btn
        :disabled="step === 1||step === 2"
        color="primary"
        depressed
        @click='send()'
      >
        Send
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import router from "../../index.js";
import axios from 'axios';
export default {
  name: "InformerProbleme",
  /*mounted() {
    this.checkLoggedIn();
  },*/
  methods: {
      redirectTo : function (key){
      
       router.push("/laveries/"+key)
      
      },
      send : function(){
          //var name = document.getElementById('name').value
          //alert(name)
          //step++;
          var name1 = document.getElementById('name').value;
          var batiment1 = document.getElementById('batiment').value;
          var machine1 = document.getElementById('machine').value;
          var description1 = document.getElementById('description').value;
          if (!name1 ||!batiment1||!machine1||!description1){
            alert("Vous devez remplir tout les champs!");
          }else{
          //document.getElementById('response').style.display = "block";
          //document.getElementById('response').innerHTML = document.getElementById('name').value;
          //alert("cole");
          axios.post('http://127.0.0.1:8000/saveProblem',
       {
           name: name1,
           batiment: batiment1,
           machine: machine1,
           description: description1
       }).then(function (response) {
          //console.log(response);
          //this.message = response.data["etat"]
          //self.message = 'thiago'
          //this.$set(this, 'example', "hahhaa");
          alert(response.data["response"]);
          router.push('/');
        })
      }}
  },
  data: () => ({
      step: 1
    }),

    computed: {
      currentTitle () {
        switch (this.step) {
          case 1: return 'Votre nom'
          case 2: return 'Bâtiment et numéro'
          case 3: return 'Description du problème:'
        }
      }
    }
}
</script>



