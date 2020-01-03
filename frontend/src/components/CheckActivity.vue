<template>
  <div class="myTable table-responsive">
    <h1>审核活动</h1>
    <Card v-for="activity in activitys" class="card">
      <td id="colum">{{activity.fields.stu_num}}</td>
      <td id="colum">{{activity.fields.stu_name}}</td>
      <td id="colum">{{activity.fields.term}}</td>
      <td id="colum">{{activity.fields.activity_name}}</td>
      <td id="colum">{{activity.fields.activity_num}}</td>
      <td id="colum">
        <label class="radio-inline">
          <input
            type="radio"
            value="不通过"
            @click="hand(0,activity.fields.stu_num,activity.fields.activity_name)"
          /> 不通过
        </label>
        <label class="radio-inline">
          <input
            type="radio"
            value="通过"
            @click="hand(1,activity.fields.stu_num,activity.fields.activity_name)"
          /> 通过
        </label>
        </label>
      </td>
    </Card>
    <h5 class="bg-info" style="padding: 10px;background: none">注:只显示还未审核的活动</h5>
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
      show_students: "",
      activitys:''
    };
  },
  created() {
    this.stu_num = window.sessionStorage.getItem("stu_num");
    // this.getOne();
     this.getAll()
  },
  methods: {
    hand: function(isagree, stu_num,activity_name) {
      let self = this
      self.$axios.get('http://127.0.0.1:8000/api/check_activity',{
        params:{
          stu_num:stu_num,
          activity_name:activity_name,
          isagree:isagree
        }
      }).then(res=>{
        if(res.data.error_num==0)
        {
             console.log(res.data)
             window.location.reload()
        }else{
          alert("审核失败")
        }
        
      })
    },
    getAll: function() {
      let self = this
      self.$axios.get('http://127.0.0.1:8000/api/show_unchecked_activity').then(res=>{
        console.log(res.data.list)
        self.activitys = res.data.list
      })
    },
    getOne: function() {
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
#colum{
  padding-right: 20px;
}
</style>
