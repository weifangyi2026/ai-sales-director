# main.py
# 爆款拆解学习工具 - 纯Python标准库，零依赖
# 作者：运营小白专用版
# 用法：直接运行 python main.py

import datetime
import re


# ==================== 工具函数 ====================

def get_now_date():
    """获取当前日期时间字符串"""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def input_multiline(prompt):
    """支持多行输入，输入 END 单独一行结束"""
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    return "\n".join(lines)


# ==================== 第3步：AI 自动生成拆解报告 ====================

def analyze_douyin(text):
    """抖音分析：侧重前3秒钩子和节奏"""
    # 取前3秒内容（约前30-50字）
    first_50 = text[:50]
    
    # 钩子词库
    hook_words = ["没想到", "竟然", "震惊", "绝了", "千万别", "一定要", "原来", "终于",
                  "揭秘", "真相", "99%的人", "所有人", "注意", "小心", "后悔", "救命",
                  "天呐", "破防", "离谱", "谁懂", "家人们", "居然", "难道", "告诉你",
                  "如果你", "当你", "知道吗", "3秒", "1分钟", "10秒", "5个", "3个",
                  "最后", "结果", "爆火", "全网", "刷屏"]
    
    # 节奏词
    rhythm_words = ["然后", "接着", "但是", "可是", "然而", "突然", "最后", "第一步",
                    "第二步", "接下来", "这时候", "瞬间", "直接", "马上", "立刻"]
    
    # 互动词
    cta_words = ["点赞", "关注", "收藏", "评论", "转发", "分享", "主页", "直播间",
                 "小黄车", "链接", "评论区", "私信", "告诉我", "你也是这样吗",
                 "有没有同款", "对不对", "同意吗", "赶紧", "快"]
    
    # 统计命中
    hooks = [w for w in hook_words if w in text[:80]]
    rhythms = [w for w in rhythm_words if w in text]
    ctas = [w for w in cta_words if w in text]
    
    # 节奏感：短句数量（5-25字为短句）
    sentences = re.split(r'[。！!？?\n]', text)
    short_count = 0
    for s in sentences:
        s = s.strip()
        if 5 <= len(s) <= 25:
            short_count += 1
    
    # 情绪标点
    emotion = text.count("!") + text.count("！") + text.count("?") + text.count("？")
    
    # 数字出现次数
    numbers = len(re.findall(r'\d+', text))
    
    # 生成报告
    report = []
    report.append("=" * 50)
    report.append("              📱 抖音爆款因子分析报告")
    report.append("=" * 50)
    report.append("")
    report.append("【一、前3秒钩子力】")
    report.append("  首屏内容：" + first_50[:40] + "...")
    report.append("  检测到钩子词：" + (", ".join(hooks) if hooks else "无"))
    if len(hooks) >= 2:
        report.append("  ✅ 前3秒具备强钩子，符合黄金3秒法则")
    elif len(hooks) == 1:
        report.append("  ⚠️ 有1个钩子词，建议再加强冲突感或悬念感")
    else:
        report.append("  ❌ 前3秒无明显钩子，建议加入冲突/悬念/利益承诺")
    report.append("")
    
    report.append("【二、节奏感】")
    report.append("  短句数量（5-25字）：" + str(short_count) + " 句")
    report.append("  节奏词：" + (", ".join(rhythms) if rhythms else "无"))
    if short_count >= 5:
        report.append("  ✅ 节奏明快，适合短视频快速消费")
    else:
        report.append("  ⚠️ 建议多用短句、分段，加快信息传递节奏")
    report.append("")
    
    report.append("【三、互动引导力】")
    report.append("  互动词：" + (", ".join(ctas) if ctas else "无"))
    if len(ctas) >= 2:
        report.append("  ✅ 有明确的互动指令，利于算法推流")
    elif len(ctas) == 1:
        report.append("  ⚠️ 互动引导较弱，建议增加行动指令")
    else:
        report.append("  ❌ 无明显互动引导，结尾建议加CTA")
    report.append("")
    
    report.append("【四、情绪感染力】")
    report.append("  情绪标点（!/?）：" + str(emotion) + " 个")
    if emotion >= 3:
        report.append("  ✅ 情绪饱满，易引发共鸣")
    else:
        report.append("  ⚠️ 建议增加情绪词、感叹号或反问")
    report.append("")
    
    report.append("【五、信息密度】")
    report.append("  数字出现次数：" + str(numbers) + " 次")
    if numbers >= 2:
        report.append("  ✅ 数据化表达，增强可信度")
    else:
        report.append("  ⚠️ 建议用具体数字替代模糊表述")
    report.append("")
    
    # 综合诊断
    total_score = len(hooks) * 15 + short_count * 5 + len(ctas) * 10
    if total_score > 80:
        diagnosis = "🔥 强爆款体质，钩子+节奏+互动三角闭环"
    elif total_score > 40:
        diagnosis = "💡 有潜力，建议重点优化" + ("钩子" if len(hooks) < 2 else "互动" if len(ctas) < 2 else "节奏")
    else:
        diagnosis = "🌱 基础薄弱，建议从重写前3秒开始"
    
    report.append("【综合诊断】")
    report.append("  " + diagnosis)
    report.append("  核心建议：前3秒抓眼球 → 中段快节奏 → 结尾强互动")
    report.append("=" * 50)
    
    # 返回报告字符串和关键因子列表
    factors = {
        "钩子词": hooks,
        "节奏词": rhythms,
        "互动词": ctas,
        "短句数": short_count,
        "情绪标点": emotion,
        "数字": numbers
    }
    return "\n".join(report), factors


def analyze_xiaohongshu(text):
    """小红书分析：侧重封面和关键词"""
    # 标题（首行或前30字）
    title = text[:30]
    
    # 爆款标题词
    title_words = ["绝了", "封神", "天花板", "挖到宝", "后悔没早点", "亲测", "保姆级",
                   "手把手", "纯干货", "宝藏", "小众", "被问爆", "闭眼入", "0基础",
                   "新手", "小白", "必看", "攻略", "合集", "测评", "推荐", "避雷",
                   "避坑", "清单", "教程", "指南", "沉浸式", "一整个"]
    
    # 痛点词
    pain_words = ["焦虑", "迷茫", "内耗", "自卑", "胖", "丑", "穷", "累", "困", "秃",
                  "黄", "黑", "痘痘", "细纹", "暗沉", "干燥", "出油", "脱发", "失眠",
                  "便秘", "痛经", "社恐", "尴尬", "踩雷", "翻车"]
    
    # 干货词
    value_words = ["方法", "技巧", "步骤", "公式", "模板", "口诀", "秘诀", "捷径",
                   "思路", "逻辑", "底层", "认知", "干货", "经验", "总结", "整理",
                   "盘点", "对比", "区别", "教程", "攻略"]
    
    # Emoji
    emojis = ["🔥", "✨", "💯", "🌟", "❗", "❓", "💡", "🎉", "👍", "💪", "🆘", "📝",
              "🎁", "💰", "❤", "⭐", "🌈", "🙏", "😭", "😍", "👀", "🤔", "👉"]
    
    # 统计
    titles = [w for w in title_words if w in text[:60]]
    pains = [w for w in pain_words if w in text]
    values = [w for w in value_words if w in text]
    emo_found = [e for e in emojis if e in text]
    
    # 结构（序号、项目符号）
    structure = len(re.findall(r'[①②③④⑤❶❷❸❹❺·•\d+\.]', text)) + text.count("\n")
    
    # 标签模拟
    tags = []
    if any(w in text for w in ["穿搭", "衣服", "OOTD", "搭配", "衣橱"]):
        tags.append("穿搭")
    if any(w in text for w in ["护肤", "美妆", "化妆", "口红", "粉底", "眼影"]):
        tags.append("美妆")
    if any(w in text for w in ["减肥", "健身", "瑜伽", "减脂", "瘦", "运动"]):
        tags.append("健身")
    if any(w in text for w in ["学习", "考研", "英语", "读书", "备考", "单词"]):
        tags.append("学习")
    if any(w in text for w in ["职场", "简历", "面试", "升职", "领导", "同事"]):
        tags.append("职场")
    if any(w in text for w in ["家居", "装修", "收纳", "厨房", "卧室"]):
        tags.append("家居")
    if any(w in text for w in ["旅行", "旅游", "酒店", "攻略", "景点"]):
        tags.append("旅行")
    if not tags:
        tags.append("生活/综合")
    
    report = []
    report.append("=" * 50)
    report.append("              📕 小红书爆款因子分析报告")
    report.append("=" * 50)
    report.append("")
    report.append("【一、封面/标题吸引力】")
    report.append("  标题预览：" + title[:35] + "...")
    report.append("  爆款关键词：" + (", ".join(titles) if titles else "无"))
    if len(titles) >= 2:
        report.append("  ✅ 标题具备高点击率特征")
    elif len(titles) == 1:
        report.append("  ⚠️ 标题吸引力一般，建议加入数字或情绪词")
    else:
        report.append("  ❌ 标题较平淡，建议用'数字+情绪+身份'公式")
    report.append("")
    
    report.append("【二、痛点共鸣力】")
    report.append("  痛点词：" + (", ".join(pains) if pains else "无"))
    if len(pains) >= 2:
        report.append("  ✅ 精准击中用户痛点，代入感强")
    elif len(pains) == 1:
        report.append("  ⚠️ 有1个痛点，建议开篇先强化共鸣")
    else:
        report.append("  ❌ 无明显痛点，小红书用户先看'这说的是我'")
    report.append("")
    
    report.append("【三、干货价值感】")
    report.append("  干货关键词：" + (", ".join(values) if values else "无"))
    if len(values) >= 3:
        report.append("  ✅ 信息密度高，收藏转发价值大")
    elif len(values) >= 1:
        report.append("  ⚠️ 干货密度一般，建议增加步骤/清单/模板")
    else:
        report.append("  ❌ 干货感不足，建议给出可落地的方法论")
    report.append("")
    
    report.append("【四、视觉友好度】")
    report.append("  Emoji使用：" + str(len(emo_found)) + " 个")
    report.append("  结构标记/分段：" + str(structure) + " 处")
    if len(emo_found) >= 2 and structure >= 5:
        report.append("  ✅ 排版清爽，适合小红书图文阅读")
    else:
        report.append("  ⚠️ 建议多用Emoji分段、加序号，提升可读性")
    report.append("")
    
    report.append("【五、赛道标签】")
    report.append("  识别领域：" + " / ".join(tags))
    report.append("  建议标签：#" + tags[0] + " #" + tags[0] + "干货 #" + tags[0] + "分享")
    report.append("")
    
    # 综合
    total = len(titles) * 15 + len(pains) * 15 + len(values) * 10 + len(emo_found) * 5
    if total > 80:
        diag = "🔥 典型小红书爆款：痛点+干货+清单体"
    elif total > 40:
        diag = "💡 有基础，建议强化" + ("标题" if len(titles) < 2 else "痛点" if len(pains) < 2 else "干货")
    else:
        diag = "🌱 建议重写标题，并加入痛点+清单结构"
    
    report.append("【综合诊断】")
    report.append("  " + diag)
    report.append("  核心公式：痛点标题 → 经历共鸣 → 步骤干货 → 互动提问")
    report.append("=" * 50)
    
    factors = {
        "标题词": titles,
        "痛点": pains,
        "干货": values,
        "Emoji": emo_found,
        "结构": structure,
        "赛道": tags
    }
    return "\n".join(report), factors


def analyze_shipinhao(text):
    """视频号分析：侧重信任感和私域钩子"""
    # 信任词
    trust_words = ["从业", "做了", "年", "经验", "专业", "专家", "创始人", "老师",
                   "博士", "硕士", "研究", "专注", "深耕", "累计", "服务过", "帮助",
                   "学员", "客户", "案例", "实测", "亲身经历", "亲眼", "亲测", "数据",
                   "报告", "权威", "官方", "认证", "资质"]
    
    # 私域钩子
    private_words = ["微信", "V", "加", "私聊", "私信", "领取", "资料", "福利", "群",
                     "社群", "扫码", "二维码", "链接", "主页", "简介", "关注", "添加",
                     "助理", "顾问", "免费", "赠送", "礼包", "名额", "预约", "咨询",
                     "诊断", "体验", "找我", "联系我"]
    
    # 故事词
    story_words = ["曾经", "那时候", "刚开始", "后来", "直到有一天", "记得", "故事",
                   "经历", "历程", "过程", "转折", "逆袭", "翻身", "蜕变", "成长",
                   "从0到1", "一路", "创业", "负债", "裸辞", "裁员", "离婚", "低谷",
                   "迷茫", "觉醒", "顿悟", "感悟", "心得"]
    
    # 认知词
    value_words = ["认知", "思维", "格局", "底层逻辑", "本质", "真相", "规律", "趋势",
                   "风口", "机会", "红利", "赛道", "模型", "方法论", "体系", "闭环",
                   "链路", "生态", "维度", "高度"]
    
    # 统计
    trusts = [w for w in trust_words if w in text]
    privates = [w for w in private_words if w in text]
    stories = [w for w in story_words if w in text]
    values = [w for w in value_words if w in text]
    
    # 人设感
    persona = text.count("我") + text.count("我们") + text.count("本人")
    
    report = []
    report.append("=" * 50)
    report.append("              🎬 视频号爆款因子分析报告")
    report.append("=" * 50)
    report.append("")
    report.append("【一、信任感建设】")
    report.append("  信任关键词：" + (", ".join(trusts) if trusts else "无"))
    if len(trusts) >= 3:
        report.append("  ✅ 快速建立专业人设，降低决策门槛")
    elif len(trusts) >= 1:
        report.append("  ⚠️ 信任背书较弱，建议亮明身份/年限/成果")
    else:
        report.append("  ❌ 无明显信任状，视频号用户很看重'你是谁'")
    report.append("")
    
    report.append("【二、私域导流力】")
    report.append("  私域钩子词：" + (", ".join(privates) if privates else "无"))
    if len(privates) >= 3:
        report.append("  ✅ 有明确的私域承接路径，利于沉淀用户")
    elif len(privates) >= 1:
        report.append("  ⚠️ 私域引导较弱，建议明确给出添加理由")
    else:
        report.append("  ❌ 无私域钩子，视频号核心在私域转化，建议增加")
    report.append("")
    
    report.append("【三、故事感染力】")
    report.append("  故事线索词：" + (", ".join(stories) if stories else "无"))
    if len(stories) >= 3:
        report.append("  ✅ 用故事包裹观点，接受度高")
    elif len(stories) >= 1:
        report.append("  ⚠️ 故事性一般，建议用个人经历增强真实感")
    else:
        report.append("  ❌ 偏说教，建议用'曾经…后来…现在…'结构")
    report.append("")
    
    report.append("【四、认知价值感】")
    report.append("  认知/思维词：" + (", ".join(values) if values else "无"))
    if len(values) >= 2:
        report.append("  ✅ 输出高维认知，易引发转发")
    elif len(values) >= 1:
        report.append("  ⚠️ 认知深度一般，建议从'是什么'升级到'为什么'")
    else:
        report.append("  ❌ 价值感偏浅，建议加入底层逻辑或反常识观点")
    report.append("")
    
    report.append("【五、人设真实感】")
    report.append("  第一人称出现次数：" + str(persona) + " 次")
    if persona >= 5:
        report.append("  ✅ 人设鲜明，真实感强")
    else:
        report.append("  ⚠️ 建议多用'我'的视角，像朋友聊天")
    report.append("")
    
    # 综合
    total = len(trusts) * 15 + len(privates) * 20 + len(stories) * 10 + len(values) * 10
    if total > 100:
        diag = "🔥 视频号高转化模型：信任+故事+私域钩子"
    elif total > 50:
        diag = "💡 有基础，建议补齐" + ("信任背书" if len(trusts) < 2 else "私域钩子" if len(privates) < 2 else "故事线")
    else:
        diag = "🌱 视频号需要'真人真事真经验'，建议从人设建立开始"
    
    report.append("【综合诊断】")
    report.append("  " + diag)
    report.append("  核心公式：身份锚定 → 故事引入 → 认知升级 → 私域承接")
    report.append("  提示：视频号完播率不如抖音重要，关键是信任转粉+私域添加")
    report.append("=" * 50)
    
    factors = {
        "信任": trusts,
        "私域": privates,
        "故事": stories,
        "认知": values,
        "人设": persona
    }
    return "\n".join(report), factors


# ==================== 第5步：AI 对比点评 ====================

def compare_review(platform, ai_factors, user_note):
    """将用户心得与AI报告对比，像老师一样点评"""
    user_lower = user_note.lower()
    
    if platform == "1":
        platform_name = "抖音"
        checkpoints = {
            "前3秒钩子": ["钩子", "开头", "首句", "前3", "黄金", "开场", "第一眼", "吸引"],
            "节奏感": ["节奏", "快", "短句", "紧凑", "速度", "分段", "呼吸感"],
            "互动引导": ["互动", "点赞", "评论", "关注", "转发", "CTA", "引导", "指令"],
            "情绪感染": ["情绪", "感染力", "共鸣", "感叹", "反问", "上头", "破防"],
            "信息密度": ["数字", "数据", "量化", "具体", "统计", "密度"]
        }
        key_tip = "前3秒钩子"
        platform_logic = "抖音是'杀时间'逻辑，前3秒决定生死，节奏决定完播"
        
    elif platform == "2":
        platform_name = "小红书"
        checkpoints = {
            "封面标题": ["标题", "封面", "首图", "点击", "吸引", "眼球"],
            "痛点共鸣": ["痛点", "共鸣", "代入", "焦虑", "困扰", "问题", "说的是我"],
            "干货价值": ["干货", "步骤", "方法", "技巧", "教程", "清单", "可落地"],
            "视觉排版": ["排版", "结构", "分段", "emoji", "清晰", "可读", "舒服"],
            "标签搜索": ["标签", "赛道", "关键词", "搜索", "流量", "领域"]
        }
        key_tip = "封面标题和痛点共鸣"
        platform_logic = "小红书是'搜索+发现'双引擎，标题决定点击，干货决定收藏"
        
    else:
        platform_name = "视频号"
        checkpoints = {
            "信任背书": ["信任", "专业", "身份", "背书", "经验", "权威", "年限"],
            "私域钩子": ["私域", "微信", "添加", "领取", "社群", "转化", "导流", "沉淀"],
            "故事线": ["故事", "经历", "历程", "真实", "案例", "过程", "曾经"],
            "认知输出": ["认知", "思维", "底层", "本质", "格局", "升级", "反常识"],
            "人设感": ["人设", "真实", "个人", "IP", "形象", "第一人称"]
        }
        key_tip = "信任感和私域钩子"
        platform_logic = "视频号是'信任电商'逻辑，关系链推荐，私域沉淀比爆款更重要"
    
    # 检查用户提到了哪些
    praised = []
    missed = []
    suggestions = []
    
    for point, keywords in checkpoints.items():
        found = False
        for kw in keywords:
            if kw in user_lower:
                found = True
                break
        if found:
            praised.append(point)
        else:
            missed.append(point)
    
    # 生成点评
    if len(praised) >= 4:
        level = "🌟 优秀"
        comment = "你的拆解已经抓住了核心骨架，运营嗅觉很敏锐！"
    elif len(praised) >= 2:
        level = "📈 良好"
        comment = "你看到了部分亮点，但还有几个关键维度可以补充。"
    else:
        level = "🌱 入门"
        comment = "作为运营小白，先看到表面很正常。这次对比正是帮你建立系统框架的好机会。"
    
    # 遗漏建议
    if missed:
        suggestions.append("你暂时忽略了【" + "、".join(missed) + "】，而这正是" + key_tip + "的核心。")
        for m in missed:
            if m == "前3秒钩子":
                suggestions.append("→ 改进：先看前3秒有没有'冲突/悬念/利益承诺'，这是完播率的第一道闸门。")
            elif m == "节奏感":
                suggestions.append("→ 改进：注意句长和分段，短句制造呼吸感，长句容易让人划走。")
            elif m == "互动引导":
                suggestions.append("→ 改进：爆款往往在结尾埋了'行动指令'，引导算法推流。")
            elif m == "情绪感染":
                suggestions.append("→ 改进：情绪是抖音的燃料，看看作者用了哪些词让你'上头'。")
            elif m == "信息密度":
                suggestions.append("→ 改进：数字降低认知成本，'3个方法'比'一些方法'更有说服力。")
            elif m == "封面标题":
                suggestions.append("→ 改进：小红书标题就是封面，想想用了哪些'爆款标题公式'。")
            elif m == "痛点共鸣":
                suggestions.append("→ 改进：好的笔记先让你'觉得在说自己'，再给你解决方案。")
            elif m == "干货价值":
                suggestions.append("→ 改进：收藏率取决于'可落地性'，看有没有给步骤、清单、模板。")
            elif m == "视觉排版":
                suggestions.append("→ 改进：小红书是'读图'逻辑，分段、emoji、序号都是信息路标。")
            elif m == "标签搜索":
                suggestions.append("→ 改进：标签决定搜索流量，想想会出现在哪些关键词结果里。")
            elif m == "信任背书":
                suggestions.append("→ 改进：视频号用户更谨慎，作者如何快速让你相信'他说的是对的'？")
            elif m == "私域钩子":
                suggestions.append("→ 改进：视频号核心是私域，注意作者怎么自然把流量引到微信/社群。")
            elif m == "故事线":
                suggestions.append("→ 改进：故事是视频号的'糖衣'，把观点包在个人经历里，接受度翻倍。")
            elif m == "认知输出":
                suggestions.append("→ 改进：高转发内容往往输出'反常识认知'，让你想转发到朋友圈。")
            elif m == "人设感":
                suggestions.append("→ 改进：视频号讲究'真人真事'，看作者怎么让你感觉在跟朋友聊天。")
    
    review = []
    review.append("=" * 50)
    review.append("              🎓 AI老师对比点评报告")
    review.append("=" * 50)
    review.append("")
    review.append("【你的拆解水平】" + level)
    review.append(comment)
    review.append("")
    review.append("【你捕捉到的亮点】" + (" / ".join(praised) if praised else "（暂未捕捉到核心维度）"))
    review.append("")
    review.append("【你忽略的关键维度】" + (" / ".join(missed) if missed else "无，全面覆盖！"))
    review.append("")
    review.append("【针对性改进建议】")
    if suggestions:
        for s in suggestions:
            review.append(s)
    else:
        review.append("你已经考虑得很全面了！建议下一步：用这些维度去拆解一条低播放内容，")
        review.append("对比看看爆款和普通内容的差距到底在哪里。")
    review.append("")
    review.append("【平台底层逻辑提醒】")
    review.append("  " + platform_logic)
    review.append("")
    review.append("【下次拆解作业】")
    review.append("  找一条同赛道的'普通内容'（点赞<100），用今天学到的5个维度对比分析，")
    review.append("  你会更深刻理解：爆款不是偶然，是系统化的结果。")
    review.append("=" * 50)
    
    return "\n".join(review)


# ==================== 第6步：保存到文件 ====================

def save_to_file(platform_name, content, report, note, review):
    """追加保存到经验库文件"""
    filename = "经验库_每日积累.txt"
    date_line = get_now_date()
    
    lines = []
    lines.append("\n")
    lines.append("╔" + "═" * 58 + "╗")
    lines.append("║" + " " * 15 + "📚 每日拆解积累" + " " * 28 + "║")
    lines.append("║" + " 日期：" + date_line + " " * (50 - len(date_line)) + "║")
    lines.append("╠" + "═" * 58 + "╣")
    lines.append("║ 平台：" + platform_name + " " * (51 - len(platform_name)) + "║")
    lines.append("╠" + "═" * 58 + "╣")
    lines.append("║【原文案/图文内容】")
    lines.append("║" + "-" * 58)
    # 处理换行，保持格式
    for line in content.split("\n"):
        # 每行最多58字符，超出换行
        while len(line) > 58:
            lines.append("║ " + line[:58])
            line = line[58:]
        lines.append("║ " + line + " " * (57 - len(line)))
    lines.append("╠" + "═" * 58 + "╣")
    lines.append("║【AI 爆款因子分析报告】")
    lines.append("║" + "-" * 58)
    for line in report.split("\n"):
        while len(line) > 58:
            lines.append("║ " + line[:58])
            line = line[58:]
        lines.append("║ " + line + " " * (57 - len(line)))
    lines.append("╠" + "═" * 58 + "╣")
    lines.append("║【我的个人拆解心得】")
    lines.append("║" + "-" * 58)
    for line in note.split("\n"):
        while len(line) > 58:
            lines.append("║ " + line[:58])
            line = line[58:]
        lines.append("║ " + line + " " * (57 - len(line)))
    lines.append("╠" + "═" * 58 + "╣")
    lines.append("║【AI 老师对比点评】")
    lines.append("║" + "-" * 58)
    for line in review.split("\n"):
        while len(line) > 58:
            lines.append("║ " + line[:58])
            line = line[58:]
        lines.append("║ " + line + " " * (57 - len(line)))
    lines.append("╚" + "═" * 58 + "╝")
    lines.append("\n")
    
    # 追加写入
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print("\n✅ 已自动保存到文件：" + filename)
    except Exception as e:
        print("\n❌ 保存文件失败：" + str(e))


# ==================== 主程序 ====================

def main():
    print("=" * 60)
    print("   🚀 爆款拆解学习工具 v1.0 | 运营小白专用")
    print("   支持：抖音(1) | 小红书(2) | 视频号(3)")
    print("   多行输入结束时，单独输入 END 即可")
    print("=" * 60)
    print()
    
    # 步骤1：选择平台
    while True:
        print("请选择平台：")
        print("  1 = 抖音（侧重：前3秒钩子 + 节奏）")
        print("  2 = 小红书（侧重：封面标题 + 关键词）")
        print("  3 = 视频号（侧重：信任感 + 私域钩子）")
        choice = input(">>> ").strip()
        if choice in ("1", "2", "3"):
            break
        print("❌ 输入错误，请重新输入 1、2 或 3\n")
    
    platform_names = {"1": "抖音", "2": "小红书", "3": "视频号"}
    platform_name = platform_names[choice]
    print("\n✅ 已选择：" + platform_name + "\n")
    
    # 步骤2：粘贴文案
    content = input_multiline("请粘贴爆款文案/图文内容（输入 END 结束）：")
    if not content.strip():
        print("⚠️ 未检测到内容，使用示例文案演示...")
        if choice == "1":
            content = "救命！我真的会谢！3秒告诉你为什么99%的人减肥都失败了！不是你不努力，是你根本不知道这个底层逻辑！点赞收藏，看完这条视频你会回来感谢我的！"
        elif choice == "2":
            content = "🔥被问爆的早八通勤妆！5分钟搞定伪素颜✨\n\n姐妹们谁懂啊！每天多睡30分钟真的太香了！\n\n💡步骤超简单：\n① 防晒+隔离二合一\n② 气垫快速拍全脸\n③ 眉毛+口红提气色\n\n亲测有效！新手小白也能闭眼入！\n\n#早八妆容 #通勤妆 #伪素颜"
        else:
            content = "我做了15年财税，服务过3000多家企业，今天说一个得罪人的真相：为什么你的公司总是缺现金流？不是生意不好，是你根本看不懂这三张表。加我微信，免费领取《老板必懂的财税避坑指南》，仅限前50名。"
    
    print("\n📋 已接收文案（" + str(len(content)) + " 字），正在分析...\n")
    
    # 步骤3：AI 生成报告
    if choice == "1":
        report, factors = analyze_douyin(content)
    elif choice == "2":
        report, factors = analyze_xiaohongshu(content)
    else:
        report, factors = analyze_shipinhao(content)
    
    print(report)
    print("\n" + "=" * 60)
    print("   分析完成！请阅读上方的爆款因子报告")
    print("=" * 60)
    
    # 步骤4：输入个人心得
    print("\n")
    note = input_multiline("📝 请输入你对这条爆款的个人拆解心得（输入 END 结束）：")
    if not note.strip():
        note = "（本次未输入个人心得）"
    
    print("\n⏳ 正在对比你的心得与AI分析报告...\n")
    
    # 步骤5：AI 对比点评
    review = compare_review(choice, factors, note)
    print(review)
    
    # 步骤6：保存到文件
    save_to_file(platform_name, content, report, note, review)
    
    # 结束语
    print("\n" + "=" * 60)
    print("💡 小提示：")
    print("   1. 这个工具完全离线运行，零API费用，可无限次使用")
    print("   2. 随着拆解的爆款越来越多，你会建立自己的'网感'")
    print("   3. 建议把每次拆解保存成笔记，30天后回头看，进步肉眼可见")
    print("\n🎯 加油，运营小白！爆款是科学，不是玄学。")
    print("=" * 60)


# 程序入口
if __name__ == "__main__":
    main()
