<template>
    <div class="class-time">
        <p class="day">{{classDay}}</p>
        <p class="time">{{ startTime }} - {{ endTime }}</p>
    </div>
</template>

<script>
export default {
    props: {
        classDay: {
            type: String,
            required: true
        },
        startTime: {
            type: String,
            required: true
        },
        endTime: {
            type: String,
            required: true
        }
    }
}
</script>
<style scoped>
.class-time {
    display: inline-block;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    padding: 1em;
    margin: 0.1em;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
}
.class-time p {
    margin: 0;
    font-size: 0.9em;
    color: #333;
}
.day {
    font-weight: bold;
    font-size: 0.8em;
    text-align: center;
    margin-bottom: 10px;
}

.time{
    padding:0;
}
</style>