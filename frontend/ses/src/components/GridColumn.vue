<template>
    <div class="grid-column">
        <div class="column-header">{{ header }}</div>
        <div class="row" v-for="row in rows" :key="row.id">
            <div class="column-content">{{ row.content }}</div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'GridColumn',
    props: {
        header: {
            type: String,
            required: true,
        },
        rows: {
            type: Array,
            required: true,
        },
    }
}
</script>

<style scoped>
.grid-column {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    padding: 0px;
    width: 100%;
    height: 100%;
}
.column-header {
    font-size: 1.5em;
    font-weight: bold;
    margin-bottom: 10px;
    border-bottom: 1px solid #f0f0f0;
    padding: 20px;
}
.column-content {
    margin-bottom: 10px;
    text-align: center;
}
.row{
    padding: 20px;
    border-bottom: 1px solid #f0f0f0;
}
.row:last-child{
    border-bottom: none;
}
</style>
