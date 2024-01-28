<template>
    <div class="header">
        <div class="header-item">ADMIN TOOLS</div>
        <div class="header-item right">{{ collegeCourseName }}</div>
        <div class="header-item">
            <button class="exit-button" @click="exitAdminTools">
                <i class="pi pi-sign-out"></i> EXIT
            </button>
        </div>
    </div>
    <div class="admin-page">
        <div class="side-menu">
            <div class="menu-item" :class="{ 'selected': isSearchEditClassSelected }"
                @click="toggleButton('search-edit-class')" data-button="search-edit-class">
                <i class="pi pi-search"></i>
                SEARCH/EDIT CLASS
            </div>
            <div class="menu-item" :class="{ 'selected': isAddClassSelected }" @click="toggleButton('add-class')"
                data-button="add-class">
                <i class="pi pi-plus-circle"></i>
                ADD CLASS
            </div>
            <div class="menu-item" :class="{ 'selected': isSetEnrollmentDatesSelected }"
                @click="toggleButton('set-enrollment-dates')" data-button="set-enrollment-dates">
                <i class="pi pi-calendar"></i>
                SET ENROLLMENT DATES
            </div>
            <div class="menu-item disabled" :class="{ 'selected': isSetupUniversitySelected }"
                data-button="setup-university">
                <i class="pi pi-cog"></i>
                SETUP UNIVERSITY AND COURSE
            </div>
        </div>
        <div class="main-content">
        </div>
    </div>
</template>
  
<script setup lang="ts">
import { ref, watch } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const collegeCourseName = ref("UFRGS - Ciência da Computação"); 

const buttonActions = {
    'search-edit-class': () => {

    },
    'add-class': () => {
    
    },
    'set-enrollment-dates': () => {

    },
    'setup-university': () => {

    },
};

const selectedButton = ref('');

const toggleButton = (button: string) => {
    selectedButton.value = button;

    if (buttonActions[selectedButton.value]) {
        buttonActions[selectedButton.value]();
    }
};

watch(selectedButton, (newValue) => {
    resetSelectedClasses();
    const el = document.querySelector(`.menu-item[data-button="${newValue}"]`);
    if (el) {
        el.classList.add('selected');
    }
});

const resetSelectedClasses = () => {
    const menuItems = document.querySelectorAll('.menu-item');
    menuItems.forEach((item) => {
        item.classList.remove('selected');
    });
};
</script>
  
<style scoped>
.admin-page {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 95vh;
    width: 100vw;
    padding: 50px;
    background-color: #0e0720;
    background-size: repeat;
    background-position: center;
}

.side-menu {
    width: 300px;
    background-color: #000000;
    color: #fff;
    padding: 20px;
    display: flex;
    flex-direction: column;
    border-radius: 10px;
}

.menu-item {
    cursor: pointer;
    padding: 20px;
    background-color: #3a0754;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.15);
    border-radius: 10px;
    transition: background-color 0.3s ease;
}

.menu-item:hover {
    background-color: #4a156b;
}

.menu-item i {
    margin-right: 10px;
}

.menu-item.selected {
    background-color: #e371ff;
}

.menu-item.disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

.main-content {
    flex: 1;
    padding: 20px;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    background-color: #2f0b4d;
    color: #fff;
    height: 5vw;
    width: 100vw;
}

.header-item {
    font-size: 42px;
    font-family: 'Roboto', sans-serif;
}

.header-item.right {
    text-align: right;
}

.exit-button {
  background: none;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  color: #fff;
  font-size: 36px;
  font-family: 'Roboto', sans-serif;
  padding: 10px;
  transition: background-color 0.3s ease;
}

.exit-button:hover {
  background-color: #4a156b; 
}

.exit-button i {
  font-size: 36px; 
}
</style>
  