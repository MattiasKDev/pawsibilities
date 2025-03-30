<template>
  <div class="grid grid-cols-5 grid-rows-5 gap-4 min-h-screen">
    <div
      :style="{
        transform: searchActivated ? 'translateY(-40vh)' : 'translateY(0)',
      }"
      class="transition-transform duration-1000 ease-in-out col-start-2 col-end-5 row-start-3 self-center"
    >
      <input
        v-model="searchQuery"
        class="w-full bg-white text-gray-800 rounded-full px-6 py-3 shadow-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-green-500"
        type="text"
        placeholder="Type to search..."
        @keyup.enter="fetchResults"
      />
    </div>
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
        // const url = "http://192.168.0.167:8000/data";
        // const res = await $fetch(url, {
        //   method: "POST",
        //   headers: {
        //     "Content-Type": "application/json",
        //   },
        //   body: JSON.stringify({ query: this.searchQuery, lat: 0, lon: 0 }),
        // });
        // console.log("Response:", res);
        // this.results = res;
        const url =
          "https://raw.githubusercontent.com/MattiasKDev/pawsibilities/refs/heads/main/frontend/public/data.json";
        const res = await $fetch(url);
        this.results = JSON.parse(res);
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

input {
  transition: grid-row-start 0.3s ease-in-out, grid-row-end 0.5s ease-in-out;
}
</style>
