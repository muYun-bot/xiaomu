from receive import rev_msg
from sendMessage import send_msg

id_list = []

while True:
    rev = rev_msg()
    id = rev['message_id']
#收到信息超过50条则更新消息列表(解决重复接收消息的问题)
    if (len(id_list) >= 50):
        id_list = []
    print(id_list)
    # print(time1==time2)
    if id not in id_list:
        id_list.append(id)
 #       print(rev)
    else:
        continue

    if rev["message_type"] == "message":
        # print(rev) #需要功能自己DIY
        if rev["message_type"] == "private":  # 私聊
            if rev['raw_message'] == '在吗':
                qq = rev['sender']['user_id']
                send_msg({'msg_type': 'private', 'number': qq, 'msg': '我在'})
        elif rev["message_type"] == "group":  # 群聊
            group = rev['group_id']
            if "[CQ:at,qq=2192892649]" in rev["raw_message"]:
                if rev['raw_message'].split(' ')[1] == '在吗':
                    qq = rev['sender']['user_id']
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:poke,qq={}]'.format(qq)})
        else:
            continue
    else:  # rev["post_type"]=="meta_event":
        continue
