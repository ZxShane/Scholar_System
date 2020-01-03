<template>
  <div id="app">
    <div class="layout">
      <Layout>
        <Header>
          <p style="color:white;text-align:center;font-size:25px;">奖学金管理系统</p>
        </Header>
        <Layout>
          <Sider hide-trigger :style="{background: '#fff'}">
            <Menu active-name="1-2" theme="light" width="auto" :open-names="['1']">
             <router-link to ="info"> <MenuItem name="4-1"><Icon type="ios-analytics"></Icon>主页</MenuItem></router-link>
             <router-link to ="allgrade"> <MenuItem name="4-2"><Icon type="ios-analytics"></Icon>成绩排名</MenuItem></router-link>
              <Submenu name="1">
                <template slot="title">
                  <Icon type="ios-navigate"></Icon>成绩管理
                </template>
                <router-link to ="addmajorgrade"><MenuItem name="1-1">添加专业成绩</MenuItem></router-link>
                <router-link to ="CreateNewcase"><MenuItem name="1-2">提交发展性测评</MenuItem></router-link>
                <router-link to ="evaluate"><MenuItem name="1-3">班级互评</MenuItem></router-link>
              </Submenu>
              <Submenu name="2">
                <template slot="title">
                  <Icon type="ios-keypad"></Icon>奖学金管理
                </template>
                <router-link to ="apply_scholar"><MenuItem name="2-1">申请奖学金</MenuItem></router-link>
                <router-link to ="showallscholar"><MenuItem name="2-2">查看奖学金</MenuItem></router-link>
              </Submenu>
              <Submenu name="3">
                <template slot="title">
                  <Icon type="ios-analytics"></Icon>后台管理
                </template>
                <router-link to ="checkactivity"><MenuItem name="3-1">审核发展性测评</MenuItem></router-link>
                <router-link to ="checkscholar"><MenuItem name="3-2">审核奖学金</MenuItem></router-link>
              </Submenu>
            </Menu>
          </Sider>
          <Layout :style="{padding: '0 24px 24px',overflow:'scroll'}">
            <Content :style="{padding: '24px', minHeight: '650px', background: '#fff'}">
              <router-view />
            </Content>
          </Layout>
        </Layout>
      </Layout>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style scoped>
.layout {
  border: 1px solid #d7dde4;
  background: #f5f7f9;
  position: relative;
  border-radius: 4px;
  overflow: hidden;
  height: 800px;
}
.layout-logo {
  width: 100px;
  height: 30px;
  background: #5b6270;
  border-radius: 3px;
  float: left;
  position: relative;
  top: 15px;
  left: 20px;
}
.layout-nav {
  width: 420px;
  margin: 0 auto;
  margin-right: 20px;
}
a{
  color:#5b6270;
}
</style>

