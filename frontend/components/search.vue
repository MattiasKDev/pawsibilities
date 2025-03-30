<template>
        <input
      v-model="searchQuery"
      class="rounded-full text-black px-4 py-2"
      type="text"
      placeholder="Type to search..."
      @keyup.enter="goToResults"
    />
</template>

<script>
export default{
    data() {
    return {
      searchQuery: '',
    };
  },
  methods: {
    goToResults() {
    //   if (this.searchQuery.trim()) {
    //     this.$router.push(`/results/${encodeURIComponent(this.searchQuery)}`);
    //   }
        this.$emit('search', this.searchQuery);

    },

  },
}
</script>