import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import base64

# 页面配置
st.set_page_config(
    page_title="多功能整合平台",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊"
)

# 自定义全局样式
st.markdown("""
<style>
    :root {
        --primary-color: #4CAF50;
        --secondary-color: #0079c2;
        --background-color: #f8f9fa;
        --card-bg: #ffffff;
    }
    body {
        background-color: var(--background-color);
        color: #333333;
    }
    .sidebar-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: var(--primary-color);
        margin-bottom: 1rem;
    }
    .module-title {
        color: var(--primary-color);
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
    }
    .card {
        background-color: var(--card-bg);
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #f0f7ff;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .skill-tag {
        background-color: var(--primary-color);
        color: white;
        padding: 3px 8px;
        border-radius: 4px;
        margin-right: 5px;
        margin-bottom: 5px;
        display: inline-block;
    }
    .cert-tag {
        background-color: #f0f7ff;
        border: 1px solid var(--secondary-color);
        padding: 3px 8px;
        border-radius: 4px;
        margin-right: 5px;
        margin-bottom: 5px;
        display: inline-block;
    }
    .video-container {
        text-align: center;
        margin: 8px 0;
        border-radius: 8px;
        overflow: hidden;
        transition: transform 0.2s;
    }
    .video-container:hover {
        transform: scale(1.02);
        background-color: #f0f0f0;
    }
</style>
""", unsafe_allow_html=True)

# 视频播放模块
def video_player():
    st.markdown("<h2 class='module-title'>Streamlit 视频播放器</h2>", unsafe_allow_html=True)
    st.markdown("点击下方视频缩略图选择要播放的视频")
    
    # 初始化会话状态
    if "current_video" not in st.session_state:
        st.session_state.current_video = None
    
    # 视频播放区域
    st.markdown("### 视频播放")
    if st.session_state.current_video:
        st.video(st.session_state.current_video)
    else:
        st.info("请选择一个视频开始播放")
    
    # 视频库分类选择
    st.markdown("### 视频库筛选")
    categories = ["全部", "动画演示", "教程演示", "电影预告片"]
    selected_category = st.selectbox("选择视频分类", categories)
    
    # 视频数据
    videos = [
        {
            "title": "Big Buck Bunny",
            "duration": "1:03",
            "category": "动画演示",
            "preview": "https://picsum.photos/seed/bbb/400/225",
            "video": "https://www.w3school.com.cn/example/html5/mov_bbb.mp4"
        },
        {
            "title": "W3Schools 示例视频",
            "duration": "0:46",
            "category": "教程演示",
            "preview": "https://picsum.photos/seed/w3s/400/225",
            "video": "https://www.w3schools.com/html/movie.mp4"
        },
        {
            "title": "Sintel 预告片",
            "duration": "2:00",
            "category": "电影预告片",
            "preview": "https://picsum.photos/seed/sintel/400/225",
            "video": "https://media.w3.org/2010/05/sintel/trailer.mp4"
        }
    ]
    
    # 根据分类过滤视频
    if selected_category == "全部":
        filtered_videos = videos
    else:
        filtered_videos = [v for v in videos if v["category"] == selected_category]
    
    # 点击视频缩略图时，更新当前播放的视频
    def set_current_video(video):
        st.session_state.current_video = video["video"]
    
    # 展示视频列表
    st.markdown("### 视频库")
    cols = st.columns(3)
    for i, video in enumerate(filtered_videos):
        with cols[i % 3]:
            # 使用容器和链接替代按钮
            with st.container():
                # 图片作为链接
                if st.image(
                    video["preview"],
                    caption=video["title"],
                    use_column_width=True,
                    output_format="JPEG"
                ):
                    set_current_video(video)
                
                # 视频信息
                st.markdown(
                    f"""
                    <div>
                        <span style="font-size: 12px; color: #666666;">{video["duration"]} | {video["category"]}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# 南宁美食模块
def nanning_food():
    st.markdown("<h2 class='module-title'>南宁美食探索</h2>", unsafe_allow_html=True)
    st.markdown("探索广西南宁最受欢迎的美食地点！从传统老友粉到创新桂菜，南宁美食融合了酸、辣、鲜的独特风味。")
    
    # 分栏展示地图和数据
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📍 南宁美食地图")
        map_data = pd.DataFrame({
            "lat": [22.842, 22.835, 22.851, 22.863, 22.829],  # 南宁大致纬度
            "lon": [108.293, 108.301, 108.285, 108.312, 108.278],  # 南宁大致经度
            "name": ["甘家界柠檬鸭", "三街两巷老友粉", "老南宁牛杂", "东盟美食城", "中山路美食街"]
        })
        st.map(map_data, zoom=12)
    
    with col2:
        st.markdown("### 💰 餐厅价格对比")
        price_data = pd.DataFrame({
            "餐厅": ["甘家界柠檬鸭", "三街两巷老友粉", "老南宁牛杂", "东盟美食城", "中山路美食街", "肥仔饭店", "表妹嘢味"],
            "人均价格(元)": [68, 18, 35, 45, 25, 58, 42]
        })
        st.bar_chart(price_data, x="餐厅", y="人均价格(元)", color="#0079c2")
    
    # 客流量趋势和美食分布
    tab1, tab2 = st.tabs(["📈 历史客流量趋势", "🍲 美食类别分布"])
    
    with tab1:
        line_data = pd.DataFrame({
            "日期": pd.date_range(start="2023-01-01", periods=30),
            "甘家界柠檬鸭": np.random.randint(100, 300, 30),
            "三街两巷老友粉": np.random.randint(200, 500, 30),
            "老南宁牛杂": np.random.randint(150, 400, 30),
            "东盟美食城": np.random.randint(180, 450, 30),
            "中山路美食街": np.random.randint(300, 700, 30)
        })
        st.line_chart(line_data, x="日期", y=["甘家界柠檬鸭", "三街两巷老友粉", "老南宁牛杂", "东盟美食城", "中山路美食街"])
    
    with tab2:
        area_data = pd.DataFrame({
            "美食类别": ["老友粉", "柠檬鸭", "酸嘢", "生榨米粉", "卷筒粉", "海鲜", "烧烤"],
            "市场占比(%)": [30, 15, 10, 12, 8, 18, 7]
        })
        st.area_chart(area_data, x="美食类别", y="市场占比(%)")
    
    # 餐厅详情和小贴士
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🏷️ 餐厅详情")
        
        # 餐厅数据
        restaurants = {
            "甘家界柠檬鸭": {"评分": 4.7, "人均": 68, "菜系": "桂菜", "推荐": ["柠檬鸭", "老友鱼", "上汤时蔬"]},
            "三街两巷老友粉": {"评分": 4.5, "人均": 18, "菜系": "传统小吃", "推荐": ["老友粉", "粉饺", "叉烧"]},
            "老南宁牛杂": {"评分": 4.6, "人均": 35, "菜系": "特色小吃", "推荐": ["牛杂粉", "牛巴粉", "生榨米粉"]},
            "东盟美食城": {"评分": 4.3, "人均": 45, "菜系": "东南亚风味", "推荐": ["越南春卷", "冬阴功汤", "咖喱饭"]},
            "中山路美食街": {"评分": 4.2, "人均": 25, "菜系": "综合小吃", "推荐": ["酸嘢", "烤生蚝", "卷筒粉"]}
        }
        
        selected_rest = st.selectbox("选择餐厅查看详情", list(restaurants.keys()))
        rest_info = restaurants[selected_rest]
        
        # 用卡片样式展示餐厅信息
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color:#005082;">{selected_rest}</h3>
            <div style="display:flex; justify-content:space-between;">
                <div>
                    <p><strong>评分：</strong>{rest_info['评分']}/5.0</p>
                    <p><strong>人均消费：</strong>¥{rest_info['人均']}</p>
                    <p><strong>菜系：</strong>{rest_info['菜系']}</p>
                </div>
                <div>
                    <p><strong>推荐菜品：</strong></p>
                    <ul>
                        {''.join([f'<li>{dish}</li>' for dish in rest_info["推荐"]])}
                    </ul>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🍴 美食小贴士")
        
        # 随机显示美食小贴士
        tips = [
            "南宁老友粉以酸、辣、香、咸闻名，建议搭配柠檬和辣椒！",
            "中山路美食街晚上最热闹，各种小吃应有尽有，记得带上足够的胃容量！",
            "甘家界柠檬鸭是南宁必尝名菜，鸭肉鲜嫩，柠檬清香解腻。",
            "南宁人喜欢吃酸嘢，酸甜可口的酸嘢是开胃佳品。",
            "生榨米粉是南宁特有的美食，米香浓郁，口感独特。"
        ]
        
        st.markdown(f"""
        <div class="metric-card">
            <h4 style="color:#005082;">今日小贴士</h4>
            <p style="font-style:italic;">"{np.random.choice(tips)}"</p>
        </div>
        """, unsafe_allow_html=True)
        
        # 显示当前时间的用餐建议
        current_hour = datetime.now().hour
        if 6 <= current_hour < 10:
            meal_type = "早餐"
            suggestion = "推荐尝试南宁老友粉或生榨米粉！"
        elif 11 <= current_hour < 14:
            meal_type = "午餐"
            suggestion = "甘家界柠檬鸭或老南宁牛杂是不错的选择！"
        elif 17 <= current_hour < 20:
            meal_type = "晚餐"
            suggestion = "中山路美食街或东盟美食城适合晚餐！"
        else:
            meal_type = "夜宵"
            suggestion = "烧烤和酸嘢是夜宵的绝佳搭配！"
        
        st.markdown(f"""
        <div class="metric-card">
            <h4 style="color:#005082;">{meal_type}时间</h4>
            <p>{suggestion}</p>
        </div>
        """, unsafe_allow_html=True)

# 简历报告模块
def resume_builder():
    st.markdown("<h2 class='module-title'>个人简历生成器</h2>", unsafe_allow_html=True)
    
    # 初始化 Session State
    if "name" not in st.session_state:
        st.session_state.update({
            "name": "xiedexiang",
            "position": "数据分析师",
            "phone": "13987654321",
            "email": "chenxingyu@example.com",
            "location": "上海",
            "github": "github.com/chenxy-data",
            "linkedin": "linkedin.com/in/chenxingyu",
            "birthday": datetime(1995, 8, 15),
            "gender": "男",
            "education": "硕士",
            "languages": ["中文", "英语"],
            "skills": ["Python", "SQL", "数据分析", "机器学习", "数据可视化"],
            "self_rating": ["问题解决", "团队协作", "沟通能力"],
            "certificates": ["AWS认证", "PMP认证", "Python数据分析证书"],
            "work_exp": 3,
            "expected_salary": "18000-25000",
            "project": """
### 电商用户行为分析系统  
- 负责设计用户画像模型，通过RFM分析提升用户留存率15%  
- 使用Python+Pandas处理日均100万条用户行为数据  
- 开发数据可视化仪表盘，支持业务决策  
### 智能推荐算法优化  
- 基于协同过滤算法，实现个性化商品推荐功能  
- 模型上线后，商品点击率提升23%，用户停留时长增加18%  
- 设计A/B测试框架，持续迭代推荐策略  
""",
            "intro": """
xiedexiang，上海财经大学统计学硕士，拥有3年数据分析经验。  
擅长使用Python、SQL处理大规模数据集，熟悉机器学习与数据可视化。  
曾在电商、金融领域负责用户行为分析与商业智能项目，  
具备从数据挖掘到业务落地的全流程经验。  
""",
            "avatar": None
        })
    
    # 分栏：左侧表单 + 右侧实时预览
    col_left, col_right = st.columns([2, 3])
    
    with col_left:
        st.markdown("### 个人信息表单")
        with st.form("info_form"):
            # 基本信息
            name = st.text_input("姓名", value=st.session_state["name"])
            position = st.text_input("求职意向", value=st.session_state["position"])
            phone = st.text_input("电话", value=st.session_state["phone"])
            email = st.text_input("邮箱", value=st.session_state["email"])
            location = st.text_input("所在地", value=st.session_state["location"])
            
            # 社交链接
            github = st.text_input("GitHub", value=st.session_state["github"])
            linkedin = st.text_input("LinkedIn", value=st.session_state["linkedin"])
            
            # 个人概况
            birthday = st.date_input("出生日期", value=st.session_state["birthday"])
            gender = st.radio("性别", ["男", "女", "其他"], 
                             index=0 if st.session_state["gender"]=="男" else 1 if st.session_state["gender"]=="女" else 2)
            education = st.selectbox("最高学历", ["本科", "硕士", "博士", "大专"], 
                                    index=["本科", "硕士", "博士", "大专"].index(st.session_state["education"]))
            work_exp = st.slider("工作经验（年）", 0, 10, value=st.session_state["work_exp"])
            expected_salary = st.text_input("期望薪资（范围）", value=st.session_state["expected_salary"])
            
            # 能力标签
            languages = st.multiselect("语言能力", ["中文", "英语", "日语", "韩语"], 
                                      default=st.session_state["languages"])
            skills = st.multiselect("专业技能", ["Python", "SQL", "数据分析", "机器学习", "数据可视化", 
                                                 "Java", "C++", "UI/UX设计", "产品管理"], 
                                   default=st.session_state["skills"])
            self_rating = st.multiselect("个人优势", ["沟通能力", "团队协作", "问题解决", "创新思维", 
                                                     "抗压能力", "领导力"], 
                                      default=st.session_state["self_rating"])
            
            # 证书与经历
            certificates = st.multiselect("专业证书", ["AWS认证", "PMP认证", "CFA", "CPA", "CET-6", 
                                                       "TOEFL", "雅思", "Python数据分析证书"], 
                                        default=st.session_state["certificates"])
            project = st.text_area("项目经历", value=st.session_state["project"], height=150)
            intro = st.text_area("个人简介", value=st.session_state["intro"], height=150)
            
            # 头像上传
            avatar = st.file_uploader("上传头像", type=["png", "jpg", "jpeg"], accept_multiple_files=False)
            
            # 提交按钮
            if st.form_submit_button("保存并预览"):
                st.session_state.update({
                    "name": name, "position": position, "phone": phone, "email": email,
                    "location": location, "github": github, "linkedin": linkedin,
                    "birthday": birthday, "gender": gender, "education": education,
                    "work_exp": work_exp, "expected_salary": expected_salary,
                    "languages": languages, "skills": skills, "self_rating": self_rating,
                    "certificates": certificates, "project": project, "intro": intro,
                    "avatar": avatar
                })
                st.experimental_rerun()
    
    with col_right:
        # 顶部信息区（包含头像）
        header_col1, header_col2 = st.columns([1, 3])
        with header_col1:
            if st.session_state["avatar"]:
                st.image(st.session_state["avatar"], width=150)
            else:
                st.image("https://via.placeholder.com/150x150.png?text=Avatar", width=150)
        
        with header_col2:
            st.markdown(f"<h2>{st.session_state['name']}</h2>", unsafe_allow_html=True)
            st.markdown(f"**{st.session_state['position']}**")
            st.markdown(f"📍 {st.session_state['location']} | 📱 {st.session_state['phone']} | ✉️ {st.session_state['email']}")
            
            # 社交链接
            social_links = []
            if st.session_state["github"]:
                social_links.append(f"[GitHub]({st.session_state['github']})")
            if st.session_state["linkedin"]:
                social_links.append(f"[LinkedIn]({st.session_state['linkedin']})")
            if social_links:
                st.markdown(" | ".join(social_links))
        
        # 个人简介
        st.markdown("### 📝 个人简介")
        st.markdown(st.session_state["intro"])
        
        # 个人概况卡片
        st.markdown("### 👤 个人概况")
        profile_cols = st.columns(3)
        with profile_cols[0]:
            st.markdown(f"**出生日期**\n\n{st.session_state['birthday'].strftime('%Y-%m-%d')}")
            st.markdown(f"**最高学历**\n\n{st.session_state['education']}")
        with profile_cols[1]:
            st.markdown(f"**工作经验**\n\n{st.session_state['work_exp']}年")
            st.markdown(f"**期望薪资**\n\n{st.session_state['expected_salary']}")
        with profile_cols[2]:
            st.markdown(f"**性别**\n\n{st.session_state['gender']}")
            st.markdown(f"**语言能力**\n\n{', '.join(st.session_state['languages'])}")
        
        # 技能标签
        st.markdown("### 💻 专业技能")
        skill_html = " ".join([f"<span class='skill-tag'>{skill}</span>" for skill in st.session_state["skills"]])
        st.markdown(skill_html, unsafe_allow_html=True)
        
        # 个人优势
        st.markdown("### 🌟 个人优势")
        rating_html = " ".join([f"<span class='skill-tag'>{item}</span>" for item in st.session_state["self_rating"]])
        st.markdown(rating_html, unsafe_allow_html=True)
        
        # 证书
        st.markdown("### 🎖️ 专业证书")
        cert_html = " ".join([f"<span class='cert-tag'>{cert}</span>" for cert in st.session_state["certificates"]])
        st.markdown(cert_html, unsafe_allow_html=True)
        
        # 项目经历
        st.markdown("### 🚀 项目经历")
        st.markdown(st.session_state["project"])

# 盖伦介绍模块
def garen_introduction():
    st.markdown("<h2 class='module-title'>盖伦 - 无畏先锋</h2>", unsafe_allow_html=True)
    
    with st.expander("📑 英雄档案", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.write("英雄ID: Garen-001")
            st.write("加入时间: 符文之地历 763 年")
            st.write("所属阵营: 德玛西亚")
            st.write("推荐位置: 上单")
        with col2:
            st.write("状态: ✅ 活跃")
            st.write("英雄定位: 战士/坦克")
            st.write("难度: ⭐️⭐️☆☆☆")
    
    with st.expander("📊 技能评级", expanded=True):
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
    
    with st.expander("🔱 技能详情", expanded=True):
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
    st.markdown("### 🛡️ 出装建议")
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
    st.markdown("### 🎙️ 经典台词")
    st.write("- \"德玛西亚！\"")
    st.write("- \"正义必将战胜邪恶！\"")
    st.write("- \"为了父王！\"")
    st.write("- \"人在塔在！\"")
    
    with st.expander("📜 英雄语录", expanded=True):
        st.markdown("> \"在别的游戏里，像我这么帅的一般都是主角哟！\"")
    
    # 符文推荐
    st.markdown("### 🔮 符文推荐")
    rune_data = {
        "主系": ["不灭之握", "生命源泉", "调节", "过度生长"],
        "副系": ["骸骨镀层", "坚定"],
        "小符文": ["自适应之力", "自适应之力", "生命值"]
    }
    rune_df = pd.DataFrame(rune_data)
    st.table(rune_df)

# 主应用
def main():
    # 侧边栏导航
    st.sidebar.markdown("<div class='sidebar-title'>功能导航</div>", unsafe_allow_html=True)
    page = st.sidebar.radio("", ["视频播放器", "南宁美食探索", "个人简历生成器", "盖伦介绍"])
    
    # 根据选择显示不同页面
    if page == "视频播放器":
        video_player()
    elif page == "南宁美食探索":
        nanning_food()
    elif page == "个人简历生成器":
        resume_builder()
    elif page == "盖伦介绍":
        garen_introduction()
    
    # 页脚
    st.markdown("---")
    st.markdown("© 2025 多功能整合平台 | 使用Streamlit构建")

if __name__ == "__main__":
    main()