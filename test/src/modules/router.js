import routes from '~pages'
import { createRouter, createWebHistory } from "vue-router"
const router = createRouter({
    routes,     //~pages自动扫描pages目录下的所有.vue文件
    history: createWebHistory()
})

export default router 