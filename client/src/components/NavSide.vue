<template>
    <el-menu id="nav-side" router="True">
        <h1 class="header">Lin/Zhe</h1>
        <el-menu-item class="menu-item" index="/"  >
           <span>首页</span>
        </el-menu-item>
        <el-menu-item class="menu-item" index="/NER" >
            <span>NER</span>
        </el-menu-item>
        <el-menu-item class="menu-item" index="">
            <span>数字识别</span>
        </el-menu-item>
        <el-menu-item class="menu-item" index="">
            <span>关于</span>
        </el-menu-item>
    </el-menu>
</template>

<script>

export default {
}
</script>
<style  scoped>
#nav-side {
    width: 200px;
    height: 100%;
    background-color: #222222;
}

h1.header {
    color: #eeeeee;
    font-size: 30px;
    text-align: center;
    width: 100%;
    height: 80px;
    line-height: 80px;
}

.menu-item {
    color: #eeeeee;
    font-size: 16px;
    font-weight: 700;
    padding: 0px;
}
.menu-item:hover{
    background-color: #eeeeee;
    color:#222222
}


</style>