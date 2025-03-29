<script setup>
const route = useRoute();
console.log(typeof route.params.query);
const query = route.params.query;
const results = getResults(query);
</script>
<template>
  <div class="grid-flow-row">
    <div>
      <card
        v-for="result in results"
        :name="result.name"
        :price="result.price"
      />
    </div>
  </div>
</template>
