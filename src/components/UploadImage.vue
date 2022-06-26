<template>
  <div class="text-center">
    <v-btn
        color="primary"
    >
      Upload image

      <v-dialog
          v-model="dialog"
          activator="parent"
          persistent
      >
        <v-card class="pa-3" min-width="300px" max-width="100%">
          <div class="d-flex justify-end mb-1" @click="closeDialog">
            <v-btn icon="mdi-close" size="small" variant="plain"></v-btn>
          </div>
          <div class="d-flex flex-column">
            <v-btn
                class="mb-3"
                color="primary"
                @click="toggleCamera"
                v-if="!imageData"
            >
              <span v-if="!isCameraOpen">Open Camera</span>
              <span v-else>Close Camera</span>
            </v-btn>
            <v-btn @click="upload" color="primary" v-if="!isCameraOpen" type=" ">Choose from gallery</v-btn>
            <v-file-input
                v-show="false"
                type="file"
                ref="upload"
                accept="image/*"
                v-model="d"
                @change="onSelectFile"
            />
            <v-btn
                v-if="imageData"
                color="success"
                :disabled="isLoading"
                class="mt-2"
                @click="uploadPhoto"
            >Upload this photo</v-btn>
          </div>

          <div v-if="isCameraOpen" v-show="!isLoading" class="camera-box" :class="{ 'flash' : isShotPhoto }">

            <div class="camera-shutter" :class="{'flash' : isShotPhoto}"></div>

            <video v-show="!isPhotoTaken" ref="camera" style="max-width: 300px" :height="250" autoplay></video>

            <canvas v-show="isPhotoTaken" id="photoTaken" ref="canvas" style="max-width: 300px" :height="250"></canvas>
          </div>

          <div v-if="isCameraOpen && !isLoading" class="d-flex justify-center">
            <v-btn :icon="isPhotoTaken ? 'mdi-backup-restore': 'mdi-camera'" size="large" color="primary" @click="takePhoto">
            </v-btn>
          </div>

          <div v-if="isPhotoTaken && isCameraOpen" class="d-flex justify-center mt-3">
            <v-btn @click="downloadImage" color="success" :disabled="isLoading">
              Upload
            </v-btn>
          </div>
          <div
              v-if="imageData"
              :style="{ 'background-image': `url(${imageData})`}"
              class="f d-flex justify-end pa-2"
          >
            <v-btn
                icon="mdi-close"
                color="primary"
                variant="outlined"
                size="small"
                @click="this.imageData = null"
            ></v-btn>
          </div>
        </v-card>
      </v-dialog>
    </v-btn>
  </div>
</template>

<script>
export default {
  name: "UploadImage",
  data() {
    return {
      isCameraOpen: false,
      isPhotoTaken: false,
      isShotPhoto: false,
      isLoading: false,
      link: '#',
      dialog: false,
      imageData: null,
      d: [],
      im: null
    }
  },
  methods: {
    async uploadPhoto() {
      const fd = new FormData()
      fd.append('image', this.im, this.im.name)
      this.isLoading = true
      const data = await fetch('http://2c7d-185-139-137-40.ngrok.io/main/upload/', {
        method: 'POST',
        body: fd
      })
      const products = await data.json()
      this.isLoading = false
      this.$emit('getData', {
        products,
        dirty: true
      })
      this.dialog = false
      this.imageData = null
    },
    closeDialog() {
      this.dialog = false
      this.imageData = false
      this.isCameraOpen = false
      this.isPhotoTaken = false
    },
    onSelectFile(event) {
      this.im = event.target.files[0]
      const input = this.$refs.upload
      const files = input.files
      if (files && files[0]) {
        const reader = new FileReader
        reader.onload = e => {
          this.imageData = e.target.result
        }
        reader.readAsDataURL(files[0])
        this.$emit('input', files[0])
      }
    },
    upload() {
      this.$refs.upload.click()
    },
    toggleCamera() {
      if(this.isCameraOpen) {
        this.isCameraOpen = false;
        this.isPhotoTaken = false;
        this.isShotPhoto = false;
        this.stopCameraStream();
      } else {
        this.isCameraOpen = true;
        this.createCameraElement();
      }
    },

    createCameraElement() {
      this.isLoading = true;

      const constraints = (window.constraints = {
        audio: false,
        video: true
      });


      navigator.mediaDevices
          .getUserMedia(constraints)
          .then(stream => {
            this.isLoading = false;
            this.$refs.camera.srcObject = stream;
          })
          .catch(error => {
            this.isLoading = false;
            alert("May the browser didn't support or there is some errors.");
          });
    },

    stopCameraStream() {
      let tracks = this.$refs.camera.srcObject.getTracks();

      tracks.forEach(track => {
        track.stop();
      });
    },

    takePhoto() {
      if(!this.isPhotoTaken) {
        this.isShotPhoto = true;

        const FLASH_TIMEOUT = 50;

        setTimeout(() => {
          this.isShotPhoto = false;
        }, FLASH_TIMEOUT);
      }

      this.isPhotoTaken = !this.isPhotoTaken;

      const context = this.$refs.canvas.getContext('2d');
      context.drawImage(this.$refs.camera, 0, 0, 300, 230);
    },

    async downloadImage() {
      const canvas = document.getElementById("photoTaken").toDataURL("image/jpeg")
      const fd = new FormData()
      let ff = this.dataURLtoFile(canvas, 'new.jpg')
      this.isLoading = true
      fd.append('image', ff, 'new.jpg')
      const data = await fetch('http://2c7d-185-139-137-40.ngrok.io/main/upload/', {
        method: 'POST',
        body: fd
      })
      const products = await data.json()
      this.$emit('getData', {
        products,
        dirty: true
      })
      this.isLoading = false
      this.dialog = false
      this.isCameraOpen = false
      this.stopCameraStream()
    },
    dataURLtoFile(dataurl, filename) {

      let arr = dataurl.split(','),
          mime = arr[0].match(/:(.*?);/)[1],
          bstr = atob(arr[1]),
          n = bstr.length,
          u8arr = new Uint8Array(n);

      while(n--){
        u8arr[n] = bstr.charCodeAt(n);
      }

      return new File([u8arr], filename, {type:mime});
    }
  }
}
</script>

<style scoped>
.f {
  width: 300px;
  align-self: center;
  margin: 10px;
  height: 320px;
  background-size: cover;
  background-position: center center;
}
</style>
