<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useRoute } from 'vue-router'       //用来获取路由信息
import axios from 'axios'
import * as echarts from 'echarts'

const router = useRouter()

let gaugeChart = ref(null)
let barChart = ref(null)

let gaugechart_1_value = ref(10)
let gaugechart_2_value = ref(20)
let gaugechart_3_value = ref(30)
let gaugechart_4_value = ref(40)
let gaugechart_5_value = ref(50)
let gaugechart_6_value = ref(60)
let gaugechart_7_value = ref(65)

let barchart_1_value = ref(80)
let barChart_2_value = ref(70)
let barChart_3_value = ref(60)
let barChart_4_value = ref(70)
let barChart_5_value = ref(85)
let barChart_6_value = ref(88)

let showText = ref(false)

setTimeout(() => {
  showText.value = true
}, 2000)

onMounted(() => {
  const chart1 = echarts.init(gaugeChart.value)
  const chart2 = echarts.init(barChart.value)

  const option1 = {
    series: [
      {
        name: '语文',
                    type: 'gauge',
                    center: ['50%', '55%'],
                    radius: '90%',
                    min: 100,
                    max: 0,
                    itemStyle: {
                        color: '#4FC3F7',
                        shadowColor: 'rgba(0,138,255,0.45)'
                    },
                    // 进度条
                    progress: {
                        show: true,
                        width: 20,
                        roundCap: true
                    },
                    // 坐标轴线
                    axisLine: {
                        show: true,
                        roundCap: true,
                        lineStyle: {
                            width: 20
                        }
                    },
                    // 仪表盘指针
                    pointer: {
                        show: false
                    },
                    // 刻度标签
                    axisLabel: {
                        show: false
                    },
                    // 刻度
                    axisTick: {
                        show: false
                    },
                    // 分隔线
                    splitLine: {
                        show: false
                    },
                    title: {
                        offsetCenter: [0, '20%'],
                        fontSize: 20
                    },
                    startAngle: 90,
                    endAngle: -180,
                    detail: {
                        
                        offsetCenter: ['-28%', '-94%'],
                        valueAnimation: true,
                        textStyle: {
                            fontSize: 10
                        },
                        formatter: '语文:全省前{value}%'
                    },
                    data: [
                        { value: gaugechart_1_value.value }
                    ]
      },
      {
        name: '数学',
                    type: 'gauge',
                    center: ['50%', '55%'],
                    radius: '80%',
                    min: 100,
                    max: 0,
                    itemStyle: {
                        color: 'red',
                        shadowColor: 'rgba(0,138,255,0.45)'
                    },
                    // 进度条
                    progress: {
                        show: true,
                        width: 20,
                        roundCap: true
                    },
                    // 坐标轴线
                    axisLine: {
                        show: true,
                        roundCap: true,
                        lineStyle: {
                            width: 20
                        }
                    },
                    // 仪表盘指针
                    pointer: {
                        show: false
                    },
                    // 刻度标签
                    axisLabel: {
                        show: false
                    },
                    // 刻度
                    axisTick: {
                        show: false
                    },
                    // 分隔线
                    splitLine: {
                        show: false
                    },
                    title: {
                        offsetCenter: [0, '20%'],
                        fontSize: 20
                    },
                    detail: {
                        
                        offsetCenter: ['-31%', '-93%'],
                        valueAnimation: true,
                        textStyle: {
                            fontSize: 10
                        },
                        formatter: '数学:全省前{value}%'
                    },
                    startAngle: 90,
                    endAngle: -180,
                    data: [
                        { value: gaugechart_2_value.value}
                    ]
      },
      {
        name: '英语',
                    type: 'gauge',
                    center: ['50%', '55%'],
                    radius: '70%',
                    min: 100,
                    max: 0,
                    itemStyle: {
                        color: 'blonde',
                        shadowColor: 'rgba(0,138,255,0.45)'
                    },
                    // 进度条
                    progress: {
                        show: true,
                        width: 20,
                        roundCap: true
                    },
                    // 坐标轴线
                    axisLine: {
                        show: true,
                        roundCap: true,
                        lineStyle: {
                            width: 20
                        }
                    },
                    // 仪表盘指针
                    pointer: {
                        show: false
                    },
                    // 刻度标签
                    axisLabel: {
                        show: false
                    },
                    // 刻度
                    axisTick: {
                        show: false
                    },
                    // 分隔线
                    splitLine: {
                        show: false
                    },
                    title: {
                        offsetCenter: [0, '20%'],
                        fontSize: 20
                    },
                    detail: {
                        
                        offsetCenter: ['-36%', '-93%'],
                        valueAnimation: true,
                        textStyle: {
                            fontSize: 10
                        },
                        formatter: '英语:全省前{value}%'
                    },
                    startAngle: 90,
                    endAngle: -180,
                    data: [
                        { value: gaugechart_3_value.value}
                    ]
      },
      {
        name: '物理',
                    type: 'gauge',
                    center: ['50%', '55%'],
                    radius: '60%',
                    min: 100,
                    max: 0,
                    itemStyle: {
                        color: 'yellow',
                        shadowColor: 'rgba(0,138,255,0.45)'
                    },
                    // 进度条
                    progress: {
                        show: true,
                        width: 20,
                        roundCap: true
                    },
                    // 坐标轴线
                    axisLine: {
                        show: true,
                        roundCap: true,
                        lineStyle: {
                            width: 20
                        }
                    },
                    // 仪表盘指针
                    pointer: {
                        show: false
                    },
                    // 刻度标签
                    axisLabel: {
                        show: false
                    },
                    // 刻度
                    axisTick: {
                        show: false
                    },
                    // 分隔线
                    splitLine: {
                        show: false
                    },
                    title: {
                        offsetCenter: [0, '20%'],
                        fontSize: 20
                    },
                    detail: {
                        
                        offsetCenter: ['-41%', '-91%'],
                        valueAnimation: true,
                        textStyle: {
                            fontSize: 10
                        },
                        formatter: '物理:全省前{value}%'
                    },
                    startAngle: 90,
                    endAngle: -180,
                    data: [
                        { value: gaugechart_4_value.value}
                    ]
      },
      {
        name: '化学',
                    type: 'gauge',
                    center: ['50%', '55%'],
                    radius: '50%',
                    min: 100,
                    max: 0,
                    itemStyle: {
                        color: 'pink',
                        shadowColor: 'rgba(0,138,255,0.45)'
                    },
                    // 进度条
                    progress: {
                        show: true,
                        width: 20,
                        roundCap: true
                    },
                    // 坐标轴线
                    axisLine: {
                        show: true,
                        roundCap: true,
                        lineStyle: {
                            width: 20
                        }
                    },
                    // 仪表盘指针
                    pointer: {
                        show: false
                    },
                    // 刻度标签
                    axisLabel: {
                        show: false
                    },
                    // 刻度
                    axisTick: {
                        show: false
                    },
                    // 分隔线
                    splitLine: {
                        show: false
                    },
                    title: {
                        offsetCenter: [0, '20%'],
                        fontSize: 20
                    },
                    detail: {
                        
                        offsetCenter: ['-49%', '-89%'],
                        valueAnimation: true,
                        textStyle: {
                            fontSize: 10
                        },
                        formatter: '化学:全省前{value}%'
                    },
                    startAngle: 90,
                    endAngle: -180,
                    data: [
                        { value: gaugechart_5_value.value}
                    ]
      },
      {
        name: '生物',
                    type: 'gauge',
                    center: ['50%', '55%'],
                    radius: '40%',
                    min: 100,
                    max: 0,
                    itemStyle: {
                        color: 'green',
                        shadowColor: 'rgba(0,138,255,0.45)'
                    },
                    // 进度条
                    progress: {
                        show: true,
                        width: 20,
                        roundCap: true
                    },
                    // 坐标轴线
                    axisLine: {
                        show: true,
                        roundCap: true,
                        lineStyle: {
                            width: 20
                        }
                    },
                    // 仪表盘指针
                    pointer: {
                        show: false
                    },
                    // 刻度标签
                    axisLabel: {
                        show: false
                    },
                    // 刻度
                    axisTick: {
                        show: false
                    },
                    // 分隔线
                    splitLine: {
                        show: false
                    },
                    title: {
                        offsetCenter: [0, '20%'],
                        fontSize: 20
                    },
                    detail: {
                        
                        offsetCenter: ['-62%', '-86%'],
                        valueAnimation: true,
                        textStyle: {
                            fontSize: 10
                        },
                        formatter: '生物:全省前{value}%'
                    },
                    startAngle: 90,
                    endAngle: -180,
                    data: [
                        { value: gaugechart_6_value.value}
                    ]
      },
      {
        name: '总分',
                    type: 'gauge',
                    center: ['50%', '55%'],
                    radius: '30%',
                    min: 100,
                    max: 0,
                    itemStyle: {
                        color: 'purple',
                        shadowColor: 'rgba(0,138,255,0.45)'
                    },
                    // 进度条
                    progress: {
                        show: true,
                        width: 20,
                        roundCap: true
                    },
                    // 坐标轴线
                    axisLine: {
                        show: true,
                        roundCap: true,
                        lineStyle: {
                            width: 20
                        }
                    },
                    // 仪表盘指针
                    pointer: {
                        show: false
                    },
                    // 刻度标签
                    axisLabel: {
                        show: false
                    },
                    // 刻度
                    axisTick: {
                        show: false
                    },
                    // 分隔线
                    splitLine: {
                        show: false
                    },
                    title: {
                        offsetCenter: [0, '20%'],
                        fontSize: 20
                    },
                    detail: {
                        
                        offsetCenter: ['-82%', '-82%'],
                        valueAnimation: true,
                        textStyle: {
                            fontSize: 10
                        },
                        formatter: '总分:全省前{value}%'
                    },
                    startAngle: 90,
                    endAngle: -180,
                    data: [
                        { value: gaugechart_7_value.value}
                    ]
      }
    ]
  }
  const option2 = {
  backgroundColor: 'transparent', // 设置背景颜色为透明
  tooltip: {
    trigger: 'axis', // 在轴上触发提示框
    axisPointer: { // 使用轴指针
      type: 'shadow' // 使用阴影类型
    }
  },
  grid: { // 设置网格
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true // 确保标签被包含在内
  },
  xAxis: {
    type: 'value',
    boundaryGap: [0, 0.01] // 设置边界间隙
  },
  yAxis: {
    type: 'category',
    data: ['语文', '数学', '英语', '物理', '化学', '生物'],
    axisLine: { // 设置轴线
      lineStyle: {
        color: '#888'
      }
    },
    axisLabel: { // 设置轴标签
      color: '#888'
    }
  },
  series: [
    {
      name: '分数',
      type: 'bar',
      data: [barchart_1_value.value, barChart_2_value.value, barChart_3_value.value, barChart_4_value.value, barChart_5_value.value, barChart_6_value.value],
      itemStyle: { // 设置项目样式
        normal: {
          color: '#6f86d6'
        },
        emphasis: {
          color: '#8ea8e1'
        }
      }
    }
  ]
}

  chart1.setOption(option1)
  chart2.setOption(option2)
})

const fetchData = async () => {
  try {
    const response = await axios.get('http://192.168.186.212:5000/getdata');
    gaugechart_1_value.value = response.data[0].gaugechart_1;
    gaugechart_2_value.value = response.data[0].gaugechart_2;
    gaugechart_3_value.value = response.data[0].gaugechart_3;
    gaugechart_4_value.value = response.data[0].gaugechart_4;
    gaugechart_5_value.value = response.data[0].gaugechart_5;
    gaugechart_6_value.value = response.data[0].gaugechart_6;
    gaugechart_7_value.value = response.data[0].gaugechart_7;

    barchart_1_value.value = response.data[0].barChart_1;
    barChart_2_value.value = response.data[0].barChart_2;
    barChart_3_value.value = response.data[0].barChart_3;
    barChart_4_value.value = response.data[0].barChart_4;
    barChart_5_value.value = response.data[0].barChart_5;
    barChart_6_value.value = response.data[0].barChart_6;
    
  } catch (error) {
    console.error(error);
  }
}
onMounted(fetchData);  // 在组件挂载后获取数据
</script>

<template>

    <div>
        <div ref="gaugeChart" style="background-color: transparent;position:absolute;top:0px;width: 400px; height: 400px; background-color: #ffffff; padding: 0px; border-radius: 20px;"></div>
    </div>
    <div>
        <div ref="barChart" style="position:absolute;top:400px;width: 400px; height: 400px; background-color: #ffffff; padding: 0px; border-radius: 20px;"></div>
    </div>
    <img src="../assets/girlride.png" class="girlride">
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
.girlride {
    position: absolute;
left: 347px;
top: 329px;
width: 49px;
height: 100px;
opacity: 1;
z-index: 1;
}
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