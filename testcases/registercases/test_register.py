import unittest
from datas.CasesDatas import CasesDatas
import ddt
from handllers.RegisterPage import RegisterPage
from common.LogUtil import log_recorder


CASE_SHEET = "registercases"
case_datas = CasesDatas().get_row_values(CASE_SHEET)
@ddt.ddt
class TestRegister(unittest.TestCase):

    def setUp(self) -> None:
        log_recorder.get_logger().debug("----------------------> 测试开始 <----------------------")
        self.register_handler = RegisterPage("http://www.5itest.cn/register", "chrome")

    @ddt.data(*case_datas)  # 参数化注册信息
    @ddt.unpack
    def test_register(self, *case_data):
        user_email, user_name, pass_word, captcha_code, assert_code = case_data
        error_texts = self.register_handler.regist(user_email, user_name, pass_word, captcha_code)
        self.assertIn(assert_code, error_texts)

    def tearDown(self) -> None:
        self.register_handler.close()
        log_recorder.get_logger().debug("----------------------> 测试结束 <----------------------")
        log_recorder.close()


if __name__ == '__main__':
    unittest.main()
