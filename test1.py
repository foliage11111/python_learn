
#coding=GBK
# 1. �������к����ѭ�������������
# 2. ������������0����ӡ�����������Ϣ����ÿ����������Ľ���
# 3. ������������1����ӡ�������д洢�����пγ�ID���γ�����
# 4. ����2����ӡ���γ�����
# 5. ����3����ӡ����Ŀγ���������ID
# 6. ����4��ɾ�����һ���γ̲���ӡ��ʣ��γ�����
# 7. ����5���˳�����
# �������ɳ����õ���֪ʶ�㶼�����п����ҵ������������뼰ʱ���ʣ��������ҵ��չʾ�����ܵ�ʵ���ĵ��С�
# 3.2 ʵ����ʾ
# ����ʹ���������ʾ���д����д��Ҳ���԰����Լ��������ʵ����Ŀ��
# 1. ʹ��while��ʵ�ֽ����������ѭ��
# 2. ʹ��input()��ȡ��������
# 3. ʹ��printf()��ӡ�������
# 4. ʹ��if-elif-else������ͬ����������
# 5. ����γ��б�courses��ÿ��Ԫ�ذ����γ�ID�Ϳγ�����
# 6. ����γ����鲢ʹ�������γ������г�ʼ����ID�����⣺Linux,C++,HTML,HTML5,NodeJS,Shell,Python�ȡ�
# 7. ʹ��for��while���ʿγ��б�ʵ�ִ�ӡ���пγ�ID�����ƣ�����������1
# 8. ʹ���б�����ȡ����ӡcourses���ȣ�ʵ�ֲ�������2
# 9. ʹ��for��while�����γ��б�ʹ���ַ�������������Ŀγ����ƣ�ʵ������3
# 10. ʹ���б���ɾ��Ԫ�أ�ʵ�ֲ�������4
# 11. ����whileѭ����������ʵ��break����ѭ����ʵ�ֲ�������5
#
# ������ŵ��ļ���/home/shiyanlou/Code/shiyanlou_cs421/lab1/�в��ύ��

# 1. �������к����ѭ�������������
    # while ��������ݲ���0-5��ʱ�򣬲�ͣ��Ҫ�����룬����ʾ��Ҫ����0��5
dict_kecheng={1:'Linux',2:'HTML',3:'HTML5',4:'NodeJS',5:'Shell',6:'Python'}

def print_help_info ():
    print "XXXXX�γ̹���ϵͳ"
    print "����1����ӡ�������д洢�����пγ�ID���γ�����"
    print "����2����ӡ���γ�����"
    print "����3����ӡ����Ŀγ���������ID"
    print "����4��ɾ�����һ���γ̲���ӡ��ʣ��γ�����"
    print "����5���˳�����"

def any_key_c():
 print " "
 print " "
 if raw_input("����س���ֵ����........."):
  pass

def case_1():
 #����1����ӡ�������д洢�����пγ�ID���γ�����"
 for k in dict_kecheng :
   print "�γ� "+str(k)+" �ǣ� "+dict_kecheng.get(k)
 print "ѡ���뷵�����˵�"
 any_key_c()

def case_2():
 #����2����ӡ���γ�����
  print "��ǰ�ܹ���" + str(len(dict_kecheng))+" �ſγ̡�"
  print "ѡ���뷵�����˵�"
  any_key_c()

def case_3():
 #����3����ӡ����Ŀγ���������ID
 print "��ѡ��3"
 dic4len={}
 list4dic_len=[]
 max_leeson=0
 if len(dict_kecheng.values()):
    for v in dict_kecheng.values() :
      list4dic_len.append(len(str(v)))
    max_leeson=max(list4dic_len)
    print "�γ����������Ϊ"+str(max_leeson)
    dic4len=zip(list4dic_len,dict_kecheng.values())

    for k,j in dic4len :
      if k==max_leeson :
        print "�γ��������" + str(j)

    #print dic4len
 else :
  print "û��һ���γ�"
 #print dict_kecheng.get(max(dic4len.keys()))
 any_key_c()

def case_4():
 #����4��ɾ�����һ���γ̲���ӡ��ʣ��γ�����
 del_lesson=dict_kecheng.pop(len(dict_kecheng))
 print "��ɾ�����һ���γ�"+str(del_lesson)
 case_2()


def case_5():
 #����5���˳�����
 print "�˳����򣬴����С�������"
 condition_1=False
 any_key_c()
 exit()

def case_wrong(str_in):
 #����������ʾ
 print "�������" +str_in +"������Ч�ַ�"
 any_key_c()


def main():
 #������ѭ����ͨ��if�ж��Ƿ�1-5����ִ�ж�Ӧ�ĳ���
 condition_1 = True
 while condition_1:
   print_help_info()
   str_choice = raw_input("������1-5ѡ��һ��ָ��")
   if str_choice.isdigit():
     int_choice = int(str_choice)
     if int_choice < 6 and int_choice > 0:
       if int_choice==1 :
         case_1()
       if int_choice==2 :
         case_2()
       if int_choice==3:
         case_3()
       if int_choice==4:
         case_4()
       if int_choice==5:
         case_5()

       continue
     else :
           case_wrong (str_choice)
           continue
   else :
     case_wrong (str_choice)
     continue


main()
