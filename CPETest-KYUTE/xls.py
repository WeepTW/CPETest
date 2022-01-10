#import excel
import pandas as pd
#參考網路上登入註冊的範例，所以我就直接用成array，下面是老師跟學生的登入註冊判斷
#https://tomyhhc.com/%E5%AF%A6%E7%94%A8%E9%9B%BB%E8%85%A6%E6%89%8B%E6%A9%9F%E6%8A%80%E5%B7%A7/%E3%80%90python-%E5%9F%BA%E7%A4%8E%E7%B3%BB%E5%88%97%E3%80%91%E5%B8%B3%E8%99%9F%E7%99%BB%E5%85%A5%E8%A8%BB%E5%86%8A%E7%B2%BE%E9%97%A2%E8%A7%A3%E6%9E%90%EF%BD%9C%E9%99%84%E5%9C%96%E8%A7%A3%E8%AA%AA/
class xls:
    def __init__(stu,tech):
        self.peopleArray = []
        tech.peopleArray = []
        pass

    def stu_register(self,  stuacc_num, stuacc_password):
        for person in self.peopleArray:
            if person[0] == stuacc_num:
                print("帳號已被註冊!請選擇其他帳號")
                return False
        
        print("註冊成功")
        self.peopleArray.append([stu_accnum, stu_password , stu_name , stu_class, stu_ID])
        return True

    def tech_register(self,  tech_num, tech_password):
        for person in self.peopleArray:
            if person[0] == tech_num:
                print("帳號已被註冊!請選擇其他帳號")
                return False
        
        print("註冊成功")
        self.peopleArray.append([stu_accnum, stu_password , stu_name , stu_class, stu_ID])
        return True

    def stu_login(self, stu_accnum, stu_password):
        for person in self.peopleArray:
            print (person)
            if person[0] == stu_accnum:
                if person[1] == stu_password:
                    print("登入成功")
                else:
                    print("密碼錯誤")
            else:
                print("此帳號不存在。請回首頁註冊")

    def tech_login(self, tech_num, tech_password):
        for person in self.peopleArray:
            print (person)
            if person[0] == tech_num:
                if person[1] == tech_password:
                    print("登入成功")
                else:
                    print("密碼錯誤")
            else:
                print("此帳號不存在。請回首頁註冊")

    def sheetName(is_log):
        if is_log == 1:
            return "學生"
        if is_log == 2:
            return "管理者"
        else:
            return ""
