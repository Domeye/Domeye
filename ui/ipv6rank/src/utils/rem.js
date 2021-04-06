// 设计稿以1920px为宽度（1920*1080），而我把页面宽度设计为10rem的情况下

const baseSize1 = 192; // 128这个是设计稿中1rem的大小。
const baseSize2 = 225;
function setRem() {
    const w = document.documentElement.clientWidth;
    const h = document.documentElement.clientHeight;
    // 实际设备页面宽度和设计稿的比值
    const scale = w / 1920;
    console.log("clientWidth:", w)
    console.log("clientHeight:", h)
    document.documentElement.style.fontSize = (baseSize1 * scale) + 'px';
    // 如果屏幕长/屏幕宽 > 1920 / 1080, 会出现滚动条
    console.log("HTML根节点px:", document.documentElement.style.fontSize)

    // if(w / h <= (1920 / 1080)) {
    //   const scale = w / 1920;
    //   console.log("clientWidth:", w)
    //   console.log("clientHeight:", h)
    //   // 计算实际的rem值并赋予给html的font-size
    //   document.documentElement.style.fontSize = (baseSize1 * scale) + 'px';
    //   // 如果屏幕长/屏幕宽 > 1920 / 1080, 会出现滚动条
    //   // console.log("HTML根节点px:", document.documentElement.style.fontSize)
    // } else {
    //   const scale = h / 1080;
    //   console.log("clientWidth:", w)
    //   console.log("clientHeight:", h)
    //   // 计算实际的rem值并赋予给html的font-size
    //   document.documentElement.style.fontSize = (baseSize2 * scale) + 'px';
    //   // 如果屏幕长/屏幕宽 > 1920 / 1080, 会出现滚动条
    //   // console.log("HTML根节点px:", document.documentElement.style.fontSize)
    // }
}
setRem();
window.addEventListener('resize', () => {
    setRem();
});

// function setRem () {
//     //  PC端
//     console.log('非移动设备')
//     // 基准大小
//     baseSize = 100;
//     let basePc = baseSize / 1920; // 表示1920的设计图,使用100PX的默认值
//     let vW = window.innerWidth; // 当前窗口的宽度
//     let vH = window.innerHeight; // 当前窗口的高度
//     console.log("vW", vH);
//     console.log("vH:", vH);
//     // 非正常屏幕下的尺寸换算
//     let dueH = vW * 1080 / 1920  // 正常情况下自适应应有的高度
//     if (vH < dueH) { // 当前屏幕高度小于应有的屏幕高度，就需要根据当前屏幕高度重新计算屏幕宽度
//       vW = vH * 1920 /1080
//     }
//     let rem = vW * basePc; // 以默认比例值乘以当前窗口宽度,得到该宽度下的相应font-size值
//     console.log("px:", rem)
//     document.documentElement.style.fontSize =  rem + "px";
// }
// // 初始化
// setRem();
// // 改变窗口大小时重新设置 rem
// window.onresize = function () {
//   setRem()
// };
