<template>
  <div>
    <el-container style="height: 800px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1', '10']">
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
        <el-main>
          <el-form>
            <!--<label for="project_name">项目名称：</label><input name="project_name" v-model="update_list.project_name"-->
            <!--value="update_list.project_name" type="text"><br>-->
            <label for="case_name" style="padding-left: 450px">用例名称</label>
            <el-input name="case_name" v-model="update_list.case_name"></el-input>
            <br>
            <span v-if="error_message.case_name !== ''" style="color: red;padding-left: 600px">{{error_message.case_name}}</span>
            <br>
            <label for="project_name" style="padding-left: 450px">项目名称</label>
            <el-select v-model="update_list.project_name">
              <el-option v-for="item in sites"
                         :key="item.project_name"
                         :label="item.project_name"
                         :value="item.project_name">{{item.project_name}}
              </el-option>
            </el-select>
            <br>
            <span v-if="error_message.project_name !== ''" style="color: red;padding-left: 600px">{{error_message.project_name}}</span>
            <br>
            <label for="request_data" style="padding-left: 450px">请求数据</label>
            <el-input name="request_data" v-model="update_list.request_data"></el-input>
            <br>
            <span v-if="error_message.request_data !== ''" style="color: red;padding-left: 600px;">{{error_message.request_data}}</span>
            <br>
            <label for="request_type" style="padding-left: 450px">请求类型</label>
            <el-select name="request_type" v-model="update_list.request_type">
              <el-option v-for="i in request_type"
                         :key="i"
                         :label="i"
                         :value="i">{{i}}
              </el-option>
            </el-select>
            <br>
            <span v-if="error_message.request_type !== ''" style="color: red;padding-left: 600px">{{error_message.request_type}}</span>
            <br>
            <label for="url" style="padding-left: 482px">URL</label>
            <el-input name="url_name" v-model="update_list.url" type="text"></el-input>
            <br>
            <span v-if="error_message.url !== ''" style="color: red;padding-left: 600px">{{error_message.url}}</span>
            <br>
            <label for="case_bz" style="padding-left: 465px">备注：</label>
            <el-input name="case_bz" v-model="update_list.case_bz" type="textarea" style="width:300px"></el-input>
            <br>
            <br>
            <el-button value="保存" @click="updatecase" style="margin-left: 540px">保存</el-button>
            <router-link to="/case_list/">
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
        case_bz: '',
        url: '',
        request_data: '',
        request_type: ['get', 'post', 'put', 'delete'],
        case_name: '',
        select1: '',
        sites: [],
        case_id: '',
        error_message: []
      }
    },

    mounted: function () {
      this.getid();
      this.getlist();

    },
    methods: {
      getid: function () {
        var id = this.$route.params.id;
        this.$axios.get('http://127.0.0.1:8000/update_case/' + id).then((res) => {
          console.log(res.data);
          this.update_list = res.data
        }).catch((error) => {
          console.log(error)
        })
      },
      updatecase: function () {
        var id = this.$route.params.id;
        this.$axios.get('http://127.0.0.1:8000/update_case/' + id).then((res) => {
          console.log(res.data);
          this.update_list = res.data
        }).catch((error) => {
          console.log(error)
        });
        this.$axios.put('http://127.0.0.1:8000/update_case/' + id, {
          project_name: this.update_list.project_name,
          url: this.update_list.url,
          case_bz: this.update_list.case_bz,
          request_data: this.update_list.request_data,
          request_type: this.update_list.request_type,
          case_name: this.update_list.case_name

        }).then((res) => {
          console.log(res);
          this.$router.push('/case_list/');
        }).catch((error) => {
          console.log(error)
          this.error_message = error.response.data
        })
      },
      getlist: function () {
        this.$axios.get('http://127.0.0.1:8000/url_list/').then((res) => {
          console.log(res.data.results);
          this.sites = res.data.results;
        }).catch(function (error) {
          console.log(error)
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
