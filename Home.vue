<template>
    <div>
        
  <v-navigation-drawer permanent>
    <v-toolbar flat>
      <v-list>
        <v-list-tile>
          <v-list-tile-title class="title">
            Application
          </v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-toolbar>

    <v-divider></v-divider>

    <v-list dense class="pt-0">
      <v-list-tile
        v-for="item in items"
        :key="item.title"
        @click="redirectTo(item.title)"
      >
        <v-list-tile-action>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-tile-action>

        <v-list-tile-content>
          <v-list-tile-title>{{ item.title }}</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
    </v-list>
  </v-navigation-drawer>

        <h1>Hi !</h1>
        <p>You're logged in with Vue + Vuex JWT!!</p>
        <h3>Users from secure api end point:</h3>
        
        <p>
            <router-link to="/laveries">Laveries</router-link>
        </p>
        <p>
            
            <router-link to="/auth">Authentification</router-link>
        </p>
    </div>
</template>


<script>
import router from "../../index.js";
export default {
  name: "Home",
  /*mounted() {
    this.checkLoggedIn();
  },

  methods: {
    checkLoggedIn() {
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/auth/");
      }
    }
  }*/
  methods: {
    redirectTo : function (key){
      if (key=='Laveries'){
        router.push("/laveries");
    }else{
      router.push("/auth");
    }
    }

  },
  
    data () {
      return {
        items: [
          { title: 'Laveries', icon: 'dashboard' },
          { title: 'Auth', icon: 'question_answer' }
        ],
        right: null
      }
    }
  
};
</script>
