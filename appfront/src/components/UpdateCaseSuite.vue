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
            <label for="suite_name" style="padding-left: 400px;width: 200px">套件名称：</label>
            <el-input name="suite_name" v-model="update_case_list.suite_name" style="width: 300px;"></el-input>
            <br>
            <span v-if="error_message.suite_name !== ''" style="color: red; padding-left: 560px">{{error_message.suite_name}}</span>
            <br>
            <label for="project_name" style="padding-left: 410px">项目名称:</label>
            <el-select v-model="update_case_list.project_name">
              <el-option v-for="pn in sites" :key="pn.project_name" :value="pn.project_name">{{pn.project_name}}
              </el-option>
            </el-select>
            <br>
            <span v-if="error_message.project_name !== ''" style="color: red;padding-left: 470px">{{error_message.project_name}}</span>
            <br>
            <label for="yuming" style="padding-left: 440px">域名:</label>
            <el-select v-model="update_case_list.yuming">
              <el-option v-for="pn in sites" :key="pn.url_name" :value="pn.url_name">{{pn.url_name}}</el-option>
            </el-select>
            <br>
            <span v-if="error_message.yuming !== ''"
                  style="color: red;padding-left: 470px">{{error_message.yuming}}</span>
            <br>
            <label for="headers" style="padding-left: 425px">头文件:</label>
            <el-select v-model="update_case_list.headers">
              <el-option v-for="pn in header" :key="pn" :value="pn"></el-option>
            </el-select>
            <br>
            <span v-if="error_message.headers !== ''"
                  style="color: red;padding-left: 510px">{{error_message.headers}}</span>
            <br>
            <label for="case1" style="padding-left: 425px">用例名:</label>
            <el-select v-model="update_case_list.case">
              <el-option v-for="pn in cases" :key="pn.case_name" :value="pn.case_name"></el-option>
            </el-select>
            <br>
            <span v-if="error_message.case !== ''" style="color: red;padding-left: 470px">{{error_message.case}}</span>
            <br>
            <label for="bz" style="padding-left: 430px">备注：</label>
            <el-input name="bz" v-model="update_case_list.bz" type="textarea" style="width: 300px"></el-input>
            <br>
            <br>
            <el-button value="保存" @click="updateCaseSuite" size="middle" style="margin-left: 500px">保存</el-button>
            <router-link to="/case_suite_list/">
              <el-button value="取消" size="middle" style="margin-left: 60px">取消</el-button>
            </router-link>
          </el-form>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
  export default {
    name: "UpdateCaseSuite",
    data() {
      return {
        update_case_list: [],
        project_name: "",
        url_name: "",
        bz: "",
        case: '',
        cases: [],
        yms: [],
        header: ['{"Content-Type":"application/json"}'],
        headers: "",
        suite_name: "",
        yuming: "",
        sites: [],
        error_message: []

      }
    },
    mounted: function () {
      this.getid();
      this.getCase();
      this.getUrl();
    },
    methods: {
      getid: function () {
        var id = this.$route.params.id;
        this.$axios.get('http://127.0.0.1:8000/update_case_suite/' + id).then((res) => {
          console.log(res.data);
          this.update_case_list = res.data
        }).catch((error) => {
          console.log(error)
        })
      },
      updateCaseSuite: function () {
        var id = this.$route.params.id;
        this.$axios.get('http://127.0.0.1:8000/update_case_suite/' + id).then((res) => {
          console.log(res);
          this.update_case_list = res.data
        }).catch((error) => {
          console.log(error);
        });
        this.$axios.put('http://127.0.0.1:8000/update_case_suite/' + id, {
          project_name: this.update_case_list.project_name,
          yuming: this.update_case_list.yuming,
          bz: this.update_case_list.bz,
          case: this.update_case_list.case,
          case_name: this.update_case_list.case_name,
          headers: this.update_case_list.headers,
          suite_name: this.update_case_list.suite_name

        }).then((res) => {
          console.log(res);
          this.$router.push('/case_suite_list/');
        }).catch((error) => {
          console.log(error)
          this.error_message = error.response.data
        })
      },
      getUrl: function () {
        this.$axios.get("http://127.0.0.1:8000/url_list/").then((res) => {
          console.log(res.data.results);
          this.sites = res.data.results
        })
      },
      getCase: function () {
        this.$axios.get("http://127.0.0.1:8000/case_list/").then((res) => {
          console.log(res.data.results);
          this.cases = res.data.results
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
</style>
