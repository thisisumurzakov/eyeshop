<template>
  <v-app>
    <v-navigation-drawer
        v-model="drawer"
        temporary
    >
      <v-list nav>
        <v-list-group>
          <template v-slot:activator="{ props }">
            <v-list-item
                v-bind="props"
                prepend-icon="mdi-shape"
                title="Categories"
                value="Users"
            ></v-list-item>
          </template>
          <v-list nav>
            <v-list-item-subtitle>Man</v-list-item-subtitle>
            <v-divider class="mb-1"></v-divider>
            <v-list-item
                v-for="cat in man"
                :title="cat.title"
                :value="cat.id"
            ></v-list-item>

            <v-list-item-subtitle>Women</v-list-item-subtitle>
            <v-divider class="mb-1"></v-divider>
            <v-list-item
                v-for="cat in women"
                :title="cat.title"
                :value="cat.id"
            ></v-list-item>
          </v-list>
        </v-list-group>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
        color="primary"
    >
      <v-app-bar-nav-icon class="mr-5" @click="drawer = true"></v-app-bar-nav-icon>

      <v-app-bar-title>E-commerce</v-app-bar-title>
    </v-app-bar>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  components: {
  },

  data: () => ({
    drawer: false,
    man: [],
    women: []
  }),
  async created() {
    try {
      const data = await fetch('http://2c7d-185-139-137-40.ngrok.io/v1/category/M/')
      this.man = await data.json()
      const data2 = await fetch('http://2c7d-185-139-137-40.ngrok.io/v1/category/W/')
      this.women = await data2.json()
    } catch (e) {
      console.log(e)
    }
  }
}
</script>
