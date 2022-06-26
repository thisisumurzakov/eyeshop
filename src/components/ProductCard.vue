<template>
  <v-hover
      v-slot="{ isHovering, props }"
  >
  <v-card
      class="mx-auto"
      width="344"
      :elevation="isHovering ? 9 : 3"
      v-bind="props"
  >
    <v-img
        :src="`http://2c7d-185-139-137-40.ngrok.io${product.image}`"
        height="200px"
    ></v-img>

    <v-card-title>
      {{ product.title }}
    </v-card-title>

    <v-card-subtitle>
      {{ product.price }}
    </v-card-subtitle>

    <v-card-actions>
      <v-btn
          color="primary"
          variant="text"
      >
        Buy
      </v-btn>

      <v-spacer></v-spacer>

      <v-btn
          :icon="show ? 'mdi-chevron-up' : 'mdi-chevron-down'"
          @click="show = !show"
      ></v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
  </v-hover>
</template>

<script>
export default {
  name: "ProductCard",
  props: ['product'],
  data: () => ({
    show: false,
  })
}
</script>

<style scoped>

</style>
