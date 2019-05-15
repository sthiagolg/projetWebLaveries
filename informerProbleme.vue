<template>
    <div>
        
        <p>Informer un Problème</p>

         <p>Votre nom: <br><textarea id="name" name="name" rows="1" cols="30" ></textarea></p>
            <p>Batiment: <br><textarea id="batiment" name="batiment" rows="1" cols="4"></textarea></p>
            <p>Machine: <br><textarea id="machine" name="machine" rows="1" cols="15"></textarea></p>
            <p>Description du problème:<br><textarea id="description" name="description" rows="10" cols="50"></textarea></p>
            


        <p><v-btn color="info"
        @click="send()"
        >send</v-btn></p>
        <div id="response"  style="display:none;" class="answer_list" > Hello</div>

        
        
        
    </div>
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
          document.getElementById('response').style.display = "block";
          document.getElementById('response').innerHTML = document.getElementById('name').value;
          //alert("cole");
          axios.post('http://127.0.0.1:8000/saveProblem',
       {
           name: document.getElementById('name').value,
           batiment: document.getElementById('batiment').value,
           machine: document.getElementById('machine').value,
           description: document.getElementById('description').value

       }).then(function (response) {
          //console.log(response);
          //this.message = response.data["etat"]
          //self.message = 'thiago'
          //this.$set(this, 'example', "hahhaa");
          alert(response.data["response"]);
        })

      }
  }
}
</script>
