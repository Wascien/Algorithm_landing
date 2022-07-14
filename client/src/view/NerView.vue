<template>
    <el-container>
        <el-aside width="200px" class="nav-side">
            <nav-side></nav-side>
        </el-aside>
        <el-main class="main">
            <main-header></main-header>
            <div class="container">
                <div class="input-container">
                    <div class="input">

                        <textarea class="text-area" v-model="text"></textarea>
                        <button class="input-button" v-on:click="clear">clear</button>
                        <button class="input-button" v-on:click="submit">submit</button>

                        <div class="clear"></div>
                    </div>
                    <div class="ans-space">
                        <div class="ans-space-text" v-html="processed_text">
                        </div>
                        <ul class="tag-list">
                            <li class="item" v-for="tag in Object.keys(tags)" :key="tag">
                                <span class="item-dot" :style="styles[tag]" ></span>
                                {{tag}}
                            </li>
                        </ul>
                    </div>
                    <div class="clear"></div>
                </div>
                <div class="information">
                    数据集：人民日报2014 测试：<a href="http://www.people.com.cn/">here</a>
                </div>
            </div>
            <home-footer></home-footer>
        </el-main>
    </el-container>

</template>

<script>
import NavSide from '@/components/NavSide.vue'
import MainHeader from '@/components/MainHeader.vue'
import HomeFooter from '@/components/HomeFooter.vue'
import axios from 'axios'

export default {
    data() {
        return {
            text: '新华社南宁7月13日电 （记者郭轶凡）中国—越南双边合作指导委员会第十四次会议13日在广西南宁举行，国务委员兼外长王毅和越南常务副总理范平明共同主持。',
            processed_text: '<span style="background-color:#E0FFFF;">新</span><span style="background-color:#E0FFFF;">华</span><span style="background-color:#E0FFFF;">社</span><span style="background-color:#E0FFFF;">南</span><span style="background-color:#E0FFFF;">宁</span><span style="background-color:#E0FFFF;">7</span><span style="background-color:#E0FFFF;">月</span><span style="background-color:#E0FFFF;">13</span><span style="background-color:#E0FFFF;">日</span>电 （记者<span style="background-color:#F0FFF0;">郭</span><span style="background-color:#F0FFF0;">轶</span><span style="background-color:#F0FFF0;">凡</span>）<span style="background-color:#FFE4C4;">中</span><span style="background-color:#FFE4C4;">国</span>—<span style="background-color:#FFE4C4;">越</span><span style="background-color:#FFE4C4;">南</span>双边合作指导委员会第十四次会议<span style="background-color:#E3E3E3;">13</span><span style="background-color:#E3E3E3;">日</span>在<span style="background-color:#FFE4C4;">广</span><span style="background-color:#FFE4C4;">西</span><span style="background-color:#FFE4C4;">南</span><span style="background-color:#FFE4C4;">宁</span>举行，国务委员兼外长<span style="background-color:#F0FFF0;">王</span><span style="background-color:#F0FFF0;">毅</span>和<span style="background-color:#FFE4C4;">越</span><span style="background-color:#FFE4C4;">南</span>常务副总理<span style="background-color:#F0FFF0;">范</span><span style="background-color:#F0FFF0;">平</span><span style="background-color:#F0FFF0;">明</span>共同主持。',
            tags: {"ORG": "#E0FFFF", "PER": "#F0FFF0", "LOC": "#FFE4C4", "T": "#E3E3E3"},
            styles:{ORG: 'background-color:#E0FFFF;', PER: 'background-color:#F0FFF0;', LOC: 'background-color:#FFE4C4;', T: 'background-color:#E3E3E3;'}
        }
    },
    components: {
        NavSide,
        MainHeader,
        HomeFooter
    }, methods: {
        clear() {
            this.text = '';
        },
        submit() {
            let data = { text: this.text }
            axios.post('http://127.0.0.1:8000/NER/', data).then(response => {
                this.processed_text = response.data.parsed_text
                console.log(this.processed_text)
                this.tags=response.data.tags
                this.styles={}
                for(var tag in this.tags){
                    this.styles[tag]=`background-color:${this.tags[tag]};`
                }
            })
        }
        
    }
}
</script>
<style  scoped>
.main {
    background-color: #eeeeee;
    padding: 0px;
}

div.container {
    width: 100%;
    height: 620px;
}

textarea.text-area {
    width: 600px;
    height: 300px;
    padding: 20px;
    float: left;
    resize: none;
    outline: none;
    border: none;
    border-right: 3px solid #eeeeee;
    font-size: 16px;
    color: #222222;
    background-color: white;
    font-weight: 600;
}

.input-container {
    width: 1200px;
    margin: auto;
    margin-top: 30px;
}

div.clear {
    clear: both;
}

.input {
    width: 600px;
    height: 340px;
    float: left;
}

.input-button {
    float: right;
    margin-left: 1px;
    margin-right: 2px;
    width: 100px;
    height: 40px;
    font-size: 18px;
    background-color: #222222;
    color: #eeeeee;
}

.input-button:hover {
    background-color: #eeeeee;
    color: #222222;
}

.ans-space{
    width: 600px;
    float: left;
    color: #222222;
    font-size: 16px;
}

.ans-space-text {
    padding: 20px;
    width: 600px;
    height: 300px;
    background-color: white;
}

ul.tag-list {
    padding: 20px;
    width: 600px;
    list-style: none;



}
li.item{
    float: right;
    height: 50px;
    line-height: 50px;
    margin-left: 10px;
}
span.item-dot{
    float: left;
    width: 30px;
    height: 30px;
    border-radius: 100%;
    background-color: #222222;
    margin-right: 10px;
    margin-top: 10px;
}

div.information{
    margin-top:40px;
    color: #222222;
    font-size:16px;
    text-align: center;
}
a{
    color: #222222;
    
}
a:hover{
    color: blue;
}
</style>