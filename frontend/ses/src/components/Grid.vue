<template>
    <div class="grid">
        <div class="column" v-for="column in columns" :key="column.id">
            <GridColumn
                :header="column.header"
                :rows="column.rows"
            />
        </div>
    </div>
</template>

<script>
import GridColumn from './GridColumn.vue'
export default {
    name: 'Grid',
    props:{
        columns: {
            type: Array,
            required: true,
        },
    },
    components: {
        GridColumn,
    },
    // Your component's properties, methods, etc. go here
}
</script>

<style scoped>
.grid {
    display: flex;
    background-color:#fff;
    color:black;
    border-radius:10px;
}
.column{
    border-right:1px solid #f0f0f0;
    padding: 0px;
    width: 100%;
}
.column:last-child{
    border-right: none;
}
</style>
