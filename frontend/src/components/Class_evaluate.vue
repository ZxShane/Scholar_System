<template>
  <div class="myTable table-responsive">
    <div class>
      <h4 class="col-sm-6">专业班级:{{ stu_class }}</h4>
      <h4 class="col-sm-6">{{stu_num}}</h4>
    </div>

    <Card v-for="student in show_students" class="card">
      <td>{{student.fields.be_evaluate_num}}</td>
      <td>{{student.fields.be_evaluate_name}}</td>
      <td>
        <label class="radio-inline">
          <input
            type="radio"
            value="A"
            @click="hand('A',student.fields.be_evaluate_num)"
          /> A
        </label>
        <label class="radio-inline">
          <input
            type="radio"
            value="B"
            @click="hand('B',student.fields.be_evaluate_num)"
          /> B
        </label>
        <label class="radio-inline">
          <input
            type="radio"
            value="C"
            @click="hand('C',student.fields.be_evaluate_num)"
          /> C
        </label>
        <label class="radio-inline">
          <input
            type="radio"
            value="D"
            @click="hand('D',student.fields.be_evaluate_num)"
          /> D
        </label>
      </td>
    </Card>

    <!-- <tbody>
        <tr v-for="student in show_students">
          <td>{{student.fields.be_evaluate_num}}</td>
          <td>{{student.fields.be_evaluate_name}}</td>
          <td>
            <label class="radio-inline">
              <input type="radio" value="A" /> A
            </label>
            <label class="radio-inline">
              <input type="radio" value="B"/> B
            </label>
            <label class="radio-inline">
              <input type="radio" value="C"/> C
            </label>
            <label class="radio-inline">
              <input type="radio" value="D"/> D
            </label>
          </td>
        </tr>
    </tbody>-->
    <h5 class="bg-info" style="padding: 10px;background: none">注:只显示还未评价的同学</h5>
    <!-- <button class="btn btn-success btn-lg" @click="submit()">提交</button> -->
  </div>
</template>
<script>
export default {
  name: "Wallet",
  data() {
    return {
      stu_num: "",
      stu_class: "",
      all_students: "",
      show_students: ""
    };
  },
  created() {
    this.stu_num = window.sessionStorage.getItem("stu_num");
    this.getOne();
    //  this.getAll()
  },
  methods: {
    hand: function(grade, be_evaluate_stu_num) {
      let self = this;
      this.$axios
        .get("http://127.0.0.1:8000/api/evaluate", {
          params: {
            evaluate_stu_num: self.stu_num,
            be_evaluate_stu_num: be_evaluate_stu_num,
            grade: grade
          }
        })
        .then(res => {
          console.log(res.data);
          if (res.data.error_num == 0) {
            self.$axios
              .get("http://127.0.0.1:8000/api/change_is_evaluate", {
                params: {
                  stu_num: self.stu_num,
                  be_evaluate_num: be_evaluate_stu_num
                }
              })
              .then(results => {
                console.log(results.data)
                if (results.data.error_num == 0) {
                  self.getstudents();
                } else {
                  alert("get wrong!");
                }
              });
          } else {
            alert("评价失败");
          }
        });
    },
    getstudents: function() {
      this.$axios
        .get("http://127.0.0.1:8000/api/show_students", {
          params: {
            stu_num: self.stu_num
          }
        })
        .then(res => {
          console.log(res.data);
          self.show_students = res.data.list;
          window.location.reload()
        });
    },
    getAll: function() {
      let self = this;
      console.log(self.stu_class);
      this.$axios
        .get("http://127.0.0.1:8000/api/show_all_student", {
          params: {
            stu_class: self.stu_class
          }
        })
        .then(res => {
          console.log(res.data);
          self.all_students = res.data.list;
          console.log(self.all_students);
          self.$axios
            .get("http://127.0.0.1:8000/api/show_students", {
              params: {
                stu_num: self.stu_num
              }
            })
            .then(res => {
              console.log(res.data.list);
              if (res.data.list == []) {
                for (var i = 0; i < self.all_students.length; i++) {
                  self.$axios
                    .get("http://127.0.0.1:8000/api/add_is_evaluate", {
                      params: {
                        stu_num: self.stu_num,
                        be_evaluate_num: self.all_students[i].pk,
                        be_evaluate_name: self.all_students[i].fields.stu_name
                      }
                    })
                    .then(response => {});
                }
              } else {
                self.show_students = res.data.list;
              }
            });
        });
    },
    getOne: function() {
      let self = this;
      console.log(self.stu_num);
      this.$axios
        .get("http://127.0.0.1:8000/api/show_one_student", {
          params: {
            stu_num: self.stu_num
          }
        })
        .then(res => {
          if (res.data.error_num == 0) {
            console.log(res.data.list);
            self.stu_class = res.data.list[0].fields.stu_class;
            self.getAll();
          } else {
            alert("访问出错");
          }
        });
    }
  }
};
</script>
<style scoped>
.card {
  margin-bottom: 1%;
}
.radio-inline {
  margin-left: 20px;
}
</style>
