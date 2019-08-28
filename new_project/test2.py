from qqbot import _bot as bot

def sendMsgToBuddy(msg,buddyList,bot):
    pass

def main(bot):
    buddyMsg= '你好'
    with open('./qq.txt','r') as fr:
        qqBuddy = fr.readline().strip()
    
    qqBuddyList = qqBuddy.split(',')
    sendMsgToBuddy(buddyMsg,qqBuddyList,bot)

if __name__=='__main__':
    bot.Login(['-q','1511325099'])
    main(bot)