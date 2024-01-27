<script>
import LoginForm from "../components/LoginForm.vue";
export default {
    components: {
        LoginForm
    }
};
</script>

<template>
    <div class="login-screen">
        <LoginForm/>
    </div>
</template>

<style scoped>
.login-screen {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-color: #0e0720;
  background-size: repeat;
  background-position: center;
}
</style>
