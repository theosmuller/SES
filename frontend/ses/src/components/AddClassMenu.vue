<template>
  <div class="add-class-menu">
    <div class="menu-title">Add new class information</div>
    <div class="form-container">
      <div class="form-field">
        <label for="className">Name:</label>
        <input type="text" id="className" v-model="className" />
      </div>
      <div class="form-field">
        <label for="classCode">Code:</label>
        <input type="text" id="classCode" v-model="classCode" />
      </div>
      <div class="form-field checkbox-field">
        <label for="offerToOtherCourses">Offer to other courses:</label>
        <input type="checkbox" id="offerToOtherCourses" v-model="offerToOtherCourses" />
      </div>
      <div class="form-field">
        <label for="credits">Credits:</label>
        <input type="number" id="credits" v-model="credits" />
      </div>
      <div class="form-field">
        <label for="prerequisites">Pre-requisites:</label>
        <div v-for="(prerequisite, index) in prerequisites" :key="index" class="prerequisite-item">
          <button class="item-content" @click="removePrerequisite(index)">
            {{ prerequisite }} x
          </button>
        </div>
        <button @click="addPrerequisite">+</button>
      </div>
      <div class="form-field">
        <label for="classOptions">Class options:</label>
        <div v-for="(option, index) in classOptions" :key="index" class="class-option-item">
          <button class="item-content" @click="removeClassOption(index)">
            {{ option }} x
          </button>
        </div>
        <button @click="addClassOption">+</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const className = ref('');
const classCode = ref('');
const offerToOtherCourses = ref(false);
const credits = ref(0);
const prerequisites = ref([]);
const classOptions = ref([]);

const addPrerequisite = () => {
  prerequisites.value.push('A LOT OF TEXT ABASDABADSSAF');
};

const removePrerequisite = (index) => {
  prerequisites.value.splice(index, 1);
};

const addClassOption = () => {
  classOptions.value.push('test');
};

const removeClassOption = (index) => {
  classOptions.value.splice(index, 1);
};
</script>

<style scoped>
.add-class-menu {
  display: flex;
  flex-direction: column;
  border-radius: 10px;
  padding: 30px;
  height: fit-content;
  width: fit-content;
  background-color: #b1b5b5;
  background-size: repeat;
  background-position: center;
}

.menu-title {
  font-size: 42px;
  font-weight: bold;
  width: fit-content;
  margin-bottom: 10px;
  border-radius: 10px;
  padding: 10px;
  background-color: #8e8e8e;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.15);
}

.form-container {
  max-width: 400px !important; /* Set your desired maximum width */
}

.form-field {
  display: flex;
  flex-direction: row;
  border-radius: 4px;
  margin-bottom: 15px;
  width: fit-content;
}

.form-field label {
  width: max-content;
  margin-bottom: 5px;
}

.checkbox-field {
  display: flex;
  align-items: center;
  border-radius: 20px;
}

.checkbox-field input {
  margin-left: 5px;
  border-radius: 20px;
}

.prerequisite-item,
.class-option-item {

}

.prerequisite-item button,
.class-option-item button {

}


.form-field button {
  width: fit-content;
  height: fit-content;
  min-height: 25px;
  margin: 15px 15px 15px 15px;
  position: relative;
  -webkit-border-radius: 200px;
  -moz-border-radius: 200px;
  -ms-border-radius: 200px;
  -o-border-radius: 200px;
  border-radius: 200px;
  margin-left: auto;
}

</style>