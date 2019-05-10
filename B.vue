<template>
    <div>
        Batiment B

        <p>I can put whatever I want here </p>
        
        <div id="example">example: {{ message }}</div>
        <div id="message">msg: </div>
        
        
        
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
    data: {
    // declare message with an empty value
    //message: 'Foo'
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
