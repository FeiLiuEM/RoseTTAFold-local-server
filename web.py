from os import X_OK
import remi.gui as gui
from remi import start, App
import random
import re
import time
import pandas as pd

name=''
s = 'acdefghiklmnopqrstuvwyACDEFGHIKLMNOPQRSTUVWX'

# 匹配不是中文、大小写、数字的其他字符
cop = re.compile("[^a^c-i^k-n^p-t^v^w^y^A^C-I^K-N^P-T^V^W^Y]")

#r = random.choice(s) #获取随机字母
#for i in range(10):
#    name = name + random.choice(s)  #生成十位的随机字母


class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.VBox(width=720, height=650)
        #container.css_border_style=NoneType
        self.lbl_1 = gui.Label('浙医二院急诊科通用计算平台——RoseTTAFold蛋白质结构预测系统')
        self.lbl = gui.Label('请在下方文本框中输入氨基酸序列(氨基酸为单字母缩写形式)：')
        self.lbl2 = gui.Label('您的项目代号为：')
        self.lbl3 = gui.Label('')
        self.input=gui.Input(input_type='', default_value='',width=200, height=100)
        self.input2=gui.Input(input_type='', default_value='')
        self.bt = gui.Button('提交')
        self.bt2 = gui.Button('查询结果')
        self.download=gui.FileDownloader(text='',filename='/media/math/DATA/RESULT/CIRP.tar.gz')   #your result folder here
        #self.lbl4 = gui.Label('引用文献：Fei Liu et.al, A chronotherapeutics-applicable multi-target therapeutics based on AI: the example of therapeutic hypothermia, Briefings in Bioinformatics, DOI:10.1093/bib/bbac365.')
        self.lbl4 = gui.Label('引用文献：Liu F, Jiang X, Yang J, Tao J, Zhang M. A chronotherapeutics-applicable multi-target therapeutics based on AI: Example of therapeutic hypothermia. Brief Bioinform (2022).')
        self.lbl5 = gui.Label('M. Baek, et al., Accurate prediction of protein structures and interactions using a three-track neural network, Science (2021). ')
        self.lbl6 = gui.Label('I.R. Humphreys, J. Pei, M. Baek, A. Krishnakumar, et al, Computed structures of core eukaryotic protein complexes, Science (2021).')

        # setting the listener for the onclick event of the buttons
        self.bt.onclick.do(self.on_button_pressed)
        self.bt2.onclick.do(self.on_button_pressed2)
        #self.input.onclick.do(self.on_button_pressed3)
        #self.input.ontouchenter(self.on_button_pressed)

        # appending a widget to another
        container.append(self.lbl_1)
        container.append(self.lbl)
        container.append(self.input)
        container.append(self.bt)
        container.append(self.lbl2)
        container.append(self.input2)
        container.append(self.bt2)
        container.append(self.lbl3)
        container.append(self.download)   
        container.append(self.lbl4)
        container.append(self.lbl5)
        container.append(self.lbl6)
        
        # returning the root widget
        return container

    # listener function
    def on_button_pressed(self, widget):
        x=self.input.get_value()
        
        x_char = cop.sub('', x)
        x_char=x_char.upper()

        if len(x_char) < 20:
            widget.set_text('请输入正确的氨基酸序列!')
            self.input.set_value('')
        else:
            widget.set_text('氨基酸序列已成功提交！')
            self.input.set_value(x_char)
            name = random.choice(s) + random.choice(s) + random.choice(s) + random.choice(s) + random.choice(s) + random.choice(s) + random.choice(s) + random.choice(s) + random.choice(s) + random.choice(s)  #生成十位的随机字母
            self.input2.set_value(name)
            ticks = time.time()
            newline=[]
            newline.append(ticks)
            newline.append(name)
            newline.append(x_char)
            apply=pd.read_csv("/home/math/DATA/RoseTTAFold/apply.csv")                        # your query list here
            apply_list=apply.values.tolist()
            apply_list.append(newline)
            apply_new=pd.DataFrame(apply_list,columns=['Date', 'Project_code', 'Amino_acid_sequence'])

            apply_new.to_csv("/home/math/DATA/RoseTTAFold/apply.csv",index=False,sep=',')     # your query list here

            #fa=[">test |"]
            #fa.append(x_char)
            #写入fa文件
            #f = open("/home/math/DATA/RoseTTAFold/running/test.fa","w",encoding='utf-8')

            #for line in code0:
            #    f.write(line+'\n')
            #f.close()


    def on_button_pressed2(self, widget):
        x2=self.input2.get_value()
        #self.lbl.set_text(x.values)
        if x2 == '':
            self.input2.set_value('请输入项目代号')
        #self.input.set_value(x)
        #self.lbl3.set_text('计算仍在进行中，请稍后。')
        #self.lbl3.set_text('计算已完成，请点击下方按钮下载数据：')
        else:
            result=pd.read_csv("/home/math/DATA/RoseTTAFold/result.csv")                # your result list here
            if result.loc[result['Project_code'] == x2].values.tolist() != []:
                self.download._filename=result.loc[result['Project_code'] == x2].values.tolist()[0][3]
                self.lbl3.set_text('已完成计算，点击下方按钮下载结果，文件名正常情况下与项目名一致，文件名与项目名不一致时，说明此氨基酸链此前计算过。')
                self.download.set_text('点击下载运算结果')
            else:
                self.lbl3.set_text('任务正在计算中，请稍等。')


#    def on_button_pressed3(self, widget):
#        self.input.set_value('')        

# starts the web server
start(MyApp, address='0.0.0.0', port=46429, multiple_instance=True, enable_file_cache=True, update_interval=0.1, start_browser=False)
#start(MyApp, address='192.168.31.32', port=46429, multiple_instance=True, enable_file_cache=True, update_interval=0.1, start_browser=False)
#start(MyApp, address='10.241.1.3', port=46429, multiple_instance=True, enable_file_cache=True, update_interval=0.1, start_browser=False)

