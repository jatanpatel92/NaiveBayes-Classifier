from __future__ import division
import sys


train_file = sys.argv[1]
test_file = sys.argv[2]
attributes = 0
instance = -1
data = []
count_class_0 = 0
count_class_1 = 0
p_class_0 = 0
p_class_1 = 0
joint_distribution = []

for line in open(train_file,'r'):
    row = line.split()
    if instance==-1:
        attributes = len(row)-1
    else:
        data.append(row)
    instance = instance + 1;

print(data)
print(attributes)
print(instance)

for i in range(len(data)):
    if(data[i][attributes]=="0"):
        count_class_0+=1
    else:
        count_class_1+=1

p_class_0 = count_class_0/instance
p_class_1 = count_class_1/instance
print(count_class_0)
print(count_class_1)
print(p_class_0)
print(p_class_1)

for i in range(attributes):
    joint_distribution.append([[0,0],[0,0]])

print(attributes)

for i in range(instance):
    for j in range(attributes):
        if (data[i][j]=="0" and data[i][attributes]=="0"):
            joint_distribution[j][0][0]+=1
        elif (data[i][j]=="1" and data[i][attributes]=="1"):
            joint_distribution[j][1][1]+=1
        elif (data[i][j]=="0" and data[i][attributes]=="1"):
            joint_distribution[j][0][1]+=1
        elif (data[i][j]=="1" and data[i][attributes]=="0"):
            joint_distribution[j][1][0]+=1
        
print(joint_distribution)

for i in range(len(joint_distribution)):
    joint_distribution[i][0][0]=joint_distribution[i][0][0]/count_class_0
    joint_distribution[i][1][0]=joint_distribution[i][1][0]/count_class_0
    joint_distribution[i][0][1]=joint_distribution[i][0][1]/count_class_1
    joint_distribution[i][1][1]=joint_distribution[i][1][1]/count_class_1

print(joint_distribution)

def test_nb_model(file):
    accuracy = 0
    count = -1
    test_data = []
    for line in open(file,'r'):
        row = line.split()
        if count>-1:
            test_data.append(row)
        count+=1
    print("Number of instances = "+str(count))
    for i in range(len(test_data)):
        p_of_0 = p_class_0
        p_of_1 = p_class_1
        for j in range(len(test_data[i])-1):
            if (test_data[i][j]=="0"):
                p_of_0 = p_of_0 * joint_distribution[j][0][0]
                p_of_1 = p_of_1 * joint_distribution[j][1][0]
            elif (test_data[i][j]=="1"):
                p_of_0 = p_of_0 * joint_distribution[j][0][1]
                p_of_1 = p_of_1 * joint_distribution[j][1][1]
        if (p_of_0>p_of_1):
            classification = "0"
        else:
            classification = "1"
        if(classification==test_data[i][attributes]):
            accuracy+=1
    accuracy = (accuracy/count)*100
    print("Accuracy: "+str(accuracy)+"%")

print("Accuracy on training dataset")
test_nb_model(train_file)
print("Accuracy on testing dataset")
test_nb_model(test_file)