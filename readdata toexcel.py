from bs4 import BeautifulSoup
import pandas as pd

def parse_html(file_path):
   
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
 
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 查找所有的项目信息容器
    projects = soup.find_all('ul', class_='table-row row')
    
    data_list = []
    

    for project in projects:
        data = {
            'Approval Year': project.find('div', class_='col-con', text='Approval Year').find_next('div').text.strip(),
            'Economy': project.find('div', class_='con-title', text='Economy').find_next('div').text.strip(),
            'Sector': project.find('div', class_='con-title', text='Sector').find_next('div').text.strip(),
            'Financing Type': project.find('div', class_='con-title', text='Financing Type').find_next('div').text.strip(),
            'Project Name': project.find('div', class_='con-title', text='Name').find_next('div').text.strip(),
            'Financing Amount': project.find('div', class_='con-title', text='Financing Amount').find_next('div').text.strip(),
            'Status': project.find('div', class_='con-title', text='Status').find_next('div').text.strip(),
        }
        data_list.append(data)
    
    return data_list

def save_to_excel(data, filename):
 
    df = pd.DataFrame(data)

    df.to_excel(filename, index=False)

# 我的路径
file_path = r'E:\1901\1.html'#填你自己的html路径
project_data = parse_html(file_path)

# 保存到Excel文件
save_to_excel(project_data, r'E:\1901\ProjectData.xlsx')#填你的输出文件文件名和路径
