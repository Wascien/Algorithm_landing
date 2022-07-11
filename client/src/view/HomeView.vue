<template>
    <el-container>
        <el-aside width="200px" class="nav-side">
            <nav-side></nav-side>
        </el-aside>
        <el-main class="main">
            <div class="header">
                更新日志
            </div>
            <el-timeline class="time-line" id="timeline">
                <el-timeline-item v-for="(activity, index) in activities" :key="index" :timestamp="activity.timestamp" class="time-line-item" >
                    {{ activity.content }}
                </el-timeline-item>
            </el-timeline>
            <div class="space"></div>
            <home-footer></home-footer>
        </el-main>
    </el-container>
</template>
<script>
import NavSide from '@/components/NavSide.vue'
import HomeFooter from '@/components/HomeFooter.vue'
const activities = [
    {
        content:'搭建前端页面',
        timestamp:'2022-7-10'
    }
    ,{
        content: '项目开始',
        timestamp: '2022-07-06',
    },
    {
        content: '创建github仓库',
        timestamp: '2022-07-05',
    },
    {
        content: '讨论想法',
        timestamp: '2022-07-01',
    },
]
export default {
    data() {
        return {
            activities: activities,
        }
    },
    components: {
        NavSide,
        HomeFooter
    }
}
</script>
<style  scoped>
.nav-side {
    
}

.main {
    background-color: #eeeeee;
    padding: 0px;
}

div.header {
    height: 60px;
    width: 100%;
    border-bottom: 2px solid #222222;
    font-size: 20px;
    font-weight: 700;
    line-height: 60px;
    padding-left: 40px;
}

.time-line {
    padding-top: 20px;
    padding-left: 200px;
    
}
div.space{
    width: 100%;
    height: 200px;

}

</style>