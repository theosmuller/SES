<template>
    <div class="class-list">
        <transition-group name="class-item" tag="div">
            <div v-for="classItem, i in classes" :key="classItem" class="class-item">
                <Class
                :classId="classItem"
                @enroll="handleEnroll"
                v-show="doShow(i)"/>
            </div>
        </transition-group>
        <div class="button-box">
        <button @click="prevPage" :disabled="currentPage === 1" class="pagination-btn">Previous</button>
        <button @click="nextPage" :disabled="currentPage === pageCount" class="pagination-btn">Next</button>
        </div>
    </div>
</template>

<script>
import Class from './Class.vue';
export default {
    props: {
        classes: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
            currentPage: 1,
            itemsPerPage: 2
        }
    },
    computed: {
        pageCount(){
            let l = this.classes.length,
                s = this.itemsPerPage;
            return Math.ceil(l/s);
        },
    },
    components: {
        Class
    },
    methods: {
        handleEnroll(classInfo) {
            alert(`Enrolling in class ${classInfo.id}\nSection: ${classInfo.section.section}`);
        },
        nextPage(){
            if(this.currentPage < this.pageCount) this.currentPage++;
        },
        prevPage(){
            if(this.currentPage > 1) this.currentPage--;
        },
        doShow(i) {
            const start = (this.currentPage - 1) * this.itemsPerPage;
            const end = start + this.itemsPerPage;
            return i >= start && i < end
        },
    }
};
</script>

<style scoped>
.class-list {
    background-color: #0e0720;
    padding: 10px;
    display: flex;
    flex-direction: column;
    border-radius: 5px;
    max-width: 500px;
}

.class-item {
    margin: 10px;
}

.pagination-btn {
    margin: 10px;
    padding: 10px;
    border-radius: 5px;
    border: none;
    background-color: #f9f9f9;
    color: #333333;
    font-weight: bold;
    font-size: 1em;
    cursor: pointer;
    width:6em;
    text-align: center;
}

.pagination-btn:hover {
    background-color: #ffbe33;
    color: #f9f9f9;
}
.pagination-btn:disabled {
    background-color: #cccccc;
    color: #666666;
    cursor: not-allowed;
}

.button-box{
    display: flex;
    justify-content: center;
}
</style>
