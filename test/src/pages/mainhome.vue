<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useRoute } from 'vue-router'       //用来获取路由信息
import axios from 'axios'
import { computed } from 'vue'
import { watch } from 'vue'


const router = useRouter()
let showText = ref(false)
let showModal = ref(false)

let mansaying = computed(() => {
  return '向目标'+"["+form.value.name+"]"+'已努力了' + (form.value.totaldays - form.value.restdays) + '天，还剩' + form.value.restdays + '天，加油！'
})

let nickname_input = ref('昵称')
let signiture_input = ref('个性签名')
let Uname1_input = ref('学校名称')
let term1_input = ref('学期')
let mygoal_1 = ref('我的目标1')
let mygoal_2 = ref('我的目标2')
let mygoal_3 = ref('我的目标3')
let text1 = ref('复习语文')
let text2 = ref('复习英语')
let text3 = ref('')
// let headsrc = ref('../assets/defaulthead.png')

// let animationState = ref('')

const form = ref({
  name: '复习完数学',
  restdays: 29,
  totaldays: 30
})

const fetchData = async () => {
  try {
    const response = await axios.get('http://192.168.186.212:5000/getdata');
    // console.log(response);
    console.log(response.data[0].mansaying);
    // console.log(response.data.mansaying);  
    mansaying.value = response.data[0].mansaying;
    console.log(mansaying.value);

    // form.value.name = response.data[0].goalname;
    // form.value.restdays = response.data[0].restdays;
    // form.value.totaldays = response.data[0].totaldays;
    // console.log(form.value.name);
    // console.log(form.value.restdays);
    // console.log(form.value.totaldays);

    // nickname_input.value = response.data[0].nickname_input;
    // signiture_input.value = response.data[0].signiture_input;
    // Uname1_input.value = response.data[0].Uname1_input;
    // term1_input.value = response.data[0].term1_input;
    text1.value = response.text1;
    text2.value = response.text2;
    text3.value = response.text3;
    // headsrc.value = response.headsrc;

  } catch (error) {
    console.error(error);
  }
}

const submitForm = () => {
  console.log('提交表单');
  console.log(form);
  async()=>{
    try {
        // 发送 POST 请求到后端
        const response = await axios.post('http://192.168.186.212:5000/senddata', {
            'goalname': form.value.name,
            'restdays': form.value.restdays,
            'totaldays': form.value.totaldays,
            'text1': text1.value,
            'text2': text2.value,
            'text3': text3.value
        });
        console.log(response);  // 打印后端的响应
        
        } catch (error) {
        console.error(error);
        }
    }
  showModal.value = false;
}

onMounted(fetchData);  // 在组件挂载后获取数据
onMounted(submitForm);  // 在组件挂载后submit   

const closeModal = () => {
  showModal.value = false;
  form.value.name = '复习完数学';
  form.value.totaldays = 30;
  form.value.restdays = 29;
};

const computerestdays = () => {
  form.value.restdays = form.value.totaldays;
  console.log(form.value.restdays);
}
// const progress = computed(() => {
//   if (form.value.totaldays > 0) {
//     return (form.value.totaldays - form.value.restdays) / form.value.totaldays;
//   } else {
//     return 0;
//   }
// });

// watch(progress, (newVal) => {
//   if (newVal <= 0.5) {
//     animationState.value = 'pause-animation'
//   } else {
//     animationState.value = ''
//   }
// })

setTimeout(() => {
  showText.value = true
}, 2000)

let showNicknameModal = ref(false)
let showSignitureModal = ref(false)
let showUname1Modal = ref(false)
let showTerm1Modal = ref(false)

const handleNicknameClick = () => {
  showNicknameModal.value = true
}

const handleSignitureClick = () => {
  showSignitureModal.value = true
}

const handleUname1Click = () => {
  showUname1Modal.value = true
}

const handleTerm1Click = () => {
  showTerm1Modal.value = true
}

const closeNicknameModal = () => {
  showNicknameModal.value = false
}

const closeSignitureModal = () => {
  showSignitureModal.value = false
}

const closeUname1Modal = () => {
  showUname1Modal.value = false
}

const closeTerm1Modal = () => {
  showTerm1Modal.value = false
}

</script>
<template>
    <img src="../assets/boyhead.png" class="head1">
    <!-- <div class="mwrkt1" :class="animationState" :style="{ '--progress': progress }"> -->
    <div class="mwrkt1">
        <img src="../assets/manwithrocket.png">
        <div v-if="showText" class="say1">{{mansaying}}</div>
    </div>
    <button class="nickname-box" @click="handleNicknameClick">{{nickname_input}}</button>
<div v-if="showNicknameModal" class="modal">
  <h2>修改昵称</h2>
  <form @submit.prevent="closeNicknameModal">
    <input v-model="nickname_input" type="text">
    <button type="submit">提交</button>
  </form>
</div>

<button class="signiture" @click="handleSignitureClick">{{signiture_input}}</button>
<div v-if="showSignitureModal" class="modal">
  <h2>修改个性签名</h2>
  <form @submit.prevent="closeSignitureModal">
    <input v-model="signiture_input" type="text">
    <button type="submit">提交</button>
  </form>
</div>

<button class="Uname1" @click="handleUname1Click">{{Uname1_input}}</button>
<div v-if="showUname1Modal" class="modal">
  <h2>修改学校名称</h2>
  <form @submit.prevent="closeUname1Modal">
    <input v-model="Uname1_input" type="text">
    <button type="submit">提交</button>
  </form>
</div>

<button class="term1" @click="handleTerm1Click">{{term1_input}}</button>
<div v-if="showTerm1Modal" class="modal">
  <h2>修改学期</h2>
  <form @submit.prevent="closeTerm1Modal">
    <input v-model="term1_input" type="text">
    <button type="submit">提交</button>
  </form>
</div>
    <img src="../assets/road.png" class="road1">
    <img src="../assets/goalU.png" class="goalU1">
    <img src="../assets/框.png" class="col1">
    <img src="../assets/Bigboard.png" class="vol-Bigboard">
    <img src="../assets/iboard.png" class="vol-iboard">
    <div class="paper1">
        <img src="../assets/paperon.png">
        <input v-model="text1" class="paper-content" :placeholder="mygoal_1" @blur="saveToBackend('text1', text1)" type="text">
    </div>
    <div class="paper2">
        <img src="../assets/paperon.png">
        <input v-model="text2" class="paper-content" :placeholder="mygoal_2" @blur="saveToBackend('text2', text2)" type="text">
    </div>
    <div class="paper3">
        <img src="../assets/paperon.png">
        <input v-model="text3" class="paper-content" :placeholder="mygoal_3" @blur="saveToBackend('text3', text3)" type="text">
    </div>
    <button class="button1" @click="router.push('/mainhome')"></button>
    <div class="button1-text">首页</div>
    <button class="button2" @click="router.push('/aitalk')"></button>
    <div class="button2-text">AI解答</div>
    <button class="button3" @click="router.push('/cardforu')"></button>
    <div class="button3-text">进步预测</div>
    <button class="button4" @click="router.push('/studyanalyse')"></button>
    <div class="button4-text">学运分析</div>

    <div>
    <!-- 点击按钮显示弹窗 -->
    <button class='setgoal' @click="showModal = true">目标设置</button>

    <!-- 弹窗 -->
    <div v-if="showModal" class="modal">
      <h2>目标设定</h2>

      <!-- 表单 -->
      <form @submit.prevent="submitForm">
        <label for="name">你的目标是：</label>
        <input id="name" v-model="form.name" type="text">
        <br>
        <label for="totaldays">达成目标剩余天数：</label>
        <input id="totaldays" v-model="form.totaldays" type="number">
        <br>
        <br>
        <button @click="computerestdays" type="submit">提交</button>
      </form>

      <button @click="closeModal">关闭弹窗</button>
    </div>
  </div>
</template>

<style scoped>
@keyframes movestraight {
    0% { top: 260px; }
    50% { top: 220px; }
    100% { top: 260px; }
}
/* @keyframes tothegoal{
    0% { left: 27px; }
    100% { left: 320px; top:160px}

} */
/* .pause-animation {
  animation-play-state: paused;
} */
.setgoal{
    position: absolute;
    top:50px;
}
.modal {
  position: fixed;  /* 让弹窗固定在屏幕上，不随页面滚动而移动 */
  top: 50%;  /* 让弹窗在垂直方向上居中 */
  left: 50%; 
  transform: translate(-50%, -50%);  /* 使用 transform 属性来精确地居中弹窗 */
  width: 50%;  /* 设置弹窗的宽度 */
  max-width: 400px;  /* 设置弹窗的最大宽度 */
  padding: 20px;  /* 设置弹窗的内边距 */
  background-color: white;  /* 设置弹窗的背景颜色 */
  border-radius: 10px;  /* 设置弹窗的边框圆角 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);  /* 设置弹窗的阴影 */
  z-index: 1000;  /* 设置弹窗的堆叠顺序，使其位于其他元素之上 */
  backdrop-filter: blur(5px);
}
.nickname-box {
    position: absolute;
left: 125px;
top: 89px;
width: 52px;
height: 20px;
border-radius: 5px;
opacity: 1;
	
border: none;
background-color: transparent;	

font-family: Source Han Sans;
font-size: 16px;
cursor: pointer;
}
.signiture{
    position: absolute;
left: 125px;
top: 120px;
width: 62px;
height: 17px;
opacity: 1;
border: none;
	
font-family: Source Han Sans;
font-size: 12px;
font-weight: normal;
line-height: normal;
letter-spacing: 0em;
background-color: transparent;	
	
font-variation-settings: "opsz" auto;
font-feature-settings: "kern" on;
color: #A3A3A3;
}
.Uname1{
    position: absolute;
left: 280px;
top: 89px;
width: 168px;
height: 20px;
opacity: 1;
border: none;

font-family: Source Han Sans;
font-size: 12px;
font-weight: normal;
line-height: normal;
letter-spacing: 0em;
text-decoration: underline;
background-color: transparent;	

font-variation-settings: "opsz" auto;
font-feature-settings: "kern" on;
color: #A3A3A3;
	
}
.term1{
    position: absolute;
left: 333px;
top: 115px;
width: 60px;
height: 14px;
opacity: 1;
z-index: 5;	
border: none;

font-family: Source Han Sans;
font-size: 12px;
font-weight: normal;
line-height: normal;
letter-spacing: 0em;
text-decoration: underline;
background-color: transparent;	

font-variation-settings: "opsz" auto;
font-feature-settings: "kern" on;
color: #A3A3A3;
	
}
.head1 {
    position: absolute;
left: 35px;
top: 80px;
width: 70px;
height: 70px;
opacity: 1;

}
.mwrkt1 {
    position: absolute;
    left: 27px;
    top: 244px;
    width: 94px;
    height: 106px;
    opacity: 1;
    z-index: 3;
    animation: tothegoal 2s forwards, movestraight 2s infinite 2s;
}

.mwrkt1 img{
    width: 100%;
    height: 100%;
}
.say1{
    position: absolute;
    left: -20px;
    top: -20px;
    width: 100%;
    height: 24px;
    opacity: 1;
	
font-family: Source Han Sans;
font-size: 12px;
font-weight: normal;
line-height: normal;
letter-spacing: 0em;
	
font-variation-settings: "opsz" auto;
font-feature-settings: "kern" on;
color: #A3A3A3;
	
}
.road1{
    position: absolute;
    left: -150px;
    top: 205px;
    width: 550px;
    height: 300px;
    transform: rotate(-10deg);
    opacity: 1;
    z-index: 2;
/* background: #FBDF8F; */
	
box-sizing: border-box;
border: 1px solid ;
border-image: linear-gradient(247deg, #FBDF8F 26%, rgba(0, 0, 0, 0) 54%) ;
	
/* box-shadow: 0px 4px 10px 0px rgba(0, 0, 0, 0.3); */
	
}
.goalU1 {
position: absolute;
left: 303px;
top: 122px;
width: 127px;
height: 153px;
opacity: 1;	
z-index: 1;
background: "../assets/goalU.png";
background-color: transparent;
	
}
.col1 {
position: absolute;
left: -11px;
top: 847px;
width: 456px;
height: 85px;
opacity: 1;
z-index: 4;
	
box-sizing: border-box;
border: NaNpx solid #000000;
	
}

.vol-Bigboard {
    position: absolute;
left: 2px;
top: 385px;
width: 428px;
height: 542px;
border-radius: 20px;
opacity: 1;
z-index: 1;
	
background: rgba(248, 204, 98, 0.79);
	
box-sizing: border-box;
/* border: 5px solid #000000; */
	
}
.vol-iboard{
    position: absolute;
left: 16px;
top: 420px;
width: 395px;
height: 476px;
border-radius: 20px;
opacity: 1;
z-index: 1;
	
box-sizing: border-box;
/* border: 4px dashed #000000; */
	
}
.paper1{
    position: absolute;
left: 50px;
top: 512px;
width: 177px;
height: 138px;
	
}
.paper2{
    position: absolute;
left: 214px;
top: 608px;
width: 177px;
height: 138px;

}
.paper3{
    position: absolute;
left: 50px;
top: 736px;
width: 177px;
height: 138px;

}
.paper1, .paper2, .paper3 {

    opacity: 1;
    z-index: 2;
    border:none;
}

.paper-content {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
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
</style>

