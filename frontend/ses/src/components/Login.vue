  <template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <div class="form-group">
        <label for="university">University:</label>
        <Dropdown v-model="selectedUniversity" :options="universityOptions" filter optionLabel="value" placeholder="Select a University" @onChange="selectUniversity"> </Dropdown>
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import Dropdown from 'primevue/dropdown';

interface UniversityOption {
  label: string;
  value: string;
}

const username = ref('');
const password = ref('');
const selectedUniversity = ref<UniversityOption | null>(null);
const universityOptions = ref<UniversityOption[]>([
  { label: 'UFRGS', value: 'UFRGS' },
  { label: 'PUCRS', value: 'PUCRS' },
  { label: 'UFCSPA', value: 'UFCSPA' },
]);

const login = () => {
  const validUsername = 'SES';
  const validPassword = 'ses123';
  const validUniversity = 'UFRGS';
  if (username.value === validUsername && password.value === validPassword && selectedUniversity.value?.value === validUniversity) {
    alert('OK');
  } else {
    alert('Username or Password not recognized for university: ' + selectedUniversity.value?.value);
  }
};

const selectUniversity = (option: UniversityOption) => {
  selectedUniversity.value = option;
};
</script>

<style scoped>
.login-container {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
    margin-bottom: 10px;
  }
  
  button {
    background-color: #4caf50;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 3px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #45a049;
  }

.dropdown {
  position: relative;

}

.dropdown-toggle {
  cursor: pointer;
  display: flex;
  align-items: center;
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
  margin-bottom: 10px;
}

.arrow {
  border: solid #000;
  border-width: 0 2px 2px 0;
  display: inline-block;
  padding: 3px;
  transform: rotate(45deg);
  transition: transform 0.3s; 
}

.arrow.open {
  transform: rotate(225deg);
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  display: none;
  background-color: #fff;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
  margin-bottom: 10px;      
}

.dropdown.open .dropdown-menu {
  display: block;
}
</style>
