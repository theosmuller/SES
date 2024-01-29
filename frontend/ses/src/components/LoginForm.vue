<template>
  <div class="login-card">
    <h1 class="login-title">SES Login</h1>
    <form class="form" @submit.prevent="login">
      <label for="university" class="form-label">University</label>
      <select id="university" class="form-input">
        <option v-for="university in universities" :key="university.id" :value="university.id">
          {{ university.name }}
        </option>
      </select>
      <label for="username" class="form-label">Username</label>
      <input type="text" id="username" class="form-input" placeholder="Enter your username" v-model="username" required/>

      <label for="password" class="form-label">Password</label>
      <input type="password" id="password" class="form-input" placeholder="Enter your password" v-model="password" required/>
      <button class="login-button">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import Cookies from 'js-cookie'
export default {
  data() {
      return {
          username: '',
          password: '',
          universities: [],
      };
  },
  methods: {
      login() {
          if(this.username == 'admin' && this.password == 'admin') {
              Cookies.set('auth', 'admin')
              this.$router.push('/home');
          } else {
              if(this.username == 'admin2' && this.password == 'admin') {
                Cookies.set('auth', 'admin')
                this.$router.push('/admin');
              } else {
                alert('Invalid credentials!');
              }
          }
      },
  },
  created() {
      axios.get('http://localhost:8000/university/')
          .then(response => {
              this.universities = response.data;
          });
  },
};
</script>

<style scoped>
.login-form {
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
height: 100vh;
background-color: #f2f2f2;
}

.login-card {
background-color: #ffffff;
border-radius: 10px;
padding: 20px;
box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.15);
border-color:#333333;
border-width: 5px;
}

.login-title {
font-size: 24px;
margin-bottom: 20px;
color: #333333;
}

.form {
display: flex;
flex-direction: column;
align-items: center;
}

.form-label {
font-size: 16px;
margin-bottom: 10px;
color: #666666;
}

.form-input {
width: 300px;
height: 40px;
padding: 8px;
border: 1px solid #cccccc;
border-radius: 4px;
margin-bottom: 20px;
}

.login-button {
width: 120px;
height: 40px;
background-color: #ffba26;
color: #ffffff;
border: none;
border-radius: 4px;
font-size: 16px;
cursor: pointer;
}

.login-button:hover {
background-color: #ffae00;
}
select {
width: 300px;
height: 40px;
padding: 8px;
border: 1px solid #cccccc;
border-radius: 4px;
margin-bottom: 20px;
background-color: #ffffff; /* Brighter background color */
color: #333333; /* Darker text color */
font-size: 16px;
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
</style>
