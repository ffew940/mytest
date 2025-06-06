import streamlit as st
import pandas as pd

# 页面配置
st.set_page_config(page_title="盖伦 - 无畏先锋", layout="wide")

# 基础信息
st.header("盖伦 - 无畏先锋")
st.subheader("🔑 英雄档案")
st.write("英雄ID: Garen-001")
st.write("加入时间: 符文之地历 763 年 | 状态: ✅ 活跃")
st.write("所属阵营: 德玛西亚 | 英雄定位: 战士/坦克")
st.write("推荐位置: 上单 | 难度: ⭐️⭐️☆☆☆")

# 技能矩阵
st.subheader("📊 技能评级")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.write("坚韧")
    st.write("90% ⭐️⭐️⭐️⭐️☆")
with col2:
    st.write("伤害")
    st.write("75% ⭐️⭐️⭐️☆☆")
with col3:
    st.write("控制")
    st.write("60% ⭐️⭐️☆☆☆")
with col4:
    st.write("机动性")
    st.write("50% ⭐️⭐️☆☆☆")
with col5:
    st.write("支援")
    st.write("65% ⭐️⭐️⭐️☆☆")

# 技能详情
st.subheader("🔱 技能详情")

# 被动技能
st.markdown("**被动：勇气**")
st.write("盖伦在脱离战斗后会每秒回复最大生命值的3%。")

# Q技能
st.markdown("**Q：致命打击**")
st.write("冷却：8/7/6/5/4秒 | 消耗：30/35/40/45/50法力")
st.write("盖伦挥舞大剑，对面前的敌人造成60/90/120/150/180(+1.0*总AD)物理伤害。如果命中敌人，会移除自身的减速效果并获得30%移动速度加成，持续1.5秒。")

# W技能
st.markdown("**W：勇气**")
st.write("冷却：20/18/16/14/12秒 | 消耗：25法力")
st.write("被动：护甲和魔抗提升10/15/20/25/30。")
st.write("主动：激活后获得60/70/80/90/100%伤害减免，持续1.5秒。")

# E技能
st.markdown("**E：审判**")
st.write("冷却：12/11/10/9/8秒 | 消耗：25/30/35/40/45法力")
st.write("盖伦快速旋转大剑，对周围敌人每0.33秒造成20/28/36/44/52(+0.25*总AD)物理伤害，持续3秒，最多造成6次伤害。")

# R技能
st.markdown("**R：德玛西亚正义**")
st.write("冷却：100/85/70秒 | 消耗：100法力")
st.write("盖伦跃向目标，造成真实伤害，数值相当于目标最大生命值的20/30/40%加上额外的175/300/425点伤害。如果用此技能击杀目标，则会重置冷却时间。")

# 出装建议
st.subheader("🛡️ 出装建议")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**对抗物理伤害**")
    st.write("- 斯特拉克的挑战护手")
    st.write("- 守护天使")
    st.write("- 亡者的板甲")
    st.write("- 荆棘之甲")
with col2:
    st.markdown("**对抗魔法伤害**")
    st.write("- 振奋盔甲")
    st.write("- 兰顿之兆")
    st.write("- 自然之力")
    st.write("- 石像鬼石板甲")

# 英雄台词
st.subheader("🎙️ 经典台词")
st.write("- \"德玛西亚！\"")
st.write("- \"正义必将战胜邪恶！\"")
st.write("- \"为了父王！\"")
st.write("- \"人在塔在！\"")

# 英雄语录
st.subheader("📜 英雄语录")
st.markdown("> \"在别的游戏里，像我这么帅的一般都是主角哟！\"")

# 符文推荐
st.subheader("🔮 符文推荐")
rune_data = {
    "主系": ["不灭之握", "生命源泉", "调节", "过度生长"],
    "副系": ["骸骨镀层", "坚定"],
    "小符文": ["自适应之力", "自适应之力", "生命值"]
}
rune_df = pd.DataFrame(rune_data)
st.table(rune_df)

# 运行命令：streamlit run garen_profile.py