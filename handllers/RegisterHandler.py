from Page.Page import Page


class RegisterHandler:

    def __init__(self, url, driver_type):
        self.page = Page(url, driver_type)
        self.REGISTER_SECTION = "RegisterElements"
        self.USER_NAME_OPTION = "username"
        self.USER_EMAIL_OPTION = "useremail"
        self.PASSWORD_OPTION = "password"
        self.CPATCHA_CODE_OPTION = "captchacode"
        self.REGISTER_BUTTON_OPTION = "registerbutton"
        self.USER_TERM_OPTION = "usertermcheckbox"
        self.ERROR_ELEMS_OPTION = ["captchacodeerror", "usernameerror", "useremailerror", "passworderror",
                                   "usertermerror"]

    def regist(self, user_email, user_name, pass_word, captcha_code, userterm_selected=False) -> list:
        """
        输入用户信息点击登录后找到错误提示信息的元素并以dict形式返回这些元素的集合
        :param user_email: 用户邮箱
        :type user_email:str
        :param user_name: 用户名
        :type user_name:str
        :param pass_word: 密码
        :type pass_word:str
        :param captcha_code: 验证码
        :type captcha_code:str
        :param userterm_selected: 是否勾选用户协议,默认不勾选
        :type userterm_selected:bool
        :return: 返回包含错误提示对象标识，错误提示对象的dict
        """
        # 输入注册信息
        self.page.get_element(self.REGISTER_SECTION, self.USER_EMAIL_OPTION).send_keys(user_email)
        self.page.get_element(self.REGISTER_SECTION, self.USER_NAME_OPTION).send_keys(user_name)
        self.page.get_element(self.REGISTER_SECTION, self.PASSWORD_OPTION).send_keys(pass_word)
        self.page.get_element(self.REGISTER_SECTION, self.CPATCHA_CODE_OPTION).send_keys(captcha_code)
        # 如果userterm_selected为True则勾选用户协议，否则不勾选
        if userterm_selected:
            if self.page.get_element(self.REGISTER_SECTION, self.USER_TERM_OPTION).is_selected():
                pass
            else:
                self.page.get_element(self.REGISTER_SECTION, self.USER_TERM_OPTION).click()
        else:
            if self.page.get_element(self.REGISTER_SECTION, self.USER_TERM_OPTION).is_selected():
                self.page.get_element(self.REGISTER_SECTION, self.USER_TERM_OPTION).click()
            else:
                pass
        # 点击登录按钮
        self.page.get_element(self.REGISTER_SECTION, self.REGISTER_BUTTON_OPTION).click()
        # 找到页面上的错误提示信息并全部放入error_texts
        error_texts = []
        for option in self.ERROR_ELEMS_OPTION:
            error_element = self.page.get_element(self.REGISTER_SECTION, option)
            if error_element is not None:
                error_texts.append(error_element.text)
        return error_texts

    def close(self):
        self.page.close()


if __name__ == '__main__':
    pass
