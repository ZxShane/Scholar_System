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
      <h2>添加专业成绩</h2>
       <Form-item label="学期">
          <Select v-model="term" style="width:200px">
            <Option v-for="item in terms" :value="item.name" :key="item.name">{{ item.name }}</Option>
          </Select>
        </Form-item>
        <Form-item label="专业成绩">
          <Poptip trigger="focus">
            <Input v-model="grade" placeholder="Enter number" style="width: 120px" />
            <div slot="content">{{ grade }}</div>
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
      grade:'',
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
        .get("http://127.0.0.1:8000/api/add_major_grade", {
          params: {
            stu_num: self.stu_num,
            term:self.term,
            stu_major_grade:self.grade
          }
        })
        .then(res => {
          console.log(res.data)
          if(res.data.error_num==0){
            alert("活动专业成绩成功！")
            window.location.reload()
          }else{
            alert("添加失败！")
          }
        });
    }
  }
};
</script>
