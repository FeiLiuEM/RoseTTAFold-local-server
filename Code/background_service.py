#  code = UTF-8
#author = Liu Fei

import time
import os
import pandas as pd
 
def sleep_time(hour, min, sec):
    return hour * 3600 + min * 60 + sec
 
 
# 时间间隔
#second = sleep_time(0, 0, 2)

'''
while True:
    time.sleep(second)
    print('hello world!')
'''

while True:
    time.sleep(30) #时间间隔，单位是秒，每隔30秒运行一次

    apply=pd.read_csv("RunningData/apply.csv")    # your apply list here 申请文件，所有申请而没有运行的数据都保存在这里
    result=pd.read_csv("RunningData/result.csv")  # your result list here 结果文件

    #判定是否删除运行指示器并且对文件进行压缩处理
    if os.path.exists("RunningData/running/model/model_1.pdb") == True:     # check if it is running
        
        #apply=pd.read_csv("/Users/liufei/Desktop/test.csv")  #申请文件，所有申请而没有运行的数据都保存在这里

        tar_filename=str(apply.values.tolist()[0][1])+".tar.gz"
        resultpath=r"RunningData/"+tar_filename            # your apply file here
        targetpath=r"Result/"+tar_filename    # your result folder here
        newline=apply.values.tolist()[0]
        newline.append(targetpath)
        
        #将新数据合并到结果csv中
        result_list=result.values.tolist()
        result_list.append(newline)
        new_result=pd.DataFrame(result_list,columns=['Date', 'Project_code', 'Amino_acid_sequence', 'Target_path'])
        
        new_result.to_csv("RunningData/result.csv",index=False,sep=',')

        #apply文件的修改及写入
        apply_new=apply.values.tolist()
        apply_new=pd.DataFrame(apply_new[1:],columns=['Date', 'Project_code', 'Amino_acid_sequence'])
        apply_new.to_csv("RunningData/apply.csv",index=False,sep=',')


        #创建结果压缩包，移动到新文件夹中，并且初始化运行文件夹。
        instruction=r"cd RunningData ;tar -zcvf "+tar_filename  +r" /home/math/DATA/RoseTTAFold/running ;mv " + resultpath +r" /media/math/DATA/RESULT/RoseTTAFold"
        os.system(r'cp RunningData/running/model/model_1.crderr.pdb Result/pdb/'+str(apply.values.tolist()[0][1])+'.pdb')
        os.system(instruction)
        os.system(r"rm -rf RunningData/running")
        os.system(r"mkdir RunningData/running")

        apply=pd.read_csv("RunningData/apply.csv")  #申请文件，所有申请而没有运行的数据都保存在这里
        result=pd.read_csv("RunningData/result.csv") #结果文件



#通过申请文件及运行指示器（fa文件）判定是否运行下一个蛋白
    if apply.values.tolist() != []:
        #判定运行文件是否存在
        if os.path.exists("RunningData/running/test.fa") == False:
            RNA = apply.values.tolist()[0][2]
            project_code = apply.values.tolist()[0][0]
            
            #查找这个蛋白以前是否算过
            if result.loc[result['Amino_acid_sequence'] == apply.values.tolist()[0][2]].values.tolist() != []:
                same=result.loc[result['Amino_acid_sequence'] == apply.values.tolist()[0][2]].values.tolist()[0]
                same[0]=apply.values.tolist()[0][0]
                same[1]=apply.values.tolist()[0][1]

               #将新数据合并到结果csv中
                result_list=result.values.tolist()
                result_list.append(same)
                new_result=pd.DataFrame(result_list,columns=['Date', 'Project_code', 'Amino_acid_sequence', 'Target_path'])

                new_result.to_csv("RunningData/result.csv",index=False,sep=',')

                #apply文件的修改及写入
                apply_new=apply.values.tolist()
                apply_new=pd.DataFrame(apply_new[1:],columns=['Date', 'Project_code', 'Amino_acid_sequence'])
                apply_new.to_csv("RunningData/apply.csv",index=False,sep=',')
                
                apply=pd.read_csv("RunningData/apply.csv")  #申请文件，所有申请而没有运行的数据都保存在这里
                result=pd.read_csv("RunningData/result.csv") #结果文件

            
            else:
                fa=[">test |"]
                fa.append(RNA)

                f = open("RunningData/running/test.fa","w",encoding='utf-8')

                for line in fa:
                    f.write(line+'\n')
                f.close()

                os.system("cd Code;./apply.sh")   #运行计算程序
                notification = "正在运行 "+apply.values.tolist()[0][1]
                print(notification)

                apply=pd.read_csv("RunningData/apply.csv")  #申请文件，所有申请而没有运行的数据都保存在这里
                result=pd.read_csv("RunningData/result.csv") #结果文件





'''
apply=pd.read_csv("/Users/liufei/Downloads/apply.csv")
result=pd.read_csv("/Users/liufei/Downloads/result.csv")


result.loc[result['Amino_acid_sequence'] == apply.values.tolist()[0][2]].values.tolist() != []
same=result.loc[result['Amino_acid_sequence'] == apply.values.tolist()[0][2]].values.tolist()[0]
same[0]=apply.values.tolist()[0][0]
same[1]=apply.values.tolist()[0][1]


#将新数据合并到结果csv中
result_list=result.values.tolist()
result_list.append(same)
new_result=pd.DataFrame(result_list,columns=['Date', 'Project_code', 'Amino_acid_sequence', 'Target_path'])
'''
