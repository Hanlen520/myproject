<template>
    <div>
      <el-container style="height: 800px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1', '4']">
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
      </el-container>
    </div>
</template>

<script>
    export default {
        name: "common"
    }
</script>

<style scoped>

</style>
