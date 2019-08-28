from Page.Page import Page
import time


class RegisterPage(Page):

    def __init__(self, url, driver_type):
        super().__init__(url, driver_type)
        self.REGISTER_SECTION = "RegisterElements"
        self.USER_NAME_OPTION = "username"
        self.USER_EMAIL_OPTION = "useremail"
        self.PASSWORD_OPTION = "password"
        self.CPATCHA_CODE_OPTION = "captchacode"
        self.REGISTER_BUTTON_OPTION = "registerbutton"
        self.USER_TERM_OPTION = "usertermcheckbox"
        self.ERROR_ELEMS_OPTION = ["captchacodeerror", "usernameerror", "useremailerror", "passworderror",
                                   "usertermerror"]

    def regist(self, user_email, user_name, pass_word, captcha_code, userterms_selected=False) -> list:
        """
        输入用户信息点击登录后找到错误提示元素的提示文字信息并以list形式返回这些文字信息的集合
        :param user_email: 用户邮箱
        :type user_email:str
        :param user_name: 用户名
        :type user_name:str
        :param pass_word: 密码
        :type pass_word:str
        :param captcha_code: 验证码
        :type captcha_code:str
        :param userterms_selected: 是否勾选用户协议,默认不勾选
        :type userterms_selected:bool
        :return: 返回包含错误提示元素的提示文字list
        """
        # 输入注册信息
        self.get_element(self.REGISTER_SECTION, self.USER_EMAIL_OPTION).send_keys(user_email)
        self.get_element(self.REGISTER_SECTION, self.USER_NAME_OPTION).send_keys(user_name)
        self.get_element(self.REGISTER_SECTION, self.PASSWORD_OPTION).send_keys(pass_word)
        self.get_element(self.REGISTER_SECTION, self.CPATCHA_CODE_OPTION).send_keys(captcha_code)
        # 如果userterms_selected为True则勾选用户协议，否则不勾选
        userterm_element = self.get_element(self.REGISTER_SECTION, self.USER_TERM_OPTION)
        if userterms_selected:
            if userterm_element.is_selected():
                pass
            else:
                userterm_element.click()
        else:
            if userterm_element.is_selected():
                userterm_element.click()
            else:
                pass
        # 点击登录按钮
        time.sleep(2)
        self.get_element(self.REGISTER_SECTION, self.REGISTER_BUTTON_OPTION).click()
        # 找到页面上的错误提示信息并全部放入error_texts
        error_texts = []
        for option in self.ERROR_ELEMS_OPTION:
            error_element = self.get_element(self.REGISTER_SECTION, option)
            if error_element is not None:
                error_texts.append(error_element.text)
        return error_texts


if __name__ == '__main__':
    pass
