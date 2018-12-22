<template>
  <div>
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
            </el-dropdown-menu>
          </el-dropdown>
          <span>郑兴趣</span>
        </el-header>
        <el-main>
          <el-form>
            <label for="project_name" style="padding-left: 400px">项目名称：</label>
            <el-input name="project_name" v-model="update_list.project_name"
                      value="update_list.project_name"></el-input>
            <br>
            <span v-if="error_message.project_name !== ''" style="color: red; padding-left: 550px">{{error_message.project_name}}</span>

            <br>
            <label for="url_name" style="padding-left: 430px">域名：</label>
            <el-input name="url_name" v-model="update_list.url_name"></el-input>
            <br>
            <span v-if="error_message.url_name !== ''" style="color: red; padding-left: 550px">{{error_message.url_name}}</span>
            <br>
            <label for="bz" style="padding-left: 435px">备注：</label>
            <el-input name="bz" v-model="update_list.bz" type="textarea" style="width: 300px;"></el-input>
            <br>
            <br>
            <el-button type="button" value="保存" @click="updateurl" style="margin-left: 500px">保存</el-button>
            <router-link to="/url_list/">
              <el-button value="取消" style="margin-left: 80px">取消</el-button>
            </router-link>
          </el-form>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
  export default {
    name: "update_url",
    data() {
      return {
        update_list: [],
        project_name: '',
        bz: '',
        url_name: '',
        error_message: []
      }
    },

    mounted: function () {
      this.getid();

    },
    methods: {
      getid: function () {
        var id = this.$route.params.id;
        this.$axios.get('update_url/' + id).then((res) => {
          console.log(res.data)
          this.update_list = res.data
        }).catch((error) => {
          console.log(error)
        })
      },
      updateurl: function () {
        var id = this.$route.params.id;
        this.$axios.put('update_url/' + id, {
          project_name: this.update_list.project_name,
          url_name: this.update_list.url_name, bz: this.update_list.bz
        }).then((res) => {
          console.log(res);
          this.$router.push('/url_list/');
        }).catch((error) => {
          console.log(error);
          this.error_message = error.response.data
        })
      }
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

  .el-input {
    width: 300px;
  }
</style>
