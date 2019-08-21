import time

print('小精灵：您好，欢迎古灵阁，请问您需要帮助吗？需要or不需要？')
time.sleep(1)
QS1 = input('你:')
if QS1 == '需要':
    print('小精灵：请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询')
    time.sleep(1)
    QS2 = input('你:')
    if QS2 == '2':
        print('小精灵：金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        time.sleep(1)
        print('小精灵：请问您需要兑换多少金加隆呢？')
        time.sleep(1)
        QS3 = input('你:')
        time.sleep(1)
        print('小精灵：好的，我知道了，您需要兑换' + str(QS3) + '金加隆。')
        time.sleep(1)
        print('小精灵：那么，您需要付给我' + str(int(QS3) * 51.3) + '人民币。')
    elif QS2 == '1':
        print('小精灵：请去存取款窗口')
    else:
        print('小精灵：请去咨询窗口')
else:
    print('好的，再见。')
