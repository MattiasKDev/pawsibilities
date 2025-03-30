<template>
  <a
    :href="url"
    target="_blank"
    class="block bg-gradient-to-b from-gray-100 to-gray-200 text-black rounded-lg border-2 border-purple-500 shadow-md p-4 transition-transform hover:scale-125 hover:shadow-lg shadow-indigo-500/50"
  >
    <h2 class="text-lg font-bold">{{ name }}</h2>
    <p class="text-gray-600 text-sm">{{ address }}</p>
    <p class="text-gray-600 text-sm">Hours: {{ hour }}</p>
    <p class="text-gray-700">Price: ${{ price }}</p>
  </a>
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
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
a {
  display: block;
  overflow: auto; /* Enables scrolling for overflowing content */
  max-height: 150px; /* Set a maximum height for the card */
  text-overflow: clip; /* Prevents ellipsis and shows full text */
  white-space: normal; /* Allows text wrapping */
}

h2 {
  font-size: 1.25rem; /* Larger font size for the title */
}

p {
  max-height: 50px; /* Set a maximum height for each text block */
  white-space: normal; /* Allows text wrapping */
}

p.text-sm {
  font-size: 0.875rem; /* Smaller font size for Address and Hours */
  color: #4b5563; /* Slightly lighter gray for better readability */
}
</style>
