<template>
    <div>
        <br><br>
        <h2>Page Administrateur</h2>
        
        

        <br>
        <br><br>
        <a href="http://127.0.0.1:8000/laveries/problemes"><h3>Voir liste de problèmes</h3></a>
        <br><br>
        <a href="http://127.0.0.1:8000/laveries/controler"><h3>Contrôler une machine</h3></a>
        
    </div>
</template>

<script>
import router from "../../index.js";
export default {
  name: "Admin",
  /*mounted() {
    this.checkLoggedIn();
  },*/
  mounted() {
            this.checkLoggedIn();
        },
  methods: {

    
  
    checkLoggedIn: function(){
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/auth");
      }
    },  

    informerProbleme: function(){

        router.push("/informerProbleme")

      },
      redirectTo : function (key){
      
       router.push("/laveries/"+key)
      
      },
      
    /*checkLoggedIn: function() {
        router.push('/auth');
    }*/
  }
  

}

</script>


