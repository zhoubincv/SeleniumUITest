import time
import unittest
import ProjectDirPath
import HTMLTestReportCN


if __name__ == '__main__':
    now_time = time.strftime("%Y%m%d", time.localtime())
    case_path = ProjectDirPath.project_path + "/testcases"
    suite = unittest.TestLoader().discover(case_path)  # unittest.TestLoader().discover(cases_path)
    report_path = ProjectDirPath.project_path + "/reports/自动化测试报告" + now_time + ".html"
    with open(report_path, "wb") as report_file:
        runner = HTMLTestReportCN.HTMLTestRunner(stream=report_file, title="登录自动化测试", description="登录页面的自动化"
                                                                                                  "测试结果")
        runner.run(suite)
