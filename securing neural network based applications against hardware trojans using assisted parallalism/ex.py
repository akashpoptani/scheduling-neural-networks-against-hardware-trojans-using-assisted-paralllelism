networknum=int(input('enter the network number(1-resnet18,2-alexnet,3-vgg16,4-squeezenet1_0,5-googlenet,6-mobilenet_v2)'))
frequency_l_core= int(input('frequency of Little core?(1-200Hz,2-600Hz,3-1000Hz,4-1400Hz)'))
frequency_b_core= int(input('frequency of Big core?(1-800Hz,2-1200Hz,3-1600Hz,4-2000Hz)'))

nnetwork= networknum*4 -5
line_number_lcore= nnetwork + frequency_l_core
line_number_bcore= nnetwork + frequency_b_core + 6*4 
#print(nnetwork,line_number_lcore, line_number_bcore)

with open("nn_layerruntimes.csv","r") as file:
    data = file.readlines()
file.close()

data_l= data[line_number_lcore].split(',')
nlayers=int(data_l[3])
thgc = [None] * nlayers
for i in range(0,nlayers):
    thgc[i]=int(data_l[i+4])

data_h= data[line_number_bcore].split(',')
tpc = [None] * nlayers
for i in range(0,nlayers):
    tpc[i]=int(data_h[i+4])
print(nlayers,thgc,tpc)

with open("network_shapes.csv","r") as file:
    data = file.readlines()
file.close()

data_comm= data[networknum-1].split(',')
#print (data_comm)

with open("socket_times.csv","r") as file:
    data= file.readlines()
file.close()

lno= nnetwork + frequency_b_core + 2

comm=data[lno].split(',')
#print(comm)

tcomm = [None] * nlayers

for i in range(0,nlayers):
    num=4*1024
    c=2
    while (1<2):
        if(int(data_comm[i+2])<num):
            tcomm[i]=comm[c]
            #print(data_comm[i+2], num, comm[c])
            break
        else:
            num= num*2
            c=c+1
print(tcomm)