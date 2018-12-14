<template>
  <div>
    <el-container style="height: 800px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1', '3']">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>导航一</template>
            <el-menu-item-group>
              <el-dropdown-item>
                <router-link to="/url_list/" style="text-decoration: none;">域名</router-link>
              </el-dropdown-item>
              <el-dropdown-item>
                <router-link to="/case_list/" style="text-decoration: none;">测试用例</router-link>
              </el-dropdown-item>
              <el-dropdown-item>
                <router-link to="/case_suite_list/" style="text-decoration: none;">测试套件</router-link>
              </el-dropdown-item>
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
            </el-dropdown-menu>
          </el-dropdown>
          <span>王小虎</span>
        </el-header>
        <el-main>
          <el-form>
            <label for="project_name" style="padding-left: 400px">项目名称：</label>
            <el-input name="project_name" v-model="project_name"
                      style="width: 300px;"></el-input><br>
            <span v-if="error_message.project_name !== ''" style="color: red; padding-left: 550px">{{error_message.project_name}}</span>

            <br>
            <label for="url_name" style="padding-left: 430px">域名：</label>
            <el-input name="url_name" v-model="url_name" style="width: 300px"></el-input>
            <br>
            <span v-if="error_message.url_name !== ''" style="color: red; padding-left: 550px">{{error_message.url_name}}</span>
            <br>
            <label for="bz" style="padding-left: 430px;">备注：</label>
            <el-input name="bz" v-model="bz" type="textarea" style="width: 300px"></el-input>
            <br>
            <br>
            <el-button type="button" value="保存" @click="addurls" size="middle" style="margin-left: 500px">保存</el-button>
            <router-link to="/url_list/">
              <el-button value="取消" size="middle" style="margin-left: 80px">取消</el-button>
            </router-link>
          </el-form>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
  export default {
    name: "addurl",
    data() {
      return {
        project_name: "",
        url_name: "",
        bz: "",
        error_message: []
      }
    },
    mounted: function () {
      // this.addurls();
    },
    methods: {
      addurls: function () {

        this.$axios.post('http://127.0.0.1:8000/add_url/', {
          project_name: this.project_name,
          url_name: this.url_name,
          bz: this.bz
        }).then((response) => {
          if (response.status === 201) {
            console.log(response);
            this.addOpen()
            this.$router.push('/url_list/')

           }


        }).catch((error) => {
          console.log(error);
          this.error_message = error.response.data

        })

      },
      addOpen() {
        this.$notify({
          title: '成功',
          message: '新增域名成功',
          type: 'success'
        });
      },

    }
  }
</script>

<style scoped>
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }

  .el-aside {
    color: #333;
  }
</style>
