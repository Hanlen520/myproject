<template>
  <div>
    <el-container style="height: 800px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1', '3']">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>导航一</template>
            <el-menu-item-group>
              <el-menu-item index="1-1">
                <router-link to="/url_list/" style="text-decoration: none;">域名
                </router-link>
              </el-menu-item>
              <el-menu-item index="1-2">
                <router-link to="/case_list/" style="text-decoration: none;">
                  测试用例
                </router-link>
              </el-menu-item>
              <el-menu-item index="1-2">
                <router-link to="/case_suite_list/"
                             style="text-decoration: none;">测试套件
                </router-link>
              </el-menu-item>
              <el-menu-item index="1-4">
                <router-link to="/user_list/" style="text-decoration: none;">
                  用户管理
                </router-link>
              </el-menu-item>
              <el-menu-item index="1-5">
              </el-menu-item>
              <el-menu-item index="1-6">
              </el-menu-item>
              <el-menu-item index="1-7">
              </el-menu-item>
              <el-menu-item index="1-8">
              </el-menu-item>
              <el-menu-item index="1-9">
              </el-menu-item>
              <el-menu-item index="1-10">
              </el-menu-item>
              <el-menu-item index="1-11">
              </el-menu-item>
              <el-menu-item index="1-12">
              </el-menu-item>
              <el-menu-item index="1-13">
              </el-menu-item>
              <el-menu-item index="1-14">
              </el-menu-item>
              <el-menu-item index="1-15">
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
              <el-dropdown-item>
                <router-link to="/user_list/" style="text-decoration: none;">
                  用户管理
                </router-link>
              </el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <span>郑兴趣</span>
        </el-header>
        <el-main>
          <el-form>
            <router-link to="/add_cases/">
              <el-button type="primary" style="color: #fff;
              background-color: #71c7ad;
              border-color: #71c7ad;
              transition: all .2s ease-out;">
                <i class="el-icon-plus"></i>
                新增
              </el-button>
            </router-link>
            <label style="padding-left: 370px;padding-right: 5px">用例搜索</label>
            <el-input name="search_case" placeholder="项目名称/用例名/URL/"
                      v-model="search_data"
                      style="width: 200px;padding-right: 36px"
                      @change="search1"></el-input>
            <label style="padding-right: 5px"> 请求类型 </label>
            <el-select v-model="value" placeholder="请选择"
                       style="padding-right: 36px" @change="search1">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>

            <el-button value="搜索" @click="search1" icon="el-icon-search">搜索
            </el-button>
            <br>
            <br>
            <div class="dxy-dividing-line"
                 style="margin-top: 0px; margin-bottom: 24px;"></div>
            <el-button class="small" type="warning" size="small"
                       @click="removeBatch" :loading=delete_status>批量删除
            </el-button>
            <!--<el-dialog-->
            <!--title="提示"-->
            <!--:visible.sync="dialogVisible"-->
            <!--width="30%"-->
            <!--:modal-append-to-body='false'>-->
            <!--<span>确定要删除该数据吗？</span>-->
            <!--<span slot="footer" class="dialog-footer">-->
            <!--<el-button @click="dialogVisible = false">取 消</el-button>-->
            <!--<el-button type="primary" @click="removeBatch()">确 定</el-button>-->
            <!--</span>-->
            <!--</el-dialog>-->
          </el-form>

          <el-table :data="sites" style="margin-top: 30px" stripe border
                    @selection-change="handleSelectionChange"
                    :header-cell-style="getRowClass">
            <el-table-column type="selection" width="55"
                             class="selection"></el-table-column>
            <el-table-column prop="case_id" label="编号" width="140" fixed>
            </el-table-column>
            <el-table-column prop="case_name" label="用例名">
            </el-table-column>
            <!--<el-table-column prop="project_name" label="项目名称" width="120">-->
            <!--</el-table-column>-->
            <el-table-column prop="url" label="域名地址">
            </el-table-column>
            <el-table-column prop="request_data" label="请求数据"
                             :show-overflow-tooltip="true">
            </el-table-column>
            <el-table-column prop="request_type" label="请求类型">
            </el-table-column>
            <el-table-column prop="invoking_login" label="是否调用登陆">
            </el-table-column>
            <el-table-column prop="case_bz" label="备注">
            </el-table-column>
            <el-table-column prop="expected_result" label="预期结果"
                             :show-overflow-tooltip="true">
            </el-table-column>
            <el-table-column label="操作">
              <template slot-scope="scope">
                <!--<el-button size="mini" type="primary" @click="getUpdate(scope.row.case_id)">编辑</el-button>-->
                <!--&lt;!&ndash;<el-button size="mini" type="danger" @click="getDelete(scope.row.case_id)">删除</el-button>&ndash;&gt;-->
                <!--<el-button type="danger" @click="dialogVisible = true" size="mini">删除</el-button>-->
                <el-button @click="getUpdate(scope.row.case_id)" type="button"
                           style="border: transparent;background-color: transparent;width: 20px">
                  <span style="color: #71c7ad;">编辑</span>
                </el-button>
                <el-button @click="dialogVisible = true" type="button"
                           style="border: transparent;background-color: transparent;width: 20px">
                  <span style="color: #71c7ad;">删除</span>
                </el-button>
                <el-dialog
                  title="提示"
                  :visible.sync="dialogVisible"
                  width="30%"
                  :modal-append-to-body='false'>
                  <span>确定要删除该数据吗？</span>
                  <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible = false">取 消</el-button>
    <el-button type="primary"
               @click="getDelete(scope.row.case_id)">确 定</el-button>
  </span>
                </el-dialog>
              </template>

            </el-table-column>
          </el-table>
          <div class="block" style="margin-top: 30px;margin-left: 750px">
            <el-pagination
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
              :current-page="currentPage"
              :page-sizes="[10, 20, 50, 100]"
              :page-size="10"
              layout="total, sizes, prev, pager, next, jumper"
              :total="totalNum">
            </el-pagination>

          </div>
        </el-main>
      </el-container>
    </el-container>


  </div>
</template>

<script>
  export default {
    name: "case",
    data() {
      return {
        sites: [],
        check_list: [],
        search_data: "",
        case_name: "",
        project_name: "",
        request_type: "",
        url: "",
        case_bz: "",
        options: [{
          // value: '选项1',
          value: '全部'
        }, {
          // value: '选项2',
          value: 'get'
        }, {
          // value: '选项3',
          value: 'post'
        }, {
          // value: '选项4',
          value: 'put'
        }, {
          // value: '选项5',
          value: 'delete'
        }],
        value: '全部',
        totalNum: 0,
        dialogVisible: false,
        currentPage: 1,
        pageSize: 10,
        multipleSelection: [],
        list1: [],
        yz: false,
        delete_status: false,
        expected_result: ''

      }
    },

    mounted: function () {
      this.getlist1();

    },
    methods: {
      handleSizeChange: function (size) {
        this.pageSize = size;
        console.log(this.pageSize);  //每页下拉显示数据
        let t = (size / 10);
        if (t <= 1) {
          this.$axios.get('case_list/').then((res) => {
            this.sites = res.data.results;
          })

        }

      },
      handleCurrentChange: function (currentPage) {
        this.currentPage = currentPage;
        console.log(this.currentPage); //点击第几页
        if (this.pageSize === 10 && currentPage <= 10) {
          this.$axios.get('case_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          })
        }
        if (this.pageSize === 10 && currentPage > 10) {
          let t = parseInt(currentPage / 10) + 1;
          this.$axios.get('case_list/?page=' + t).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          });
        }
        if (this.pageSize === 20 && currentPage <= 5) {
          this.$axios.get('case_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          })
        }
        if (this.pageSize === 20 && currentPage > 5) {
          let t = parseInt(currentPage / 5) + 1;
          this.$axios.get('case_list/?page=' + t).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          });
        }
        if (this.pageSize === 50 && currentPage <= 2) {
          this.$axios.get('case_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          })
        }
        if (this.pageSize === 50 && currentPage > 2) {
          let t = parseInt(currentPage / 2) + 1;
          this.$axios.get('case_list/?page=' + t).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          });
        }
        if (this.pageSize === 100 && currentPage <= 1) {
          this.$axios.get('case_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          })
        }
        if (this.pageSize === 100 && currentPage > 1) {
          let t = parseInt(currentPage / 2) + 1;
          this.$axios.get('case_list/?page=' + t).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          });
        }
      },
      getlist1: function () {
        this.$axios.get('case_list/').then((res) => {
          console.log(res.data.results);
          this.sites = res.data.results;
          this.totalNum = res.data.count
        }).catch(function (error) {
          console.log(error)
        })
      },
      search1: function () {
        if (this.search_data === '' && this.value !== '') {
          this.param = {
            search: this.value,
          }
        }
        if (this.search_data !== '' && this.value === '全部') {
          this.param = {
            search: this.search_data,
          }

        }
        if (this.value === '全部' && this.search_data === '') {
          this.param = {
            search: '',
          }
        }

        this.$axios.get('search_case/', {
          params: this.param
        }).then((res) => {
          console.log(res.data.results);
          this.sites = res.data.results
        }).catch(function (error) {
          console.log(error)

        })
      }
      ,
      getUpdate: function (row) {
        this.$router.push({path: "/update_case" + '/' + row});
      }
      ,
      getDelete: function (row) {
        this.$axios.delete('delete_case/' + row).then((res) => {
          console.log(res);
          this.dialogVisible = false;
          this.deleteOpen();
          this.getlist1()
        }).catch((error) => {
          console.log(error)
        })
      },
      deleteOpen() {
        this.$notify({
          title: '成功',
          message: '删除测试用例成功',
          type: 'success'
        });
      },
      removeBatch() {
        this.delete_status = true;
        this.multipleSelection.forEach(i => {
          this.list1.push(i.case_id)
        });
        this.$axios.put('delete_cases/', {"ids": this.list1}).then((res) => {
          if (res.data !== '') {
            this.delete_status = false
          }
          console.log(res);
          this.getlist1()
          this.list1.splice(0, this.list1.length)
        }).catch((err) => {
          console.log(err)
        })
      },
      handleSelectionChange(val) {
        this.multipleSelection = val;
      },
      getRowClass({row, column, rowIndex, columnIndex}) {
        if (rowIndex == 0) {
          return 'background: #F0FFFF'
        } else {
          return ''
        }
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

  .dxy-dividing-line {
    height: 0;
    margin: 16px 0;
    border: 1px dashed #f0f2f5;
  }

</style>
