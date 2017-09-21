#coding = utf-8

"""
*****************************************信控自动化各种策略定义参数配置文件*****************************************
----说明：
--------1.policy_id纯5位数字
-----------停机类从10000-19999
-----------开机类从20000-29999
-----------拆机从30000-39999
--------2.每新增一个必须有remark字段说明
"""

"""
===========欠费关联停机策略===========
"""
OTHER_TRADE_OWNFEESTOP_A = {
	"para1":"8800|8900|8910|8920",
	"para2":"40|50",
	"policy_id":"10000",
	"remark":"欠费关联停机策略A"
}

OTHER_TRADE_OWNFEESTOP_B = {
	"para1":"8920",
	"para2":"50",
	"policy_id":"10001",
	"remark":"欠费关联停机策略B"
}

OTHER_TRADE_OWNFEESTOP_C = {
	"para1":"20",
	"para2":"50",
	"policy_id":"10002",
	"remark":"欠费关联停机策略C"
}