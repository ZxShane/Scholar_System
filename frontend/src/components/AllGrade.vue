<template>
  <div class="allgrade">
    <h2 style="margin-bottom:20px;" align = "center">综合成绩成绩排名</h2>
    <table border="0" align = "center">
      <tr>
        <th>排名</th>
        <th>学号</th>
        <th>专业成绩</th>
        <th>发展性测评成绩</th>
        <th>总成绩</th>
      </tr>
      <tr v-for="(calculate,index) in calculates">
        <td>{{ index+1 }}</td>
        <td>{{ calculate.pk }}</td>
        <td>{{ calculate.fields.stu_major_grade }}</td>
        <td>{{ calculate.fields.activity_grade }}</td>
        <td>{{ calculate.fields.stu_sum_grade }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: "MyTrade",
  data() {
    return {
      calculates: []
    };
  },
  created() {
    this.getall();
  },
  methods: {
    getall() {
      let self = this
      this.$axios
        .get("http://127.0.0.1:8000/api/show_all_calculate")
        .then(res => {
          console.log(res.data.list);
          self.calculates = res.data.list;
        });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
#btn {
  margin-right: 110px;
  padding: 0.5% 1%;
  border-radius: 10px;
  background-color: ghostwhite;
  margin-top: 30px;
  text-decoration: none;
  outline: none;
}

table tr th{
  padding-right: 150px;
  font-size: 15px;
}
table tr td{
  padding-right: 150px;
  font-size: 15px;
}
</style>
