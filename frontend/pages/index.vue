<template>
  <div class="grid grid-cols-5 grid-rows-6 gap-4 min-h-screen relative">
    <div
      class="absolute left-1/2 transform -translate-x-1/2 transition-all duration-1000 ease-in-out text-center flex flex-col items-center"
      :style="inputPositionStyle"
    >
      <p class="text-4xl font-bold text-green-600 mb-4">Pawsibilities</p>
      <input
        v-model="searchQuery"
        class="w-96 bg-white text-gray-800 rounded-full px-6 py-3 shadow-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-green-500"
        type="text"
        placeholder="Type to search..."
        @keyup.enter="fetchResults"
      />
    </div>

    <!-- Loading Animation -->
    <div
      v-if="searchActivated && !loading"
      class="absolute inset-0 flex justify-center items-center"
    >
      <div class="loader"></div>
    </div>

    <div
      class="grid grid-cols-2 grid-rows-2 gap-4 col-start-2 col-end-5 row-start-3 row-end-6"
    >
      <card
        class="grid-item"
        v-if="loading"
        v-for="result in results"
        :key="result.name"
        :name="result.name"
        :address="result.address"
        :url="result.website"
        :hour="result.hours"
        :price="result.price"
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
      long: 0,
      lat: 0,
    };
  },
  methods: {
    async fetchResults() {
      if (this.searchQuery.trim()) {
        this.searchActivated = true;
        this.loading = false; // Ensure loading is false initially
        const url = "http://159.89.117.226:8080/data";
        const res = await useFetch(url, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            query: this.searchQuery,
            lat: this.lat,
            long: this.long,
          }),
        });
        console.log("Response:", res);
        this.results = res;
        this.loading = true; // Set loading to true when results are ready
      }
    },
  },

  created() {
    const getGeolocation = async () => {
      try {
        const response = await useFetch("http://ip-api.com/json/");
        const data = response.data.value;
        console.log("Latitude:", data.lat);
        this.lat = data.lat;
        console.log("Longitude:", data.lon);
        this.long = data.lon;
      } catch (error) {
        console.error("Error fetching geolocation from IP-API:", error.message);
      }
    };

    getGeolocation();
  },
  computed: {
    inputPositionStyle() {
      return {
        top: this.searchActivated ? "10%" : "50%", // Moves from 50% to 10% of the screen height
      };
    },
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

/* Loader Animation */
.loader {
  border: 8px solid #f3f3f3; /* Light gray */
  border-top: 8px solid #4caf50; /* Green */
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
