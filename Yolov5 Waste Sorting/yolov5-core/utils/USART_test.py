import serial
import time
# COMX，启用几号串口
portx = "COM3"
# 波特率
bps=115200
# 发送阻塞延时
timex = 0

# 发送调用函数
def Usart_send(send_msg):
    ser = serial.Serial(portx, bps, timeout=timex)
    ser.write(send_msg.encode("gbk"))
# 串口接收函数
def Usart_receive():
    ser = serial.Serial(portx, bps, timeout=timex)
    receive_msg = ser.readline().decode("gbk")
    return receive_msg

a = '(20,50,50),zzf'
b = 0
if __name__ == "__main__":
    # 不要改
    ser = serial.Serial(portx, bps, timeout=timex)
    # 下面的ser.write('a'.encode("gbk"))单引号位置为发送信息
    # result = ser.write(a.encode("gbk"))


    # 串口接收用法示例
    Usart_send("aaabx")
    # 以下为USART接收部分
    while(1):
        # b = ser.readline().decode("gbk")

        # 串口接收用法示例
        b = Usart_receive()

        if(b != ''):
            b = int(b)
        else: b = 0
        if b == 1:
            print('received 1')
        elif b == 2:
            print('received 2')
        else:
            if(b != 0):
                print('I do not know what the hell things transit on uart')