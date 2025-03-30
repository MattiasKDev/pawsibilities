<template>
  <div class="min-h-screen flex justify-center items-center">
    <search @keyup.enter="showGrid = true" v-model="searchQuery"/>
    <h1 ></h1>
    <grid v-if="showGrid"/>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showGrid: false,
    };
  },
  // methods: {
  //   goToResults() {
  //     if (this.searchQuery.trim()) {
  //       this.$router.push(`/results/${encodeURIComponent(this.searchQuery)}`);
  //     }
  //   },
  // },
  
  created() {
    const getGeolocation = async () => {
      if (navigator.geolocation) {
      try {
        const position = await new Promise((resolve, reject) => {
        navigator.geolocation.getCurrentPosition(resolve, reject);
        });
        console.log("Latitude:", position.coords.latitude);
        console.log("Longitude:", position.coords.longitude);
      } catch (error) {
        console.error("Error getting geolocation:", error.message);
      }
      } else {
      console.error("Geolocation is not supported by this browser.");
      }
    };

    getGeolocation();
  }
};
</script>
