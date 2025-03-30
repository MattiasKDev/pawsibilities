<template>
  <div class="grid grid-cols-5 grid-rows-5" grid-gap-4 min-h-screen>
    <input
      v-model="searchQuery"
      class="grid-item col-start-2 col-end-5 row-start-1 rounded-full text-black px-4 py-2"
      type="text"
      placeholder="Type to search..."
      @keyup.enter="fetchResults"
    />
    <div
      class="grid grid-cols-3 grid-rows-2 gap-4 col-start-2 col-end-5 row-start-2"
    >
      <card
        class="grid-item"
        v-if="loading"
        v-for="result in results"
        :name="result.name"
        :address="result.address"
        :url="result.url"
        :hour="result.hour"
        :price="result.price"
        :distance="result.distance"
      />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: "",
      showGrid: false,
      searchActivated: false, // New state to track animation
      results: [], // New state to store results
      loading: false,
    };
  },
  methods: {
    async fetchResults() {
      if (this.searchQuery.trim()) {
        this.searchActivated = true;
        const url = "http://192.168.0.167:8000/data";
        const res = await $fetch(url, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ query: this.searchQuery, lat: 0, lon: 0 }),
        });
        console.log("Response:", res);
        this.results = res;
        console.log(this.results);
        console.log(this.results[0].name);
        this.loading = true;
      }
    },
  },

  created() {
    const getGeolocation = async () => {
      try {
        const response = await fetch("http://ip-api.com/json/");
        const data = await response.json();
        console.log("Latitude:", data.lat);
        console.log("Longitude:", data.lon);
      } catch (error) {
        console.error("Error fetching geolocation from IP-API:", error.message);
      }
    };

    getGeolocation();
  },
};
</script>
<style scoped>
.grid {
  gap: 1rem; /* Adjust spacing between items */
}

.grid-item {
  width: 100%; /* Ensures the item spans the full width of its cell */
  height: 150px; /* Fixed height for each grid item */
}

.card {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
