<template>
<div class="sonlife" v-if="isUpdate">{{son}}</div>
</template>

<script>
export default {
    name: "sonlife",
    props: ['son'],
    data() {
        return {
            isUpdate: false,
        }
    },
    watch: {
        son: function() {
            console.log("检测到son变化了")
            this.isUpdate = true;
        }
    },
    mounted() {
        console.log("mounted")
    }
}
</script>

<style lang="scss" scoped>
</style>
