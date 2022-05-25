import numpy as np
#Task 1
#Viết một chương trình cho phép người dùng nhập tên của một tệp và truy cập đọc.
filename=input('Enter the file name: ')
try:
    f_handle=open(filename,'r')
    print('Successfully opened ',filename)
except:
    print('File cannot be found.')
#Task 2
#Báo cáo tổng số dòng dữ liệu được lưu trữ trong tệp.
lines=f_handle.readlines()
print('Total lines of data:',len(lines))
#Báo cáo tổng số dòng dữ liệu không hợp lệ trong tệp. Nếu một dòng dữ liệu không hợp lệ, bạn nên báo cáo cho người dùng bằng cách in ra một thông báo lỗi.
valid_lines=0
invalid_lines=0
valid_lst=[]
for line in lines:
    line=line.rstrip()
    lst=line.split(',')
    if len(lst)==26:
        if lst[0][0]=='N':
            if lst[0][1:].isnumeric():
                if len(lst[0][1:])==8:
                    valid_lines=valid_lines+1
                    valid_lst.append(line)
                else:
                    invalid_array=np.array(line)
                    print('Invalid line of data: N# is invalid\n',invalid_array)
                    invalid_lines=invalid_lines+1
            else:
                invalid_array=np.array(line)
                print('Invalid line of data: N# is invalid\n',invalid_array)
                invalid_lines=invalid_lines+1
        else:
            invalid_array=np.array(line)
            print('Invalid line of data: N# is invalid\n',invalid_array)
            invalid_lines=invalid_lines+1
    else:
        invalid_array=np.array(line)
        print('Invalid line of data: does not contain exactly 26 values\n',invalid_array)
        invalid_lines=invalid_lines+1
print('Total valid lines:',valid_lines)
print('Total invalid lines:',invalid_lines)
#Task 3
#Viết một chương trình để chấm điểm các bài thi cho một phần nhất định.
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_lst=answer_key.split(',')
diem_thi={}
for valid_line in valid_lst:
    valid_line=valid_line.rstrip()
    valid_line=valid_line.split(',')
    diem_thi[valid_line[0]]=0
    for i in range(25):
        if valid_line[i+1]=='':
            diem_thi[valid_line[0]]=diem_thi[valid_line[0]]
        elif valid_line[i+1]==answer_lst[i]:
            diem_thi[valid_line[0]]=diem_thi[valid_line[0]]+4
        else:
            diem_thi[valid_line[0]]=diem_thi[valid_line[0]]-1
        i=i+1
diem_lst=list(diem_thi.values())
#Đếm số lượng học sinh đạt điểm cao (>80).
diem_cao=0
for i in diem_lst:
    if i>80:
        diem_cao+=1
print('Total student of high score:',diem_cao)
#Điểm trung bình.
diem_tb=sum(diem_lst)/len(diem_lst)
print('Mean (average) score:',diem_tb)
#Điểm cao nhất.
diem_cao_nhat=max(diem_lst)
print('Highest score:',diem_cao_nhat)
#Điểm thấp nhất.
diem_thap_nhat=min(diem_lst)
print('Lowest score:',diem_thap_nhat)
#Miền giá trị của điểm (cao nhất trừ thấp nhất).
print('Range of scores:',diem_cao_nhat - diem_thap_nhat)
diem_lst.sort()
#Giá trị trung vị
if len(diem_lst)%2==0:
    gia_tri_trung_vi=(diem_lst[int(len(diem_lst)/2)-1]+diem_lst[int(len(diem_lst)/2)])/2
else:
    gia_tri_trung_vi=diem_lst[len(diem_lst)//2]
print('Median score:',gia_tri_trung_vi)
#Trả về các câu hỏi bị học sinh bỏ qua nhiều nhất theo thứ tự: số thứ tự câu hỏi - số lượng học sinh bỏ qua -  tỉ lệ bị bỏ qua
dict_boqua={}
for valid_line in valid_lst:
    valid_line=valid_line.rstrip()
    valid_line=valid_line.split(',')
    for j in range(26):
        if valid_line[j]=='':
            dict_boqua[j]=dict_boqua.get(j,0)+1
        j+=1
for key,value in dict_boqua.items():
    if dict_boqua[key]==max(list(dict_boqua.values())):
        print('Question that most people skip:',key,'-',dict_boqua[key],'-',round(dict_boqua[key]/valid_lines,3))
#Trả về các câu hỏi bị học sinh sai qua nhiều nhất theo thứ tự: số thứ tự câu hỏi - số lượng học sinh trả lời sai - tỉ lệ bị sai
dict_sai={}
for valid_line in valid_lst:
    valid_line=valid_line.rstrip()
    valid_line=valid_line.split(',')
    for x in range(1,26):
        if valid_line[x] != answer_lst[x-1] and valid_line[x] != '':
            dict_sai[x]=dict_sai.get(x,0)+1
        x+=1
for key,value in dict_sai.items():
    if dict_sai[key]==max(list(dict_sai.values())):
        print('Question that most people answer incorrectly:',key,'-',dict_sai[key],'-',round(dict_sai[key]/valid_lines,3))
f_handle.close()
#Task 4:
#Tạo một tệp “kết quả” chứa các kết quả chi tiết cho từng học sinh trong lớp, mỗi dòng của tệp này phải chứa số ID của học sinh, dấu phẩy và sau đó là điểm của họ.
newfile='class'+filename[5]+'_grades.txt'
keys_lst=list(diem_thi.keys())
with open (newfile,'w') as nf_handle:
    for k in keys_lst:
        nf_handle.write(k+','+str(diem_thi[k])+'\n')
