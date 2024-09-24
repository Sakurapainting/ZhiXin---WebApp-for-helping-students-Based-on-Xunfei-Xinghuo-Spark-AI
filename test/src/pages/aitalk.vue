<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useRoute } from 'vue-router'       //用来获取路由信息
import axios from 'axios'


const router = useRouter()

let showText = ref(false)

setTimeout(() => {
  showText.value = true
}, 2000)
 
let messages = ref([  
// 示例消息 no  
])

let inputText = ref('')
let userAvatarMe =ref('../assets/defaulthead.png')
let userAvatarOther= ref('../assets/defaulthead.png')

const sendMessage = async () => {  
  if (inputText.value) {  //
    messages.value.push({ text: inputText.value, from: 'me' }); // 发送你的消息 
    
    try {
      // 发送 POST 请求到后端
      const response = await axios.post('http://192.168.11.212:5000/senddata', {
        'askk': inputText.value
      });
      console.log(response);  // 打印后端的响应
      messages.value.push({ text: response.data, from:'other'});
      
    } catch (error) {
      console.error(error);
    }

    inputText.value = ''; // 清空输入框  
  }
}

const fetchData = async () => {
  try {
    const response = await axios.get('http://192.168.11.212:5000/shuaxin');
     
    for (const item of response.data) {
      const answer = item.answer;
      const ask = item.ask
      messages.value.push({ text: ask, from: 'me'});
      messages.value.push({ text: answer, from: 'other' })  ;
    }
    

  } catch (error) {
    console.error(error);
  }
}

onMounted(fetchData);  // 在组件挂载后获取数据
onMounted(sendMessage);  // 在组件挂载后获取数据
</script>
<template>
    
  <div class="chat-container">  
    <div class="chat-window">  
      <div  
        class="message"  
        v-for="(message, index) in messages"  
        :key="index"  
        :class="{ 'sent': message.from === 'me', 'received': message.from !== 'me' }"  
      >  
        <!-- <div class="message-avatar">  
          <img :src="message.from === 'me' ? userAvatarMe : userAvatarOther" alt="Avatar" />  
        </div>   -->
        <div class="message-content">  
          <div class="message-text">{{ message.text }}</div>  
        </div>  
      </div>  
    </div>  
    <div class="input-container">  
      <input type="text" v-model="inputText" placeholder="输入消息...">  
      <button @click="sendMessage">发送</button>  
    </div>  
  </div>  

    <img src="../assets/框.png" class="col1">

    <button class="button1" @click="router.push('/mainhome')"></button>
    <div class="button1-text">首页</div>
    <button class="button2" @click="router.push('/aitalk')"></button>
    <div class="button2-text">AI解答</div>
    <button class="button3" @click="router.push('/cardforu')"></button>
    <div class="button3-text">进步预测</div>
    <button class="button4" @click="router.push('/studyanalyse')"></button>
    <div class="button4-text">学运分析</div>
</template>

<style scoped>
.col1 {
position: absolute;
left: -11px;
top: 847px;
width: 456px;
height: 85px;
opacity: 1;
z-index: 2;
	
box-sizing: border-box;
border: NaNpx solid #000000;
	
}
.button1{
    position: absolute;
left: 51px;
top: 876px;
width: 33px;
height: 30px;
opacity: 1;
z-index: 9;
background-image: url("../assets/but1.png");
background-color: transparent;
border: none;
cursor:pointer;
}
.button2{
    position: absolute;
left: 157px;
top: 874px;
width: 41px;
height: 32px;
opacity: 1;
z-index: 9;
background-image: url("../assets/but2.png");
background-color: transparent;
border:none;
cursor: pointer;
}
.button3{
    position: absolute;
left: 252px;
top: 875px;
width: 41px;
height: 30px;
opacity: 1;
z-index: 9;
background-image: url("../assets/but3.png");
background-color: transparent;
border:none;
cursor: pointer;
}
.button4{
    position: absolute;
left: 347px;
top: 871px;
width: 41px;
height: 32px;
opacity: 1;
z-index: 9;
background-image: url("../assets/but4.png");
background-color: transparent;
border:none;
cursor: pointer;
}
.button1-text{
    position: absolute;
left: 55px;
top: 908px;
width: 27px;
height: 10px;
opacity: 1;
z-index: 9;
	
font-family: Source Han Sans;
font-size: 12px;
font-weight: normal;
line-height: normal;
letter-spacing: 0em;
	
font-variation-settings: "opsz" auto;
font-feature-settings: "kern" on;
color: #3D3D3D;
	
}
.button2-text{
    position: absolute;
left: 160px;
top: 908px;
width: 37px;
height: 10px;
opacity: 1;
z-index: 9;
	
font-family: Source Han Sans;
font-size: 12px;
font-weight: normal;
line-height: normal;
letter-spacing: 0em;
	
font-variation-settings: "opsz" auto;
font-feature-settings: "kern" on;
color: #3D3D3D;
	
}
.button3-text{
    position: absolute;
left: 249px;
top: 908px;
width: 48px;
height: 10px;
opacity: 1;
z-index: 9;
	
font-family: Source Han Sans;
font-size: 12px;
font-weight: normal;
line-height: normal;
letter-spacing: 0em;
	
font-variation-settings: "opsz" auto;
font-feature-settings: "kern" on;
color: #3D3D3D;
	
}
.button4-text{
    position: absolute;
left: 344px;
top: 908px;
width: 48px;
height: 10px;
opacity: 1;
z-index: 9;
	
font-family: Source Han Sans;
font-size: 12px;
font-weight: normal;
line-height: normal;
letter-spacing: 0em;
	
font-variation-settings: "opsz" auto;
font-feature-settings: "kern" on;
color: #3D3D3D;
	
}

.chat-container {  
    position: absolute;
left: -12px;
top: 67px;
width: 460px;
height: 859px;
opacity: 1;
	
background: #FFFFFF;
	
box-sizing: border-box;
border: none;
	
  padding: 10px;  
  overflow-y: auto; /* 启用垂直滚动 */  
}  
  
.chat-window {  
  height: 700px;  
  border-bottom: 1px solid #ccc;  
  padding-bottom: 10px;  
  overflow-y: auto; /* 启用垂直滚动 */  
}  
  
.message {  
  display: flex;  
  margin-bottom: 10px;  
  align-items: flex-start;  
}  
  
.sent {  
    flex-direction: row-reverse;
    justify-content: flex-end; 
}  
  
.received {  
    flex-direction: row;
  justify-content: flex-start;  
}  
  
.message-avatar {  
  width: 40px;  
  height: 40px;  
  border-radius: 50%;  
  overflow: hidden;  
  margin-right: 10px;  
}  
  
.message-avatar img {  
  width: 100%;  
  height: 100%;  
  object-fit: cover;  
}  
  
.message-content {  
  background-color: #f0f0f0;  
  border-radius: 10px;  
  padding: 10px;  
  max-width: 200px;  
  position: relative;  
  word-wrap: break-word;
}  
  
.sent .message-content {  
  background-color: #5285f2;  
  color: #fff;  
  margin-left: auto;  
  margin-right: 10px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
}  

.sent .message-avatar {
    margin-left: 10px;
}
  
.received .message-content {  
  background-color: #ffffff;  
  color: #000;  
  margin-right: 10px;  
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
  
}  
  
.input-container {  
    position: absolute;
left: 32px;
top: 720px;
width: 386px;
height: 46px;
opacity: 1;
	
  margin-top: 10px;  
}  
  
input[type="text"] {  
  width: 300px;
  height:20px;  
  padding: 5px;  
  border-radius: 15px;
}  
  
button {  
  padding: 5px 10px;  
  margin-left: 5px;  
} 

</style>