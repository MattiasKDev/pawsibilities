<template>
    <div class="grid-container">
        <div class="card" v-for="card in cards" :key="card.id">
            <h3>{{ card.title }}</h3>
            <p>{{ card.description }}</p>
        </div>
    </div>
</template>

<script>
export default {
    
};
</script>

<style scoped>
.grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
}

.card {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 16px;
    text-align: center;
    background-color: #f9f9f9;
}
</style>