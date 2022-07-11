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
                    <div class="ans-space" v-html="processed_text">

                    </div>
                    <div class="clear"></div>
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
            text: '',
            processed_text: '<span style="background-color:#E0FFFF;">新</span><span style="background-color:#E0FFFF;">华</span><span style="background-color:#E0FFFF;">社</span><span style="background-color:#FFE4C4;">印</span><span style="background-color:#FFE4C4;">度</span><span style="background-color:#FFE4C4;">尼</span><span style="background-color:#FFE4C4;">西</span><span style="background-color:#FFE4C4;">亚</span><span style="background-color:#FFE4C4;">巴</span><span style="background-color:#FFE4C4;">厘</span><span style="background-color:#FFE4C4;">岛</span><span style="background-color:#FFE4C4;">7</span><span style="background-color:#FFE4C4;">月</span><span style="background-color:#FFE4C4;">9</span><span style="background-color:#FFE4C4;">日</span>电（记者<span style="background-color:#F0FFF0;">余</span><span style="background-color:#F0FFF0;">谦</span><span style="background-color:#F0FFF0;">梁</span>）当地时间<span style="background-color:#E3E3E3;">2</span><span style="background-color:#E3E3E3;">0</span><span style="background-color:#E3E3E3;">2</span><span style="background-color:#E3E3E3;">2</span><span style="background-color:#E3E3E3;">年</span><span style="background-color:#E3E3E3;">7</span>月9日，国务委员<span style="background-color:#F0FFF0;">兼</span><span style="background-color:#F0FFF0;">外</span>长<span style="background-color:#FFE4C4;">王</span><span style="background-color:#FFE4C4;">毅</span><span style="background-color:#FFE4C4;">在</span>巴厘岛出席二十国集团外长<span style="background-color:#FFE4C4;">会</span><span style="background-color:#FFE4C4;">后</span>同美国<span style="background-color:#F0FFF0;">国</span><span style="background-color:#F0FFF0;">务</span><span style="background-color:#F0FFF0;">卿</span>布林肯举行会晤。双方就中美关系及共同关心的国际和地区问题进行了全面、深入、坦诚和长时间的沟通。双方都认为，此次对话是实质性的，也具有建设性，有助于增进彼此相互了解，减少误解误判，并<span style="background-color:#E3E3E3;">为</span><span style="background-color:#E3E3E3;">两</span>国未来高层交往积累了条件。'
           
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
            let data={text:this.text}
            axios.post('http://127.0.0.1:8000/NER/', data).then(response=>{
                this.processed_text=response.data.parsed_text
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

.ans-space {
    width: 600px;
    height: 300px;
    float: left;
    background-color: white;
    padding: 20px;
    color: #222222;
    font-size: 16px;
}
</style>