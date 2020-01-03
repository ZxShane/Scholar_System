<template>
  <div id="load">
    <h1 style="margin-left:20%;margin-bottom:10%;">登录</h1>
    <i-form inline>
      <Form-item>
        <h4 style="block:inline;">用户名：</h4>
        <i-input type="text" placeholder="Username" inline margin-bottom="10%" v-model="username">
          <Icon type="ios-person-outline" slot="prepend"></Icon>
        </i-input>
      </Form-item>
      <br />
      <Form-item>
        <h4 style="block:inline;">密码：</h4>
        <i-input type="password" placeholder="Password" inline v-model="password">
          <Icon type="ios-pin-outline" slot="prepend"></Icon>
        </i-input>
      </Form-item>
      <br />
      <Form-item style="margin-top:3%;">
        <i-button type="primary" @click="handleSubmit()" style="margin-left:130px;">登录</i-button>
        <!-- <i-button type="primary" @click="register()" >注册</i-button> -->
      </Form-item>
    </i-form>
  </div>
</template>
<script>
export default {
  name: "Load",
  data() {
    return {
      username: "",
      password: "",
      doctorId: "",
      stu_num: ""
    };
  },
  created() {
    this.stu_num = window.sessionStorage.getItem("stu_num");
    if (this.doctorid != "" && this.doctorid != undefined) {
      this.$router.push({
        path: "/createnewcase"
      });
    }
  },
  methods: {
    handleSubmit() {
      let self = this;
      this.$axios
        .get("http://127.0.0.1:8000/api/show_one_student",{
          stu_num: self.stu_num
        }).then(res => {
          console.log(res.data.list);
          if(res.data.list=[]){
            self.$router.push({
            name:'PersonalInfo',
            params:{
              stu_num:self.stu_num
            }
        })
          }
          // if (self.username==self.password){
          //  window.sessionStorage.setItem('stu_num',self.username)
          //  self.$router.push({
          //   path:'/createnewcase'
          // })
          // }else{
          //   alert("账号或密码错误！")
          // }
        })

      // this.$axios.post("http://117.78.1.3:8080/invoke",{
      //   func:'doctorLogin',
      //   username:self.username,
      //   password:self.password
      // }).then((res)=>{
      //   self.doctorId = res.data
      //   console.log(res)
      //   window.sessionStorage.setItem('doctorId',res.data)
      //   self.$router.push({
      //     path:'/createnewcase'
      //   })
      // })
    },
    register() {
      this.$router.push({
        name: "PersonalInfo",
        params:{
          stu_num:self.stu_num
        }
      });
    }
  }
};
</script>
<style scoped>
#load {
  margin-top: 70px;
  /* border-style: solid;
  border-color: cornflowerblue; */
  border-radius: 10px;
  margin-left: 30%;
  margin-right: 40%;
  padding-left: 5%;
  padding-right: 2%;
}
</style>
