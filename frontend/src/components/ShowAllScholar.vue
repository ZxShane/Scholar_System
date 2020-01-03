<template>
<div>
    <h2 align="center">奖学金审核情况</h2>
    <Table stripe :columns="columns1" :data="data1"></Table>
    </div>
</template>
<script>
    export default {
        data () {
            return {
                columns1: [
                    {
                        title: '学号',
                        key: 'stu_num'
                    },
                    {
                        title: '申请奖学金',
                        key: 'scholar_name'
                    },
                    {
                        title: '结果',
                        key: 'isagree'
                    }
                ],
                data1: [
                ],
                onestudent:{
                  stu_num :'',
                  scholar_name:'',
                  isagree:''
                }
            }
        },
        created(){
            this.getallscholar()
        },
        methods:{
          getallscholar:function(){
            let self = this
            this.$axios.get('http://127.0.0.1:8000/api/show_all_scholar').then(res=>{
              console.log(res.data.list)
              for(var i = 0;i<res.data.list.length;i++)
              {
                if(res.data.list[i].fields.ischeck){
                  if(res.data.list[i].fields.isagree){
                    res.data.list[i].fields.isagree = "通过"
                  }else{
                    res.data.list[i].fields.isagree = "未通过"
                  }
                }else{
                  res.data.list[i].fields.isagree = "未审核"
                }
                self.onestudent.stu_num = res.data.list[i].pk
                self.onestudent.scholar_name = res.data.list[i].fields.scholar_name
                self.onestudent.isagree = res.data.list[i].fields.isagree
                self.data1.push(self.onestudent)
              }
              
            })
          }
        }
    }
</script>
