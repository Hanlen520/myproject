<template>

  <div>
    <el-container style="height: 800px; border: 1px solid #DCDFE6">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1', '3']">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>导航一</template>
            <el-menu-item-group>
              <el-menu-item index="1-1">
                <router-link to="/url_list/" style="text-decoration: none;">
                  <span style="color: #303133">域名</span>
                </router-link>
              </el-menu-item>
              <el-menu-item index="1-2">
                <router-link to="/case_list/" style="text-decoration: none;">
                  测试用例
                </router-link>
              </el-menu-item>
              <el-menu-item index="1-3">
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
                <router-link to="/url_list/" style="text-decoration: none;">
                  <span style="color: black">域名</span>
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
            <router-link to="/add_user/">
              <el-button type="primary" style="color: #fff;
              background-color: #71c7ad;
              border-color: #71c7ad;
              transition: all .2s ease-out;">
                <i class="el-icon-plus"></i>
                新增
              </el-button>
            </router-link>
            <label for="project_name"
                   style="padding-left: 680px;padding-right: 5px">用户搜索</label>
            <el-input name="search_username" placeholder="用户名/邮箱"
                      v-model="username"
                      style="width: 200px;padding-right: 36px"
                      @change="search"></el-input>
            <!--<el-button type="button" value="搜索" icon="el-icon-search" @click="search">搜索</el-button>-->
            <el-button icon="el-icon-search" @click="search">搜索</el-button>
            <br>
            <br>
            <div class="dxy-dividing-line"
                 style="margin-top: 0px; margin-bottom: 24px;"></div>
            <el-button class="small" type="warning" size="small"
                       @click="removeBatch">批量删除
            </el-button>
            <!--<el-dialog-->
            <!--title="提示"-->
            <!--:visible.sync="dialogVisible"-->
            <!--width="30%"-->
            <!--:modal-append-to-body='false'>-->
            <!--<span>确定要删除该数据吗？</span>-->
            <!--<span slot="footer" class="dialog-footer">-->
            <!--<el-button @click="dialogVisible = false">取 消</el-button>-->
            <!--<el-button type="primary" @click="removeBatch(sel)">确 定</el-button>-->
            <!--</span>-->
            <!--</el-dialog>-->
          </el-form>
          <el-table
            :data="sites.slice((currentPage-1)*pageSize,currentPage*pageSize)"
            style="margin-top: 30px" stripe
            border @selection-change="handleSelectionChange"
            :header-cell-style="getRowClass">
            <el-table-column type="selection" width="55"
                             class="selection"></el-table-column>
            <el-table-column prop="user_id" label="编号" width="140" fixed>
            </el-table-column>
            <el-table-column prop="username" label="用户名" width="140" fixed>
            </el-table-column>
            <el-table-column prop="email" label="邮箱" width="120">
            </el-table-column>
            <el-table-column label="操作">
              <template slot-scope="scope">
                <el-button @click="getUpdate(scope.row.user_id)" type="button"
                           style="border: transparent;background-color: transparent">
                  <span style="color: #71c7ad;">编辑</span>
                </el-button>
                <el-button @click="dialogVisible = true" type="button"
                           style="border: transparent;background-color: transparent">
                  <span style="color: #71c7ad;">删除</span>
                </el-button>
                <el-button type="button" @click="reset(scope.row.user_id)"
                           style="border: transparent;background-color: transparent"><span
                  style="color: #71c7ad;">重置密码</span>
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
               @click="getDelete(scope.row.user_id)">确 定</el-button>
  </span>
                </el-dialog>
              </template>


            </el-table-column>
          </el-table>

          <div class="block" style="margin-top: 30px;margin-left: 750px">
            <!--<el-pagination-->
            <!--:page-sizes="[5, 10, 20, 40]"-->
            <!--layout="total, sizes, prev, pager, next, jumper"-->
            <!--:total="totalNum">-->
            <!--</el-pagination>-->
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
    name: "search-url",
    data() {
      return {
        sites: [],
        check_list: [],
        username: "",
        email: "",
        first_name: "",
        last_name: '',
        totalNum: 0,
        dialogVisible: false,
        currentPage: 1,
        pageSize: 10,
        multipleSelection: [],
        list1: [],
        user_id: '',
        delete_status: false


      }

    },


    mounted: function () {
      this.getlist();
    },
    methods: {
      handleSizeChange: function (size) {
        this.pageSize = size;
        console.log(this.pageSize);  //每页下拉显示数据
        let t = (size / 10);
        if (t <= 1) {
          this.$axios.get('http://127.0.0.1:8000/user_list/').then((res) => {
            this.sites = res.data.results;
          })

        }

      },
      handleCurrentChange: function (currentPage) {
        this.currentPage = currentPage;
        console.log(this.currentPage); //点击第几页
        if (this.pageSize === 10 && currentPage <= 10) {
          this.$axios.get('http://127.0.0.1:8000/user_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          })
        }
        if (this.pageSize === 10 && currentPage > 10) {
          let t = parseInt(currentPage / 10) + 1;
          this.$axios.get('http://127.0.0.1:8000/user_list/?page=' + t).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          });
        }
        if (this.pageSize === 20 && currentPage <= 5) {
          this.$axios.get('http://127.0.0.1:8000/user_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          })
        }
        if (this.pageSize === 20 && currentPage > 5) {
          let t = parseInt(currentPage / 5) + 1;
          this.$axios.get('http://127.0.0.1:8000/user_list/?page=' + t).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          });
        }
        if (this.pageSize === 50 && currentPage <= 2) {
          this.$axios.get('http://127.0.0.1:8000/user_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          })
        }
        if (this.pageSize === 50 && currentPage > 2) {
          let t = parseInt(currentPage / 2) + 1;
          this.$axios.get('http://127.0.0.1:8000/user_list/?page=' + t).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          });
        }
        if (this.pageSize === 100 && currentPage <= 1) {
          this.$axios.get('http://127.0.0.1:8000/user_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          })
        }
        if (this.pageSize === 100 && currentPage > 1) {
          let t = parseInt(currentPage / 2) + 1;
          this.$axios.get('http://127.0.0.1:8000/user_list/?page=' + t).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          });
        }
      },
      getlist: function () {
        if (this.currentPage === 1) {
          this.$axios.get('http://127.0.0.1:8000/user_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
            this.totalNum = res.data.count
          }).catch(function (error) {
            console.log(error)
          })
        } else {
          this.$axios.get('http://127.0.0.1:8000/user_list/?page=' + this.currentPage).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;

          })
        }
      },
      search: function () {
        this.$axios.get('http://127.0.0.1:8000/search_user/', {
          params: {
            search: this.username,
          }
        }).then((res) => {
          console.log(res.data.results);
          this.sites = res.data.results
        }).catch(function (error) {
          console.log(error)

        })
      },
      getUpdate: function (row) {
        this.$router.push({path: "/update_user/" + row});
      },
      getDelete: function (row) {
        this.$axios.delete('http://127.0.0.1:8000/delete_user/' + row).then((res) => {
          console.log(res);
          this.dialogVisible = false;
          this.deleteOpen();
          this.getlist()

        }).catch((error) => {
          console.log(error)
        })
      },
      reset: function (row) {
        this.$router.push({path: "/reset_pwd/" + row});
      },
      deleteOpen() {
        this.$notify({
          title: '成功',
          message: '删除用户成功',
          type: 'success'
        });
      },
      removeBatch() {
        this.delete_status = true;
        this.multipleSelection.forEach(i => {
          this.list1.push(i.user_id)
        });
        this.$axios.put('delete_users/', {"ids": this.list1}).then((res) => {
          if (res.data !== '') {
            this.delete_status = false
          }
          // this.deleteOpen();
          this.getlist();
          // this.list1.splice(0, this.list1.length)
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
    background-color: red;
  }

  .dxy-dividing-line {
    height: 0;
    margin: 16px 0;
    border: 1px dashed #f0f2f5;
  }
</style>
