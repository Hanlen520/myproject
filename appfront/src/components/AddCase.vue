<template>
  <div>
    <el-container style="height: 800px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1', '3']">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>导航一</template>
            <el-menu-item-group>
              <el-dropdown-item>
                <router-link to="/url_list/" style="text-decoration: none;">域名
                </router-link>
              </el-dropdown-item>
              <el-dropdown-item>
                <router-link to="/case_list/" style="text-decoration: none;">
                  测试用例
                </router-link>
              </el-dropdown-item>
              <el-dropdown-item>
                <router-link to="/case_suite_list/"
                             style="text-decoration: none;">测试套件
                </router-link>
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
                <router-link to="/url_list/" style="text-decoration: none;">域名
                </router-link>
              </el-dropdown-item>
              <el-dropdown-item>
                <router-link to="/case_list/" style="text-decoration: none;">
                  测试用例
                </router-link>
              </el-dropdown-item>
              <el-dropdown-item>
                <router-link to="/case_suite_list/"
                             style="text-decoration: none;">测试套件
                </router-link>
              </el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <span>王小虎</span>
        </el-header>
        <el-main>
          <el-form>
            <label for="case_name" style="padding-left: 450px">用例名称</label>
            <el-input name="case_name" v-model="case_name"
                      style="width: 300px;"></el-input>
            <br>
            <span v-if="error_message.case_name !== ''"
                  style="color: red;padding-left: 600px">{{error_message.case_name}}</span>
            <br>
            <label for="project_name" style="padding-left: 450px">项目名称</label>
            <el-select v-model="project_name">
              <el-option
                v-for="item in sites"
                :key="item.project_name"
                :label="item.label"
                :value="item.project_name">
              </el-option>
            </el-select>
            <br>
            <span v-if="error_message.project_name !== ''"
                  style="color: red;padding-left: 600px">{{error_message.project_name}}</span>
            <br>
            <label for="request_data" style="padding-left: 450px">请求数据</label>
            <el-input name="request_data" v-model="request_data"
                      style="width: 300px"></el-input>
            <br>
            <span v-if="error_message.request_data !== ''"
                  style="color: red;padding-left: 600px;">{{error_message.request_data}}</span>
            <br>
            <label for="request_type" style="padding-left: 450px">请求类型</label>
            <el-select v-model="value" placeholder="请选择">
              <el-option
                v-for="item in request_type"
                :key="item"
                :label="item"
                :value="item">{{item}}
              </el-option>
              <br>
            </el-select>
            <br>
            <span v-if="error_message.request_type !== ''"
                  style="color: red;padding-left: 600px">{{error_message.request_type}}</span>
            <br>
            <label for="url" style="padding-left: 465px">URL：</label>
            <el-input name="url" v-model="url" style="width: 300px"></el-input>
            <br>
            <span v-if="error_message.url !== ''"
                  style="color: red;padding-left: 600px">{{error_message.url}}</span>
            <br>
            <label for="" style="padding-left: 465px">备注：</label>
            <el-input name="case_bz" v-model="case_bz" type="textarea"
                      style="width:300px;"></el-input>
            <br>
            <br>
            <label for="invoking_login" style="padding-left: 370px">是否调用登陆接口：</label>
            <el-input name="invoking_login" v-model="invoking_login"
                      type="textarea"
                      style="width:300px;"></el-input>
            <br>
            <br>
            <label for="expected_result"
                   style="padding-left: 430px">预期结果：</label>
            <el-select v-model="assert_value">
              <el-option v-for="i in assert_type"
                         :key="i"
                         :label="i"
                         :value="i">{{i}}
              </el-option>
            </el-select>
            <br>
            <br>
            <el-input name="expected_result" v-model="expected_result"
                      type="textarea"
                      style="width:300px;padding-left: 510px"></el-input>
            <br>
            <br>
            <el-button value="保存" @click="addcase" style="margin-left: 520px">
              保存
            </el-button>
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
    name: "addcase",
    data() {
      return {
        project_name: '',
        case_bz: "",
        url: "",
        request_data: "",
        request_type: ['get', 'post', 'put', 'delete'],
        case_name: "",
        sites: [],
        selected: 'get',
        expected_result: '',
        assert_type: ['==', '!=', 'in', 'not in'],
        assert_value: '==',
        invoking_login: "",
        options: [
          {
            value: '选项2',
            label: 'get'
          }, {
            value: '选项3',
            label: 'post'
          }, {
            value: '选项4',
            label: 'put'
          }, {
            value: '选项5',
            label: 'delete'
          }],
        value: 'get',
        error_message: []

      }
    },
    created: function () {
      this.getlist();
    },
    methods: {
      addcase: function () {

        this.$axios.post('add_cases/', {
          project_name: this.project_name,
          url: this.url,
          case_bz: this.case_bz,
          case_name: this.case_name,
          request_data: this.request_data,
          request_type: this.value,
          expected_result: this.expected_result,
          assert_value: this.assert_value,
          invoking_login: this.invoking_login

        }).then((response) => {
          if (response.status === 201) {
            console.log(response);
            this.addOpen();
            this.$router.push('/case_list/')
          }


        }).catch((error) => {
          console.log(error);
          this.error_message = error.response.data
        })

      },
      getlist: function () {
        this.$axios.get('url_list/').then((res) => {
          console.log(res.data.results);
          this.sites = res.data.results;
        }).catch(function (error) {
          console.log(error)
        })
      },
      addOpen() {
        this.$notify({
          title: '成功',
          message: '新增用例成功',
          type: 'success'
        });
      },
    }
  }
</script>
.el-header {
background-color: #B3C0D1;
color: #333;
line-height: 60px;
}

.el-aside {
color: #333;
}
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
