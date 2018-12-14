<template>
  <el-container style="height: 800px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1', '3']">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>导航一</template>
            <el-menu-item-group>
              <el-menu-item index="1-1">
                <router-link to="/url_list/" style="text-decoration: none;">域名</router-link>
              </el-menu-item>
              <el-menu-item index="1-2">
                <router-link to="/case_list/" style="text-decoration: none;">测试用例</router-link>
              </el-menu-item>
              <el-menu-item index="1-2">
                <router-link to="/case_suite_list/" style="text-decoration: none;">测试套件</router-link>
              </el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>
                <router-link to="/url_list/" style="text-decoration: none;">域名</router-link>
              </el-dropdown-item>
              <el-dropdown-item>
                <router-link to="/case_list/" style="text-decoration: none;">测试用例</router-link>
              </el-dropdown-item>
              <el-dropdown-item>
                <router-link to="/case_suite_list/" style="text-decoration: none;">测试套件</router-link>
              </el-dropdown-item>
              <el-dropdown-item>
                <router-link to="/case_suite_list/" style="text-decoration: none;">用户管理</router-link>
              </el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <span>郑兴趣</span>
        </el-header>
  <div class="login-wrap" style="text-align: center">
    <el-form>
      <el-input v-model="sites.username" placeholder="用户名" style="width: 300px"></el-input>
      <br>
      <el-input placeholder="邮箱" v-model="sites.email" style="width: 300px"
                @keyup.enter.native="submitForm('ruleForm')"></el-input>
      <br>
      <div class="login-btn">
        <el-button type="primary" style="width: 300px" @click="submitForm()">确定</el-button>
      </div>
      <div>
        <router-link to="/user_list/">返回</router-link>
      </div>
    </el-form>
  </div>
      </el-container>
  </el-container>
</template>

<script>
  export default {
    data: function () {
      return {
        username: '',
        password: '',
        email: '',
        first_name: '',
        last_name: '',
        sites: [],
      }
    },
    mounted: function () {
      this.getuser();
    },
    methods: {
      getuser: function () {
        var id = this.$route.params.id;
        this.$axios.get("update_user/" + id).then((res) => {
          console.log(res);
          this.sites = res.data
        }).catch((err) => {
          console.log(err)
        })
      },
      submitForm() {
        var id = this.$route.params.id;
        this.$axios.put('update_user/' + id, {
          username: this.sites.username,
          password: this.sites.password,
          email: this.sites.email
        }).then((res) => {
          this.$router.push('/user_list/');
        }).catch((err) => {
          console.log(err);
        });
      }
    }
  }
</script>

<style scoped>
  .login-wrap {
    position: relative;
    width: 100%;
    height: 100%;
  }

  .ms-title {
    position: absolute;
    top: 50%;
    width: 100%;
    margin-top: -230px;
    text-align: center;
    font-size: 30px;
    color: #fff;

  }

  .ms-login {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 300px;
    height: 160px;
    margin: -150px 0 0 -190px;
    padding: 40px;
    border-radius: 5px;
    background: #fff;
  }

  .login-btn {
    text-align: center;
  }

  .login-btn button {
    width: 100%;
    height: 36px;
  }
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }

  .el-aside {
    color: #333;
  }

  .el-input {
    width: 300px;
  }
</style>
