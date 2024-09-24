import {defineStore} from "pinia"   //从pinia中引入defineStore方法

export const useCounterStore = defineStore('counter', {//定义一个名为counter的store
    state(){

        return {
            num :1
        } 
    },
    actions: {
        increment() {
            this.num++  //this指向当前store实例
        },
        decrement() {
            this.num--
        }
    }
})