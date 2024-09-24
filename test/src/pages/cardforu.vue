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

let isFlipped = ref(false)
let imageurl = ref("../assets/cardback.png")

const flipCard = () => {
  isFlipped.value = !isFlipped.value

  // if (isFlipped.value) {
  //   axios.get('http://192.168.186.212:5000/getdata')
  //     .then(response => {
  //       imageurl.value = response.data[0].cardget
  //       console.log(response)
  //     })
  //     .catch(error => {
  //       console.error(error)
  //     })
  // }

}
</script>

<template>
  <div class="homebox">
    <div class="card" @click="flipCard">
      <div class="card-inner" :class="{ 'is-flipped': isFlipped }">
        <div class="card-front">
          <img src="../assets/cardback.png">
        </div>
        <div class="card-back">
          <img src="../assets/cardcont.png">
        </div>
      </div>
    </div>
      <!-- <button @click="button1Click" class='but1'>自定义</button>
      <button @click="button2Click" class='but2'>随机抽</button> -->

      <!-- <img src="../assets/cardback.png" class="cardback1">
      <img src="../assets/cardback.png" class="cardback2">
      <img src="../assets/cardback.png" class="cardback3"> -->

      <img src="../assets/schoolman.png" class="schoolman">
      <div class="speech-bubble" v-if="showText">抽一张牌来看看今天可能收获什么吧（点击卡牌）</div>
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
.homebox{
  position: fixed;
		width: 100%;
		height: 100%;
		top: 0px;
		background-image:url("../assets/bgpng3.png");
    background-size:cover;
    background-repeat: no-repeat;

}
.card {
  perspective: 1000px;
  position: absolute;
left: 60px;
top: 167px;
width: 287px;
height: 488px;
opacity: 1;
}

.card-inner {
  text-align: center;
  transition: transform 0.8s;
  transform-style: preserve-3d;
}

.card-inner.is-flipped {
  transform: rotateY(180deg);
}

.card-front {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
}

.card-back{
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  transform: scale(0.5);
}
.card-front {
  background-color: #bbb;
  color: black;
}

.card-back {
  background-color: #2980b9;
  color: white;
  transform: rotateY(180deg);
}
/* .cardback1{
    position: absolute;
left: 76px;
top: 153px;
width: 287px;
height: 488px;
opacity: 1;
	
box-sizing: border-box;
border: 1px solid #FFFFFF;
	
}
.cardback2{
    position: absolute;
left: 68px;
top: 160px;
width: 287px;
height: 488px;
opacity: 1;
	
box-sizing: border-box;
border: 1px solid #FFFFFF;
	
}
.cardback3{
    position: absolute;
left: 60px;
top: 167px;
width: 287px;
height: 488px;
opacity: 1;
	
box-sizing: border-box;
border: 1px solid #FFFFFF;
	
} */
.schoolman {
    position: absolute;
left: 215px;
top: 579px;
width: 237px;
height: 292px;
opacity: 1;

background-color:transparent;
}
.speech-bubble {
  position: absolute;
  left: 70px;
  top: 700px;
  width: 240px;  
  height: 20px; 
  text-decoration:underline;
  z-index: 10;
  font-size: 15px;
}
/* .but1{
    position: absolute;
left: 70px;
top: 752px;
width: 86px;
height: 38px;
border-radius: 10px;
opacity: 1;
	
box-sizing: border-box;
border: 1px solid ;
border-image: linear-gradient(180deg, rgba(0, 0, 0, 0) 0%, #000000 100%) 1;
	
cursor:pointer;
}
.but2{
    position: absolute;
left: 177px;
top: 752px;
width: 86px;
height: 38px;
border-radius: 10px;
opacity: 1;
	
box-sizing: border-box;
border: 1px solid ;
border-image: linear-gradient(180deg, rgba(0, 0, 0, 0) 0%, #000000 100%) 1;
	
cursor:pointer;
} */
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
</style>

