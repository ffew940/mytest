import streamlit as st
from datetime import datetime

# 页面配置
st.set_page_config(page_title="个人简历生成器", layout="wide")

# 自定义深色主题样式
st.markdown("""
<style>
body {
    background-color: #1E1E1E;
    color: #FFFFFF;
}
.st-column:first-child .st-form {
    background-color: #2B2B2B;
    padding: 20px;
    border-radius: 8px;
}
.st-markdown h1, .st-markdown h2 {
    color: #4CAF50;
}
.st-button>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 4px;
}
.st-file_uploader {
    background-color: #3A3A3A;
    padding: 10px;
    border-radius: 4px;
}
</style>
""", unsafe_allow_html=True)

# 初始化 Session State（使用虚构数据）
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
        gender = st.radio("性别", ["男", "女", "其他"], index=0 if st.session_state["gender"]=="男" else 1 if st.session_state["gender"]=="女" else 2)
        education = st.selectbox("最高学历", ["本科", "硕士", "博士", "大专"], index=["本科", "硕士", "博士", "大专"].index(st.session_state["education"]))
        work_exp = st.slider("工作经验（年）", 0, 10, value=st.session_state["work_exp"])
        expected_salary = st.text_input("期望薪资（范围）", value=st.session_state["expected_salary"])
        
        # 能力标签
        languages = st.multiselect("语言能力", ["中文", "英语", "日语", "韩语"], default=st.session_state["languages"])
        skills = st.multiselect("专业技能", ["Python", "SQL", "数据分析", "机器学习", "数据可视化", "Java", "C++", "UI/UX设计", "产品管理"], default=st.session_state["skills"])
        self_rating = st.multiselect("个人优势", ["沟通能力", "团队协作", "问题解决", "创新思维", "抗压能力", "领导力"], default=st.session_state["self_rating"])
        
        # 证书与经历
        certificates = st.multiselect("专业证书", ["AWS认证", "PMP认证", "CFA", "CPA", "CET-6", "TOEFL", "雅思", "Python数据分析证书"], default=st.session_state["certificates"])
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
        st.markdown(f"# {st.session_state['name']}")
        st.markdown(f"**{st.session_state['position']}**")
        st.markdown(f"📍 {st.session_state['location']} | 📱 {st.session_state['phone']} | ✉️ {st.session_state['email']}")
        
        # 社交链接（可选）
        social_links = []
        if st.session_state["github"]:
            social_links.append(f"[GitHub]({st.session_state['github']})")
        if st.session_state["linkedin"]:
            social_links.append(f"[LinkedIn]({st.session_state['linkedin']})")
        if social_links:
            st.markdown(" | ".join(social_links))
    
    # 个人简介
    st.markdown("## 📝 个人简介")
    st.markdown(st.session_state["intro"])
    
    # 个人概况卡片（整合基础信息）
    st.markdown("## 👤 个人概况")
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
    
    # 技能标签（使用emoji图标）
    st.markdown("## 💻 专业技能")
    skill_html = " ".join([f"<span style='background-color:#3A3A3A; padding:3px 8px; border-radius:4px; margin-right:5px; margin-bottom:5px; display:inline-block'>{skill}</span>" for skill in st.session_state["skills"]])
    st.markdown(skill_html, unsafe_allow_html=True)
    
    # 个人优势
    st.markdown("## 🌟 个人优势")
    rating_html = " ".join([f"<span style='background-color:#4CAF50; color:white; padding:3px 8px; border-radius:4px; margin-right:5px; margin-bottom:5px; display:inline-block'>{item}</span>" for item in st.session_state["self_rating"]])
    st.markdown(rating_html, unsafe_allow_html=True)
    
    # 证书
    st.markdown("## 🎖️ 专业证书")
    cert_html = " ".join([f"<span style='background-color:#2B2B2B; border:1px solid #4CAF50; padding:3px 8px; border-radius:4px; margin-right:5px; margin-bottom:5px; display:inline-block'>{cert}</span>" for cert in st.session_state["certificates"]])
    st.markdown(cert_html, unsafe_allow_html=True)
    
    # 项目经历
    st.markdown("## 🚀 项目经历")
    st.markdown(st.session_state["project"])