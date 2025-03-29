<template>
  <div class="bg-white text-black rounded-lg shadow-md p-4">
    <h2 class="text-lg font-bold">{{ name }}</h2>
    <p class="text-gray-700">Price: ${{ price }}</p>
  </div>
</template>

<script>
export default {
  props: {
    name: {
      type: String,
      required: true,
    },
    price: {
      type: Number,
      required: true,
    },
  },
};
</script>
