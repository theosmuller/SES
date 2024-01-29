<template>
  <div class="class-item">
    <div class="class-item-header">
      <div class="class-item-header-title">
        <h2>{{ className }}</h2>
        <p class="code">{{ classCode }}</p>
      </div>
      <div class="right-top-group">
        <p class="credits">Credits: {{ credits }}</p>
        <p class="select-section">
          <span class="section-text">Section</span>
          <p class="enrolled-section" v-if="enrolled">{{ selectedSection.section }}</p>
          <select v-model="selectedSection" v-show="!enrolled">
            <option v-for="section in sections" :key="section.id" :value="section" :disabled="enrolled">{{ section.section }}</option>
          </select>
        </p>
    </div>
    </div>
    <div class="class-item-body">
      <p v-if="selectedSection"><span class="info-title">Professor:</span> <span>{{ professor }}</span></p>
      <p><span class="info-title">Time Schedule:</span>
        <div class="class-times">
        <span v-for="time in timeSchedule">
          <ClassTime
          :classDay="time.day"
          :startTime="time.start_time"
          :endTime="time.end_time"
          />
        </span>  
      </div>
      </p>
      <p><span class="info-title">Description:</span> {{ description }}</p>
      <button class="enroll-button" @click="enroll" v-if="!enrolled">Enroll</button>
      <button class="unenroll-button" @click="unenroll" v-else>Unenroll</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ClassTime from './ClassTime.vue';
export default {
  components: {
    ClassTime
  },
  props: {
    classId: {
      type: Number,
      required: true,
    }
  },
  data() {
    return {
      className: '',
      classCode: '',
      professor: '',
      credits: 0,
      sections: [],
      timeSchedule: [],
      selectedSection: null,
      description: '',
      enrolled: false
    }
  },
  methods:{
    enroll() {
      this.enrolled = true;
      this.$emit('enroll', {id:this.classId, section: this.selectedSection});
    },
    unenroll() {
      this.enrolled = false;
      this.$emit('unenroll', {id:this.classId, section: this.selectedSection});
    }
  },
  async created(){
    try{
      const response = await axios.get('http://localhost:8000/class/' + this.classId + '/');
      this.className = response.data.name;
      this.sections = response.data.sections;
      this.credits = response.data.credits;
      this.year = response.data.year;
      this.classCode = response.data.code;
      if(this.sections.length > 0) {
        this.selectedSection = this.sections[0];
      } else {
        console.log('No sections found');
      }
    } catch (error) {
      console.log(`Error connecting to the api: ${error}`);
    }
  },
  watch: {
    async selectedSection(newSection) {
      console.log(newSection);
      try {
        this.professor = this.selectedSection.professor;
        this.timeSchedule = this.selectedSection.time;
      } catch (error) {
        console.log(error);
        this.professor = '';
        this.timeSchedule = '';
      }
    }
  }
}
</script>

<style scoped>

.enrolled-section{
  font-weight: bold;
  color: #333;
  margin-right: 5px;
  margin-left: 0px;
  margin-top: 0;
  text-align: center;
  align-self: center;

}
.class-item-header-title{
  display: flex;
  flex-flow:column;
  justify-content: flex-start;
  align-items: flex-start;
  flex-wrap: nowrap;
}
.class-item-header-title h2{
  flex-basis: 90%;
  margin: 0;
  white-space: nowrap;
}
.class-item-header-title p{
  white-space: normal;
  margin: 0;
  text-align: left;
  align-self: flex-start;
}
.code{
  font-size: 0.8em;
  color: #999;
  text-align: center;
  margin-right: 1em;
}
.class-times {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 1em;
}
.right-top-group{
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: right;

}
.class-item {
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
  background-color: #fcfcfc;
}

.class-item-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.9em;
  color: #333;
}

.credits {
  font-size: 0.8em;
  color: #666;
  text-align: center;
  margin-right: 1em;
}

.select-section{
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 0.8em;
  color: #666;
  text-align: center;
  flex-basis: 10%;
}

.class-item-header-title{
  display: flex;
  justify-content: flex-start;
  align-items: center;
  font-size: 1.2em;
}

.class-item-header > h2 {
  margin: 0;
}

.class-item-header > select {
  padding: 5px;
  font-size: 1em;
}

.class-item-body {
  display: flex;
  flex-direction: column;
  gap: 1.5em;
}

.class-item-body p{
  margin: 0;
  font-size: 0.9em;
  color: #333;
}

.info-title {
  font-weight: bold;
  color: #333;
  margin-right: 5px;
}


select {
padding: 8px;
border: 1px solid #cccccc;
border-radius: 4px;
margin-bottom: 1em;
background-color: #ffffff; /* Brighter background color */
color: #333333; /* Darker text color */
font-size: 1em;
}

/* Style for the dropdown options */
select option {
padding: 10px;
}

/* Style when the select is focused */
select:focus {
outline: none;
border-color: #007BFF; /* Change border color */
}



.enroll-button {
height: 40px;
background-color: #ffba26;
color: #ffffff;
border: none;
border-radius: 4px;
font-size: 16px;
cursor: pointer;
}

.enroll-button:hover {
background-color: #ffae00;
}

.unenroll-button{
height: 40px;
background-color: #8b0000;
color: #ffffff;
border: none;
border-radius: 4px;
font-size: 16px;
cursor: pointer;
}

.unenroll-button:hover {
background-color: #b31c1c;
}


@media(max-width: 992px) {
  select{
    font-size:12px;
  }
  .class-item-header-title{
    flex-direction: column;
  }
  .class-item-header-title h2{
    margin: 0;
  }
  .class-item-header-title p{
    margin: 0;
  }
}




@media (max-width: 768px) {
  .class-item-header h2 {
    flex-basis: 60%;
  }

  .credits {
    flex-basis: 10 0%;
  }

}


</style>