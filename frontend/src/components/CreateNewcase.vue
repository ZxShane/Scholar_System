<template>
  <div style="font-size:15px;">
    <i-form :label-width="80" style="overflow:scroll;">
      <h2>学生基本信息</h2>
      <br />
      <Form-item label="学号">
        <i-input disabled v-model="stu_num"></i-input>
      </Form-item>
      <Form-item label="姓名">
        <i-input disabled v-model="stu_name">{{ stu_name }}</i-input>
      </Form-item>
      <Form-item label="学院">
        <i-input disabled v-model="stu_college">{{ stu_college }}</i-input>
      </Form-item>
      <Form-item label="班级">
        <i-input disabled v-model="stu_class">{{ stu_class }}</i-input>
      </Form-item>
      <h2>添加活动材料</h2>
      <br />
      <i-form :label-width="80">
        <Form-item label="学期">
          <Select v-model="term" style="width:200px">
            <Option v-for="item in terms" :value="item.name" :key="item.name">{{ item.name }}</Option>
          </Select>
        </Form-item>
        <Form-item label="活动名称">
          <i-input placeholder="请输入活动名称" v-model="activity_name"></i-input>
        </Form-item>

        <Form-item label="赋分">
          <Poptip trigger="focus">
            <Input v-model="activity_num" placeholder="Enter number" style="width: 120px" />
            <div slot="content">{{ activity_num }}</div>
          </Poptip>
        </Form-item>
        <Form-item>
          <i-button type="primary" @click="handleSubmit()">提交</i-button>
          <!-- <i-button type="ghost" style="margin-left: 8px ;color:black;">重置</i-button> -->
        </Form-item>
      </i-form>
    </i-form>
  </div>
</template>
<script>
export default {
  name: "CreateNewCase",
  data() {
    return {
      stu_num: "",
      stu_name: "",
      stu_college: "",
      stu_class: "",
      term: "",
      terms: [
        { name: "2016-2017-1" },
        { name: "2016-2017-2" },
        { name: "2016-2017-3" },
        { name: "2017-2018-1" },
        { name: "2017-2018-2" },
        { name: "2017-2018-3" },
        { name: "2018-2019-1" },
        { name: "2018-2019-2" },
        { name: "2018-2019-3" },
        { name: "2019-2020-1" },
        { name: "2019-2020-2" }
      ],
      activity_name: "",
      activity_num: ""
    };
  },
  created() {
    //this.getPatientInfo();
    this.stu_num = window.sessionStorage.getItem("stu_num");
    if (this.stu_num == "") {
      alert("请先登录！");
      this.$router.push({
        path: "/"
      });
    } else {
      this.getStudentinfo();
    }
  },
  methods: {
    getStudentinfo: function() {
      let self = this;
      self.$axios
        .get("http://127.0.0.1:8000/api/show_one_student", {
          params: {
            stu_num: self.stu_num
          }
        })
        .then(res => {
          console.log(res.data.list[0]);
          self.stu_name = res.data.list[0].fields.stu_name;
          self.stu_college = res.data.list[0].fields.stu_college;
          self.stu_class = res.data.list[0].fields.stu_class;
        });
    },
    handleSubmit:function(){
      let self = this;
      self.$axios
        .get("http://127.0.0.1:8000/api/add_activity", {
          params: {
            stu_num: self.stu_num,
            stu_name:self.stu_name,
            term:self.term,
            activity_name:self.activity_name,
            activity_num:self.activity_num
          }
        })
        .then(res => {
          console.log(res.data)
          if(res.data.error_num==0){
            alert("活动材料添加成功！")
            window.location.reload()
          }else{
            alert("提交失败，请稍后重试或联系管理员！")
          }
        });
    }
  }
};
</script>
