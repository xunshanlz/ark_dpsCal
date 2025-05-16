import math


# 风笛1计算
def calculate_fengdi_1_dps(buff_levels):
    """计算迅捷打击的DPS"""
    module = 85
    atk = (586 + 85 + 25 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1 / (1 + 0.45 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 0.45 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu  # 攻击伤害
    damage_min = (atk * (1 + 0.45 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 保底伤害
    damage_strike = ((atk * (1 + 0.45 + buff_levels[1] / 100) + buff_levels[2]) * 1.4 - buff_levels[7]) * mul * redu
    # 暴击伤害
    damage_strike_min = (atk * (1 + 0.45 + buff_levels[1] / 100) + buff_levels[2]) * 1.4 * 0.05 * mul * redu
    # 暴击保底伤害

    skill_coverage_rate = 35 / 70  # 技能覆盖率

    dps_equa = (f'(max([{damage}, {damage_min}]) * 0.67 + max([{damage_strike}, {damage_strike_min}]) * 0.33)'
                f' * / {atk_interval}')  # 技能dps计算公式
    dps = ((max([damage_min, damage]) * 0.67 + max([damage_strike, damage_strike_min]) * 0.33) / atk_interval)  # 技能dps

    damage_total = dps * 35

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu  # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 常态保底伤害
    damage_normal_strike = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.4 - buff_levels[7]) * mul * redu
    # 常态暴击伤害
    damage_normal_strike_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.4 * 0.05 * mul * redu
    # 常态暴击保底伤害

    dps_normal_equa = (f'(max([{damage_normal}, {damage_normal_min}]) * 0.67 + max([{damage_normal_strike},'
                       f' {damage_normal_strike_min}]) * 0.33) / 1')  # 普攻dps计算公式
    dps_normal = ((max([damage_normal_min, damage_normal]) * 0.67 +
                   max([damage_normal_strike, damage_normal_strike_min]) * 0.33) / 1)  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '棍棒与口袋',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能暴击伤害': max([damage_strike, damage_strike_min]),
            '普攻攻击伤害': max([damage_normal, damage_normal_min]),
            '普攻暴击伤害': max([damage_normal_strike, damage_normal_strike_min]),
            '技能覆盖率': skill_coverage_rate,
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


# 风笛2计算
def calculate_fengdi_2_dps(buff_levels):
    """计算高效冲击的DPS"""
    module = 85
    atk = (586 + 85 + 25 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2 - buff_levels[7]) * mul * redu  # 攻击伤害
    damage_min = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2 * 0.05) * mul * redu  # 保底伤害
    damage_strike = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2 * 1.4 - buff_levels[7]) * mul * redu
    # 暴击伤害
    damage_strike_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2 * 1.4 * 0.05 * mul * redu
    # 暴击保底伤害

    dps_equa = (f'(max([{damage}, {damage_min}]) * 0.67 + max([{damage_strike}, {damage_strike_min}]) * 0.33)'
                f' * 2 / 4')  # 技能dps计算公式
    dps = (max([damage, damage_min]) * 0.67 + max([damage_strike, damage_strike_min]) * 2 / 4)  # 技能dps

    damage_total = dps * 4

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu  # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 常态保底伤害
    damage_normal_strike = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.4 - buff_levels[7]) * mul * redu
    # 常态暴击伤害
    damage_normal_strike_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.4 * 0.05 * mul * redu
    # 常态暴击保底伤害

    dps_normal_equa = (f'(max([{damage_normal}, {damage_normal_min}]) * 0.67 + max([{damage_normal_strike},'
                       f' {damage_normal_strike_min}]) * 0.33) / 1')  # 普攻dps计算公式
    dps_normal = ((max([damage_normal_min, damage_normal]) * 0.67 +
                   max([damage_normal_strike, damage_normal_strike_min]) * 0.33) / 1)  # 普攻dps

    hit_num = 4 / atk_interval  # 计算每两个技能期间的平a次数

    dps_cycle_equa = (f'(({hit_num} - 1) * max([{damage_normal}, {damage_normal_min}])'
                      f' + max([{damage}, {damage_min}]) * 2) / 4')  # 周期dps计算公式
    dps_cycle = ((hit_num - 1) * max([damage_normal, damage_normal_min]) + max([damage, damage_min]) * 2) / 4  # 周期dps

    hero = {'模组': '棍棒与口袋',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能暴击伤害': max([damage_strike, damage_strike_min]),
            '常态攻击伤害': max([damage_normal, damage_normal_min]),
            '常态暴击伤害': max([damage_normal_strike, damage_normal_strike_min])
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


# 风笛3计算
def calculate_fengdi_3_dps(buff_levels):
    """计算闭膛连发的DPS"""
    module = 85
    atk = (586 + 85 + 25 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1 * 1.7 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 1.2 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu  # 攻击伤害
    damage_min = (atk * (1 + 1.2 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 保底伤害
    damage_strike = ((atk * (1 + 1.2 + buff_levels[1] / 100) + buff_levels[2]) * 1.4 - buff_levels[7]) * mul * redu
    # 暴击伤害
    damage_strike_min = (atk * (1 + 1.2 + buff_levels[1] / 100) + buff_levels[2]) * 1.4 * 0.05 * mul * redu
    # 暴击保底伤害

    skill_coverage_rate = 20 / 60  # 技能覆盖率

    dps_equa = (f'(max([{damage}, {damage_min}]) * 0.67 + max([{damage_strike}, {damage_strike_min}]) * 0.33) * 3'
                f' */ {atk_interval}')  # 技能dps计算公式
    dps = ((max([damage_min, damage]) * 0.67 + max([damage_strike, damage_strike_min]) * 0.33) * 3 / atk_interval)
    # 技能dps

    damage_total = dps * 20

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu  # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 常态保底伤害
    damage_normal_strike = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.4 - buff_levels[7]) * mul * redu
    # 常态暴击伤害
    damage_normal_strike_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.4 * 0.05 * mul * redu
    # 常态暴击保底伤害

    dps_normal_equa = (f'(max([{damage_normal}, {damage_normal_min}]) * 0.67 + max([{damage_normal_strike},'
                       f' {damage_normal_strike_min}]) * 0.33) / 1')  # 普攻dps计算公式
    dps_normal = ((max([damage_normal_min, damage_normal]) * 0.67 +
                   max([damage_normal_strike, damage_normal_strike_min]) * 0.33) / 1)  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '棍棒与口袋',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能暴击伤害': max([damage_strike, damage_strike_min]),
            '普攻攻击伤害': max([damage_normal, damage_normal_min]),
            '普攻暴击伤害': max([damage_normal_strike, damage_normal_strike_min]),
            '技能覆盖率': skill_coverage_rate
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


# 伊内丝1计算
def calculate_yineisi_1_dps(buff_levels):
    """计算淬影突袭的DPS"""
    module = 35
    atk = (589 + 50 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1 / (1 + buff_levels[5] / 100 + 0.08)  # 计算攻速条件下的攻击间隔

    mul_phy = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    mul_mag = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 法术易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = (((atk * (1 + buff_levels[1] / 100) + 120 + buff_levels[2]) * 0.8 * (1 - buff_levels[8] / 100))
              * mul_mag * redu)  # 技能伤害
    damage_min = (atk * (1 + buff_levels[1] / 100) + 120 + buff_levels[2]) * 0.8 * 0.05 * mul_mag * redu  # 技能保底伤害

    dps_equa = f'max([{damage}, {damage_min}])'  # 技能dps计算公式
    dps = max([damage, damage_min])  # 技能dps

    damage_total = dps * 3

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + 120 + buff_levels[2]) - buff_levels[7]) * mul_phy * redu
    # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + 120 + buff_levels[2]) * 0.05 * mul_phy * redu
    # 常态保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval  # 普攻dps

    dps_cycle_equa = f'{dps} + {dps_normal}'  # 周期dps计算公式
    dps_cycle = dps + dps_normal  # 周期dps

    hero = {'模组': '角部“护理”套组',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能伤害': max([damage, damage_min]),
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '周期回费效率(费用/s)': atk_interval/ 2,
            '说明': '天赋偷攻击默认触发一层'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


# 伊内丝2计算
def calculate_yineisi_2_dps(buff_levels):
    """计算暗夜无明的DPS"""
    module = 35
    atk = (589 + 50 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval_min = 1 / (1 + buff_levels[5] / 100 + 0.08)  # 计算攻速条件下的初始攻击间隔
    atk_interval_max = 1 / (1 + buff_levels[5] / 100 + 0.08 + 0.7)  # 计算攻速条件下的最终攻击间隔
    heating_time = sum([1 / (1 + buff_levels[5] / 100 + 0.08 + 0.07 * x) for x in range(10)])  # 暖机时间

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 1.1 + buff_levels[1] / 100) + 120 + buff_levels[2]) - buff_levels[7]) * mul * redu
    # 技能击伤害
    damage_min = (atk * (1 + 1.1 + buff_levels[1] / 100) + 120 + buff_levels[2]) * 0.05 * mul * redu  # 保底技能攻击伤害

    skill_coverage_rate = 12 / 32  # 技能覆盖率

    dps_equa = (f'max((10 * {damage} + (12 - {heating_time}) / {atk_interval_max} * {damage}),'
                f'(10 * {damage_min} + (12 - {heating_time}) / {atk_interval_max} * {damage_min})) / 12'
                f' * {mul} * {redu}')  # 技能dps计算公式
    dps = max((10 * damage + (12 - heating_time) / atk_interval_max * damage),
              (10 * damage_min + (12 - heating_time) / atk_interval_max * damage_min)) / 12  # 技能dps

    damage_total = dps * 12

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + 120 + buff_levels[2]) - buff_levels[7]) * mul * redu
    # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + 120 + buff_levels[2]) * 0.05 * mul * redu  # 常态保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval_min}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval_min  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '角部“护理”套组',
            '攻击力': atk,
            '初始攻击间隔': atk_interval_min,
            '最终攻击间隔': atk_interval_max,
            '暖机时间': heating_time,
            '技能攻击伤害': max([damage, damage_min]),
            '普攻攻击伤害': max([damage_normal, damage_normal_min]),
            '技能覆盖率': skill_coverage_rate,
            '技能期间回复费用': 10 + (12 - heating_time) / atk_interval_max,
            '说明': '天赋偷攻击默认触发一层'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


# 伊内丝3计算
def calculate_yineisi_3_dps(buff_levels):
    """计算闭膛连发的DPS"""
    module = 35
    atk = (589 + 50 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1 / (1 + buff_levels[5] / 100 + 0.08)  # 计算攻速条件下的攻击间隔

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 1.6 + buff_levels[1] / 100) + 120 + buff_levels[2]) - buff_levels[7]) * mul * redu
    # 技能攻击伤害
    damage_min = (atk * (1 + 1.6 + buff_levels[1] / 100) + 120 + buff_levels[2]) * 0.05 * mul * redu  # 保底技能攻击伤害

    damage_summons = ((atk * (1 + 1.6 + buff_levels[1] / 100) + 120 + buff_levels[2]) * 2 - buff_levels[7]) * mul * redu
    # 影哨伤害
    damage_summons_min = (atk * (1 + 1.6 + buff_levels[1] / 100) + 120 + buff_levels[2]) * 2 * 0.05 * mul * redu
    # 保底影哨伤害

    skill_coverage_rate = 16 / 47  # 技能覆盖率

    dps_equa = (f'(max([{damage_min}, {damage}]) * 16 / {atk_interval} + max([{damage_summons}, {damage_summons_min}]))'
                f'/ 16')  # 技能dps计算公式
    dps = (max([damage_min, damage]) * 16 / atk_interval + max([damage_summons, damage_summons_min])) / 16  # 技能dps

    damage_total = dps * 16

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + 120 + buff_levels[2]) - buff_levels[7]) * mul * redu
    # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + 120 + buff_levels[2]) * 0.05 * mul * redu  # 常态保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '角部“护理”套组',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '影哨伤害': max([damage_summons, damage_summons_min]),
            '技能覆盖率': skill_coverage_rate,
            '技能期间回费费用': 1 + 16 / atk_interval,
            '说明': '天赋偷攻击默认触发一层, 技能结束立即撤退再部署'
            }
    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_jian_1_dps(buff_levels):
    """计算纯粹的武力的DPS"""
    defense_1 = buff_levels[7]
    defense_2 = buff_levels[7] * 0.75
    module = 50
    atk = (635 + 50 + 23 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.3 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的技能攻击间隔

    cover_rate = 1 - (1 - 0.19) ** (5 / atk_interval)
    # 战栗覆盖率

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage_1 = ((atk * (1+ buff_levels[1] / 100) + buff_levels[2]) * 2.2 - defense_1) * mul * redu
    # 技能攻击伤害(不战栗)
    damage_2 = ((atk * (1+ buff_levels[1] / 100) + buff_levels[2]) * 2.2 - defense_2) * mul * redu
    # 技能攻击伤害(战栗)
    damage_min = (atk * (1 + buff_levels[1] / 100 ) + buff_levels[2]) * 2.2 * 0.05 * mul * redu
    # 保底技能攻击伤害
    damage_strike_1 = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2.2 * 1.7 - defense_1) * mul * redu
    # 技能暴击伤害(不战栗)
    damage_strike_2 = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2.2 * 1.7 - defense_2) * mul * redu
    # 技能暴击伤害(战栗)
    damage_strike_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2.2 * 1.7 * 0.05 * mul * redu
    # 技能暴击保底伤害

    damage_normal_1 = ((atk * (1+ buff_levels[1] / 100) + buff_levels[2]) - defense_1) * mul * redu
    # 普攻伤害(不战栗)
    damage_normal_2 = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - defense_2) * mul * redu
    # 普攻伤害(战栗)
    damage_normal_min = (atk * (1+ buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu
    # 普攻保底伤害
    damage_normal_strike_1 = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - defense_1) * 1.7 * mul * redu
    # 普攻暴击伤害(不战栗)
    damage_normal_strike_2 = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - defense_2) * 1.7 * mul * redu
    # 普攻暴击伤害(战栗)
    damage_normal_strike_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.7 * 0.05 * mul * redu
    # 普攻暴击保底伤害

    dps_1 = (((max([damage_1, damage_min]) * 0.9 + max([damage_strike_1, damage_strike_min]) * 0.1) * 2 +
              (max([damage_normal_1,damage_normal_min])  * 0.9 + max([damage_normal_strike_1, damage_normal_strike_min])
               * 0.1) * 6) / atk_interval / 4)
    dps_2 = ((((max([damage_1, damage_min]) * 0.9 + max([damage_strike_1, damage_strike_min]) * 0.1) * 2 +
              (max([damage_normal_1,damage_normal_min])  * 0.9 + max([damage_normal_strike_1, damage_normal_strike_min])
               * 0.1) * 6) / atk_interval / 4) * (1 - cover_rate) +
             (((max([damage_2, damage_min]) * 0.9 + max([damage_strike_2, damage_strike_min]) * 0.1) * 2 +
              (max([damage_normal_2,damage_normal_min])  * 0.9 + max([damage_normal_strike_2, damage_normal_strike_min])
               * 0.1) * 6) / atk_interval / 4) *  cover_rate)

    dps_cycle_equa = f'太长了'
    # 周期dps计算公式
    dps_cycle = f'\n{dps_1}(免疫战栗)\n{dps_2}(不免疫战栗)'  # 周期dps

    damage_total = f'\n{max([damage_1, damage_min])}(免疫战栗)\n{max([damage_2, damage_min])}(不免疫战栗)'  # 总伤

    hero = {'模组': '过往的注脚',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害(免疫战栗)': max([damage_1, damage_min]),
            '技能攻击伤害(不免疫战栗)': max([damage_2, damage_min]),
            '技能暴击伤害(免疫战栗)': max([damage_strike_1, damage_strike_min]),
            '技能暴击伤害(不免疫战栗)': max([damage_strike_2, damage_strike_min]),
            '战栗覆盖率': cover_rate,
            '说明': '只计算周期伤害'
            }

    return '不计', '不计', '不计', '不计', dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_jian_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_jian_3_dps(buff_levels):
    """计算纯粹的武力的DPS"""
    defense_1 = buff_levels[7]
    defense_2 = buff_levels[7] * 0.75
    module = 50
    atk = (635 + 50 + 23 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.3 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的技能攻击间隔

    cover_rate = 1 - (1 - 0.19) ** (5 / atk_interval)
    # 战栗覆盖率

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage_1 = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2.35 * 1.75 - defense_1) * 1.1 * mul * redu
    # 技能单段攻击伤害(不战栗)
    damage_2 = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2.35 * 1.75 - defense_2) * 1.1 * mul * redu
    # 技能单段攻击伤害(战栗)
    damage_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2.35 * 1.75 * 1.1 * 0.05 * mul * redu
    # 技能单段攻击保底伤害
    damage_final_1 = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 3.3 * 1.75 - defense_1) * 1.1 * mul * redu
    # 技能尾刀伤害(不战栗)
    damage_final_2 = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 3.3 * 1.75 - defense_2) * 1.1 * mul * redu
    # 技能尾刀伤害(战栗)
    damage_final_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 3.3 * 1.75 * 1.1 * 0.05 * mul * redu
    # 技能尾刀保底伤害

    damage_normal_1 = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - defense_1) * mul * redu
    # 普攻伤害(不战栗)
    damage_normal_2 = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - defense_2) * mul * redu
    # 普攻伤害(战栗)
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu
    # 普攻保底伤害
    damage_normal_strike_1 = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - defense_1) * 1.75 * mul * redu
    # 普攻暴击伤害(不战栗)
    damage_normal_strike_2 = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - defense_2) * 1.75 * mul * redu
    # 普攻暴击伤害(战栗)
    damage_normal_strike_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.75 * 0.05 * mul * redu
    # 普攻暴击保底伤害

    damage_total_1 = (max([damage_1, damage_min]) * 10 + max([damage_final_1, damage_final_min]))  # 技能总伤(免疫战栗)
    damage_total_2 = (max([damage_2, damage_min]) * 10 + max([damage_final_2, damage_final_min]))  # 技能总伤(不免疫战栗)

    damage_total = f'\n{damage_total_1}(免疫战栗)\n{damage_total_2}(不免疫战栗)'  # 总伤
    
    dps_skill_1 =  damage_total_1 / 5 # 技能dps(不战栗)
    dps_skill_2 = damage_total_2 / 5 # 技能dps(战栗)

    dps_equa = (f'\n(max([{damage_1}, {damage_min}] * 10) + max([{damage_final_1}, {damage_final_min}])) / 5(免疫战栗)'
                f'\n(max([{damage_2}, {damage_min}] * 10) + max([{damage_final_2}, {damage_final_min}])) / 5(不免疫战栗)')
    dps = f'\n{dps_skill_1}(免疫战栗)\n{dps_skill_2}(不免疫战栗)'

    dps_normal_1 = (max([damage_normal_1, damage_normal_min]) * 2 * 0.9 +
                    max([damage_normal_strike_1, damage_normal_strike_min]) * 2 * 0.1) / atk_interval  # 普攻dps(不战栗)
    dps_normal_2 = ((max([damage_normal_1, damage_normal_min]) * 2 * 0.9 +
                     max([damage_normal_strike_1, damage_normal_strike_min]) * 2 * 0.1) * (1 - cover_rate) +
                    (max([damage_normal_2, damage_normal_min]) * 2 * 0.9 +
                     max([damage_normal_strike_2, damage_normal_strike_min]) * 2 * 0.1) * cover_rate) / atk_interval
                    # 普攻dps(战栗)
    dps_normal = f'\n{dps_normal_1}(免疫战栗)\n{dps_normal_2}(不免疫战栗)'
    
    dps_cycle_1 = (dps_skill_1 * 5 + dps_normal_1 * 30) / 35
    dps_cycle_2 = (dps_skill_2 * 5 + dps_normal_2 * 30) / 35
    dps_cycle_equa = (f'\n({dps_skill_1} * 5 + {dps_normal_1} * 30) / 35(免疫战栗)'
                      f'\n({dps_skill_2} * 5 + {dps_normal_2}* 30) / 35(不免疫战栗)')
    # 周期dps计算公式
    dps_cycle = f'\n{dps_cycle_1}(免疫战栗)\n{dps_cycle_2}(不免疫战栗)'  # 周期dps

    hero = {'模组': '过往的注脚',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击单段伤害(免疫战栗)': max([damage_1, damage_min]),
            '技能攻击单段伤害(不免疫战栗)': max([damage_2, damage_min]),
            '技能尾刀伤害(免疫战栗)': max([damage_final_1, damage_final_min]),
            '技能尾刀伤害(不免疫战栗)': max([damage_final_2, damage_final_min]),
            '战栗覆盖率': cover_rate,
            '说明': '覆盖率不计算技能影响'
            }

    return dps_equa, dps, '太长了', dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero

def calculate_yinhui_1_dps(buff_levels):
    """计算强力击·γ型的DPS"""
    module = 70
    atk = (713 + 50 + 26 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.3 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的技能攻击间隔

    mul_phy = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    mul_mag = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 法术易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1+ buff_levels[1] / 100 + 0.27) + buff_levels[2]) * 1.15 * 2.9 - buff_levels[7]) * mul_phy * redu
    # 技能攻击伤害
    damage_min = (atk * (1 + buff_levels[1] / 100 + 0.27) + buff_levels[2]) * 1.15 * 2.9 * 0.05 * mul_phy * redu
    # 保底技能攻击伤害
    damage_normal = ((atk * (1+ buff_levels[1] / 100 + 0.27) + buff_levels[2]) * 1.15 * 0.8 - buff_levels[7]) * mul_phy * redu
    # 普攻伤害
    damage_normal_min = ((atk * (1+ buff_levels[1] / 100 + 0.27) + buff_levels[2]) * 1.15 * 0.8) * 0.05 * mul_phy * redu
    # 普攻保底伤害
    damage_mag = (((atk * (1 + buff_levels[1] / 100 + 0.27) + buff_levels[2]) * 0.1 * (1 - buff_levels[8] / 100)) *
                  mul_mag * redu)  # 附带法伤
    damage_mag_min = (atk * (1 + buff_levels[1] / 100 + 0.27) + buff_levels[2]) * 0.1 * 0.05 * mul_mag * redu
    # 附带保底法伤

    dps_cycle_equa = (f'max([{damage}, {damage_min}]) + max([{damage_normal}, {damage_normal_min}])* 2 + '
                      f'max([{damage_mag}, {damage_mag_min}]) * 3 / {atk_interval} / 3')
    # 周期dps计算公式
    dps_cycle = (max([damage, damage_min]) + max([damage_normal, damage_normal_min])* 2 +
                 max([damage_mag, damage_mag_min]) * 3) / atk_interval / 3  # 周期dps

    damage_total = damage  # 总伤

    hero = {'模组': '雪境羽兽护理套组',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能附带法伤': max([damage_mag, damage_mag_min]),
            '说明': '只计算周期伤害:默认攻击精英/领袖敌人'
            }

    return '不计', '不计', '不计', '不计', dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_yinhui_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_yinhui_3_dps(buff_levels):
    """计算真银斩的DPS"""
    module = 70
    atk = (713 + 50 + 26 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.3 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的技能攻击间隔

    mul_phy = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    mul_mag = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 法术易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 2 + buff_levels[1] / 100 + 0.27) + buff_levels[2]) * 1.15 - buff_levels[7]) * mul_phy * redu
    # 技能攻击伤害
    damage_min = (atk * (1 + 2 + buff_levels[1] / 100 + 0.27) + buff_levels[2]) * 1.15 * 0.05 * mul_phy * redu
    # 保底技能攻击伤害
    damage_mag = ((atk * (1 + 2 + buff_levels[1] / 100 + 0.27) + buff_levels[2]) * 0.1 *
                  (1 - buff_levels[8] / 100)) * mul_mag * redu  # 技能附带法伤
    damage_mag_min = (atk * (1 + 2 + buff_levels[1] / 100 + 0.27) + buff_levels[2]) * 0.1 * 0.05 * mul_mag * redu
    # 技能附带保底法伤

    dps_equa = (f'(max([{damage}, {damage_min}]) / {atk_interval} + '
                f'max([{damage_mag}, {damage_mag_min}]) / {atk_interval})')  # 技能dps计算公式
    dps = (max([damage, damage_min]) / atk_interval + max([damage_mag, damage_mag_min]) / atk_interval)  # 技能dps

    damage_total = dps * 30  # 总伤

    hero = {'模组': '雪境羽兽护理套组',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能附带法伤': max([damage_mag, damage_mag_min]),
            '说明': '不计算平a伤害;不计算周期伤害:默认攻击精英/领袖敌人'
            }

    return dps_equa, dps, "不计", "不计", "不计", "不计", damage_total, hero


def calculate_qiubai_1_dps(buff_levels):
    """计算留羽的DPS"""
    module = 55
    atk = (718 + 50 + 26 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.3 / (1 + 0.07 + buff_levels[5] / 100)  # 计算攻速条件下的技能攻击间隔

    mul_phy = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    mul_mag = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 法术易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    cover_rate = 1 - (1 - 0.2) ** (1.5 / atk_interval) * max([1 - 3 / atk_interval / 5, 0])  # 束缚覆盖率

    damage = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 3 * (1 - buff_levels[8] / 100) * mul_mag * redu
    # 技能伤害
    damage_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 3 * 0.05 * mul_mag * redu
    # 技能保底伤害
    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.8 - buff_levels[7]) * mul_phy * redu
    # 普攻伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.8 * 0.05 * mul_phy * redu
    # 普攻保底伤害
    damage_shadow = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.48 * (1 - buff_levels[8] / 100) * mul_mag * redu
    # 残影伤害
    damage_shadow_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.48 * 0.05 * mul_mag * redu
    # 残影保底伤害
    damage_mag = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.1 * (1 - buff_levels[8] / 100) * mul_mag * redu
    # 附带法伤
    damage_mag_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.1 * 0.05 * mul_mag * redu
    # 附带保底法伤
    damage_ave = ((max([damage_normal, damage_normal_min]) + max([damage_mag, damage_mag_min])) * (1 - cover_rate) +
                  (max([damage_normal, damage_normal_min]) + max([damage_shadow, damage_shadow_min]) +
                   max([damage_mag, damage_mag_min])) * cover_rate)
    # 单次普攻期望伤害

    dps_cycle_equa = (f'{damage_ave} / {atk_interval} + (max([{damage}, {damage_min}]) + '
                      f'max([{damage_mag}, {damage_mag_min}]) + max([{damage_shadow}, {damage_shadow_min}])) / '
                      f'{atk_interval} / 5')
    # 周期dps计算公式
    dps_cycle = damage_ave / atk_interval + (max([damage, damage_min]) + max([damage_mag, damage_mag_min]) +
                                             max([damage_shadow, damage_shadow_min])) / atk_interval / 5  # 周期dps

    damage_total = damage  # 总伤

    hero = {'模组': '雪浸过的斗笠',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '束缚覆盖率': cover_rate,
            '技能伤害': max([damage, damage_min]),
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '天赋附带伤害': max([damage_shadow, damage_shadow_min]),
            '特性附带法伤': max([damage_mag, damage_mag_min]),
            '单次普攻期望伤害': damage_ave,
            '说明': '只计算周期伤害'
            }

    return '不计', '不计', '不计', '不计', dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_qiubai_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_qiubai_3_dps(buff_levels):
    """计算问雪的DPS"""
    module = 55
    atk = (718 + 50 + 26 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval_min = 1.3 / (1 + 0.07 + buff_levels[5] / 100)  # 计算技能攻击间隔(暖机前)
    atk_interval_max = 1.3 / (1 + 0.07 + 1.04 + buff_levels[5] / 100)  # 计算技能攻击伤害(暖机后)

    heating_time = (atk_interval_min + atk_interval_max) / 2 * 8

    mul_phy = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    mul_mag = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 法术易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    cover_rate = 1 - (1 - 0.2) ** (1.5 / atk_interval_max)  # 技能期间束缚覆盖率
    cover_rate_normal = 1 - (1 - 0.2) ** (1.5 / atk_interval_min)  # 普攻束缚覆盖率

    damage_skill = (atk * (1 + 0.55 + buff_levels[1] / 100) + buff_levels[2]) * (1 - buff_levels[8]) * mul_mag * redu
    # 技能伤害
    damage_skill_min = (atk * (1 + 0.55 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul_mag * redu
    # 技能保底伤害
    damage_skill_shadow = ((atk * (1 + 0.55 + buff_levels[1] / 100) + buff_levels[2]) * 0.96 * (1 - buff_levels[8]) *
                           mul_mag * redu)  # 技能期间残影伤害
    damage_skill_shadow_min = (atk * (1 + 0.55 + buff_levels[1] / 100) + buff_levels[2]) * 0.96 + 0.05 * mul_mag * redu
    # 技能期间残影保底伤害
    damage_skill_mag = ((atk * (1 + 0.55 + buff_levels[1] / 100) + buff_levels[2]) * 0.1 * (1 - buff_levels[8]) *
                        mul_mag * redu)  # 技能期间特性附加伤害
    damage_skill_mag_min = (atk * (1 + 0.55 + buff_levels[1] / 100) + buff_levels[2]) * 0.1 * 0.05 * mul_mag * redu
    # 技能期间特性附加保底伤害
    damage_ave_skill = ((max([damage_skill, damage_skill_min]) + max([damage_skill_mag, damage_skill_mag_min])) * (
                1 - cover_rate) +
                        (max([damage_skill, damage_skill_min]) + max(
                            [damage_skill_shadow, damage_skill_shadow_min]) + max(
                            [damage_skill_mag, damage_skill_mag_min])) * cover_rate)
    # 单次期望伤害

    dps_equa = f'({damage_ave_skill} * 8 + {damage_ave_skill} / {atk_interval_max} * (30 - {heating_time})) / 30'
    dps = (damage_ave_skill * 8 + damage_ave_skill / atk_interval_max * (30 - heating_time)) / 30

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.8 - buff_levels[7]) * mul_phy * redu
    # 普攻伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.8 * 0.05 * mul_phy * redu
    # 普攻保底伤害
    damage_shadow = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.48 * (1 - buff_levels[8]) * mul_mag * redu
    # 残影伤害
    damage_shadow_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.48 * 0.05 * mul_phy * redu
    # 残影保底伤害
    damage_mag = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.1 * (1 - buff_levels[8] / 100) * mul_mag * redu
    # 特性附加法伤
    damage_mag_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.1 * 0.05 * mul_mag * redu
    # 特性附加保底法伤
    damage_ave_normal = ((max([damage_normal, damage_normal_min]) + max([damage_mag, damage_mag_min])) * (
                1 - cover_rate_normal) +
                         (max([damage_normal, damage_normal_min]) + max([damage_shadow, damage_shadow_min]) + max(
                             [damage_mag, damage_mag_min])) * cover_rate_normal)
    # 单次普攻期望伤害

    dps_normal_equa = f'{damage_ave_normal} / {atk_interval_min}'
    dps_normal = damage_ave_normal / atk_interval_min

    skill_cover_rate = 30 / 85  # 技能覆盖率

    dps_cycle_equa = f'{dps} * {skill_cover_rate} + {dps_normal} * (1 - {skill_cover_rate})'
    # 周期dps计算公式
    dps_cycle = dps * skill_cover_rate + dps_normal * (1 - skill_cover_rate)  # 周期dps

    damage_total = dps * 30  # 总伤

    hero = {'模组': '雪浸过的斗笠',
            '攻击力': atk,
            '初始攻击间隔': atk_interval_min,
            '暖机后攻击间隔': atk_interval_max,
            '初始束缚覆盖率': cover_rate_normal,
            '暖机后束缚覆盖率': cover_rate,
            '暖机时间': heating_time,
            '技能期间伤害': max([damage_skill, damage_skill_min]),
            '技能期间残影伤害': max([damage_skill_shadow, damage_skill_shadow_min]),
            '技能期间特性附带法伤': max([damage_skill_mag, damage_skill_mag_min]),
            '技能期间单次普攻期望伤害': damage_ave_skill,
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '残影伤害': max([damage_shadow, damage_shadow_min]),
            '特性附带法伤': max([damage_mag, damage_mag_min]),
            '单次普攻期望伤害': damage_ave_normal,
            '说明': '计算dps时束缚覆盖率按暖机后覆盖率计算; 未计算全程束缚+停顿时的伤害, 如要计算的话大约是原数值乘以1.3, 高攻速下乘以1.2'
            }
    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_maenna_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_maenna_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_maenna_3_dps(buff_levels):
    """计算未照耀的荣光的DPS"""
    module = 35  # 模组攻击力
    atk = (355 + 30 + 25 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.2 / (1 + 0.07 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul_phy = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    mul_real = (1 + buff_levels[11] / 100) * (1 + buff_levels[6] / 100)
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 4 + buff_levels[1] / 100) + buff_levels[2]) * 1.8 * 1.23 - buff_levels[7]) * mul_phy * redu
    # 攻击伤害
    damage_min = (atk * (1 + 4 + buff_levels[1] / 100) + buff_levels[2]) * 1.8 * 1.23 * 0.05 * mul_real * redu
    # 保底伤害
    damage_real = (atk * (1 + 4 + buff_levels[1] / 100) + buff_levels[2]) * 0.15  # 附带真伤

    skill_coverage_rate = 28 / 70  # 技能覆盖率

    dps_equa = f'(max({damage}, {damage_min}) + {damage_real}) / {atk_interval}'  # 技能dps计算公式
    dps = (max(damage, damage_min) + damage_real) / atk_interval  # 技能dps

    damage_total = dps * 28

    dps_cycle_equa = f'{dps} * {skill_coverage_rate}'
    dps_cycle = dps * skill_coverage_rate  # 周期dps

    hero = {'模组': '鞘中人',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能附带真伤': damage_real,
            '技能覆盖率': skill_coverage_rate,
            '说明': '不计算杀人掉被动;1天赋仅计算触发前半段;默认磨满刀'
            }

    return dps_equa, dps, '常态不攻击', '常态不攻击', dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_wuerbian_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_wuerbian_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_wuerbian_3_dps(buff_levels):
    """计算必须开辟的道路的DPS"""
    module = 120  # 模组攻击力
    atk = (1569 + 80 + 45 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 2.5 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 2.6 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu  # 技能伤害
    damage_min = (atk * (1 + 2.6 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 保底伤害

    damage_impact = ((atk * (1 + 2.6 + buff_levels[1] / 100) + buff_levels[2]) * 1.6 - buff_levels[7]) * mul * redu
    # 肘击伤害
    damage_impact_min = ((atk * (1 + 2.6 + buff_levels[1] / 100) + buff_levels[2]) * 1.6) * 0.05 * mul * redu
    # 肘击保底伤害

    dps_equa = f'max([{damage}, {damage_min}]) / {atk_interval} + max([{damage_impact}, {damage_impact_min}]) / 25'
    # 技能dps计算公式
    dps = max([damage, damage_min]) / atk_interval + max([damage_impact, damage_impact_min]) / 25  # 技能dps

    damage_total = dps * 25  # 总伤

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu  # 普攻伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 普攻伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval  # 普攻dps

    skill_coverage_rate = 25 / 50

    dps_cycle_equa = (f'(max([{damage}, {damage_min}]) + max([{damage_normal}, {damage_normal_min}]) * 2)'
                      f' / {atk_interval} / 3')  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '乌尔比安的衣橱',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '肘击伤害': max([damage_impact, damage_impact_min]),
            '技能攻击伤害': max([damage, damage_min]),
            '普攻攻击伤害': max([damage_normal, damage_normal_min]),
            '说明': '计算时默认不叠加二天赋,每次技能打满'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_hedelei_1_dps(buff_levels):
    """计算重锋不熄的DPS"""
    module = 130  # 模组攻击力
    atk = (1576 + 80 + 45 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 2.5 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2.6 * 1.1 - buff_levels[7]) * 1.1 * mul * redu
    # 技能伤害
    damage_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2.6 * 1.1 * 1.1 * 0.05 * mul * redu  # 保底伤害

    dps_equa = f'max([{damage}, {damage_min}]) / {atk_interval} / 3'  # 技能dps计算公式
    dps = max([damage, damage_min]) / atk_interval / 3  # 技能dps

    damage_total = max([damage, damage_min])

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.1 - buff_levels[7]) * 1.1 * mul * redu
    # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.1 * 1.1 * 0.05 * mul * redu
    # 常态保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval  # 普攻dps

    dps_cycle_equa = (f'(max([{damage}, {damage_min}]) + max([{damage_normal}, {damage_normal_min}]) * 2)'
                      f' / {atk_interval} / 3')  # 周期dps计算公式
    dps_cycle = (max([damage, damage_min]) + max([damage_normal, damage_normal_min]) * 2) / atk_interval / 3  # 周期dps

    hero = {'模组': '新的生活',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '普攻攻击伤害': max([damage_normal, damage_normal_min]),
            '说明': '计算时默认不触发一天赋'
            }

    return '不计', '不计', '不计', '不计', dps_cycle_equa, dps_cycle, damage_total, hero


# 赫德雷2计算
def calculate_hedelei_2_dps(buff_levels):
    """计算余烬重荷的DPS"""
    module = 130  # 模组攻击力
    atk = (1576 + 80 + 45 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 3 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔
    atk_interval_off = 2.5 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔（未开启技能）

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage_1 = ((atk * (1 + 0.4 + buff_levels[1] / 100) + buff_levels[2]) * 1.4 - buff_levels[7]) * 1.1 * mul * redu
    # 可晕敌人技能伤害
    damage_1_min = (atk * (1 + 0.4 + buff_levels[1] / 100) + buff_levels[2]) * 1.4 * 1.1 * 0.05 * mul * redu
    # 可晕敌人技能保底伤害

    damage_2 = ((atk * (1 + 0.4 + buff_levels[1] / 100) + buff_levels[2]) * 1.1 - buff_levels[7]) * 1.1 * mul * redu
    # 暴击伤害
    damage_2_min = (atk * (1 + 0.4 + buff_levels[1] / 100) + buff_levels[2]) * 1.1 * 1.1 * 0.05 * mul * redu
    # 暴击保底伤害

    dps_equa = (f'max([{damage_1}, {damage_1_min}]) / {atk_interval}(可晕)\n'
                f'max([{damage_2}, {damage_2_min}]) / {atk_interval}(不可晕)')  # 技能dps计算公式
    dps_1 = max([damage_1, damage_1_min]) / atk_interval  # 可晕敌人技能dps
    dps_2 = max([damage_2, damage_2_min]) / atk_interval  # 不可晕敌人技能dps

    dps = (f'{dps_1}(可晕)\n'
           f'{dps_2}(不可晕)')

    damage_total = '永续类技能不计算总伤'

    damage_normal = (((atk * (1 + 0.4 + buff_levels[1] / 100) + buff_levels[2]) * 1.1 - buff_levels[7]) * 1.1
                     * mul * redu)  # 常态攻击伤害
    damage_normal_min = (atk * (1 + 0.4 + buff_levels[1] / 100) + buff_levels[2]) * 1.1 * 1.1 * 0.05 * mul * redu
    # 常态保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval_off}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval_off  # 普攻dps

    dps_cycle_equa = '永续类技能不计算周期dps'  # 周期dps计算公式
    dps_cycle = dps  # 周期dps

    hero = {'模组': '新的生活',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害(可晕)': max([damage_1, damage_1_min]),
            '技能攻击伤害(不可晕)': max([damage_2, damage_2_min]),
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


# 赫德雷3计算
def calculate_hedelei_3_dps(buff_levels):
    """计算死境硝烟的DPS"""
    module = 130  # 模组攻击力
    atk = (1576 + 80 + 45 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 2.5 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul_phy = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    mul_real = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 真伤易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    cover_rate = 1 - (1 - 0.25) ** ((5 / atk_interval + 1) if (5 / atk_interval) % 1 == 0 else int(5 / atk_interval))
    # 天赋触发概率

    damage = (((atk * (1 + 1.2 + buff_levels[1] / 100) + buff_levels[2]) * 1.1 - buff_levels[7]) * 1.1 *
              mul_phy * redu)  # 技能攻击伤害
    damage_min = (atk * (1 + 1.2 + buff_levels[1] / 100) + buff_levels[2]) * 1.1 * 1.1 * 0.05 * mul_phy * redu
    # 技能保底伤害
    damage_strike = (((atk * (1 + 1.2 + buff_levels[1] / 100) + buff_levels[2]) * 1.4 - buff_levels[7]) * 1.1 *
                     mul_phy * redu)  # 暴击伤害
    damage_strike_min = (atk * (1 + 1.2 + buff_levels[1] / 100) + buff_levels[2]) * 1.4 * 1.1 * 0.05 * mul_phy * redu
    # 暴击保底伤害

    damage_real = 200 * mul_real

    skill_coverage_rate = 70 / 120  # 技能覆盖率

    dps_equa = (
        f'(max([{damage}, {damage_min}]) * (1 - {cover_rate}) + max([{damage_strike}, {damage_strike_min}]) * '
        f'{cover_rate} / {atk_interval} + {damage_real})(可晕)\n'
        f'max([{damage}, {damage_min}]) / {atk_interval} + {damage_real}(不可晕)')  # 技能dps计算公式
    dps_1 = ((max([damage, damage_min]) * (1 - cover_rate) + max([damage_strike, damage_strike_min]) * cover_rate) /
             atk_interval + damage_real)
    # 可晕敌人技能dps
    dps_2 = max([damage, damage_min]) / atk_interval + damage_real
    # 不可晕敌人技能dps
    dps = (f'\n{dps_1}(可晕)\n'
           f'{dps_2}(不可晕)')
    damage_total = (f'\n{dps_1 * 70}(可晕)\n'
                    f'{dps_2 * 70}(不可晕)')

    damage_normal = (((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.1 - buff_levels[7]) * 1.1 *
                     mul_phy * redu)  # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.1 * 1.1 * 0.05 * mul_phy * redu
    # 常态保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval  # 普攻dps

    dps_cycle_equa = (f'{dps_1} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})(可晕)\n'
                      f'{dps_2} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})(不可晕)')
    dps_cycle_1 = dps_1 * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 可晕敌人周期dps
    dps_cycle_2 = dps_2 * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 不可晕敌人周期dps
    dps_cycle = (f'\n{dps_cycle_1}(可晕)\n'
                 f'{dps_cycle_2}(不可晕)')
    hero = {'模组': '新的生活',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '眩晕期望覆盖率': cover_rate,
            '技能攻击伤害': max([damage, damage_min]),
            '技能暴击伤害': max([damage_strike, damage_strike_min]),
            '技能附带每秒真伤': damage_real,
            '技能覆盖率': skill_coverage_rate
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_peipei_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_peipei_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_peipei_3_dps(buff_levels):
    """计算时光震荡的DPS"""
    module = 113
    atk = (1290 + 70 + 35 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 2 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的技能攻击间隔
    atk_interval_normal = 2 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的普攻攻击间隔

    mul_phy = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    mul_mag = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 法术易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage_1 = (((atk * (1 + 2.4 + 0.2 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) *
                mul_phy * redu)
    damage_2 = (((atk * (1 + 2.65 + 0.2 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) *
                mul_phy * redu)
    damage_3 = (((atk * (1 + 2.9 + 0.2 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) *
                mul_phy * redu)
    damage_4 = (((atk * (1 + 3.15 + 0.2 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) *
                mul_phy * redu)
    damage_5 = (((atk * (1 + 3.4 + 0.2 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) *
                mul_phy * redu)
    # 技能攻击伤害

    damage_1_min = ((atk * (1 + 2.4 + 0.2 + buff_levels[1] / 100) + buff_levels[2]) * 1.15 * 0.05 *
                    mul_phy * redu)
    damage_2_min = ((atk * (1 + 2.65 + 0.2 + buff_levels[1] / 100) + buff_levels[2]) * 1.15 * 0.05 *
                    mul_phy * redu)
    damage_3_min = ((atk * (1 + 2.9 + 0.2 + buff_levels[1] / 100) + buff_levels[2]) * 1.15 * 0.05 *
                    mul_phy * redu)
    damage_4_min = ((atk * (1 + 3.15 + 0.2 + buff_levels[1] / 100) + buff_levels[2]) * 1.15 * 0.05 *
                    mul_phy * redu)
    damage_5_min = ((atk * (1 + 3.4 + 0.2 + buff_levels[1] / 100) + buff_levels[2]) * 1.15 * 0.05 *
                    mul_phy * redu)
    # 保底技能攻击伤害

    skill_coverage_rate = 40 / 85  # 技能覆盖率

    dps_equa = (f'sum([max([{damage_1}, {damage_1_min}]), max([{damage_2}, {damage_2_min}]), '
                f'max([{damage_3}, {damage_3_min}]), max([{damage_4}, {damage_4_min}]), '
                f'max([{damage_5}, {damage_5_min}]) * (40 - {atk_interval} * 4) / {atk_interval}]) / 40')  # 技能dps计算公式
    dps = sum([max([damage_1, damage_1_min]), max([damage_2, damage_2_min]), max([damage_3, damage_3_min]),
               max([damage_4, damage_4_min]), max([damage_5, damage_5_min]) * (40 - atk_interval * 4) / atk_interval]) / 40  # 技能dps

    damage_total = dps * 40  # 总伤

    damage_normal = ((atk * (1 + 0.2 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul_phy * redu
    # 普攻攻击伤害
    damage_normal_min = (atk * (1 + 0.2 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul_phy * redu

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval_normal}'  # 普攻伤害
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval_normal  # 常套dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '晴雨',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能第一锤伤害': max([damage_1, damage_1_min]),
            '技能第二锤伤害': max([damage_2, damage_2_min]),
            '技能第三锤伤害': max([damage_3, damage_3_min]),
            '技能第四锤伤害': max([damage_4, damage_4_min]),
            '技能后续每一锤伤害': max([damage_5, damage_5_min]),
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '普攻攻击间隔': atk_interval_normal,
            '技能覆盖率': skill_coverage_rate,
            '说明': '不触发击杀回技力;不触发模组特性(溅射范围≥3人).'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_shierteer_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_shierteer_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_shierteer_3_dps(buff_levels):
    """计算黄昏的DPS"""
    buff_levels[8] = min([72, max([5, buff_levels[8] - 28])])
    module = 60  # 模组攻击力
    atk = (672 + 100 + 28 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.25 / (1 + 0.08 + buff_levels[5] / 100)  # 计算攻速条件下的技能攻击间隔

    mul_mag = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 法术易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 常态攻击的减伤和闪避

    damage = (atk * (1 + 3.3 + buff_levels[1] / 100) + buff_levels[2]) * (1 - buff_levels[8] / 100) * mul_mag * redu  # 技能伤害

    dps_equa = f'{damage} / {atk_interval} '  # 技能dps计算公式
    dps = damage / atk_interval

    hero = {'模组': '萨米的不灭心脏碎片',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能攻击伤害': damage,
            '说明': '只计算技能dps, 不计算总伤'
            }

    return dps_equa, dps, '不计算', '不计算', '不计算', '不计算', '不计算', hero


def calculate_weina_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_weina_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_weina_3_dps(buff_levels):
    """计算俱以我之名的DPS"""
    module = 56  # 模组攻击力
    atk = (675 + 70 + 28 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1 / (1 + buff_levels[5] / 100 + 0.08)  # 计算攻速条件下的技能攻击间隔
    atk_interval_normal = 1.25 / (1 + buff_levels[5] / 100 + 0.08)  # 计算攻速条件下的常态攻击间隔

    mul_real = (1 + buff_levels[11] / 100) * (1 + buff_levels[6] / 100)  # 真伤易伤和脆弱
    mul_mag = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 法术易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 常态攻击的减伤和闪避

    damage = (atk * (1 + 1.9 + buff_levels[1] / 100) + buff_levels[2]) * mul_real  # 技能伤害

    skill_coverage_rate = 25 / 75  # 技能覆盖率

    dps_equa = f'{damage} / {atk_interval} '  # 技能dps计算公式
    dps = damage / atk_interval

    damage_total = dps * 25

    damage_normal = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * (1 - buff_levels[8] / 100) * mul_mag * redu
    # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul_mag * redu  # 常态保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval}'
    # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval_normal  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '城主的冒险',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能攻击伤害': damage,
            '普攻攻击伤害': max([damage_normal, damage_normal_min]),
            '技能覆盖率': skill_coverage_rate,
            '说明': '默认不触发1天赋(需要添加的话在局内乘算加上加成)；技能期间无视敌方闪避/减伤；未计算狮子伤害。'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_yaoqishilinguang_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_yaoqishilinguang_2_dps(buff_levels):
    """计算逐夜烁光的DPS"""
    deff = buff_levels[7] * 0.672
    module = 105
    atk = (1064 + 85 + 35 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.5 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的技能攻击间隔

    mul_phy = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    mul_real = (1 + buff_levels[11] / 100) * (1 + buff_levels[6] / 100)  # 真伤易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 1.6 + buff_levels[1] / 100) + buff_levels[2]) - deff) * 1.15 * mul_phy * redu
    # 技能攻击伤害
    damage_min = (atk * (1 + 1.6 + buff_levels[1] / 100) + buff_levels[2]) * 1.15 * 0.05 * mul_phy * redu
    # 保底技能攻击伤害
    damage_impact = (atk * (1 + 1.6 + buff_levels[1] / 100) + buff_levels[2]) * 1.15 * mul_real  # 落地真伤

    dps_equa = f'max([{damage}, {damage_min}]) / {atk_interval}'  # 技能dps计算公式
    dps = max([damage, damage_min]) / atk_interval  # 技能dps

    damage_total = dps * 27 + damage_impact  # 总伤

    hero = {'模组': '耀阳锋刃',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '落地真伤': damage_impact,
            '说明': '只计算技能伤害和dps,默认x模,默认阻挡敌人,内置无视护甲'
            }

    return dps_equa, dps, "不计", "不计", "不计", "不计", damage_total, hero


def calculate_yaoqishilinguang_3_dps(buff_levels):
    """计算耀阳颔首的DPS"""
    deff = buff_levels[7] * 0.72
    module = 105
    atk = (1064 + 85 + 35 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.5 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的技能攻击间隔

    mul_phy = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    mul_real = (1 + buff_levels[11] / 100) * (1 + buff_levels[6] / 100)  # 真伤易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = (atk * (1 + 1.4 + buff_levels[1] / 100) + buff_levels[2]) * mul_real
    # 技能攻击伤害(真伤)
    damage_impact = (atk * (1 + 1.4 + buff_levels[1] / 100) + buff_levels[2]) * 2 * mul_real  # 耀阳落地真伤

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - deff) * mul_phy * redu  # 普攻伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul_phy * redu  # 普攻伤害

    skill_cover_rate = 20 / 65  # 技能覆盖率

    dps_equa = f'{damage} / {atk_interval}'  # 技能dps计算公式
    dps = damage / atk_interval

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval}'
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval

    dps_cycle_equa = f'({dps} * 25 + {damage_impact} + {dps_normal} * 40) / 65'
    dps_cycle = (dps * 25 + damage_impact + dps_normal * 40) / 65
    damage_total = dps * 25 + damage_impact  # 总伤

    hero = {'模组': '耀阳锋刃',
            '攻击力': atk,
            '技能覆盖率': skill_cover_rate,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': damage,
            '耀阳落地真伤': damage_impact,
            '普攻伤害': damage_normal,
            '说明': '默认x模,默认阻挡敌人,内置无视护甲'
            }
    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_haojiao_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_haojiao_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_haojiao_3_dps(buff_levels):
    """计算最终防线的DPS"""
    module = 120
    atk = (936 + 70 + 30 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1 / (1 + 0.25 + buff_levels[5] / 100)  # 计算攻速条件下的技能攻击间隔
    atk_interval_normal = 2.8 / (1 + 0.25 + buff_levels[5] / 100)  # 计算攻速条件下的初始攻击间隔

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 0.7 + buff_levels[1] / 100 + 0.23) + buff_levels[2]) - buff_levels[7]) * mul * redu
    # 技能攻击伤害
    damage_min = (atk * (1 + 0.7 + buff_levels[1] / 100 + 0.23) + buff_levels[2]) * 0.05 * mul * redu  # 保底技能攻击伤害
    damage_heating = ((atk * (1 + 1.4 + buff_levels[1] / 100 + 0.23) + buff_levels[2]) - buff_levels[7]) * mul * redu
    # 过载伤害
    damage_heating_min = (atk * (1 + 1.4 + buff_levels[1] / 100 + 0.23) + buff_levels[2]) * 0.05 * mul * redu
    # 过载保底伤害

    skill_coverage_rate = 24 / 59  # 技能覆盖率

    dps_equa = (f'(max([{damage}, {damage_min}]) * 12 / {atk_interval} +'
                f' max([{damage_heating}, {damage_heating_min}]) * 12 / {atk_interval})/ 24)')
    # 技能dps计算公式
    dps = ((max([damage, damage_min]) * 12 / atk_interval +
            max([damage_heating, damage_heating_min]) * 12 / atk_interval) / 24)  # 技能dps

    damage_total = dps * 24

    damage_normal = ((atk * (1 + 0.23 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu
    # 常态攻击伤害
    damage_normal_min = (atk * (1 + 0.23 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu
    # 常态保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval_normal}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval_normal  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '旧日新装',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '过载攻击伤害': max([damage_heating, damage_heating_min]),
            '普攻攻击伤害': max([damage_normal, damage_normal_min]),
            '普攻攻击间隔': atk_interval_normal,
            '技能覆盖率': skill_coverage_rate,
            '说明': '默认触发血战，技能dps为过暖机+过载的平均dps'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_shu_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_shu_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_shu_3_dps(buff_levels):
    """计算离离枯荣的DPS和hps"""
    module = 50
    atk = (479 + 50 + 25 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.2 / (1 + 0.25 + buff_levels[5] / 100)  # 计算攻速条件下的技能攻击间隔

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 0.75 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu  # 技能攻击伤害
    damage_min = (atk * (1 + 0.75 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 保底技能攻击伤害

    heal = (atk * (1 + 0.75 + buff_levels[1] / 100))  # 单次治疗量

    skill_coverage_rate = 30 / 75  # 技能覆盖率

    dps_equa = f'max([{damage}, {damage_min}]) / {atk_interval}'  # 技能dps计算公式
    dps = max([damage, damage_min]) / atk_interval  # 技能dps

    hps_equa = f'{heal} / {atk_interval}'
    hps = heal / atk_interval

    hero = {'模组': '钦天司时',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '单次治疗量': heal,
            '技能覆盖率': skill_coverage_rate,
            '说明': '默认不触发天有四时'
            }
    return dps_equa, dps, hps_equa, hps, False, False, False, hero


def calculate_zhuoxinsikadi_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_zhuoxinsikadi_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_zhuoxinsikadi_3_dps(buff_levels):
    """计算潮涌,潮枯的DPS"""
    module = 35  # 模组攻击力
    atk = (368 + 50 + 27 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻

    mul_real = (1 + buff_levels[11] / 100) * (1 + buff_levels[6] / 100)  # 真伤易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 常态攻击的减伤和闪避

    damage = (atk * (1 + 0.17 + buff_levels[1] / 100) + buff_levels[2]) * 0.7 * mul_real  # 技能伤害

    skill_coverage_rate = 20 / 55  # 技能覆盖率

    dps_equa = f'{damage} '  # 技能dps计算公式
    dps = damage

    damage_total = dps * 20

    buff_atk = (atk * (1 + 0.17 + buff_levels[1] / 100) + buff_levels[2]) * 1.1

    hero = {'模组': '蜕化的残迹',
            '攻击力': atk,
            '技能攻击伤害': damage,
            '提供加攻数值': buff_atk,
            '说明': '默认触发二天赋前半段;不计算周期伤害;dps和技能攻击伤害为单人,计算海嗣叠加请*2'
            }

    return dps_equa, dps, '不计算', '不计算', '不计算', '不计算', damage_total, hero


def calculate_mowang_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_mowang_2_dps(buff_levels):
    """计算明日渺远不及的DPS"""
    module = 27  # 模组攻击力
    atk = (369 + 30 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻

    mul_real = (1 + buff_levels[11] / 100) * (1 + buff_levels[6] / 100)  # 真伤易伤和脆弱

    damage = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2.75 * mul_real  # 技能伤害

    skill_coverage_rate = 35 / 70  # 技能覆盖率

    dps_equa = f'{damage} / 1.2'  # 技能dps计算公式
    dps = damage / 1.2

    damage_total = dps * 35

    buff_atk = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1

    hero = {'模组': '故事的结局',
            '攻击力': atk,
            '技能攻击伤害': damage,
            '提供加攻数值': buff_atk,
            '说明': '微尘全砸一个人身上'
            }

    return dps_equa, dps, '不计算', '不计算', '不计算', '不计算', damage_total, hero


def calculate_mowang_3_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_weishidaier_1_dps(buff_levels):
    """计算定点清算的DPS"""
    module = 65  # 模组攻击力
    atk = (687 + 90 + 32 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 2.1 / (1 + 0.07 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 - buff_levels[7]) * mul * redu  # 技能伤害
    damage_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 0.05 * mul * redu  # 保底伤害
    damage_aftershock = (((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.2 * 1.25 - buff_levels[7])
                         * mul * redu)  # 技能余震伤害
    damage_aftershock_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 1.2 * 0.05 * mul * redu
    # 技能余震保底伤害
    damage_aftershock_normal = (((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 0.5 - buff_levels[7]) *
                                mul * redu)  # 普攻余震伤害
    damage_aftershock_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 0.5 * 0.05 * mul * redu
    # 普攻余震保底伤害
    damage_boom = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.85 - buff_levels[7]) * mul * redu
    # 残影爆炸伤害
    damage_boom_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.85 * 0.05 * mul * redu  # 残影爆炸保底伤害

    boom_probability_skill = 1 - 0.85 ** 4  # 技能触发残影爆炸几率
    boom_probability_normal = 1 - 0.85 ** 2  # 普攻触发残影爆炸几率

    dps_equa = (f'(max([{damage}, {damage_min}] + max([{damage_aftershock}, {damage_aftershock_min}])'
                f' * 4 + max([{damage_boom}, {damage_boom_min}]) * {boom_probability_skill})) / {atk_interval}'
                f' / 3')  # 技能dps计算公式
    dps = (max([damage, damage_min]) + max([damage_aftershock, damage_aftershock_min]) * 4 +
           max([damage_boom, damage_boom_min]) * boom_probability_skill) / atk_interval / 3  # 技能dps

    damage_total = dps * atk_interval * 3

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 - buff_levels[7]) * mul * redu
    # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 0.05 * mul * redu  # 常态保底伤害

    dps_normal_equa = (f'max([{damage_normal}, {damage_normal_min}]) + '
                       f'max([{damage_aftershock_normal}, {damage_aftershock_normal_min}]) * 2 + '
                       f'max([{damage_boom}, {damage_boom_min}]) * {boom_probability_normal}) / '
                       f'{atk_interval}')  # 普攻dps计算公式
    dps_normal = (max([damage_normal, damage_normal_min]) + max([damage_aftershock, damage_aftershock_min]) * 2
                  + max([damage_boom, damage_boom_min]) * boom_probability_normal) / atk_interval  # 普攻dps

    dps_cycle_equa = f'{dps} + {dps_normal} * 2 / 3'  # 周期dps计算公式
    dps_cycle = dps + dps_normal * 2 / 3  # 周期dps

    hero = {'模组': '祖宗发射器',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能余震伤害': max([damage_aftershock, damage_aftershock_min]),
            '普攻余震伤害': max([damage_aftershock_normal, damage_aftershock_normal_min]),
            '残影爆炸伤害': max([damage_boom, damage_boom_min]),
            '技能触发爆炸几率': boom_probability_skill,
            '普攻触发爆炸几率': boom_probability_normal,
            '说明': '未计算魂灵之影伤害'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_weishidaier_2_dps(buff_levels):
    """计算饱和复仇的DPS"""
    module = 65  # 模组攻击力
    atk = (687 + 90 + 32 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.4 / (1 + 0.07 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 0.35 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 - buff_levels[7]) * mul * redu
    # 技能攻击伤害
    damage_min = (atk * (1 + 0.35 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 0.05 * mul * redu
    # 保底技能攻击伤害
    damage_heating = (((atk * (1 + 0.35 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 0.8 - buff_levels[7]) *
                      mul * redu)  # 过载伤害
    damage_heating_min = (atk * (1 + 0.35 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 0.8 * 0.05 * mul * redu
    # 过载保底伤害

    damage_aftershock = (((atk * (1 + 0.35 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 0.5 - buff_levels[7]) *
                         mul * redu)  # 余震伤害
    damage_aftershock_min = ((atk * (1 + 0.35 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 0.5 * 0.05 * mul *
                             redu)  # 余震保底伤害
    damage_aftershock_heating = ((atk * (1 + 0.35 + buff_levels[1] / 100) + buff_levels[2])
                                 * 1.25 * 0.8 * 0.5 - buff_levels[7]) * mul * redu  # 过载余震伤害
    damage_aftershock_heating_min = ((atk * (1 + 0.35 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 0.8 * 0.5 *
                                     0.05 * mul * redu)  # 过载余震保底伤害
    damage_boom = ((atk * (1 + 0.35 + buff_levels[1] / 100) + buff_levels[2]) * 1.85 - buff_levels[7]) * mul * redu
    # 技能残影爆炸伤害
    damage_boom_min = (atk * (1 + 0.35 + buff_levels[1] / 100) + buff_levels[2]) * 1.85 * 0.05 * mul * redu
    # 技能残影爆炸保底伤害

    boom_probability = 1 - 0.85 ** 4  # 单次普攻期望爆炸次数
    boom_probability_heating = 1.032994  # 过载四连击期望爆炸次数

    skill_coverage_rate = 25 / 50  # 技能覆盖率

    dps_equa = (f'((max([{damage}, {damage_min}]) + max([{damage_aftershock}, {damage_aftershock_min}]) * 2'
                f' + max([{damage_boom}, {damage_boom_min}]) * {boom_probability}) / {atk_interval})(过载前)\n'
                f'((max([{damage_heating}, {damage_heating_min}]) * 4 +'
                f'max([{damage_aftershock_heating}, {damage_aftershock_heating_min}]) * 8 +'
                f'max([{damage_boom}, {damage_boom_min}]) * {boom_probability_heating}) / {atk_interval})(过载)')
    # 技能dps计算公式

    dps_1 = ((max([damage, damage_min]) + max([damage_aftershock, damage_aftershock_min]) * 2 +
             max([damage_boom, damage_boom_min]) * boom_probability) / atk_interval)  # 过载前dps
    dps_2 = ((max([damage_heating, damage_heating_min]) * 4 +
              max([damage_aftershock_heating, damage_aftershock_heating_min]) * 8 +
             max([damage_boom, damage_boom_min]) * boom_probability_heating) / atk_interval)  # 技能dps

    dps = dps_1 * 0.5 + dps_2 * 0.5
    dps_all = f'\n{dps_1}(未过载)  \n{dps_2}(过载)  \n{dps}(平均)'

    damage_total = dps * 25

    atk_interval_normal = 2.1 / (1 + 0.07 + buff_levels[5] / 100)
    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 - buff_levels[7]) * mul * redu
    # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 0.05 * mul * redu  # 常态保底伤害
    damage_aftershock_normal = (((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 0.5 - buff_levels[7]) *
                                mul * redu)  # 普攻余震伤害
    damage_aftershock_normal_min = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 0.5 * 0.05 * mul *
                                    redu)  # 普攻余震保底伤害
    damage_boom_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.85 - buff_levels[7]) * mul * redu
    # 普攻残影爆炸伤害
    damage_boom_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.85 * 0.05 * mul * redu
    # 普攻残影爆炸保底伤害

    dps_normal_equa = (f'max([{damage_normal}, {damage_normal_min}]) + '
                       f'max([{damage_aftershock_normal}, {damage_aftershock_normal_min}]) * 2 + '
                       f'max([{damage_boom_normal}, {damage_boom_normal_min}]) * {boom_probability}) / '
                       f'{atk_interval_normal}')  # 普攻dps计算公式
    dps_normal = ((max([damage_normal, damage_normal_min]) +
                  max([damage_aftershock_normal, damage_aftershock_normal_min]) * 2 +
                  max([damage_boom_normal, damage_boom_normal_min]) * boom_probability) /
                  atk_interval_normal)  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '祖宗发射器',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '单次普攻爆炸几率': boom_probability,
            '过载四连击期望爆炸次数': boom_probability_heating,

            '技能攻击伤害': max([damage, damage_min]),
            '技能余震伤害': max([damage_aftershock, damage_aftershock_min]),
            '技能残影爆炸伤害': max([damage_boom, damage_boom_min]),
            '技能过载攻击伤害': max([damage_heating, damage_heating_min]),
            '技能过载余震伤害': max([damage_aftershock_heating, damage_aftershock_heating_min]),

            '普攻攻击间隔': atk_interval_normal,
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '普攻余震伤害': max([damage_aftershock_normal, damage_aftershock_normal_min]),
            '普攻单次残影爆炸伤害': max([damage_boom_normal, damage_boom_normal_min]),

            '技能覆盖率': skill_coverage_rate,
            '说明': '不考虑魂灵之影伤害，不考虑溅射；'
            }

    return dps_equa, dps_all, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_weishidaier_3_dps(buff_levels):
    """计算爆裂黎明的DPS"""
    module = 65  # 模组攻击力
    atk = (687 + 90 + 32 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 5 / (1 + 0.07 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔
    atk_time = atk_interval * 6  # 打完技能需要时间

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 1.8 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 2.2 - buff_levels[7]) * mul * redu
    # 技能攻击伤害
    damage_min = atk * ((1 + 1.8 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 2.2 * 0.05 * mul * redu
    # 保底技能攻击伤害

    damage_aftershock = ((atk * (1 + 1.8 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 2.2 * 0.5 -
                         buff_levels[7]) * mul * redu  # 余震伤害
    damage_aftershock_min = ((atk * (1 + 1.8 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 2.2 * 0.5 * 0.05 *
                             mul * redu)  # 余震保底伤害

    damage_boom = ((atk * (1 + 1.8 + buff_levels[1] / 100) + buff_levels[2]) * 1.85 - buff_levels[7]) * mul * redu
    # 技能残影爆炸伤害
    damage_boom_min = (atk * (1 + 1.8 + buff_levels[1] / 100) + buff_levels[2]) * 1.85 * 0.05 * mul * redu
    # 技能残影爆炸保底伤害

    skill_coverage_rate = atk_time / (50 + atk_time)  # 技能覆盖率

    dps_equa = (f'((max([{damage}, {damage_min}]) + max([{damage_aftershock}, {damage_aftershock_min}]) * 2 + '
                f'max([{damage_boom}, {damage_boom_min}]))  * 6 / {atk_time})')
    # 技能dps计算公式
    dps = ((max([damage, damage_min]) + max([damage_aftershock, damage_aftershock_min]) * 2 +
           max([damage_boom, damage_boom_min])) * 6 / atk_time)  # 技能dps

    damage_total = dps * atk_time

    atk_interval_normal = 2.1 / (1 + 0.07 + buff_levels[5] / 100)  # 普攻攻击间隔

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 - buff_levels[7]) * mul * redu
    # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 0.05 * mul * redu  # 常态保底伤害

    damage_aftershock_normal = (((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 0.5 - buff_levels[7]) *
                                mul * redu)   # 普攻余震伤害
    damage_aftershock_normal_min = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.25 * 0.5 * 0.05 * mul *
                                    redu)  # 普攻余震保底伤害

    damage_boom_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.85 - buff_levels[7]) * mul * redu
    # 普攻残影爆炸伤害
    damage_boom_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.85 * 0.05 * mul * redu
    # 普攻残影爆炸保底伤害

    boom_probability = 1 - 0.85 ** 4  # 单次普攻期望爆炸次数

    dps_normal_equa = (f'max([{damage_normal}, {damage_normal_min}]) + '
                       f'max([{damage_aftershock_normal}, {damage_aftershock_normal_min}]) * 2 + '
                       f'max([{damage_boom_normal}, {damage_boom_normal_min}]) * {boom_probability}) / '
                       f'{atk_interval_normal}')  # 普攻dps计算公式
    dps_normal = ((max([damage_normal, damage_normal_min]) +
                   max([damage_aftershock_normal, damage_aftershock_normal_min]) * 2 +
                   max([damage_boom_normal, damage_boom_normal_min]) * boom_probability) /
                  atk_interval_normal)  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '祖宗发射器',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能余震伤害': max([damage_aftershock, damage_aftershock_min]),
            '技能残影爆炸伤害': max([damage_boom, damage_boom_min]),
            '普攻攻击间隔': atk_interval_normal,
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '普攻余震伤害': max([damage_aftershock_normal, damage_aftershock_normal_min]),
            '普攻单次残影爆炸伤害': max([damage_boom_normal, damage_boom_normal_min]),
            '技能覆盖率': skill_coverage_rate,
            '说明': '不考虑魂灵之影伤害，不考虑溅射,不考虑技能和攻击前摇；'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_laiyi_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_laiyi_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_laiyi_3_dps(buff_levels):
    """计算得见光芒的DPS"""
    module = 70  # 模组攻击力
    atk = (1072 + 120 + 37 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.6 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage_1 = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.2 * (1 + 0.09 * 1) * 1.2 * 3.3 -
                buff_levels[7]) * mul * redu  # 第一枪攻击伤害
    damage_2 = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.2 * (1 + 0.09 * 2) * 1.2 * 3.3 -
                buff_levels[7]) * mul * redu  # 第二枪攻击伤害
    damage_3 = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.2 * (1 + 0.09 * 3) * 1.2 * 3.3 -
                buff_levels[7]) * mul * redu  # 第三枪攻击伤害
    damage_1_min = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * (1 + 0.09 * 1) * 1.2 * 3.3 * 0.05 * mul *
                    redu)  # 第一枪保底伤害
    damage_2_min = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * (1 + 0.09 * 2) * 1.2 * 3.3 * 0.05 * mul *
                    redu)  # 第二枪保底伤害
    damage_3_min = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * (1 + 0.09 * 3) * 1.2 * 3.3 * 0.05 * mul *
                    redu)   # 第三枪保底伤害

    hit_times_skill = [[0, 10], [9, 11], [20, 12], [35, 13], [46, 14], [62, 15], [73, 16], [90, 17], [102, 18],
                       [120, 19], [133, 20], [152, 21], [165, 22], [187, 23], [200, 24], [223, 25], [237, 26],
                       [262, 27], [276, 28], [304, 29], [319, 30], [349, 31], [364, 32], [398, 33], [413, 34],
                       [450, 35], [466, 36], [507, 37], [524, 38], [569, 39], [586, 40]]  # 莱伊技能攻击次数与攻速的关系
    hit_time = 10
    for i in hit_times_skill[-1::-1]:
        if buff_levels[5] >= i[0]:
            hit_time = i[1]
            break

    skill_coverage_rate = 16 / 46  # 技能覆盖率

    dps_equa = (f'max([damage_1, damage_1_min]) + max([damage_2, damage_2_min]) + max([damage_3, damage_3_min]) * '
                f'(hit_time - 2) / 16')  # 技能dps计算公式
    dps = ((max([damage_1, damage_1_min]) + max([damage_2, damage_2_min]) + max([damage_3, damage_3_min]) *
           (hit_time - 2)) / 16)  # 技能dps

    damage_total = dps * 16

    dps_normal_equa = '未计入'  # 普攻dps计算公式
    dps_normal = '未计入'  # 普攻dps

    dps_cycle_equa = '未计入'
    dps_cycle = '未计入'  # 周期dps

    hero = {'模组': '跳舞的月光',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '第一枪伤害': max([damage_1, damage_1_min]),
            '第二枪伤害': max([damage_2, damage_2_min]),
            '后续每一枪伤害': max([damage_3, damage_3_min]),
            '技能攻击次数': hit_time,
            '技能覆盖率': skill_coverage_rate,
            '说明': '天赋二按从0层开始叠;开启技能时默认满子弹;不触发击杀回技力'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_leimiuan_1_dps(buff_levels):
    """计算归乡邀约的DPS"""
    module = 120  # 模组攻击力
    atk = (1201 + 100 + 46 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 2.7 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔
    atk_interval_normal = 2.7 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的普攻攻击间隔
    atk_time = atk_interval * 8  # 打完技能需要时间

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 0.18 + buff_levels[1] / 100) + buff_levels[2]) * 2.1 - buff_levels[7]) * 1.12 * mul * redu  # 技能攻击伤害
    damage_min = (atk * (1 + 0.18 + buff_levels[1] / 100) + buff_levels[2]) * 2.1 * 1.12 * 0.05 * mul * redu  # 技能攻击保底伤害

    skill_coverage_rate = 2 / 3  # 技能覆盖率

    dps_equa = f'max([{damage}, {damage_min}]) / {atk_interval}'  # 技能dps计算公式
    dps = max([damage, damage_min]) / atk_interval  # 技能dps

    damage_total = max([damage, damage_min]) * 8

    damage_normal = ((atk * (1 + 0.18 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * 1.12 * mul * redu  # 常态攻击伤害
    damage_normal_min = (atk * (1 + 0.18 + buff_levels[1] / 100) + buff_levels[2]) * 1.12 * 0.05 * mul * redu  # 常态保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval_normal}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval_normal  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '弹匣与花窗',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '普攻攻击间隔': atk_interval_normal,
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '技能持续时间': atk_time,
            '技能覆盖率': skill_coverage_rate,
            '说明': '默认暖好12天赋'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_leimiuan_2_dps(buff_levels):
    """计算重逢问候的DPS"""
    module = 120  # 模组攻击力
    atk = (1201 + 100 + 46 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 4.7  # 计算攻速条件下的攻击间隔
    atk_interval_normal = 2.7 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的普攻攻击间隔
    atk_time = atk_interval * 9  # 打完技能需要时间

    heating_time = math.ceil(30 / (1 + atk_interval_normal)) * atk_interval_normal
    # 计算技能回转

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 0.18 + 0.7 + buff_levels[1] / 100) + buff_levels[2]) * 4.25 - buff_levels[7]) * 1.12 * mul * redu  # 技能攻击伤害
    damage_min = (atk * (1 + 0.18 + 0.7 + buff_levels[1] / 100) + buff_levels[2]) * 4.25 * 1.12 * 0.05 * mul * redu  # 技能攻击保底伤害

    skill_coverage_rate = 42.3 / (42.3 + heating_time)  # 技能覆盖率

    dps_equa = f'max([{damage}, {damage_min}]) / {atk_interval}'  # 技能dps计算公式
    dps = max([damage, damage_min]) / atk_interval  # 技能dps

    damage_total = max([damage, damage_min]) * 9  # 计算技能总伤

    damage_normal = ((atk * (1 + 0.18 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * 1.12 * mul * redu  # 常态攻击伤害
    damage_normal_min = (atk * (1 + 0.18 + buff_levels[1] / 100) + buff_levels[2]) * 1.12 * 0.05 * mul * redu  # 常态保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval_normal}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval_normal  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '弹匣与花窗',
            '攻击力': atk,
            '技能回转': heating_time,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '普攻攻击间隔': atk_interval_normal,
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '技能持续时间': atk_time,
            '技能覆盖率': skill_coverage_rate,
            '说明': '默认暖好12天赋,瞄准每次都蓄满,技能回转考虑模组特性回技力'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_leimiuan_3_dps(buff_levels):
    """计算礼炮·强制追思的DPS"""
    module = 120  # 模组攻击力
    atk = (1201 + 100 + 46 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval_normal = 2.7 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的普攻攻击间隔

    heating_time = math.ceil(30 / (1 + atk_interval_normal)) * atk_interval_normal
    # 计算技能回转

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 0.18 + buff_levels[1] / 100) + buff_levels[2]) * 4.5 - buff_levels[7]) * 1.12 * mul * redu  # 技能攻击伤害
    damage_min = (atk * (1 + 0.18+ buff_levels[1] / 100) + buff_levels[2]) * 4.5 * 1.12 * 0.05 * mul * redu  # 技能攻击保底伤害

    damage_total = max([damage, damage_min]) * 7  # 计算技能总伤

    hero = {'模组': '弹匣与花窗',
            '攻击力': atk,
            '技能回转': heating_time,
            '技能攻击伤害': max([damage, damage_min]),
            '说明': '默认暖好12天赋,所有轰炸都取中心范围伤害'
            }

    return '不计算', '不计算', '不计算', '不计算', '不计算', '不计算', damage_total, hero


def calculate_kongxian_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_kongxian_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_kongxian_3_dps(buff_levels):
    """计算空弦特限证章的DPS"""
    module = 55  # 模组攻击力
    atk = (528 + 90 + 27 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1 / (1 + 0.08 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔
    atk_interval_normal = 1 / (1 + 0.08 + buff_levels[5] / 100)  # 计算攻速条件下的普攻攻击间隔

    heating_time = 30 / ((1 / atk_interval) + 0.4)
    # 计算技能回转

    skill_coverage_rate = 20 / (20 + heating_time)  # 技能覆盖率

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 0.3 + 0.5 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu  # 技能攻击伤害
    damage_min = (atk * (1 + 0.3 + 0.5 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 技能攻击保底伤害

    dps_equa = f'max([{damage}, {damage_min}]) / {atk_interval}'  # 技能dps计算公式
    dps = max([damage, damage_min]) * 3 / atk_interval  # 技能dps

    damage_fireworks = ((atk * (1 + 0.3 + 0.5 + buff_levels[1] / 100) + buff_levels[2]) * 2 - buff_levels[7]) * mul * redu  # 技能期间烟花手伤害
    damage_fireworks_min = (atk * (1 + 0.3 + 0.5 + buff_levels[1] / 100) + buff_levels[2]) * 2 * 0.05 * mul * redu  # 技能期间烟花手保底伤害

    dps_fireworks_equa = f'(max([{damage}, {damage_min}]) + max([{damage_fireworks}, {damage_fireworks_min}]) * 0.25) * 3 / {atk_interval}'  # 技能dps计算公式(带烟花手)
    dps_fireworks = (max([damage, damage_min]) + max([damage_fireworks, damage_fireworks_min]) * 0.25) * 3 / atk_interval  # 技能dps(带烟花手)

    damage_total = dps * 20
    damage_total_fireworks = dps_fireworks * 20

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu  # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2])* 0.05 * mul * redu  # 常态保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval_normal}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval_normal  # 普攻dps

    damage_normal_fireworks = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2 - buff_levels[7]) * mul * redu  # 普攻期间烟花手伤害
    damage_normal_fireworks_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2 * 0.05 * mul * redu  # 普攻期间烟花手保底伤害

    dps_normal_fireworks_equa = f'(max([{damage_normal}, {damage_normal_min}]) + max([{damage_normal_fireworks}, {damage_normal_fireworks_min}]) * 0.25) / {atk_interval}'  # 技能dps计算公式(带烟花手)
    dps_normal_fireworks = (max([damage_normal, damage_normal_min]) + max([damage_normal_fireworks, damage_normal_fireworks_min]) * 0.25) / atk_interval  # 技能dps(带烟花手)

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    dps_cycle_fireworks_equa = f'{dps_fireworks} * {skill_coverage_rate} + {dps_normal_fireworks} * (1 - {skill_coverage_rate})'
    dps_cycle_fireworks = dps_fireworks * skill_coverage_rate + dps_normal_fireworks * (1 - skill_coverage_rate)

    hero = {'模组': '空弦特限证章',
            '攻击力': atk,
            '技能回转': heating_time,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能期间烟花手伤害': max([damage_fireworks, damage_fireworks_min]),
            '普攻攻击间隔': atk_interval_normal,
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '普攻烟花手伤害': max([damage_normal_fireworks, damage_normal_fireworks_min]),
            '技能覆盖率': skill_coverage_rate,
            '说明': '不考虑烟花手互相溅射'
            }

    return (dps_equa, f'\n{dps}(无烟花)\n{dps_fireworks}(带烟花)',
            dps_normal_equa, f'\n{dps_normal}(无烟花)\n{dps_normal_fireworks}(带烟花)',
            dps_cycle_equa, f'\n{dps_cycle}(无烟花)\n{dps_cycle_fireworks}(带烟花)',
            f'\n{damage_total}(无烟花)\n{damage_total_fireworks}(带烟花)', hero)


def calculate_chunjinaiyafala_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_chunjinaiyafala_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_chunjinaiyafala_3_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_yanyingweicao_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_yanyingweicao_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_yanyingweicao_3_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_Mon3tr_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_Mon3tr_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_Mon3tr_3_dps(buff_levels):
    """计算指令:熔毁的DPS"""
    module = 0  # 模组攻击力
    atk = (528 + 30 + 25 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.3 / (1 + buff_levels[5] / 100 + 0.22)  # 计算攻速条件下的技能攻击间隔

    mul_real = (1 + buff_levels[11] / 100) * (1 + buff_levels[6] / 100)  # 真伤易伤和脆弱

    damage = (atk * (1 + 3.3 + buff_levels[1] / 100) + buff_levels[2]) * mul_real  # 技能伤害

    skill_coverage_rate = 25 / 75  # 技能覆盖率

    dps_equa = f'{damage} / {atk_interval} '  # 技能dps计算公式
    dps = damage / atk_interval

    damage_total = dps * 25

    heal_skill = (atk * (1 + 3.3 + buff_levels[1] / 100) + buff_levels[2]) * 0.5
    hps_skill = heal_skill / atk_interval

    dps_cycle_equa = f'{dps} * {skill_coverage_rate}'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate  # 周期dps

    hero = {'攻击力': atk,
            '攻击间隔': atk_interval,
            '技能攻击伤害': damage,
            '技能期间hps': hps_skill,
            '技能覆盖率': skill_coverage_rate,
            '说明': '技能期间默认不触发被动加攻;全程触发加攻速.'
            }

    return dps_equa, dps, '不计算', '不计算', dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_huangwulapulande_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_huangwulapulande_2_dps(buff_levels):
    """计算逐猎狂飙的DPS"""
    module = 33  # 模组攻击力
    atk = (342 + 60 + 25 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.3 / (1 + 0.1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage_wolf = ((atk * (1 + 1.2 + buff_levels[1] / 100) + buff_levels[2]) * 1.21 * (1 - buff_levels[8] / 100) * mul *
                   redu)  # 狼头攻击伤害
    damage_wolf_min = (atk * (1 + 1.2 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * 1.21 * mul * redu
    # 狼头攻击保底伤害
    damage = (atk * (1 + 1.2 + buff_levels[1] / 100) + buff_levels[2]) * (1 - buff_levels[8] / 100) * mul * redu
    # 本体攻击伤害
    damage_min = (atk * (1 + 1.2 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu
    # 本体攻击保底伤害

    skill_coverage_rate = 22 / 50  # 技能覆盖率

    dps_equa = (f'(max([{damage_wolf}, {damage_wolf_min}]) * 5 + max([{damage}, {damage_min}])) / '
                f'{atk_interval}')  # 技能dps计算公式
    dps = (max([damage_wolf, damage_wolf_min]) * 5 + max([damage, damage_min])) / atk_interval  # 技能dps

    damage_total = dps * 22

    damage_normal_wolf = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.21 * (1 - buff_levels[8] / 100) * mul *
                          redu)  # 常态攻击狼头伤害
    damage_normal_wolf_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.21 * 0.05 * mul * redu
    # 常态攻击狼头伤害

    damage_normal = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * (1 - buff_levels[8] / 100) * mul * redu
    # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu
    # 常态保底伤害

    dps_normal_equa = (f'(max([{damage_normal}, {damage_normal_min}]) +'
                       f' max([{damage_normal_wolf}, {damage_normal_wolf_min}]) * 2) / '
                       f'{atk_interval}')  # 普攻dps计算公式
    dps_normal = ((max([damage_normal, damage_normal_min]) + max([damage_normal_wolf, damage_normal_wolf_min]) * 2) /
                  atk_interval)  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '狼时',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能狼头伤害': max([damage_wolf, damage_wolf_min]),
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '普攻狼头伤害': max([damage_normal_wolf, damage_normal_wolf_min]),
            '技能覆盖率': skill_coverage_rate,
            '说明': '默认暖好1天赋, 狼头默认最高倍率'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_huangwulapulande_3_dps(buff_levels):
    """计算终幕·浩劫的DPS"""
    module = 33  # 模组攻击力
    atk = (342 + 60 + 25 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.3 / (1 + 0.1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage_wolf = ((atk * (1 + 0.8 + buff_levels[1] / 100) + buff_levels[2]) * 1.21 * (1 - buff_levels[8] / 100) * mul *
                   redu)  # 狼头攻击伤害
    damage_wolf_min = (atk * (1 + 0.8 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * 1.21 * mul * redu
    # 狼头攻击保底伤害
    damage = (atk * (1 + 0.8 + buff_levels[1] / 100) + buff_levels[2]) * (1 - buff_levels[8] / 100) * mul * redu
    # 本体攻击伤害
    damage_min = (atk * (1 + 0.8 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 本体攻击伤害

    damage_dot = (atk * (1 + 0.8 + buff_levels[1] / 100) + buff_levels[2]) * 1.2 * (1 - buff_levels[8] / 100) * mul * redu
    # 技能dot伤害
    damage_dot_min = (atk * (1 + 0.8 + buff_levels[1] / 100) + buff_levels[2]) * 1.2 * 0.05 * mul * redu
    # 技能dot保底伤害

    skill_coverage_rate = 40 / 94  # 技能覆盖率

    dps_equa = (f'((max([{damage_wolf}, {damage_wolf_min}]) * 4 + max([{damage}, {damage_min}])) / '
                f'{atk_interval} +  max([{damage_dot}, {damage_dot_min}]))')  # 技能dps计算公式
    dps = ((max([damage_wolf, damage_wolf_min]) * 4 + max([damage, damage_min])) / atk_interval +
           max([damage_dot, damage_dot_min]))  # 技能dps

    damage_total = dps * 40

    damage_normal_wolf = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.21 * (1 - buff_levels[8] / 100) * mul *
                          redu)  # 常态攻击狼头伤害
    damage_normal_wolf_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.21 * 0.05 * mul * redu
    # 常态攻击狼头伤害

    damage_normal = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * (1 - buff_levels[8] / 100) * mul * redu
    # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 常态保底伤害

    dps_normal_equa = (f'(max([{damage_normal}, {damage_normal_min}]) +'
                       f' max([{damage_normal_wolf}, {damage_normal_wolf_min}]) * 2) / '
                       f'{atk_interval}')  # 普攻dps计算公式
    dps_normal = ((max([damage_normal, damage_normal_min]) + max([damage_normal_wolf, damage_normal_wolf_min]) * 2) /
                  atk_interval)  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '狼时',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能狼头伤害': max([damage_wolf, damage_wolf_min]),
            '技能dot伤害': max([damage_dot, damage_dot_min]),
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '普攻狼头伤害': max([damage_normal_wolf, damage_normal_wolf_min]),
            '技能覆盖率': skill_coverage_rate,
            '说明': '默认暖好1天赋, 狼头默认最高倍率, 不计算狼头飞行时间'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_luogesi_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_luogesi_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_luogesi_3_dps(buff_levels):
    """计算延异视阈的DPS"""
    buff_levels[8] = max([0, buff_levels[8] - 10])  # 天赋削抗
    module = 67  # 模组攻击力
    atk = (671 + 90 + 27 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.6 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = (atk * (1 + 3 + buff_levels[1] / 100) + buff_levels[2] + 165) * (1 - buff_levels[8] / 100) * mul * redu
    # 本体攻击伤害
    damage_min = (atk * (1 + 3 + buff_levels[1] / 100) + buff_levels[2] + 165) * 0.05 * mul * redu  # 本体攻击保底伤害
    damage_ex1 = (((atk * (1 + 3 + buff_levels[1] / 100) + buff_levels[2]) * 0.65 + 165) * (1 - buff_levels[8] / 100) * mul
                  * redu)  # 飞弹法术伤害
    damage_ex1_min = ((atk * (1 + 3 + buff_levels[1] / 100) + buff_levels[2]) * 0.65 + 165) * 0.05 * mul * redu
    # 飞弹法术保底伤害
    damage_ex2 = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.6  # 飞弹元素伤害

    damage_ave = (max([damage, damage_min]) + max([damage_ex1, damage_ex1_min])) * 0.6 + damage * 0.4  # 单次平a期望伤害
    damage_ave_min = damage_ave / (1 - buff_levels[8] / 100) * 0.05  # 单次平a期望保底伤害

    brock_time = 2000 / (max([damage_ave, damage_ave_min]) / atk_interval * 0.08)  # 单次爆条需要时间

    if brock_time <= 7.5:  # 计算技能期间爆条覆盖时间
        cover_rate = 30 - brock_time * 2
    elif brock_time <= 15:
        cover_rate = 15
    else:
        cover_rate = 30 - brock_time

    skill_coverage_rate = 30 / 75  # 技能覆盖率

    dps_1 = max([damage_ave, damage_ave_min]) / atk_interval  # 未爆条期间dps
    dps_2 = max([damage_ave, damage_ave_min]) / atk_interval + damage_ex2 * 0.6 / atk_interval + 800  # 爆条期间dps

    dps_equa = f'{dps_2} * {cover_rate} / 30 + {dps_1} * (30 - {cover_rate}) / 30'
    dps = dps_2 * cover_rate / 30 + dps_1 * (30 - cover_rate) / 30

    damage_total = dps * 30

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) + 165) * (1 - buff_levels[8] / 100) * mul * redu
    # 常态攻击伤害
    damage_normal_min = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) + 165) * 0.05 * mul * redu  # 常态保底伤害
    damage_ex1_normal = (((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.65 + 165) * (1 - buff_levels[8] / 100) *
                         mul * redu)  # 常态飞弹法术伤害
    damage_ex1_normal_min = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.65 + 165) * 0.05 * mul * redu
    # 常态飞弹保底法术伤害

    dps_normal_equa = (f'(max([{damage_normal}, {damage_normal_min}]) + '
                       f'max([{damage_ex1_normal}, {damage_ex1_normal_min}]) * 0.6) / '
                       f'{atk_interval}')  # 普攻dps计算公式
    dps_normal = ((max([damage_normal, damage_normal_min]) + max([damage_ex1_normal, damage_ex1_normal_min]) * 0.6) /
                  atk_interval)  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '来自河谷的笔盒',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能飞弹法术伤害': max([damage_ex1, damage_ex1_min]),
            '技能飞弹元素伤害(不吃脆弱易伤)': damage_ex2,
            '技能期间dps(未爆条)': dps_1,
            '技能期间dps(爆条)': dps_2,
            '技能爆条需要时间': brock_time,
            '技能期间爆条覆盖时间': cover_rate,
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '普攻飞弹法术伤害': max([damage_ex1_normal, damage_ex1_normal_min]),
            '技能覆盖率': skill_coverage_rate,
            '说明': '普攻期间默认不计爆条;技能不提前积累元素条;默认攻击boss敌人;未计算技能外爆条后续伤害'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_chengshan_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_chengshan_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_chengshan_3_dps(buff_levels):
    """计算澄净闪耀的DPS"""
    buff_levels[8] = max([0, min([buff_levels[8] - 15, 85])])  # 天赋法穿
    module = 38  # 模组攻击力
    atk = (331 + 60 + 25 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.3 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage_sign = ((atk * (1 + 0.8 + buff_levels[1] / 100) + buff_levels[2]) * 1.1 * (1 - buff_levels[8] / 100) * mul
                   * redu)  # 信标攻击伤害
    damage_sign_min = (atk * (1 + 0.8 + buff_levels[1] / 100) + buff_levels[2]) * 1.1 * 0.05 * mul * redu  # 信标攻击保底伤害

    damage_sign_boom = ((atk * (1 + 0.8 + buff_levels[1] / 100) + buff_levels[2]) * 3.6 * (1 - buff_levels[8] / 100) * mul *
                        redu)  # 信标暴击伤害
    damage_sign_boom_min = (atk * (1 + 0.8 + buff_levels[1] / 100) + buff_levels[2]) * 3.6 * 0.05 * mul * redu
    # 信标暴击保底伤害

    skill_coverage_rate = 30 / 65  # 技能覆盖率

    dps_equa = (f'((max([{damage_sign}, {damage_sign_min}]) * 0.9 + max([{damage_sign_boom}, {damage_sign_boom_min}]) * '
                f'0.1) * 3 / {atk_interval})')  # 技能dps计算公式
    dps = ((max([damage_sign, damage_sign_min]) * 0.9 + max([damage_sign_boom, damage_sign_boom_min]) * 0.1) * 3 /
           atk_interval)  # 技能dps

    damage_total = dps * 30

    damage_normal_sign = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.1 * (1 - buff_levels[8]) * mul *
                          redu)  # 常态攻击信标伤害
    damage_normal_sign_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.1 * 0.05 * mul * redu
    # 常态攻击信标保底伤害

    damage_normal = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * (1 - buff_levels[8]) * mul * redu
    # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 常态保底伤害

    dps_normal_equa = (f'(max([{damage_normal}, {damage_normal_min}]) +'
                       f' max([{damage_normal_sign}, {damage_normal_sign_min}]) * 2) / '
                       f'{atk_interval}')  # 普攻dps计算公式
    dps_normal = ((max([damage_normal, damage_normal_min]) + max([damage_normal_sign, damage_normal_sign_min])) /
                  atk_interval)  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '辛劳之翼',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能信标伤害': max([damage_sign, damage_sign_min]),
            '技能信标爆炸伤害': max([damage_sign_boom, damage_sign_boom_min]),
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '普攻信标伤害': max([damage_normal_sign, damage_normal_sign_min]),
            '技能覆盖率': skill_coverage_rate,
            '说明': '开启技能时信标默认最高倍率,不考虑转火'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_aila_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_aila_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_aila_3_dps(buff_levels):
    """计算博萨克风暴的DPS"""
    buff_levels[6] = max([buff_levels[6], 35])  # 脆弱取地雷和给定buff之间的最大值
    module = 60  # 模组攻击力
    atk = (588 + 80 + 32 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 0.5 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔
    atk_interval_normal = 0.85 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的普攻攻击间隔
    atk_time = atk_interval * 40  # 打完技能需要时间

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 0.9 + buff_levels[1] / 100) + buff_levels[2]) * 1.8 - buff_levels[7]) * mul * redu
    # 技能攻击伤害
    damage_min = (atk * (1 + 0.9 + buff_levels[1] / 100) + buff_levels[2]) * 1.8 * 0.05 * mul * redu  # 技能攻击保底伤害

    skill_coverage_rate = atk_time / (34 + atk_time)  # 技能覆盖率

    dps_equa = f'max([{damage}, {damage_min}]) / {atk_interval}'  # 技能dps计算公式
    dps = max([damage, damage_min]) / atk_interval  # 技能dps

    damage_total = max([damage, damage_min]) * 40

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu  # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 常态保底伤害
    damage_normal_strike = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.8 - buff_levels[7]) * mul * redu
    # 常态暴击伤害
    damage_normal_strike_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.8 * 0.05 * mul * redu
    # 常态暴击保底伤害

    dps_normal_equa = (f'(max([{damage_normal}, {damage_normal_min}]) * 0.5 +  '
                       f'max([{damage_normal_strike}, {damage_normal_strike_min}]) * 0.5) / {atk_interval_normal}')
    # 普攻dps计算公式
    dps_normal = ((max([damage_normal, damage_normal_min]) * 0.5 +
                  max([damage_normal_strike, damage_normal_strike_min]) * 0.5) / atk_interval_normal)  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '社会期望背包',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '普攻攻击间隔': atk_interval_normal,
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '技能持续时间': atk_time,
            '技能覆盖率': skill_coverage_rate,
            '说明': '默认技能期间地雷全覆盖,普攻期间不覆盖'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_xinyuenengtianshi_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_xinyuenengtianshi_2_dps(buff_levels):
    """计算开火成瘾症的DPS"""
    module = 65  # 模组攻击力
    atk = (708 + 70 + 30 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 0.6 / (1 + 0.7 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔
    atk_interval_normal = 1.3 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的普攻攻击间隔
    atk_time = atk_interval * 40  # 打完技能需要时间

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 0.26 + buff_levels[1] / 100) + buff_levels[2]) * 3 - buff_levels[7]) * mul * redu
    # 技能攻击伤害
    damage_min = (atk * (1 + 0.26 + buff_levels[1] / 100) + buff_levels[2]) * 3 * 0.05 * mul * redu  # 技能攻击保底伤害

    damage_strike = ((atk * (1 + 0.26 + buff_levels[1] / 100) + buff_levels[2]) * 2 - buff_levels[7]) * mul * redu
    # 轰炸伤害
    damage_strike_min = (atk * (1 + 0.26 + buff_levels[1] / 100) + buff_levels[2]) * 2 * 0.05 * mul * redu
    # 轰炸保底伤害

    skill_coverage_rate = atk_time / (30 + atk_time)  # 技能覆盖率

    dps_equa = f'max([{damage}, {damage_min}]) + max([{damage_strike, damage_strike_min}]) * 0.35 / {atk_interval}'  # 技能dps计算公式
    dps = (max([damage, damage_min]) + max([damage_strike, damage_strike_min]) * 0.35) / atk_interval  # 技能dps

    damage_total = max([damage, damage_min]) * 40 + max([damage_strike, damage_strike_min]) * 40 * 0.35

    damage_normal = ((atk * (1 + 0.26 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu  # 常态攻击伤害
    damage_normal_min = (atk * (1 + 0.26 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 常态保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval_normal}'
    # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval_normal  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '新朋友圣城生活套组',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '轰炸伤害': max([damage_strike, damage_strike_min]),
            '普攻攻击间隔': atk_interval_normal,
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '技能持续时间': atk_time,
            '技能覆盖率': skill_coverage_rate,
            '说明': '默认触发偷攻速,不计算技能前摇'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_xinyuenengtianshi_3_dps(buff_levels):
    """计算使命必达!的DPS"""
    module = 65  # 模组攻击力
    atk = (708 + 70 + 30 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.3 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔
    atk_interval_normal = 1.3 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的普攻攻击间隔
    atk_time = atk_interval * 10  # 打完技能需要时间

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 0.26 + 0.3 + buff_levels[1] / 100) + buff_levels[2]) * 1.6 - buff_levels[7]) * mul * redu
    # 技能攻击伤害
    damage_min = (atk * (1 + 0.26 + 0.3 + buff_levels[1] / 100) + buff_levels[2]) * 1.6 * 0.05 * mul * redu  # 技能攻击保底伤害

    damage_strike = ((atk * (1 + 0.26 + 0.3 + buff_levels[1] / 100) + buff_levels[2]) * 2 - buff_levels[7]) * mul * redu
    # 轰炸伤害
    damage_strike_min = (atk * (1 + 0.26 + 0.3 + buff_levels[1] / 100) + buff_levels[2]) * 2 * 0.05 * mul * redu
    # 轰炸保底伤害

    damage_boom = ((atk * (1 + 0.26 + 0.3 + buff_levels[1] / 100) + buff_levels[2]) * 2 - buff_levels[7]) * mul * redu
    # 投递爆炸伤害
    damage_boom_min = (atk * (1 + 0.26 + 0.3 + buff_levels[1] / 100) + buff_levels[2]) * 2 * 0.05 * mul * redu
    # 投递爆炸保底伤害

    skill_coverage_rate = atk_time / (35 + atk_time)  # 技能覆盖率

    dps_equa = f'(max([{damage}, {damage_min}]) + max([{damage_strike, damage_strike_min}]) * 0.35) * 5 / {atk_interval}'  # 技能dps计算公式
    dps = (max([damage, damage_min]) + max([damage_strike, damage_strike_min]) * 0.35) * 5 / atk_interval  # 技能dps

    damage_total = max([damage, damage_min]) * 50 + max([damage_strike, damage_strike_min]) * 50 * 0.35

    damage_normal = ((atk * (1 + 0.26 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu  # 常态攻击伤害
    damage_normal_min = (atk * (1 + 0.26 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 常态保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval_normal}'
    # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval_normal  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '新朋友圣城生活套组',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '轰炸伤害': max([damage_strike, damage_strike_min]),
            '投递爆炸伤害': max([damage_boom, damage_boom_min]),
            '普攻攻击间隔': atk_interval_normal,
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '技能持续时间': atk_time,
            '技能覆盖率': skill_coverage_rate,
            '说明': '计算dps和总伤时未计入投递爆炸伤害'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_jianmodekesasi_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_jianmodekesasi_2_dps(buff_levels):
    """计算阵雨连绵的DPS"""
    buff_levels[8] = buff_levels[8] * 0.7  # 天赋削法抗
    module = 65  # 模组攻击力
    atk = (569 + 90 + 22 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 0.93 / (1 + 0.1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 0.55 + 0.28 + buff_levels[1] / 100) + buff_levels[2]) * (1 - buff_levels[8] / 100) * mul
              * redu)  # 技能攻击伤害
    damage_min = (atk * (1 + 0.55 + 0.28 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 技能攻击保底伤害

    damage_boom = ((atk * (1 + 0.55 + 0.28 + buff_levels[1] / 100) + buff_levels[2]) * 2.4 *
                   (1 - buff_levels[8] / 100) * mul * redu)  # 踩一脚伤害
    damage_boom_min = ((atk * (1 + 0.55 + 0.28 + buff_levels[1] / 100) + buff_levels[2]) * 2.4 *
                       0.05 * mul * redu)  # 踩一脚保底伤害

    dps_equa = (f'(max([{damage_boom}, {damage_boom_min}]) + max([{damage}, {damage_min}]) * 10 / '
                f'{atk_interval}) / 10')  # 技能dps计算公式
    dps = (max([damage_boom, damage_boom_min]) + max([damage, damage_min]) * 2 * 10 / atk_interval) / 10  # 技能dps

    damage_total = dps * 10

    damage_normal = '不计算'  # 常态攻击伤害
    damage_normal_min = '不计算'  # 常态保底伤害

    dps_normal_equa = '不计算'  # 普攻dps计算公式
    dps_normal = '不计算'  # 普攻dps

    dps_cycle_equa = '不计算'  # 周期dps计算公式
    dps_cycle = '不计算'  # 周期dps

    hero = {'模组': '蓝莓与黑巧',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能爆发伤害': max([damage_boom, damage_boom_min]),
            '说明': '技能结束立即撤退, 不考虑技能刷新, 不考虑前后摇'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_jianmodekesasi_3_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_qilinRyedao_1_dps(buff_levels):
    """计算鬼人化的DPS"""
    module = 48  # 模组攻击力
    atk = (565 + 90 + 22 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 0.93 / (1 + 1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul_pyh = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    mul_mag = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 0.23 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul_pyh * redu
    # 技能攻击伤害
    damage_min = (atk * (1 + 0.9 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul_pyh * redu
    # 技能攻击保底伤害
    damage_magic = ((atk * (1 + 0.23 + buff_levels[1] / 100) + buff_levels[2]) * 0.2 * (1 - buff_levels[8]) * mul_mag
                    * redu)  # 攻击附带法伤
    damage_magic_min = (atk * (1 + 0.23 + buff_levels[1] / 100) + buff_levels[2]) * 0.2 * 0.05 * mul_mag * redu
    # 攻击附带保底法伤

    skill_coverage_rate = 20 / 36  # 技能覆盖率

    dps_equa = (f'(max([{damage}, {damage_min}]) + max([{damage_magic}, {damage_magic_min}])) * '
                f'10 / 4 / {atk_interval}')  # 技能dps计算公式
    dps = ((max([damage, damage_min]) + max([damage_magic, damage_magic_min])) * 10 / 4 / atk_interval * redu)  # 技能dps

    damage_total = dps * 20

    dps_cycle_equa = f'{dps} * {skill_coverage_rate}'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate  # 周期dps

    hero = {'模组': '训练用木桩',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能攻击法术伤害': max([damage_magic, damage_magic_min]),
            '技能覆盖率': skill_coverage_rate,
            '说明': '技能结束立即撤退, 未计算技能前摇'
            }

    return dps_equa, dps, '不站场', '不站场', dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_qilinRyedao_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_qilinRyedao_3_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_shuiyue_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_shuiyue_2_dps(buff_levels):
    """计算囚徒困境的DPS"""
    module = 125  # 模组攻击力
    atk = (865 + 110 + 32 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 2 / (1 + 0.5 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔
    atk_interval_normal = 3.5 / (1 + 0.5 + buff_levels[5] / 100)  # 计算攻速条件下的普攻攻击间隔
    atk_time = atk_interval * 10  # 打完技能需要时间

    mul_phy = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    mul_mag = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 法术易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 0.3 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul_phy * redu  # 技能攻击伤害
    damage_min = (atk * (1 + 0.3 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul_phy * redu  # 技能攻击保底伤害

    damage_mag = (atk * (1 + 0.3 + buff_levels[1] / 100) + buff_levels[2]) * 0.5 * buff_levels[8] / 100 * mul_mag * redu  # 天赋法伤
    damage_mag_min = (atk * (1 + 0.3 + buff_levels[1] / 100) + buff_levels[2]) * 0.5 * 0.05 * mul_mag * redu  # 天赋保底法伤

    skill_coverage_rate = 21 / 36  # 技能覆盖率

    dps_equa = f'(max([{damage}, {damage_min}]) + max([{damage_mag, damage_mag_min}])) / {atk_interval}'  # 技能dps计算公式
    dps = (max([damage, damage_min]) + max([damage_mag, damage_mag_min])) / atk_interval  # 技能dps

    damage_total = dps * 21

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul_phy * redu  # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul_phy * redu  # 常态保底伤害

    damage_normal_mag = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.5 * buff_levels[7] / 100) * mul_mag * redu  # 常态攻击伤害
    damage_normal_mag_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.5 * 0.05 * mul_mag * redu  # 常态保底伤害

    dps_normal_equa = f'(max([{damage_normal}, {damage_normal_min}]) + max([{damage_normal_mag, damage_normal_mag_min}])) / {atk_interval_normal}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) + max([damage_normal_mag, damage_normal_mag_min]) / atk_interval_normal  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '水月特限证章',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '天赋法伤': max([damage_mag, damage_mag_min]),
            '普攻攻击间隔': atk_interval_normal,
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '普攻天赋法伤': max([damage_normal_mag, damage_normal_mag_min]),
            '技能持续时间': atk_time,
            '技能覆盖率': skill_coverage_rate,
            '说明': '不计算二天赋加成(需要计算的话在局内乘算内加上)'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_shuiyue_3_dps(buff_levels):
    """计算镜花水月的DPS"""
    module = 125  # 模组攻击力
    atk = (865 + 110 + 32 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 3.5 / (1 + 0.5 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔
    atk_interval_normal = 3.5 / (1 + 0.5 + buff_levels[5] / 100)  # 计算攻速条件下的普攻攻击间隔
    atk_time = atk_interval * 10  # 打完技能需要时间

    control_cover_rate = min([1, 1 / atk_interval])

    mul_phy = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    mul_mag = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 法术易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 1.5 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul_phy * redu  # 技能攻击伤害
    damage_min = (atk * (1 + 1.5 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul_phy * redu  # 技能攻击保底伤害

    damage_mag = (atk * (1 + 1.5 + buff_levels[1] / 100) + buff_levels[2]) * 0.5 * buff_levels[8] / 100 * mul_mag * redu  # 天赋法伤
    damage_mag_min = (atk * (1 + 1.5 + buff_levels[1] / 100) + buff_levels[2]) * 0.5 * 0.05 * mul_mag * redu  # 天赋保底法伤

    skill_coverage_rate = 30 / 90  # 技能覆盖率

    dps_equa = f'(max([{damage}, {damage_min}]) + max([{damage_mag, damage_mag_min}])) / {atk_interval}'  # 技能dps计算公式
    dps = (max([damage, damage_min]) + max([damage_mag, damage_mag_min])) / atk_interval  # 技能dps

    damage_total = dps * 30

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul_phy * redu  # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul_phy * redu  # 常态保底伤害

    damage_normal_mag = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.5 * buff_levels[7] / 100) * mul_mag * redu  # 常态攻击伤害
    damage_normal_mag_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.5 * 0.05 * mul_mag * redu  # 常态保底伤害

    dps_normal_equa = f'(max([{damage_normal}, {damage_normal_min}]) + max([{damage_normal_mag, damage_normal_mag_min}])) / {atk_interval_normal}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) + max([damage_normal_mag, damage_normal_mag_min]) / atk_interval_normal  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '水月特限证章',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '眩晕覆盖率': control_cover_rate,
            '技能攻击伤害': max([damage, damage_min]),
            '天赋法伤': max([damage_mag, damage_mag_min]),
            '普攻攻击间隔': atk_interval_normal,
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '普攻天赋法伤': max([damage_normal_mag, damage_normal_mag_min]),
            '技能持续时间': atk_time,
            '技能覆盖率': skill_coverage_rate,
            '说明': '不计算二天赋加成(需要计算的话在局内乘算内加上)'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_mitu_1_dps(buff_levels):
    """计算关键线索的DPS"""
    module = 33
    atk = (566 + 40 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1 / (1 + 0.05 + buff_levels[5] / 100)  # 计算攻速条件下的技能攻击间隔

    mul_phy = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    mul_mag = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 法术易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 3 - buff_levels[7]) * mul_phy * redu
    # 技能攻击伤害
    damage_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 3 * 0.05 * mul_phy * redu
    # 保底技能攻击伤害
    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul_phy * redu
    # 普攻伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul_phy * redu
    # 普攻保底伤害

    dps_cycle_equa = f'(max([{damage}, {damage_min}]) + max([{damage_normal}, {damage_normal_min}]) * 5) / {atk_interval} / 6'
    # 周期dps计算公式
    dps_cycle = (max([damage, damage_min]) + max([damage_normal, damage_normal_min]) * 5) / atk_interval / 6  # 周期dps

    damage_total = damage  # 总伤

    hero = {'模组': '首要任务',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '周期回费效率(费用/s)': atk_interval / 2,
            '说明': '只计算周期dps;不考虑天赋'
            }

    return '不计', '不计', '不计', '不计', dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_mitu_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_xunlan_1_dps(buff_levels):
    """计算探寻的DPS"""
    module = 0
    atk = (560 + 40 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1 / (1 + 0.15 + buff_levels[5] / 100)  # 计算攻速条件下的技能攻击间隔

    mul_phy = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 1 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul_phy * redu
    # 技能攻击伤害
    damage_min = (atk * (1 + 1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul_phy * redu
    # 保底技能攻击伤害

    dps_equa = f'max([{damage}, {damage_min}]) / {atk_interval}'
    # 技能dps计算公式
    dps = max([damage, damage_min]) / atk_interval  # 技能dps

    damage_total = dps * 20  # 总伤

    hero = {'模组': '佳肴',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能期间回费': 20 / atk_interval,
            '说明': '只计算技能dps,不考虑站场;默认触发模组加攻速'
            }

    return dps_equa, dps, '不站场', '不站场', '不计算', '不计算', damage_total, hero


def calculate_xunlan_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_xiaoge_1_dps(buff_levels):
    """计算观火的DPS"""
    module = 33
    atk = (560 + 30 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1 / (1 + 0.20 + buff_levels[5] / 100)  # 计算攻速条件下的技能攻击间隔

    mul_phy = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 1 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul_phy * redu
    # 技能攻击伤害
    damage_min = (atk * (1 + 1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul_phy * redu
    # 保底技能攻击伤害

    dps_equa = f'max([{damage}, {damage_min}]) / {atk_interval}'
    # 技能dps计算公式
    dps = max([damage, damage_min]) / atk_interval  # 技能dps

    damage_total = dps * 20  # 总伤

    hero = {'模组': '不发声者',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能期间回费': 20 / atk_interval,
            '说明': '只计算技能dps,不考虑站场;默认触发被动加攻速'
            }

    return dps_equa, dps, '不站场', '不站场', '不计算', '不计算', damage_total, hero


def calculate_xiaoge_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_zhanche_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_zhanche_2_dps(buff_levels):
    """计算倾泻弹药的DPS"""
    module = 55
    atk = (621 + 40 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = max([1.3 * 0.15 / (1 + buff_levels[5] / 100), 0.1])  # 计算攻速条件下的技能攻击间隔
    atk_interval_normal = 1.3 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的普攻攻击间隔

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.1 - buff_levels[7]) * mul * redu  # 攻击伤害
    damage_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.1 * 0.05 * 1.1 * mul * redu  # 保底伤害

    damage_strike = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2 - buff_levels[7]) * 1.1 * mul * redu
    # 暴击伤害
    damage_strike_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2 * 0.05 * 1.1 * mul * redu  # 暴击保底伤害

    skill_coverage_rate = 4 / (4 + 25 * atk_interval_normal)  # 技能覆盖率

    dps_equa = (f'(max([{damage}, {damage_min}]) * 0.85 + max([{damage_strike}, {damage_strike_min}]) * 0.15) * 2 / '
                f'{atk_interval}')  # 技能dps计算公式
    dps = (max([damage, damage_min]) * 0.85 + max([damage_strike, damage_strike_min]) * 0.15) * 2 / atk_interval
    # 技能dps

    damage_total = dps * 4

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu  # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 常态保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) * 2 / {atk_interval_normal}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) * 2 / atk_interval_normal  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '轻机枪枪架',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能暴击伤害': max([damage_strike, damage_strike_min]),
            '技能覆盖率': skill_coverage_rate,
            '普攻攻击伤害': max([damage_normal, damage_normal_min]),
            '说明': '已考虑动画帧数下限'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_amiya_jinwei_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_amiya_jinwei_2_dps(buff_levels):
    """计算影宵绝影的DPS"""
    module = 45  # 模组攻击力
    atk = (657 + 45 + 28 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.25 / (1 + buff_levels[5] / 100)  # 计技能攻击间隔

    mul = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 法伤易伤和脆弱
    mul_real = (1 + buff_levels[11] / 100) * (1 + buff_levels[6] / 100)  # 真伤易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage_impact = (atk * (1 + 0.18 +buff_levels[1] / 100) + buff_levels[2]) * 2.2 * (1 - buff_levels[8]) * mul * redu
    # 斩击单段伤害
    damage_impact_min = (atk * (1 + 0.18 + buff_levels[1] / 100) + buff_levels[2]) * 2.2 * 0.05 * mul * redu
    # 斩击单段保底伤害
    damage_impact_final = (atk * (1 + 0.18 + buff_levels[1] / 100) + buff_levels[2]) * 4.4 * mul_real  # 斩击尾刀伤害

    damage = (atk * (1 + 0.18 + buff_levels[1] / 100) + buff_levels[2]) * mul_real  # 技能攻击伤害

    # skill_coverage_rate = 50 / 120  # 技能覆盖率

    dps_equa = f'{damage} / {atk_interval} + max([{damage_impact}, {damage_impact_min}]) / 32'  # 技能dps计算公式
    dps = damage / atk_interval + (max([damage_impact, damage_impact_min]) * 9 + damage_impact_final) / 35

    damage_total_impact = max([damage_impact, damage_impact_min]) * 9 + damage_impact_final
    damage_total = dps * 35

    damage_normal = (atk * (1 + 0.09 + buff_levels[1] / 100) + buff_levels[2]) * (1 - buff_levels[8]) * mul * redu  # 常态攻击伤害
    damage_normal_min = (atk * (1 + 0.09 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 常态攻击保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval  # 普攻dps

    hero = {'模组': '待调弦的怒火',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '斩击单段伤害': max([damage_impact, damage_impact_min]),
            '斩击尾刀伤害': damage_impact_final,
            '斩击总伤': damage_total_impact,
            '技能攻击伤害': damage,
            '说明': '计算dps时未计算斩击时间,默认没有击杀敌人(想加的话在局内里加)'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, '不计算', '不计算', damage_total, hero


def calculate_huihao_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_huihao_2_dps(buff_levels):
    """计算专注轰击的DPS"""
    module = 70
    atk = (865 + 50 + 32 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 2.8 * 0.35 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔
    atk_interval_normal = 2.8 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的普攻攻击间隔

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 0.2 + 0.55 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu  # 攻击伤害
    damage_min = (atk * (1 + 0.2 + 0.55 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 保底伤害

    skill_coverage_rate = 10 / 28  # 技能覆盖率

    dps_equa = f'max([{damage}, {damage_min}]) / {atk_interval}'  # 技能dps计算公式
    dps = max([damage, damage_min]) / atk_interval
    # 技能dps

    damage_total = dps * 10

    damage_normal = ((atk * (1 + 0.2 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu
    # 常态攻击伤害
    damage_normal_min = (atk * (1 + 0.2 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 常态保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '出门必备套装',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能覆盖率': skill_coverage_rate,
            '普攻攻击伤害': max([damage_normal, damage_normal_min]),
            '说明': '默认触发天赋'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_hanmangkeluosi_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_hanmangkeluosi_2_dps(buff_levels):
    """计算封喉的DPS"""
    module = 31
    atk = (502 + 75 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 0.625 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔
    atk_interval_normal = 1 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的普攻攻击间隔

    heating_time = atk_interval * 16  # 暖机时间

    hit_times = 32 + (30 - heating_time) / atk_interval * 4  # 技能期间攻击次数

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu  # 攻击伤害
    damage_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 保底伤害

    damage_fireworks = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2 - buff_levels[7]) * mul * redu  # 烟花手伤害
    damage_fireworks_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2 * 0.05 * mul * redu  # 烟花手保底伤害

    damage_strike = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.75 - buff_levels[7]) * mul * redu
    # 暴击伤害
    damage_strike_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.75 * 0.05 * mul * redu  # 暴击保底伤害

    skill_coverage_rate = 30 / 75  # 技能覆盖率

    dps_equa = f'({hit_times} * 0.8 * max([{damage}, {damage_min}]) + {hit_times} * 0.2 * max([{damage_strike},{damage_strike_min}])) / 30'
    # 技能dps计算公式
    dps = (hit_times * 0.8 * max([damage, damage_min]) + hit_times * 0.2 * max([damage_strike, damage_strike_min])) / 30
    # 技能dps
    dps_fireworks = (hit_times * 0.8 * max([damage, damage_min]) + hit_times * 0.2 * max([damage_strike,damage_strike_min]) + hit_times * 0.25 * max([damage_fireworks, damage_fireworks_min])) / 30
    # 带烟花技能dps

    damage_total = dps * 30
    damage_total_fireworks = dps_fireworks * 30

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul * redu  # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 常态保底伤害

    damage_normal_strike = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.75 - buff_levels[7]) * mul * redu
    # 常态暴击伤害
    damage_normal_strike_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.75 * 0.05 * mul * redu
    # 常态暴击保底伤害

    dps_normal_equa = (f'(max([{damage_normal}, {damage_normal_min}]) * 0.67 + max([{damage_normal_strike},'
                       f' {damage_normal_strike_min}]) * 0.33) / 1')  # 普攻dps计算公式
    dps_normal = ((max([damage_normal_min, damage_normal]) * 0.8 +
                   max([damage_normal_strike, damage_normal_strike_min]) * 0.2) / atk_interval_normal)  # 普攻dps
    dps_normal_fireworks = (max([damage_normal_min, damage_normal]) * 0.8 + max([damage_normal_strike, damage_normal_strike_min]) * 0.2 + max([damage_fireworks, damage_fireworks_min]) * 0.2) / atk_interval_normal  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps
    dps_cycle_fireworks = dps_fireworks * skill_coverage_rate + dps_normal_fireworks * (1 - skill_coverage_rate)  # 周期dps(带烟花)

    hero = {'模组': '真心的话和想冒的险',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '暖机时间': heating_time,
            '技能期间攻击次数': hit_times,
            '技能攻击伤害': max([damage, damage_min]),
            '技能暴击伤害': max([damage_strike, damage_strike_min]),
            '烟花手伤害': max([damage_fireworks, damage_fireworks_min]),
            '技能覆盖率': skill_coverage_rate,
            '说明': '默认不触发模组对空增伤'
            }

    return dps_equa, f'\n{dps}(无烟花)\n{dps_fireworks}(带烟花)', dps_normal_equa, f'\n{dps_normal}(无烟花)\n{dps_normal_fireworks}(带烟花)', dps_cycle_equa, f'\n{dps_cycle}(无烟花)\n{dps_cycle_fireworks}(带烟花)', f'\n{damage_total}(无烟花)\n{damage_total_fireworks}(带烟花)', hero


def calculate_rongquan_1_dps(buff_levels):
    """计算信号矢的DPS"""
    buff_levels[7] = buff_levels[7] * 0.7
    module = 75
    atk = (954 + 95 + 34 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 2.4 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.8 * 1.7 - buff_levels[7]) * mul * redu  # 攻击伤害
    damage_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.8 * 1.7 * 0.05 * mul * redu  # 保底伤害

    skill_coverage_rate = 20 / 45  # 技能覆盖率

    dps_equa = f'max([{damage}, {damage_min}]) / {atk_interval}'  # 技能dps计算公式
    dps = max([damage, damage_min]) / atk_interval
    # 技能dps

    damage_total = dps * 20

    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.7 - buff_levels[7]) * mul * redu
    # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.7 * 0.05 * mul * redu  # 常态保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'  # 周期dps计算公式
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '弩箭调试箱',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '技能覆盖率': skill_coverage_rate,
            '普攻攻击伤害': max([damage_normal, damage_normal_min]),
            '说明': '默认攻击萨卡兹敌人'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_rongquan_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_amiya_yiliao_1_dps(buff_levels):
    """计算哀恸共情的DPS"""
    module = 40  # 模组攻击力
    atk = (532 + 45 + 22 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.6 / (1 + 0.75 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 法伤易伤和脆弱
    mul_real = (1 + buff_levels[11] / 100) * (1 + buff_levels[6] / 100)  # 真伤易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * (1 - buff_levels[8]) * mul * redu  # 技能攻击伤害
    damage_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 技能攻击保底伤害

    skill_coverage_rate = 50 / 120  # 技能覆盖率

    dps_equa = f'max([{damage}, {damage_min}]) / {atk_interval}'  # 技能dps计算公式
    dps = max([damage, damage_min]) / atk_interval  # 技能dps

    hps = dps / 2 + (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.25 / atk_interval  # 技能hps计算公式

    damage_total = dps * 50

    damage_normal = damage  # 常态攻击伤害
    damage_normal_min = damage_min # 常态攻击保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {1.6 * (1 + buff_levels[5] / 100)}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / 1.6 * (1 + buff_levels[5] / 100)  # 普攻dps

    dps_cycle_equa = f'{dps} * {skill_coverage_rate} + {dps_normal} * (1 - {skill_coverage_rate})'
    dps_cycle = dps * skill_coverage_rate + dps_normal * (1 - skill_coverage_rate)  # 周期dps

    hero = {'模组': '带有灼痕的裙子',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            'hps': hps,
            '技能覆盖率': skill_coverage_rate,
            '说明': '未计算治疗量增加buff'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_amiya_yiliao_2_dps(buff_levels):
    """计算慈悲愿景的DPS"""
    module = 40  # 模组攻击力
    atk = (532 + 45 + 22 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.6 / (1 + 0.75 + buff_levels[5] / 100)  # 计算攻速条件下的攻击间隔

    mul = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 法伤易伤和脆弱
    mul_real = (1 + buff_levels[11] / 100) * (1 + buff_levels[6] / 100)  # 真伤易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage_impact = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2 * (1 - buff_levels[8]) * mul * redu
    # 技能前置伤害
    damage_impact_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 2 * 0.05 * mul * redu
    # 技能保底前置伤害
    damage = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * mul_real  # 技能攻击伤害

    # skill_coverage_rate = 50 / 120  # 技能覆盖率

    dps_equa = f'{damage} / {atk_interval} + max([{damage_impact}, {damage_impact_min}]) / 32'  # 技能dps计算公式
    dps = damage / atk_interval + max([damage_impact, damage_impact_min]) / 32
    hps = damage / atk_interval /2

    damage_total = dps * 32

    damage_normal = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * (1 - buff_levels[8]) * mul * redu  # 常态攻击伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul * redu  # 常态攻击保底伤害

    dps_normal_equa = f'max([{damage_normal}, {damage_normal_min}]) / {atk_interval}'  # 普攻dps计算公式
    dps_normal = max([damage_normal, damage_normal_min]) / atk_interval  # 普攻dps

    hero = {'模组': '带有灼痕的裙子',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '盖人伤害': max([damage_impact, damage_impact_min]),
            '技能攻击伤害': damage,
            'hps': hps,
            '说明': '未计算治疗效果提升buff;计算hps时默认打1,打2就乘2,不计算盖人的奶量;默认不盖人,要算上盖人加的攻可以在局内加攻里加上'
            }

    return dps_equa, dps, dps_normal_equa, dps_normal, '不计算', '不计算', damage_total, hero


def calculate_amiya_1_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_amiya_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_amiya_3_dps(buff_levels):
    """计算奇美拉的DPS"""
    module = 50  # 模组攻击力
    atk = (612 + 70 + 30 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1.6 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的技能攻击间隔

    mul_real = (1 + buff_levels[11] / 100) * (1 + buff_levels[6] / 100)  # 真伤易伤和脆弱
    mul_mag = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 法术易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 常态攻击的减伤和闪避

    damage = (atk * (1 + 2.3 + buff_levels[1] / 100) + buff_levels[2]) * mul_real  # 技能伤害

    skill_coverage_rate = '未计算'  # 技能覆盖率

    dps_equa = f'{damage} / {atk_interval} '  # 技能dps计算公式
    dps = damage / atk_interval

    damage_total = dps * 30

    hero = {'模组': 'DWDB-221E',
            '攻击力': atk,
            '攻击间隔': atk_interval,
            '技能攻击伤害': damage,
            }

    return dps_equa, dps, '未计算', '未计算', '未计算', '未计算', damage_total, hero


def calculate_mei_1_dps(buff_levels):
    """计算麻痹弹的DPS"""
    module = 27
    atk = (478 + 65 + 23 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1 / (1 + 0.08 + buff_levels[5] / 100)  # 计算攻速条件下的技能攻击间隔

    cover_rate = min([2.5 / (atk_interval * 4), 1])  # 停顿覆盖率

    mul_phy = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    mul_mag = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 法术易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + 0.13 + buff_levels[1] / 100) + buff_levels[2]) * 2 - buff_levels[7]) * mul_phy * redu
    # 技能攻击伤害
    damage_min = (atk * (1 + 0.13 +buff_levels[1] / 100) + buff_levels[2]) * 2 * 0.05 * mul_phy * redu
    # 保底技能攻击伤害
    damage_normal = ((atk * (1 + 0.13 + buff_levels[1] / 100) + buff_levels[2]) - buff_levels[7]) * mul_phy * redu
    # 普攻伤害
    damage_normal_min = (atk * (1 + 0.13 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul_phy * redu
    # 普攻保底伤害
    damage_fireworks = ((atk * (1 + 0.13 + buff_levels[1] / 100) + buff_levels[2]) * 2 - buff_levels[7]) * mul_phy * redu
    # 烟花手伤害
    damage_fireworks_min = (atk * (1 + 0.13 + buff_levels[1] / 100) + buff_levels[2]) * 2 * 0.05 * mul_phy * redu
    # 烟花手保底伤害

    dps_cycle_equa = f'(max([{damage}, {damage_min}]) + max([{damage_normal}, {damage_normal_min}]) * 3) / {atk_interval} / 4'
    # 周期dps计算公式
    dps_cycle = (max([damage, damage_min]) + max([damage_normal, damage_normal_min]) * 3) / (atk_interval * 4)  # 周期dps
    dps_cycle_fireworks = (max([damage, damage_min]) + max([damage_normal, damage_normal_min]) * 3 + 0.8 * max([damage_fireworks, damage_fireworks_min])) / (atk_interval * 4)  # 周期dps

    damage_total = damage  # 总伤

    hero = {'模组': '新手侦探礼包',
            '攻击力': atk,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '烟花手伤害': max([damage_fireworks, damage_fireworks_min]),
            '说明': '只计算周期dps, 不考虑模组对空增伤'
            }

    return '不计', '不计', '不计', '不计', dps_cycle_equa, f'\n{dps_cycle}(无烟花)\n{dps_cycle_fireworks}(带烟花)', damage_total, hero


def calculate_mei_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'


def calculate_liuxing_1_dps(buff_levels):
    """计算碎甲击的DPS"""
    deff = buff_levels[7] * 0.75
    module = 30
    atk = (465 + 65 + 23 + module) * (1 + buff_levels[0] / 100)  # 先计算局外加攻
    atk_interval = 1 / (1 + buff_levels[5] / 100)  # 计算攻速条件下的技能攻击间隔

    mul_phy = (1 + buff_levels[3] / 100) * (1 + buff_levels[6] / 100)  # 物理易伤和脆弱
    mul_mag = (1 + buff_levels[4] / 100) * (1 + buff_levels[6] / 100)  # 法术易伤和脆弱
    redu = (1 - buff_levels[9] / 100) * (1 - buff_levels[10] / 100)  # 减伤和闪避

    damage = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.8 - deff) * mul_phy * redu
    # 技能攻击伤害
    damage_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 1.8 * 0.05 * mul_phy * redu
    # 保底技能攻击伤害
    damage_normal = ((atk * (1 + buff_levels[1] / 100) + buff_levels[2]) - deff) * mul_phy * redu
    # 普攻伤害
    damage_normal_min = (atk * (1 + buff_levels[1] / 100) + buff_levels[2]) * 0.05 * mul_phy * redu
    # 普攻保底伤害

    dps_cycle_equa = f'(max([{damage}, {damage_min}]) + max([{damage_normal}, {damage_normal_min}]) * 3) / {atk_interval} / 4'
    # 周期dps计算公式
    dps_cycle_1 = (max([damage, damage_min]) + max([damage_normal, damage_normal_min]) * 4) / (
                atk_interval * 5)  # 周期dps

    dps_cycle_2 = (max([((atk * (1 + 0.13 + buff_levels[1] / 100) + buff_levels[2]) * 2 * 1.1 * 1.55 - deff) *
                        mul_phy * redu,
                        (atk * (1 + 0.13 + buff_levels[1] / 100) + buff_levels[2]) * 2 * 1.1 * 1.55 * 0.05 *
                        mul_phy * redu]) +
                   max([((atk * (1 + 0.13 + buff_levels[1] / 100) + buff_levels[2]) * 1.1 * 1.55 - deff) *
                        mul_phy * redu,
                        (atk * (1 + 0.13 + buff_levels[1] / 100) + buff_levels[2]) * 1.1 * 1.55 * 0.05 *
                        mul_phy * redu]) * 3) / (atk_interval * 4)

    damage_total = damage  # 总伤
    dps_cycle = f'\n{dps_cycle_1}(不对空)\n{dps_cycle_2}(对空)'

    hero = {'模组': '猎刀',
            '攻击力': atk,
            '敌方护甲(减防后)': deff,
            '技能攻击间隔': atk_interval,
            '技能攻击伤害': max([damage, damage_min]),
            '普攻伤害': max([damage_normal, damage_normal_min]),
            '说明': '只计算周期dps;内置技能减防公式,直接写敌方原护甲(计算藏品减防后)'
            }

    return '不计', '不计', '不计', '不计', dps_cycle_equa, dps_cycle, damage_total, hero


def calculate_liuxing_2_dps(buff_levels):
    return 0, 0, 0, 0, 0, 0, 0, '开发中'

