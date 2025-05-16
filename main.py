import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, \
    QGridLayout
import damage_calculator
from process_output import process_output



class DpsCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # 初始化UI
    def initUI(self):
        self.setWindowTitle("明日方舟dps计算器")

        # 主布局
        layout = QVBoxLayout()

        # 第一行：星级、职业、干员、技能
        start_layout = QHBoxLayout()
        self.start_label = QLabel("星级：")
        self.start_combo = QComboBox()
        self.start_combo.addItems(["六星", "五星", "四星"])
        self.start_combo.currentIndexChanged.connect(self.update_job_combo)

        self.job_label = QLabel("职业：")
        self.job_combo = QComboBox()
        self.name_combo = QComboBox()  # 插入干员名选择框
        self.skill_combo = QComboBox()  # 技能选择框
        self.update_job_combo(0)  # 初始化职业和干员

        self.name_label = QLabel("干员：")
        self.name_combo.currentIndexChanged.connect(self.update_skill_combo)
        self.job_combo.currentIndexChanged.connect(self.update_name_combo)

        self.skill_label = QLabel("技能：")

        start_layout.addWidget(self.start_label)
        start_layout.addWidget(self.start_combo)
        start_layout.addWidget(self.job_label)
        start_layout.addWidget(self.job_combo)
        start_layout.addWidget(self.name_label)
        start_layout.addWidget(self.name_combo)
        start_layout.addWidget(self.skill_label)
        start_layout.addWidget(self.skill_combo)
        layout.addLayout(start_layout)

        # 第二行：输入框
        input_layout = QGridLayout()
        self.num1_label = QLabel("局外加攻：")
        self.num2_label = QLabel("局内加攻（乘算）：")
        self.num3_label = QLabel("局内加攻（加算）：")
        self.num1_edit = QLineEdit()
        self.num2_edit = QLineEdit()
        self.num3_edit = QLineEdit()

        input_layout.addWidget(self.num1_label, 0, 0)
        input_layout.addWidget(self.num1_edit, 0, 1)
        input_layout.addWidget(self.num2_label, 0, 2)
        input_layout.addWidget(self.num2_edit, 0, 3)
        input_layout.addWidget(self.num3_label, 0, 4)
        input_layout.addWidget(self.num3_edit, 0, 5)
        layout.addLayout(input_layout)


        self.num4_label = QLabel("物理易伤：")
        self.num5_label = QLabel("法术易伤：")
        self.num6_label = QLabel("攻速：")
        self.num4_edit = QLineEdit()
        self.num5_edit = QLineEdit()
        self.num6_edit = QLineEdit()

        input_layout.addWidget(self.num4_label, 1, 0)
        input_layout.addWidget(self.num4_edit, 1, 1)
        input_layout.addWidget(self.num5_label, 1, 2)
        input_layout.addWidget(self.num5_edit, 1, 3)
        input_layout.addWidget(self.num6_label, 1, 4)
        input_layout.addWidget(self.num6_edit, 1, 5)
        layout.addLayout(input_layout)

        self.num7_label = QLabel("脆弱：")
        self.num8_label = QLabel("敌方护甲：")
        self.num9_label = QLabel("敌方法抗：")
        self.num7_edit = QLineEdit()
        self.num8_edit = QLineEdit()
        self.num9_edit = QLineEdit()

        input_layout.addWidget(self.num7_label, 2, 0)
        input_layout.addWidget(self.num7_edit, 2, 1)
        input_layout.addWidget(self.num8_label, 2, 2)
        input_layout.addWidget(self.num8_edit, 2, 3)
        input_layout.addWidget(self.num9_label, 2, 4)
        input_layout.addWidget(self.num9_edit, 2, 5)
        layout.addLayout(input_layout)

        self.num10_label = QLabel("敌方减伤：")
        self.num11_label = QLabel("敌方闪避：")
        self.num12_label = QLabel("真伤易伤：")
        self.num10_edit = QLineEdit()
        self.num11_edit = QLineEdit()
        self.num12_edit = QLineEdit()

        input_layout.addWidget(self.num10_label, 3, 0)
        input_layout.addWidget(self.num10_edit, 3, 1)
        input_layout.addWidget(self.num11_label, 3, 2)
        input_layout.addWidget(self.num11_edit, 3, 3)
        input_layout.addWidget(self.num12_label, 3, 4)
        input_layout.addWidget(self.num12_edit, 3, 5)
        layout.addLayout(input_layout)

        self.num1_edit.setText("0")
        self.num2_edit.setText("0")
        self.num3_edit.setText("0")
        self.num4_edit.setText("0")
        self.num5_edit.setText("0")
        self.num6_edit.setText("0")
        self.num7_edit.setText("0")
        self.num8_edit.setText("0")
        self.num9_edit.setText("0")
        self.num10_edit.setText("0")
        self.num11_edit.setText("0")
        self.num12_edit.setText("0")

        # 第四行：执行按钮
        self.calc_button = QPushButton("计算")
        self.calc_button.clicked.connect(self.calculate)
        layout.addWidget(self.calc_button)

        # 第五行：重置按钮
        self.reset_button = QPushButton("重置")
        self.reset_button.clicked.connect(self.reset)
        layout.addWidget(self.reset_button)

        # 第五行：干员数值展示
        self.showdata_label = QLabel('干员信息：')
        self.showdata_label.setWordWrap(True)  # 开启自动换行
        self.showdata_label.setFixedWidth(450)  # 设置最大行长
        layout.addWidget(self.showdata_label)

        # 第六行：计算公式
        self.calcproc_label = QLabel('计算过程：')
        self.calcproc_label.setWordWrap(True)  # 开启自动换行
        self.calcproc_label.setFixedWidth(450)  # 设置最大行长
        layout.addWidget(self.calcproc_label)

        # 第七行：结果显示
        self.result_label = QLabel("计算结果：")
        self.result_label.setWordWrap(True)  # 开启自动换行
        self.result_label.setFixedWidth(450)  # 设置最大行长
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    # 更新职业列表
    def update_job_combo(self, index):
        """根据星级更新职业列表"""
        start_jobes = {
            "六星": ["先锋", "近卫", "重装", "辅助", "狙击", "医疗", "术士", "特种"],
            "五星": ["先锋", "近卫", "重装", "辅助", "狙击", "医疗", "术士", "特种"],
            "四星": ["先锋", "近卫", "重装", "辅助", "狙击", "医疗", "术士", "特种"]
        }
        selected_start = self.start_combo.currentText()
        self.job_combo.clear()
        self.job_combo.addItems(start_jobes.get(selected_start, []))
        self.update_name_combo()  # 更新组别列表

    # 更新干员列表
    def update_name_combo(self):
        """根据星级和职业更新干员列表"""
        names = {
            "六星": {
                "先锋": ["风笛", "伊内丝"],
                "近卫": ["锏", "银灰", "仇白", "玛恩纳", "乌尔比安","赫德雷", "佩佩", "史尔特尔", "维娜", "耀骑士临光"],
                "重装": ["号角", "黍"],
                "辅助": ["浊心斯卡蒂", "魔王"],
                "狙击": ["维什戴尔", "莱伊", "蕾缪安", "空弦"],
                "医疗": ['纯烬艾雅法拉', '焰影苇草', 'Mon3tr'],
                "术士": ['荒芜拉普兰德', '逻各斯', '澄闪'],
                "特种": ['艾拉', '新约能天使', '缄默德克萨斯', '麒麟R夜刀', '水月']
                },
            "五星": {
                "先锋": ["谜图", "寻澜", "晓歌"],
                "近卫": ["战车", "阿米娅(近卫)"],
                "重装": ["灰毫"],
                "狙击": ["寒芒克洛丝", "熔泉"],
                "医疗": ["阿米娅(医疗)"],
                "术士": ["阿米娅(术士)"],
                "特种": []
                },
            "四星": {
                "先锋": [],
                "近卫": [],
                "重装": [],
                "狙击": ["梅", "流星"],
                "医疗": [],
                "术士": [],
                "特种": []
                }
        }
        selected_start = self.start_combo.currentText()
        selected_job = self.job_combo.currentText()
        self.name_combo.clear()
        self.name_combo.addItems(names.get(selected_start, {}).get(selected_job, []))
        self.update_skill_combo()  # 更新学生列表

    # 更新技能列表
    def update_skill_combo(self):
        """根据星级、职业和干员更新技能列表"""
        skill_data = {
            "六星": {
                "先锋": {
                    "风笛": ["迅捷打击γ", "高效冲击", "闭膛连发"],
                    "伊内丝": ["淬影突袭", "暗夜无明", "独影归途"]
                },
                "近卫": {
                    "锏": ["纯粹的武力", "无声的嘲笑", "归于宁静"],
                    "银灰": ["强力击·γ型", "雪境生存法则", "真银斩"],
                    "仇白": ["留羽", "承影", "问雪"],
                    "玛恩纳": ["未声张的怒火", "未宽解的悲哀", "未照耀的荣光"],
                    "乌尔比安": ["必须促成的接触", "必须维系的界限", "必须开辟的道路"],
                    "赫德雷": ["重锋不熄", "余烬重荷", "死境硝烟"],
                    "佩佩": ["盖戳", "阻遏混乱锤", "时光震荡"],
                    "史尔特尔": ["烈焰魔剑", "熔核巨影", "黄昏"],
                    "维娜": ["重铸晖光", "进赴故土", "俱以我之名"],
                    "耀骑士临光": ["灿焰长刃", "逐夜烁光", "耀阳颔首"]
                },
                "重装": {
                    "号角": ["照明榴弹", "暴风号令", "终极防线"],
                    "黍": ["化被草木", "嘉禾盈仓", "离离枯荣"]
                },
                "辅助": {
                    "浊心斯卡蒂": ["同归殊途之吟", "同葬无光之愿", "潮涌,潮枯"],
                    "魔王": ["往昔萦绕身旁", "明日渺远不及", "编织重构现世"]
                },
                "狙击": {
                    "维什戴尔": ['定点清算', '饱和复仇', '爆裂黎明'],
                    "莱伊": ['脱身矢', '广域警觉', '得见光芒'],
                    "蕾缪安": ['重逢问候', '归乡邀约', '礼炮·强制追思'],
                    "空弦": ['箭矢·散逸', '箭矢·追猎', '箭矢·暴风']
                },
                "医疗": {
                    "纯烬艾雅法拉": ['无声润物', '云霭荫佑', '火山回响'],
                    "焰影苇草": ['迅捷打击·γ型', '枯荣共息', '生命火种'],
                    "Mon3tr": ['策略:超压链接', '策略:超负荷', '策略:熔毁']
                },
                "术士": {
                    "荒芜拉普兰德": ['慵怠者悲鸣', '逐猎狂飙', '终幕·浩劫'],
                    "逻各斯": ['殁亡', '提喻', '延异视阈'],
                    "澄闪": ['火花四溅', '电流翻涌', '澄净闪耀']
                },
                "特种": {
                    "艾拉": ['眩目阻滞', '震荡坚守', '博萨克风暴'],
                    "新约能天使": ['天空大扫除', '开火成瘾症', '使命必达!'],
                    "缄默德克萨斯": ['细雨无声', '阵雨连绵', '剑雨滂沱'],
                    "麒麟R夜刀": ['鬼人化', '乱舞', '空中回旋乱舞'],
                    "水月": ['唤醒', '囚徒困境', '镜花水月']
                }
            },
            "五星": {
                "先锋": {
                    "谜图": ['关键线索', '疑点追踪'],
                    "寻澜": ['探寻', '洞悉'],
                    "晓歌": ['观火', '浮光'],
                    },
                "近卫": {
                    "战车": ['燃烧榴弹', '倾泻弹药'],
                    "阿米娅(近卫)": ['影霄·奔夜', '影霄·绝影']
                    },
                "重装": {
                    "灰毫": ['攻击力强化·γ型', '专注轰击']
                    },
                "狙击": {
                    "寒芒克洛丝": ["无痕", "封喉"],
                    "熔泉": ['信号矢', '便携破城矢']
                },
                "医疗": {
                    "阿米娅(医疗)": ['哀恸共情', '慈悲愿景']
                },
                "术士": {
                    "阿米娅(术士)": ["战术咏唱·γ型", '精神爆发', '奇美拉']
                },
                "特种": {

                }
            },
            "四星": {
                "先锋": {
                    },
                "近卫": {
                    },
                "重装": {
                    },
                "狙击": {
                    "梅": ['麻痹弹', '束缚电击'],
                    "流星": ['碎甲击', '碎甲击·扩散']
                }
            }
        }
        selected_start = self.start_combo.currentText()
        selected_job = self.job_combo.currentText()
        selected_name = self.name_combo.currentText()
        self.skill_combo.clear()
        self.skill_combo.addItems(
            skill_data.get(selected_start, {}).get(selected_job, {}).get(selected_name, []))

    # 计算
    def calculate(self):
        """执行计算并显示结果"""
        try:
            # 增幅
            num1 = float(self.num1_edit.text())  # 局外加攻
            num2 = float(self.num2_edit.text())  # 局内加攻（乘算）
            num3 = float(self.num3_edit.text())  # 局内加攻（加算）
            num4 = float(self.num4_edit.text())  # 物理易伤
            num5 = float(self.num5_edit.text())  # 法术易伤
            num6 = float(self.num6_edit.text())  # 攻速
            num7 = float(self.num7_edit.text())  # 脆弱
            num8 = float(self.num8_edit.text())  # 敌方护甲
            num9 = float(self.num9_edit.text())  # 敌方法抗
            num10 = float(self.num10_edit.text())  # 敌方减伤
            num11 = float(self.num11_edit.text())  # 敌方闪避
            num12 = float(self.num12_edit.text())  # 真伤易伤
            buff_level = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12]

            dps_equa, dps, normal_dps_equa, normal_dps, cycle_dps_equa, cycle_dps, total_damage, hero = process_output(
                damage_calculator.calculate_dps(self.name_combo.currentText(), self.skill_combo.currentText(),
                                                buff_level))
            self.showdata_label.setText(f'干员信息：\n'
                                        f'{hero}')
            self.calcproc_label.setText(f'计算过程： \n'
                                        f'技能dps：{dps_equa}\n'
                                        f'普攻dps：{normal_dps_equa}\n'
                                        f'周期dps：{cycle_dps_equa}')

            self.result_label.setText(f'计算结果： \n'
                                      f'技能dps：{dps}\n'
                                      f'普攻dps：{normal_dps}\n'
                                      f'周期dps：{cycle_dps}\n'
                                      f'技能总伤:{total_damage}')

            if self.name_combo.currentText() in ['黍']:
                self.calcproc_label.setText(f'计算过程： \n'
                                            f'技能dps：{dps_equa}\n'
                                            f'技能hps：{normal_dps_equa}')

                self.result_label.setText(f'计算结果： \n'
                                          f'技能dps：{dps}\n'
                                          f'技能hps：{normal_dps}\n')

        except ValueError:
            self.result_label.setText("请输入有效的数字")

    def reset(self):
        try:
            self.num1_edit.setText("0")
            self.num2_edit.setText("0")
            self.num3_edit.setText("0")
            self.num4_edit.setText("0")
            self.num5_edit.setText("0")
            self.num6_edit.setText("0")
            self.num7_edit.setText("0")
            self.num8_edit.setText("0")
            self.num9_edit.setText("0")
            self.num10_edit.setText("0")
            self.num11_edit.setText("0")
            self.num12_edit.setText("0")
            self.showdata_label.setText('干员信息：')
            self.calcproc_label.setText('计算过程：')
            self.result_label.setText('计算过程：')
        except ValueError:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = DpsCalculator()
    calc.setGeometry(100, 100, 300, 600)
    calc.show()
    sys.exit(app.exec_())
