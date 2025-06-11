import streamlit as st

# 页面配置
st.set_page_config(page_title="Streamlit 视频播放器", layout="centered")

# 自定义样式
st.markdown(
    """
    <style>
    .stApp { background-color: #1E1E1E; color: #FFFFFF; }
    .stVideo iframe { border-radius: 8px; }
    .video-container {
        text-align: center;
        margin: 8px 0;
        border-radius: 8px;
        overflow: hidden;
        transition: transform 0.2s;
    }
    .video-container:hover {
        transform: scale(1.02);
        background-color: #333333;
    }
    .video-title {
        font-size: 14px;
        margin-top: 8px;
    }
    .video-meta {
        font-size: 12px;
        color: #AAAAAA;
        margin-top: 4px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 初始化会话状态
if "current_video" not in st.session_state:
    st.session_state.current_video = None

# 标题与说明
st.title("Streamlit 视频播放器")
st.markdown("点击下方视频缩略图选择要播放的视频")

# 视频播放区域
st.markdown("## 视频播放")
if st.session_state.current_video:
    st.video(st.session_state.current_video)
else:
    st.info("请选择一个视频开始播放")

# 视频库分类选择
categories = ["全部", "动画演示", "教程演示", "电影预告片"]
selected_category = st.selectbox("视频库", categories)

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
st.markdown("## 视频库")
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
                <div class="video-meta">
                    {video["duration"]} | {video["category"]}
                </div>
                """,
                unsafe_allow_html=True
            )