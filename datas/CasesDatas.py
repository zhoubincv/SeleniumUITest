import openpyxl
import ProjectDirPath


class CasesDatas:
    def __init__(self):
        self.case_file_path = ProjectDirPath.project_path + "/testfiles/5itestcases.xlsx"
        self.case_file = openpyxl.load_workbook(self.case_file_path)

    def get_cases_value(self, sheet, location) -> str:
        """
        在sheet工作簿中找到location坐标的单元格并返回单元格中的值
        :param sheet: 工作簿名称
        :type sheet:str
        :param location: 单元格坐标
        :type location:str
        :return: 单元格中的值
        """
        case_sheet = self.case_file[sheet]
        value = case_sheet[location]
        return value

    def get_row_values(self, sheet) -> list:
        """
        获取工作簿中行数据的list
        :param sheet: 工作簿名称
        :type sheet:str
        :return: 返回一个list,list中的每个元素都是包含excel文件行数据的list
        """
        values_list = []
        start_row = 2  # 用例excel文件第一行是字段名，测试数据从第2行开始
        case_sheet = self.case_file[sheet]
        while start_row <= case_sheet.max_row:
            value_list = []
            for cell in case_sheet[str(start_row)]:
                value_list.append(cell.value)
            values_list.append(value_list)
            start_row = start_row+1
        return values_list

    def update_cases_value(self, sheet, location, values) -> None:
        """
        修改sheet中location坐标单元格的值
        :param sheet: 工作簿名称
        :type sheet:str
        :param location: 单元格坐标
        :type location:str
        :param values: 写入的值
        :return: None
        """
        case_sheet = self.case_file[sheet]
        case_sheet[location] = values
        self.case_file.save(self.case_file_path)


if __name__ == '__main__':
    pass

