<template>
  <div
    class="bg-gradient-to-b from-gray-100 to-gray-200 text-black rounded-lg border-2 border-purple-500 shadow-md p-4 transition-transform transform hover:scale-105 hover:shadow-lg"
  >
    <h2 class="text-lg font-bold">{{ name }}</h2>
    <p class="text-gray-700">Address: {{ address }}</p>
    <p class="text-gray-700">Hours: {{ hour }}</p>
    <p class="text-gray-700">Price: ${{ price }}</p>
    <p class="text-gray-700">Distance: {{ distance }} km</p>
    <a :href="url" target="_blank" class="text-blue-500 underline">
      Visit Website
    </a>
  </div>
</template>

<script>
export default {
  props: {
    name: {
      type: String,
      required: true,
    },
    address: {
      type: String,
      required: true,
    },
    url: {
      type: String,
      required: true,
    },
    hour: {
      type: String,
      required: true,
    },
    price: {
      type: Number,
      required: true,
    },
    distance: {
      type: Number,
      required: true,
    },
  },
};
</script>
