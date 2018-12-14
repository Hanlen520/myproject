<template>
  <div class="login-wrap" style="text-align: center">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="0px" class="demo-ruleForm">
      <el-form-item prop="username">
        <el-input v-model="ruleForm.username" placeholder="用户名" style="width: 300px"></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input type="password" placeholder="密码" v-model="ruleForm.password" style="width: 300px"
                  @keyup.enter.native="submitForm('ruleForm')"></el-input>
      </el-form-item>
      <el-form-item prop="email">
        <el-input placeholder="邮箱" v-model="ruleForm.email" style="width: 300px"
                  @keyup.enter.native="submitForm('ruleForm')"></el-input>
      </el-form-item>


      <div class="login-btn">
        <el-button type="primary" style="width: 300px" @click="submitForm('ruleForm')">确定</el-button>
      </div>
      <div><router-link to="/user_list/">返回</router-link></div>
    </el-form>
  </div>
</template>

<script>
  export default {
    data: function () {
      return {
        ruleForm: {
          username: '',
          password: '',
          email: '',
          first_name: '',
          last_name: ''
        },
        rules: {
          username: [
            {required: true, message: '请输入用户名', trigger: 'blur'}
          ],
          password: [
            {required: true, message: '请输入密码', trigger: 'blur'}
          ]
        },
        state: false
      }
    },
    methods: {
      submitForm(formName) {
        var _this = this;
        _this.state = false;
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.$axios.post('register/', _this.ruleForm).then((res) => {
              this.$router.push('/user_list/');
            }).catch((err) => {
              _this.state = true;
              console.log(err);
              _this.addOpen();
            });
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
            addOpen() {
        this.$notify({
          title: '成功',
          message: '新增用户成功',
          type: 'success'
        });
      },
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
</style>
