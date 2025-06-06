import streamlit as st
import pandas as pd
import numpy as np

# 页面配置 - 使用蓝色为主色调（南宁城市意象）
st.set_page_config(
    page_title="南宁美食探索", 
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🍜"
)

# 自定义样式
st.markdown("""
<style>
    .main-header {
        color: #005082;
        font-size: 2.5rem;
        text-align: center;
    }
    .subheader {
        color: #0079c2;
        border-bottom: 2px solid #0079c2;
        padding-bottom: 5px;
    }
    .metric-card {
        background-color: #f0f7ff;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stProgress > div > div > div {
        background-color: #0079c2;
    }
</style>
""", unsafe_allow_html=True)

# 页面标题
st.markdown('<h1 class="main-header">南宁美食探索</h1>', unsafe_allow_html=True)
st.markdown("""
探索广西南宁最受欢迎的美食地点！从传统老友粉到创新桂菜，南宁美食融合了酸、辣、鲜的独特风味。
""")


### 1. 南宁美食地图（Map）
map_data = pd.DataFrame({
    "lat": [22.842, 22.835, 22.851, 22.863, 22.829],  # 南宁大致纬度
    "lon": [108.293, 108.301, 108.285, 108.312, 108.278],  # 南宁大致经度
    "name": ["甘家界柠檬鸭", "三街两巷老友粉", "老南宁牛杂", "东盟美食城", "中山路美食街"]
})

st.subheader("📍 南宁美食地图")
st.map(map_data, zoom=12)


### 2. 餐厅价格对比（Bar Chart）
price_data = pd.DataFrame({
    "餐厅": ["甘家界柠檬鸭", "三街两巷老友粉", "老南宁牛杂", "东盟美食城", "中山路美食街", "肥仔饭店", "表妹嘢味"],
    "人均价格(元)": [68, 18, 35, 45, 25, 58, 42]
})

st.subheader("💰 餐厅价格对比")
st.bar_chart(price_data, x="餐厅", y="人均价格(元)", color="#0079c2")


### 3. 历史客流量趋势（Line Chart）
line_data = pd.DataFrame({
    "日期": pd.date_range(start="2023-01-01", periods=30),
    "甘家界柠檬鸭": np.random.randint(100, 300, 30),
    "三街两巷老友粉": np.random.randint(200, 500, 30),
    "老南宁牛杂": np.random.randint(150, 400, 30),
    "东盟美食城": np.random.randint(180, 450, 30),
    "中山路美食街": np.random.randint(300, 700, 30)
})

st.subheader("📈 历史客流量趋势")
st.line_chart(line_data, x="日期", y=["甘家界柠檬鸭", "三街两巷老友粉", "老南宁牛杂", "东盟美食城", "中山路美食街"])


### 4. 美食类别分布（Area Chart）
area_data = pd.DataFrame({
    "美食类别": ["老友粉", "柠檬鸭", "酸嘢", "生榨米粉", "卷筒粉", "海鲜", "烧烤"],
    "市场占比(%)": [30, 15, 10, 12, 8, 18, 7]
})

st.subheader("🍲 美食类别分布")
st.area_chart(area_data, x="美食类别", y="市场占比(%)")


### 5. 餐厅详情 & 推荐
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🏷️ 餐厅详情")
    
    # 新的餐厅数据
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
    st.subheader("🍴 美食小贴士")
    
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
    current_hour = pd.Timestamp.now().hour
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