from selenium import webdriver
from common.ReadIni import ReadIni
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import *


class Page:

    def __init__(self, url, driver_type):
        self.driver = self.get_driver(driver_type)
        self.driver.maximize_window()
        self.driver.get(url)
        self.config_file = ReadIni()

    # 根据需要的浏览器类型创建相应的driver
    @staticmethod
    def get_driver(driver_type):

        if driver_type == "chrome":
            return webdriver.Chrome()
        elif driver_type == "firefox":
            return webdriver.Firefox()
        elif driver_type == "edge":
            return webdriver.Edge()
        else:
            return None

    def get_element(self, page_section, sign_option) -> [WebElement, None]:
        """
        根据section和option找到页面元素并返回该元素对象
        :param page_section:配置文件中的section
        :type page_section:str
        :param sign_option:元素标识
        :type sign_option:str
        :return: 返回找到的元素对象，如果没有找到则返回None
        """
        locate_modes = dict(self.config_file.get_config_file().items(page_section))  # 配置文件中定位方式的集合
        if sign_option in locate_modes.keys():
            locate_mode = locate_modes[sign_option]
            try:
                if locate_mode.split("->")[0] == "id":
                    return self.driver.find_element_by_id(locate_mode.split("->")[1])
                elif locate_mode.split("->")[0] == "class":
                    return self.driver.find_element_by_class_name(locate_mode.split("->")[1])
                elif locate_mode.split("->")[0] == "name":
                    return self.driver.find_element_by_name(locate_mode.split("->")[1])
                elif locate_mode.split("->")[0] == "xpath":
                    return self.driver.find_element_by_xpath(locate_mode.split("->")[1])
                elif locate_mode.split("->")[0] == "link":
                    return self.driver.find_element_by_link_text(locate_mode.split("->")[1])
                elif locate_mode.split("->")[0] == "css":
                    return self.driver.find_element_by_css_selector(locate_mode.split("->")[1])
                elif locate_mode.split("->")[0] == "tag":
                    return self.driver.find_element_by_tag_name(locate_mode.split("->")[1])
            except WebDriverException as e:
                print(e)
                return None
            return None

    def close(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()


if __name__ == '__main__':
    pass

