<template>
  <div id="personalinfo">
    <i-form :label-width="80">
      <h2>基本信息</h2>
      <br />
      <Form-item label="学号*">
        <i-input v-model="stu_num"></i-input>
      </Form-item>
      <Form-item label="姓名*">
        <i-input v-model="name" placeholder="请填写真实姓名"></i-input>
      </Form-item>
      <!-- <Form-item label="性别*">
        <RadioGroup v-model="gender">
          <Radio label="男"></Radio>
          <Radio label="女"></Radio>
        </RadioGroup>
      </Form-item>-->
      <Form-item label="所在学院*">
        <Select v-model="college" style="width:200px">
          <Option v-for="item in colleges" :value="item.name" :key="item.name">{{ item.name }}</Option>
        </Select>
      </Form-item>
      <Form-item label="专业班级*">
        <Select v-model="majorclass" style="width:200px">
          <Option v-for="item in majors" :value="item.name" :key="item.name">{{ item.name }}</Option>
        </Select>
      </Form-item>
      <Form-item>
        <i-button type="primary" @click="handleSubmit()">保存</i-button>
        <!-- <i-button type="ghost" @click="handleReset('formValidate')" style="margin-left: 8px ;color:black;">重置</i-button>  -->
      </Form-item>
    </i-form>
  </div>
</template>
<script>
export default {
  name: "personalinfo",
  data() {
    return {
      stu_num: "",
      name: "",
      college: "",
      colleges: [
        { name: "计算机科学与技术学院" },
        { name: "石油工程学院" },
        { name: "地球科学与技术学院" },
        { name: "经济管理学院" },
        { name: "文学院" },
        { name: "信息与控制工程学院" },
        { name: "机械学院" },
        { name: "化学工程学院" }
      ],
      majorclass: "",
      majors: [
        { name: "计算1601" },
        { name: "计算1602" },
        { name: "计算1603" },
        { name: "计算1604" },
        { name: "软件1601" },
        { name: "软件1602" },
        { name: "软件1603" },
        { name: "软件1604" },
        { name: "物联网1601" },
        { name: "物联网1602" }
      ]
    };
  },
  created() {
    this.stu_num = this.$route.params.stu_num;
    //this.getinfo()
  },
  methods: {
    handleSubmit() {
      let self = this;
      this.$axios
        .get("http://localhost:8000/api/add_student", {
          params: {
            stu_num: self.stu_num,
            stu_name: self.name,
            stu_college: self.college,
            stu_class: self.majorclass
          }
        })
        .then(res => {
          if (res.data.error_num == 1) {
            console.log(self.name);
            alert("创建失败,错误：" + res.data.msg);
            console.log(res);
          } else {
            alert("创建成功！");
            console.log(res);
            self.$router.push({
            name:'CreateNewcase',
            params:{
              stu_num:self.stu_num
            }
        })
          }
        });
    },
    add(info) {
      this.doctordate.push(info);
    }
  }
};
</script>
