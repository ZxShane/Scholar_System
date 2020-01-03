<template>
  <div id="wallet" style="overflow:scroll;">
    <div style="margin-bottom:30px;">
      <h4 class="col-sm-6 inline">专业班级:{{ stu_class }}</h4>
      <h4 class="col-sm-6 inline">学号：{{stu_num}}</h4>
      <h4 class="col-sm-6 inline">姓名：{{stu_name}}</h4>
    </div>
    <Button type="success" @click="calculate_sum()" style="margin-bottom:5px;">查看成绩</Button>
    <Table :columns="columns1" :data="data1" v-show="isshowgrade" style="margin-bottom:5px;"></Table>
    <Button type="success" @click="getevaluate()" style="margin-bottom:5px;">查看评价结果</Button>
    <Table :columns="columns3" :data="data3" v-show="isshowevaluate" style="margin-bottom:5px;"></Table>
    <Button type="success" @click="getactivity()" style="margin-bottom:5px;">查看发展性评价明细</Button>
    <Table :columns="columns2" :data="data2" v-show="isshowactivity" style="margin-bottom:5px;"></Table>
  </div>
</template>
<script>
export default {
  name: "Wallet",
  data() {
    return {
      stu_num: "",
      stu_class: "",
      stu_name: "",
      A: 0,
      B: 0,
      C: 0,
      D: 0,
      evaluate_grade: 0,
      activitys: "",
      activity_grade: 0,
      major_grade: 0,
      sum_grade: 0,
      isshowgrade: false,
      isshowactivity: false,
      isshowevaluate: false,
      columns1: [
        {
          title: "姓名",
          key: "stu_name"
        },
        {
          title: "专业成绩",
          key: "major_grade"
        },
        {
          title: "班级互评成绩",
          key: "evaluate_grade"
        },
        {
          title: "发展性测评成绩",
          key: "activity_grade"
        },
        {
          title: "总成绩",
          key: "sum_grade"
        }
      ],
      columns2: [
        {
          title: "姓名",
          key: "stu_name"
        },
        {
          title: "活动名称",
          key: "activity_name"
        },
        {
          title: "赋分",
          key: "activity_num"
        },
        {
          title: "是否同意",
          key: "isagree"
        }
        
      ],
      columns3: [
        {
          title: "姓名",
          key: "stu_name"
        },
        {
          title: "A的数量",
          key: "A"
        },
        {
          title: "B的数量",
          key: "B"
        },
        {
          title: "C的数量",
          key: "C"
        },
        {
          title: "D的数量",
          key: "D"
        },
        {
          title: "评价结果",
          key: "grade"
        }
        
      ],
      data2:[],
      data1:[],
      data3:[],
      onegrade: {
        stu_name: "",
        major_grade: "",
        evaluate_grade: "",
        activity_grade: "",
        sum_grade: ""
      },
      oneactivity: {
        stu_name: "",
        activity_name: "",
        activity_num: "",
        isagree: "",
      },
      oneevaluate: {
        stu_name: self.stu_name,
        A: "",
        B: "",
        C: "",
        D:"",
        grade:""
      },
    };
  },
  created() {
    this.stu_num = window.sessionStorage.getItem("stu_num");
    this.getstudentinfo();
    this.getbeevaluate();
    this.getactivitygrade();
    this.getmajorgrade();
    // this.calculate_sum()
  },
  methods: {
    getactivity() {
      this.isshowactivity = true
    },
    getevaluate(){
        this.isshowevaluate = true
    },
    getstudentinfo: function() {
      let self = this;
      self.$axios
        .get("http://127.0.0.1:8000/api/show_one_student", {
          params: {
            stu_num: self.stu_num
          }
        })
        .then(res => {
          console.log(res.data.list);
          self.stu_class = res.data.list[0].fields.stu_class;
          self.stu_name = res.data.list[0].fields.stu_name;
        });
    },
    getbeevaluate: function() {
      let self = this;
      self.$axios
        .get("http://127.0.0.1:8000/api/query_be_evaluate", {
          params: {
            stu_num: self.stu_num
          }
        })
        .then(res => {
          console.log(res.data.list);
          for (var i = 0; i < res.data.list.length; i++) {
            switch (res.data.list[i].fields.grade) {
              case "A":
                self.A += 1;
                break;
              case "B":
                self.B += 1;
                break;
              case "C":
                self.C += 1;
                break;
              case "D":
                self.D += 1;
            }
          }
          self.evaluate_grade =
            (95 * self.A + 85 * self.B + 75 * self.C + 65 * self.D) /
            res.data.list.length;
          console.log(self.A, self.B, self.C, self.D, self.evaluate_grade);
          self.$axios
            .get("http://127.0.0.1:8000/api/add_evaluate_number", {
              params: {
                stu_num: self.stu_num,
                A_num: self.A,
                B_num: self.B,
                C_num: self.C,
                D_num: self.D,
                evaluate_grade: self.evaluate_grade
              }
            })
            .then(response => {
              console.log(response.data);
            });
            self.oneevaluate.stu_name = self.stu_name
            self.oneevaluate.A = self.A
            self.oneevaluate.B = self.B
            self.oneevaluate.C = self.C
            self.oneevaluate.D = self.D
            self.oneevaluate.grade = self.evaluate_grade
            self.data3.push(self.oneevaluate)
        });
    },
    getactivitygrade() {
      let self = this;
      self.$axios
        .get("http://127.0.0.1:8000/api/query_activity", {
          params: {
            stu_num: self.stu_num
          }
        })
        .then(res => {
          console.log(res.data.list);
          self.activitys = res.data.list;
          for (var i = 0; i < self.activitys.length; i++) {
            if (self.activitys[i].fields.isagree) {
              activity_grade += self.activitys[i].fields.activity_num;
            }
            self.oneactivity.stu_name = self.stu_name
            self.oneactivity.activity_name = self.activitys[i].fields.activity_name
            self.oneactivity.activity_num = self.activitys[i].fields.activity_num
            if(self.activitys[i].fields.ischeck)
            {
              if(self.activitys[i].fields.isagree)
              {
                self.oneactivity.isagree = "审核通过"
              }else{
                self.oneactivity.isagree = "审核未通过"
              }
            }else{
               self.oneactivity.isagree = "未审核"
            }
            self.data2.push(self.oneactivity)
          }
        });
    },
    getmajorgrade() {
      let self = this;
      self.$axios
        .get("http://127.0.0.1:8000/api/show_major_grade", {
          params: {
            stu_num: self.stu_num
          }
        })
        .then(res => {
          console.log(res.data.list);
          self.major_grade = res.data.list[0].fields.stu_major_grade;
        });
    },
    calculate_sum() {
      let self = this;
      console.log(self.major_grade, self.activity_grade, self.evaluate_grade);
      self.sum_grade =
        self.major_grade * 0.8 +
        self.activity_grade * 0.1 +
        self.evaluate_grade * 0.1;
      self.isshowgrade = true;
      self.$axios
        .get("http://127.0.0.1:8000/api/calculate", {
          params: {
            stu_num: self.stu_num,
            stu_major_grade: self.major_grade,
            activity_grade: self.activity_grade,
            stu_sum_grade: self.sum_grade
          }
        })
        .then(res => {
          console.log(res.data);

          self.onegrade.stu_name = self.stu_name;
          self.onegrade.major_grade = self.major_grade;
          self.onegrade.evaluate_grade = self.evaluate_grade;
          self.onegrade.activity_grade = self.activity_grade;
          self.onegrade.sum_grade = self.sum_grade;
          self.data1.push(self.onegrade);
        });
    }
  }
};
</script>
