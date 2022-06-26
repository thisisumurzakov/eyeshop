<template>
  <div class="pa-3">
    <div class="d-flex justify-space-around">
      <UploadImage @getData="setData"/>
      <div v-if="dirty" style="display: flex; flex-direction: column; justify-content: center">
        <p style="text-align: center">Your tone</p>
        <div
            class="tone"
        >
        </div>
      </div>
      <v-btn
          v-if="dirty"
          :disabled="loader"
          @click="getAllData"
          color="warning"
      >Clear filters
      </v-btn>
    </div>
    <div class="d-flex justify-center">
      <div>
        <v-checkbox
            v-model="checkBox"
            label="Man"
            value="Man"
            color="primary"
        ></v-checkbox>
      </div>
      <div>

        <v-checkbox
            v-model="checkBox"
            label="Woman"
            value="Woman"
            color="primary"
        ></v-checkbox>
      </div>
    </div>
    <div v-if="loader" class="d-flex justify-center mt-14">
      <v-progress-circular
          indeterminate
          color="primary"
          :size="70"
          :width="7"
      ></v-progress-circular>
    </div>
    <div class="d-flex ma-2 flex-wrap justify-center" v-else>
      <div v-if="data.length !== 0" v-for="n in data" class="d-flex-md ma-2">
        <ProductCard :product="n"/>
      </div>
      <div v-else>
        Nothing to show, try another image
      </div>
    </div>
  </div>
</template>

<script>
import ProductCard from '../components/ProductCard.vue';
import Pagination from '../components/Pagination.vue';
import UploadImage from '../components/UploadImage.vue';

export default {
  name: "Home",
  components: {UploadImage, Pagination, ProductCard},
  data() {
    return {
      loader: true,
      data: [],
      dataCopy: [],
      dirty: false,
      checkBox: ['Man', 'Woman']
    }
  },
  methods: {
    setData(products) {
      this.data = products.products
      this.dataCopy = products.products
      this.dirty = true
    },
    async getAllData() {
      this.loader = true
      try {
        const data = await fetch('http://2c7d-185-139-137-40.ngrok.io/v1/all/', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json'
          }
        })
        this.loader = false
        this.data = await data.json()
        this.dataCopy = this.data
      } catch (e) {
        console.log(e)
      }
      this.dirty = false
    }
  },
  created() {
    this.getAllData()
  },
  watch: {
    checkBox() {
      if (this.checkBox.length === 1 && this.checkBox[0] === 'Man') {
        this.data = this.dataCopy.filter(key => key.gender === 'M')
      }
      if (this.checkBox.length === 1 && this.checkBox[0] === 'Woman') {
        this.data = this.dataCopy.filter(key => key.gender === 'W')
      }
      if (this.checkBox.length === 2 || this.checkBox.length === 0) {
        this.data = this.dataCopy
      }
    }
  }
}
</script>

<style scoped>
.tone {
  background-image: url("http://2c7d-185-139-137-40.ngrok.io/media/pixel.jpg");
  height: 100px;
  width: 100px;
  border-radius: 5px;
}
</style>
