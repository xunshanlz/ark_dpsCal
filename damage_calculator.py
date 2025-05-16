from skill_calculate import *


def calculate_dps(hero_name, skill_name, buff_levels):
    """
    计算指定干员在不同加成量下指定技能的DPS、基础数据
    参数
    :param hero_name: 干员名称
    :param skill_name: 技能名称
    :param buff_levels: 加成
    :return: 技能dps
    """
    # 定义技能对应的DPS计算函数映射
    skill_dps_functions = {
        '风笛': {
            "迅捷打击γ": calculate_fengdi_1_dps,
            "高效冲击": calculate_fengdi_2_dps,
            "闭膛连发": calculate_fengdi_3_dps
        },
        '伊内丝': {
            "淬影突袭": calculate_yineisi_1_dps,
            "暗夜无明": calculate_yineisi_2_dps,
            "独影归途": calculate_yineisi_3_dps
        },
        '锏': {
            "纯粹的武力": calculate_jian_1_dps,
            "无声的嘲笑": calculate_jian_2_dps,
            "归于宁静": calculate_jian_3_dps
        },
        '银灰': {
            "强力击·γ型": calculate_yinhui_1_dps,
            "雪境生存法则": calculate_yinhui_2_dps,
            "真银斩": calculate_yinhui_3_dps
        },
        '仇白': {
            '留羽': calculate_qiubai_1_dps,
            '承影': calculate_qiubai_2_dps,
            '问雪': calculate_qiubai_3_dps
        },
        '玛恩纳': {
            "未声张的怒火": calculate_maenna_1_dps,
            "未宽解的悲哀": calculate_maenna_2_dps,
            "未照耀的荣光": calculate_maenna_3_dps
        },
        '乌尔比安': {
            "必须促成的接触": calculate_wuerbian_1_dps,
            "必须维系的界限": calculate_wuerbian_2_dps,
            "必须开辟的道路": calculate_wuerbian_3_dps,
        },
        '赫德雷': {
            "重锋不熄": calculate_hedelei_1_dps,
            "余烬重荷": calculate_hedelei_2_dps,
            "死境硝烟": calculate_hedelei_3_dps
        },
        '佩佩': {
            '盖戳': calculate_peipei_1_dps,
            '阻遏混乱锤': calculate_peipei_2_dps,
            '时光震荡': calculate_peipei_3_dps,
        },
        '史尔特尔': {
            '烈焰魔剑': calculate_shierteer_1_dps,
            '熔核巨影': calculate_shierteer_2_dps,
            '黄昏': calculate_shierteer_3_dps
        },
        '维娜': {
            "重铸晖光": calculate_weina_1_dps,
            "进赴故土": calculate_weina_2_dps,
            "俱以我之名": calculate_weina_3_dps
        },
        '耀骑士临光': {
            "灿焰长刃": calculate_yaoqishilinguang_1_dps,
            "逐夜烁光": calculate_yaoqishilinguang_2_dps,
            "耀阳颔首": calculate_yaoqishilinguang_3_dps
        },
        '号角': {
            '照明榴弹': calculate_haojiao_1_dps,
            '暴风号令': calculate_haojiao_2_dps,
            '终极防线': calculate_haojiao_3_dps
        },
        '黍': {
            '化被草木': calculate_shu_1_dps,
            '嘉禾盈仓': calculate_shu_2_dps,
            '离离枯荣': calculate_shu_3_dps
        },
        '浊心斯卡蒂': {
            '同归殊途之吟': calculate_zhuoxinsikadi_1_dps,
            '同葬无光之愿': calculate_zhuoxinsikadi_2_dps,
            '潮涌,潮枯': calculate_zhuoxinsikadi_3_dps
        },
        '魔王': {
            '往昔萦绕身旁': calculate_mowang_1_dps,
            '明日渺远不及': calculate_mowang_2_dps,
            '编织重构现世': calculate_mowang_3_dps

        },
        '维什戴尔': {
            '定点清算': calculate_weishidaier_1_dps,
            '饱和复仇': calculate_weishidaier_2_dps,
            '爆裂黎明': calculate_weishidaier_3_dps
        },
        '莱伊': {
            '脱身矢': calculate_laiyi_1_dps,
            '广域警觉': calculate_laiyi_2_dps,
            '得见光芒': calculate_laiyi_3_dps
        },
        '蕾缪安': {
            '重逢问候': calculate_leimiuan_1_dps,
            '归乡邀约': calculate_leimiuan_2_dps,
            '礼炮·强制追思': calculate_leimiuan_3_dps
        },
        '空弦': {
            '箭矢·散逸': calculate_kongxian_1_dps,
            '箭矢·追猎': calculate_kongxian_2_dps,
            '箭矢·暴风': calculate_kongxian_3_dps
        },
        '纯烬艾雅法拉': {
            '无声润物': calculate_chunjinaiyafala_1_dps,
            '云霭荫佑': calculate_chunjinaiyafala_2_dps,
            '火山回想': calculate_chunjinaiyafala_3_dps
        },
        '焰影苇草': {
            '迅捷打击·γ型': calculate_yanyingweicao_1_dps,
            '枯荣共息': calculate_yanyingweicao_2_dps,
            '生命火种': calculate_yanyingweicao_3_dps
        },
        'Mon3tr': {
            '策略:超压链接': calculate_Mon3tr_1_dps,
            '策略:超负荷': calculate_Mon3tr_2_dps,
            '策略:熔毁': calculate_Mon3tr_3_dps,
        },
        '荒芜拉普兰德': {
            '慵怠者悲鸣': calculate_huangwulapulande_1_dps,
            '逐猎狂飙': calculate_huangwulapulande_2_dps,
            '终幕·浩劫': calculate_huangwulapulande_3_dps,
        },
        '逻各斯': {
            '殁亡': calculate_luogesi_1_dps,
            '提喻': calculate_luogesi_2_dps,
            '延异视阈': calculate_luogesi_3_dps
        },
        '澄闪': {
            '火花四溅': calculate_chengshan_1_dps,
            '电流翻涌': calculate_chengshan_2_dps,
            '澄净闪耀': calculate_chengshan_3_dps
        },
        '艾拉': {
            '眩目阻滞': calculate_aila_1_dps,
            '震荡坚守': calculate_aila_2_dps,
            '博萨克风暴': calculate_aila_3_dps
        },
        '新约能天使': {
            '天空大扫除': calculate_xinyuenengtianshi_1_dps,
            '开火成瘾症': calculate_xinyuenengtianshi_2_dps,
            '使命必达!': calculate_xinyuenengtianshi_3_dps
        },
        '缄默德克萨斯': {
            '细雨无声': calculate_jianmodekesasi_1_dps,
            '阵雨连绵': calculate_jianmodekesasi_2_dps,
            '剑雨滂沱': calculate_jianmodekesasi_3_dps
        },
        '麒麟R夜刀': {
            '鬼人化': calculate_qilinRyedao_1_dps,
            '乱舞': calculate_qilinRyedao_2_dps,
            '空中回旋乱舞': calculate_qilinRyedao_3_dps
        },
        '水月': {
            '唤醒': calculate_shuiyue_1_dps,
            '囚徒困境': calculate_shuiyue_2_dps,
            '镜花水月': calculate_shuiyue_3_dps
        },
        '谜图': {
            '关键线索': calculate_mitu_1_dps,
            '疑点追踪': calculate_mitu_2_dps
        },
        '寻澜': {
            '探寻': calculate_xunlan_1_dps,
            '洞悉': calculate_xunlan_2_dps
        },
        '晓歌': {
            '观火': calculate_xiaoge_1_dps,
            '浮光': calculate_xiaoge_2_dps
        },
        '战车': {
            '燃烧榴弹': calculate_zhanche_1_dps,
            '倾泻弹药': calculate_zhanche_2_dps
        },
        '阿米娅(近卫)': {
            '影霄·奔夜': calculate_amiya_jinwei_1_dps,
            '影霄·绝影': calculate_amiya_jinwei_2_dps
        },
        '灰毫': {
            '攻击力强化·γ型': calculate_huihao_1_dps,
            '专注轰击': calculate_huihao_2_dps
        },
        '阿米娅(医疗)':{
            '哀恸共情': calculate_amiya_yiliao_1_dps,
            '慈悲愿景': calculate_amiya_yiliao_2_dps
        },
        '寒芒克洛丝': {
            '无痕': calculate_hanmangkeluosi_1_dps,
            '封喉': calculate_hanmangkeluosi_2_dps
        },
        '熔泉': {
            '信号矢': calculate_rongquan_1_dps,
            '便携破城矢': calculate_rongquan_2_dps
        },
        '阿米娅(术士)': {
            '战术咏唱·γ型': calculate_amiya_1_dps,
            '精神爆发': calculate_amiya_2_dps,
            '奇美拉': calculate_amiya_3_dps
        },
        '梅': {
            '麻痹弹': calculate_mei_1_dps,
            '束缚电击': calculate_mei_2_dps
        },
        '流星': {
            '碎甲击': calculate_liuxing_1_dps,
            '碎甲击·扩散': calculate_liuxing_2_dps
        }
    }

    # 确认技能是否有对应的DPS计算函数
    if skill_name not in skill_dps_functions[hero_name].keys():
        raise ValueError(f"未知的技能名称：{skill_name}")

    # 调用对应的DPS计算函数
    dps_function = skill_dps_functions[hero_name][skill_name]
    return dps_function(buff_levels)


# 示例使用
if __name__ == '__main__':
    hero_name = "锏"
    skill_name = "纯粹的武力"
    buff_levels = [
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    ]

    # 计算DPS
    dps_results = calculate_dps(hero_name, skill_name, buff_levels)

    # 打印结果
    print(f"DPS = {dps_results}")
