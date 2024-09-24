<script setup>
import { ref } from 'vue'
// import {toRaw} from 'vue'       //用来获取原始数据
import { useRouter } from 'vue-router'
import { useRoute } from 'vue-router'       //用来获取路由信息
import axios from 'axios'

// console.log(toRaw(useRoute()))      

// let username = ref('')
// let password = ref('')
const router = useRouter()

// const submitForm = async () => {//异步函数
//   const response = await axios.post('', {//发送post请求，把响应结果赋值给response
//     username: username.value,//获取输入框的值
//     password: password.value
//   })
//   console.log(response.data)//打印返回的数据
//   router.push('/mainhome')//跳转到mainhome页面
// }
</script>

<template>
    <img src="../assets/直线1.png" class="image-position1">
    <img src="../assets/直线2.png" class="image-position2">
    <img src="../assets/星形1.png" class="image-position3">
    <img src="../assets/book2.png" class="image-position4">
    <img src="../assets/book1.png" class="image-position5">
    <div>
     <form @submit.prevent="submitForm">
      <!-- <label for="username" class="username-pos1">用户名:</label>
      <input type="text" id="username" class="username-pos2" v-model="username" required> -->
      <input type="text" class="flat-input1" placeholder="请输入账号">

      <!-- <label for="password" class="password-pos1">密码:</label>
      <input type="password" id="password" class="password-pos2" v-model="password" required> -->
      <input type="password" class="flat-input2" placeholder="请输入密码">
      <!-- <button type="submit" class="login-pos" >登录</button> -->
      <!-- <button class="login-button" @click="submitForm">登录</button> -->
      <button class="login-button" @click="router.push('/mainhome')">登录</button>
    </form>
    </div>
    
    <button class="small-button1">注册</button>
    <button class="small-button2">忘记密码</button>

</template>

<style scoped>
.image-position1 {
position: absolute;
left: 63px;
top: 134px;
width: 238.01px;
height: 0px;
transform: rotate(0deg);
opacity: 1;
	
border-top: 1px solid #000000;
	
}

.image-position2 {
position: absolute;
left: 45px;
top: 210px;
width: 152px;
height: 0px;
transform: rotate(90deg);
opacity: 1;
	
border-top: 1px solid #000000;
	
box-shadow: 0px 4px 10px 0px rgba(0, 0, 0, 0.3),0px 4px 10px 0px rgba(0, 0, 0, 0.3),0px 4px 10px 0px rgba(0, 0, 0, 0.3),0px 4px 10px 0px rgba(0, 0, 0, 0.3);
	
}

.image-position3 {
position: absolute;
left: 99px;
top: 269px;
width: 44px;
height: 44px;
border-radius: 2px;
opacity: 1;
	
background: "../assets/星形1.png"
	
/* box-shadow: 0px 4px 10px 0px rgba(0, 0, 0, 0.3); */
	      
}

.image-position4{
position: absolute;
left: 234px;
top: 313px;
width: 133px;
height: 133px;
opacity: 1;
	
background: "../assets/book2.png";
	
/* box-shadow: 0px 4px 10px 0px rgba(0, 0, 0, 0.3),0px 4px 10px 0px rgba(0, 0, 0, 0.3),0px 4px 10px 0px rgba(0, 0, 0, 0.3),0px 4px 10px 0px rgba(0, 0, 0, 0.3); */
	
}

.image-position5{
position: absolute;
left: 180px;
top: 327.65px;
width: 132.02px;
height: 138.83px;
/* transform: rotate(-12deg); */
opacity: 1;

background: "../assets/book1.png";

/* box-shadow: 0px 4px 10px 0px rgba(0, 0, 0, 0.3),0px 4px 10px 0px rgba(0, 0, 0, 0.3),0px 4px 10px 0px rgba(0, 0, 0, 0.3),0px 4px 10px 0px rgba(0, 0, 0, 0.3),0px 4px 10px 0px rgba(0, 0, 0, 0.3); */
}

/* .username-pos1{
position: absolute;
left: 50px;
top: 7px;
width: 206px;
height: 42px;
opacity: 1;
	
font-family: Source Han Sans;
font-size: 36px;
font-weight: normal;
line-height: normal;
letter-spacing: 0em;
	
font-variation-settings: "opsz" auto;
font-feature-settings: "kern" on;
color: rgba(127, 91, 91, 0.63);
	
}
.username-pos2{
position: absolute;

} */

.flat-input1 {
position: absolute;
left: 70px;
top: 540px;
width: 235px;
height: 35px;
  padding: 10px 20px;
  border: none;
  border-radius: 20px;
  box-shadow: 0px 4px 10px 0px rgba(0, 0, 0, 0.1);
  font-family: 'Source Han Sans', sans-serif;
  font-size: 17px;
  color: rgba(127, 91, 91, 0.63);
  background-color: #f0f0f0;
}

.flat-input2 {
position: absolute;
left: 72px;
top: 609px;
width: 235px;
height: 35px;
  padding: 10px 20px;
  border: none;
  border-radius: 20px;
  box-shadow: 0px 4px 10px 0px rgba(0, 0, 0, 0.1);
  font-family: 'Source Han Sans', sans-serif;
  font-size: 17px;
  color: rgba(127, 91, 91, 0.63);
  background-color: #f0f0f0;
}

.login-button {
position: absolute;
left: 72px;
top: 709px;
width: 270px;
height: 40px;
background-color:rgba(127, 91, 91, 0.63);
  border: none; /* Remove border */
  color: white; /* White text */
  /* padding: 15px 32px; Some padding */
  text-align: center; /* Centered text */
  text-decoration: none; /* Remove underline */
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer; /* Mouse pointer on hover */
  border-radius: 12px; /* Rounded corners */
  transition-duration: 0.4s; /* Transition */
}

.login-button:hover {
  background-color: #45a049; /* Green background on hover */
  color: white; /* White text color on hover */
}

.small-button1 {
position: absolute;
left: 215px;
top: 680px;
width: 50px;
height: 17px;
opacity: 1;
	
background: #A3A3A3;
	
border: none; 
	
  background-color: transparent; /* No background */

  color:rgba(127, 91, 91, 0.63);
  padding: 5px 10px; /* Some padding */
  text-align: center; /* Centered text */
  text-decoration: underline; /* Underline text */
  display: inline-block; 
  font-size: 12px; /* Smaller font size */
  margin: 4px 2px;
  cursor: pointer; /* Mouse pointer on hover */ 
  transition-duration: 0.4s; /* Transition */ 
}

.small-button1:hover {
  color: #45a049; /* Darker green text on hover */
}   

.small-button2 {
    position: absolute;
left: 264px;
top: 680px;
width: 70px;
height: 17px;
opacity: 1;
	
background: #A3A3A3;
	
border: none;
	
  background-color: transparent; /* No background */

  color: rgba(127, 91, 91, 0.63);
  padding: 5px 10px; /* Some padding */
  text-align: center; /* Centered text */
  text-decoration: underline; /* Underline text */
  display: inline-block;
  font-size: 12px; /* Smaller font size */
  margin: 4px 2px;
  cursor: pointer; /* Mouse pointer on hover */
  transition-duration: 0.4s; /* Transition */
}

.small-button2:hover {
  color: #45a049; /* Darker green text on hover */
}   
</style>