<template>
  <div id="Addinfo">
    <div class="yuyue">
      <div class="info">
        <h1 style="margin-top:30px;">转科申请</h1>
        <h3 style="margin-top:20px;">身份证号：{{ patientId }}</h3>
        <h3 style="margin-top:20px;">姓名：{{ name }}</h3>
        <h3 style="margin-top:20px;">当前科室：{{ sector }}</h3>
        <h2 style="margin-top:20px;">转出：</h2>
        <h3 style="margin-top:20px;">请选择医院：</h3>
        <Select v-model="hospitalname" style="width:200px">
          <Option v-for="item in hospitals" :value="item.value" :key="item.value">{{ item.name }}</Option>
        </Select>
        <h3 style="margin-top:20px;">请选择科室：</h3>
        <Select v-model="outsector" style="width:200px">
          <Option v-for="item in sectorname" :value="item" :key="item" @click="searchdoctor()" >{{ item }}</Option>
        </Select>
        <h3 style="margin-top:20px;">请选择医生：</h3>
        <Select v-model="outdoctor" style="width:200px">
          <Option v-for="item in docotors" :value="item.doctorId" :key="item.doctorId">{{ item.doctorName }}</Option>
        </Select>
      </div>
      <Button
        type="primary"
        @click="submit()"
        style="margin-top:30px;margin-left:80%;margin-bottom:30px;"
      >转出</Button>
    </div>
  </div>
</template>
<script>
export default {
  name: "Inhospital",
  data() {
    return {
      patientId: "",
      name: "",
      sector: "",
      aes: "",
      hospitalname: "",
      outsector: "",
      outdoctor: "",
      doctorid:'',
      hospitals: [
        {
          name: "青岛大学附属医院黄岛分院",
          value: "青岛大学附属医院黄岛分院"
        },
        {
          name: "友爱医院",
          value: "友爱医院"
        }
      ],
      sectorname: [
        "口腔科",
        "外科",
        "脑科",
        "妇产科",
        "儿科",
        "皮肤科",
        "内科",
        "耳鼻喉科",
        "心理科"
      ],
      docotors: [""],
      //doctorId:''
    };
  },
  watch:{
    outsector:function(){
        this.searchdoctor()
    }
  },
  created() {
    this.patientId = window.sessionStorage.getItem("patientId");
    this.name = window.sessionStorage.getItem("patientname");
    this.aes = window.sessionStorage.getItem("aes");
    this.sector = window.sessionStorage.getItem("sector");
    this.doctorid = window.sessionStorage.getItem('doctorId')
    if(this.doctorid=='')
    {
      alert("请先登录！")
      this.$router.push({
        path:'/'
      })
    }
  },
  methods: {
    submit(){
      let self = this
    console.log(this.patientId,this.outdoctor)
    this.$axios
        .post("http://117.78.1.3:8080/invoke", {
          func:'transferPermission',
          doctorId: self.outdoctor,
          patientId: self.patientId
        }).then((res)=>{
          console.log(res)
          alert("转科成功！")
        })
    },
    searchdoctor() {
      let self = this;
      this.$axios
        .post("http://117.78.1.3:8080/querydoc", {
          hospitalname: self.hospitalname,
          department: self.outsector
        })
        .then(res => {
          console.log(res);
          for(var i=0;i<res.data.length;i++)
          {
            self.$axios.post('http://117.78.1.3:8080/querydoctorinfo',{
              "doctorId":res.data[i].DoctorID
            }).then((response)=>{
              console.log(response.data)
              var doctorName = response.data.doctorName
              var doctorId = response.data.doctorId
              self.docotors.push({doctorName,doctorId})
            })
          }
        });
    }
  }
};
</script>
<style scoped>
.yuyue {
  border-radius: 20px;
  border-style: solid;
  border-color: cornflowerblue;
  width: 35%;
  padding-right: 2%;
  margin-left: 25%;
  margin-top: 2%;
}
.info {
  margin-left: 30%;
}
</style>