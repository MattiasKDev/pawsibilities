<script setup>
import { onMounted, ref } from "vue";
const route = useRoute();
const query = route.params.query;

const latitude = ref(null);
const longitude = ref(null);

const getUserLocation = () => {
  navigator.geolocation.getCurrentPosition(
    (position) => {
      latitude.value = position.coords.latitude;
      longitude.value = position.coords.longitude;
    },
    (error) => {
      console.error("Error getting location:", error);
    }
  );
};

// Call the function when the component is mounted
onMounted(() => {
  getUserLocation();
});
</script>
<template>
  <div class="grid-flow-row">
    <p class="text-center text-2xl font-bold mb-4">
      Search results for: {{ query }}
    </p>
    <div v-if="latitude && longitude" class="text-center">
      <p>Your location:</p>
      <p>Latitude: {{ latitude }}</p>
      <p>Longitude: {{ longitude }}</p>
    </div>
    <div v-else class="text-center">
      <p>Fetching your location...</p>
    </div>
  </div>
</template>
