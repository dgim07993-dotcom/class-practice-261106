import html

import streamlit as st


st.set_page_config(
    page_title="나를 소개합니다",
    page_icon="✳️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Gowun+Dodum&display=swap');

    :root {
        --paper: #f4f5ef;
        --ink: #20231f;
        --muted: #72766e;
        --line: #d7d9d0;
        --lime: #d6f36a;
        --blue: #3157d5;
        --coral: #ed7256;
        --pink: #f18db5;
        --cyan: #66d8d1;
        --violet: #9e86e8;
    }

    .stApp {
        background: var(--paper);
        color: var(--ink);
        font-family: 'DM Sans', 'Gowun Dodum', sans-serif;
    }
    .block-container {
        max-width: 1220px;
        padding: 2rem 3.2rem 3rem;
    }
    [data-testid="stSidebar"] {
        background: #e9ebe3;
        border-right: 1px solid var(--line);
    }
    [data-testid="stSidebar"] h2 {
        font-family: 'Gowun Dodum', sans-serif;
        font-size: 1.35rem;
    }
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {
        color: var(--ink);
        font-size: .88rem;
        font-weight: 600;
    }
    [data-testid="stSidebar"] input,
    [data-testid="stSidebar"] textarea {
        background: #fbfcf8;
        border-color: #cdd0c6;
        border-radius: 4px;
    }
    .topline {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid var(--ink);
        padding: .3rem 0 .9rem;
        color: var(--muted);
        font-size: .72rem;
        font-weight: 700;
        letter-spacing: 1px;
    }
    .colorbar {
        height: 8px;
        margin-top: 1rem;
        background: linear-gradient(90deg, var(--coral) 0 16.6%, var(--lime) 16.6% 33.2%, var(--cyan) 33.2% 49.8%, var(--blue) 49.8% 66.4%, var(--violet) 66.4% 83%, var(--pink) 83% 100%);
    }
    .hero-label, .section-kicker {
        color: var(--blue);
        font-size: .74rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .hero-label { margin: 3.5rem 0 1rem; }
    h1.hero-title {
        margin: 0;
        color: var(--ink);
        font-family: 'Gowun Dodum', sans-serif;
        font-size: 4.2rem;
        font-weight: 400;
        line-height: 1.18;
        overflow-wrap: anywhere;
    }
    h1.hero-title span {
        display: block;
        color: var(--blue);
    }
    .hero-intro {
        max-width: 35rem;
        margin: 1.4rem 0 .75rem;
        font-size: 1.2rem;
        font-weight: 600;
        line-height: 1.65;
        overflow-wrap: anywhere;
    }
    .hero-bio {
        max-width: 34rem;
        color: var(--muted);
        font-size: 1rem;
        line-height: 1.9;
        overflow-wrap: anywhere;
    }
    .affiliation-line {
        display: inline-block;
        margin: .15rem 0 .7rem;
        padding: .45rem .7rem;
        background: var(--cyan);
        color: var(--ink);
        font-size: .82rem;
        font-weight: 700;
    }
    .hero-photo-label {
        display: flex;
        justify-content: space-between;
        margin-top: .65rem;
        color: var(--muted);
        font-size: .68rem;
        font-weight: 700;
        letter-spacing: 1px;
    }
    div[data-testid="stImage"] img {
        height: 480px;
        border-radius: 3px;
        object-fit: cover;
    }
    .section-rule {
        height: 1px;
        margin: 3rem 0 1.5rem;
        background: var(--line);
    }
    .section-title {
        margin: .25rem 0 1.1rem;
        color: var(--ink);
        font-family: 'Gowun Dodum', sans-serif;
        font-size: 1.7rem;
        font-weight: 400;
    }
    .tag-list {
        display: flex;
        flex-wrap: wrap;
        gap: .55rem;
        min-height: 2rem;
    }
    .tag {
        display: inline-block;
        padding: .5rem .85rem;
        border: 1px solid var(--ink);
        border-radius: 3px;
        color: var(--ink);
        font-size: .9rem;
    }
    .hobby-tags .tag { background: var(--lime); border-color: var(--lime); }
    .food-tags .tag { background: #ffd1bd; border-color: #ffd1bd; }
    .travel-tags .tag { background: #dcd3ff; border-color: #dcd3ff; }
    .empty-note {
        color: var(--muted);
        font-size: .95rem;
    }
    .dream-band {
        min-height: 190px;
        padding: 1.5rem 1.6rem;
        background: var(--coral);
    }
    .dream-band .section-kicker { color: #44251d; }
    .dream-copy {
        margin: 1.3rem 0 0;
        color: var(--ink);
        font-family: 'Gowun Dodum', sans-serif;
        font-size: 1.7rem;
        line-height: 1.55;
        overflow-wrap: anywhere;
    }
    .current-band {
        min-height: 190px;
        padding: 1.5rem 1.6rem;
        background: var(--pink);
        color: var(--ink);
    }
    .current-band .section-kicker { color: #51283b; }
    .current-copy {
        margin: 1.3rem 0 0;
        font-size: 1.25rem;
        line-height: 1.7;
        overflow-wrap: anywhere;
    }
    .footer-line {
        display: flex;
        justify-content: space-between;
        margin-top: 3rem;
        padding-top: .8rem;
        border-top: 1px solid var(--ink);
        color: var(--muted);
        font-size: .72rem;
        letter-spacing: .5px;
    }
    @media (max-width: 760px) {
        .block-container { padding: 1.2rem 1.1rem 2rem; }
        h1.hero-title { font-size: 3rem; }
        .hero-label { margin-top: 2rem; }
        div[data-testid="stImage"] img { height: 330px; }
        .dream-band, .current-band { min-height: 150px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown("## 프로필 편집")
name = st.sidebar.text_input("이름", value="김동규", placeholder="이름")
affiliation = st.sidebar.text_input("소속", value="청주교육대학교", placeholder="학교, 회사, 동아리 등")
tagline = st.sidebar.text_input("나를 표현하는 한 문장", placeholder="예: 호기심을 따라 새로운 걸 배우는 사람")
introduction = st.sidebar.text_area("자기소개", placeholder="나에 대해 들려주고 싶은 이야기를 적어보세요.", height=120)
hobbies_text = st.sidebar.text_input("취미", value="운동", placeholder="예: 사진, 등산, 베이킹")
foods_text = st.sidebar.text_input("좋아하는 음식", value="고기", placeholder="예: 파스타, 김밥, 딸기")
dream = st.sidebar.text_input("꿈 또는 목표", value="교사", placeholder="언젠가 이루고 싶은 일")
countries_text = st.sidebar.text_input("여행한 나라", value="베트남", placeholder="예: 일본, 이탈리아, 캐나다")
current_interest = st.sidebar.text_input("요즘 관심 있는 것", placeholder="요즘 빠져 있는 것")
profile_photo = st.sidebar.file_uploader("대표 사진", type=["png", "jpg", "jpeg", "webp"])


def split_items(value: str) -> list[str]:
    return [item.strip() for item in value.replace("，", ",").split(",") if item.strip()]


def render_tags(items: list[str], empty_message: str) -> str:
    if not items:
        return f'<p class="empty-note">{empty_message}</p>'
    tags = "".join(f'<span class="tag">{html.escape(item)}</span>' for item in items)
    return f'<div class="tag-list">{tags}</div>'


safe_name = html.escape(name.strip())
safe_affiliation = html.escape(affiliation.strip())
safe_tagline = html.escape(tagline.strip())
safe_introduction = html.escape(introduction.strip()).replace("\n", "<br>")
safe_dream = html.escape(dream.strip())
safe_interest = html.escape(current_interest.strip())

st.markdown(
    '<div class="topline"><span>PERSONAL PROFILE</span><span>ABOUT / 01</span></div>',
    unsafe_allow_html=True,
)
st.markdown('<div class="colorbar"></div>', unsafe_allow_html=True)

intro_column, photo_column = st.columns([1.08, 0.92], gap="large", vertical_alignment="center")
with intro_column:
    title = f'{safe_name}<span>의 이야기</span>' if safe_name else '나를 소개합니다<span>좋아하는 것과 꿈</span>'
    st.markdown('<p class="hero-label">안녕하세요, 반가워요</p>', unsafe_allow_html=True)
    st.markdown(f'<h1 class="hero-title">{title}</h1>', unsafe_allow_html=True)
    if safe_affiliation:
        st.markdown(f'<p class="affiliation-line">{safe_affiliation}</p>', unsafe_allow_html=True)
    if safe_tagline:
        st.markdown(f'<p class="hero-intro">{safe_tagline}</p>', unsafe_allow_html=True)
    if safe_introduction:
        st.markdown(f'<p class="hero-bio">{safe_introduction}</p>', unsafe_allow_html=True)

with photo_column:
    if profile_photo is not None:
        st.image(profile_photo, use_container_width=True)
        photo_label = "MY PHOTO"
    else:
        st.image(
            "https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=1400&q=85",
            use_container_width=True,
        )
        photo_label = "TRAVEL MOODBOARD"
    st.markdown(
        f'<div class="hero-photo-label"><span>{photo_label}</span><span>01 — 04</span></div>',
        unsafe_allow_html=True,
    )

st.markdown('<div class="section-rule"></div>', unsafe_allow_html=True)
hobby_column, food_column, country_column = st.columns(3, gap="large")
with hobby_column:
    st.markdown('<p class="section-kicker">HOBBIES / 02</p><h2 class="section-title">취미</h2>', unsafe_allow_html=True)
    st.markdown(f'<div class="hobby-tags">{render_tags(split_items(hobbies_text), "취미를 적어보세요.")}</div>', unsafe_allow_html=True)
with food_column:
    st.markdown('<p class="section-kicker">FAVORITE FOOD / 03</p><h2 class="section-title">좋아하는 음식</h2>', unsafe_allow_html=True)
    st.markdown(f'<div class="food-tags">{render_tags(split_items(foods_text), "좋아하는 음식을 적어보세요.")}</div>', unsafe_allow_html=True)
with country_column:
    st.markdown('<p class="section-kicker">TRAVEL LOG / 04</p><h2 class="section-title">여행한 나라</h2>', unsafe_allow_html=True)
    st.markdown(f'<div class="travel-tags">{render_tags(split_items(countries_text), "여행한 나라를 적어보세요.")}</div>', unsafe_allow_html=True)

st.markdown('<div class="section-rule"></div>', unsafe_allow_html=True)
dream_column, interest_column = st.columns([1.15, 0.85], gap="medium")
with dream_column:
    dream_text = safe_dream or "앞으로 이루고 싶은 꿈을 적어보세요."
    st.markdown(
        f'<div class="dream-band"><p class="section-kicker">LOOKING AHEAD / 04</p><p class="dream-copy">{dream_text}</p></div>',
        unsafe_allow_html=True,
    )
with interest_column:
    interest_text = safe_interest or "요즘의 관심사를 기록해보세요."
    st.markdown(
        f'<div class="current-band"><p class="section-kicker">RIGHT NOW / 05</p><p class="current-copy">{interest_text}</p></div>',
        unsafe_allow_html=True,
    )

footer_name = safe_name if safe_name else "나의 소개 페이지"
st.markdown(
    f'<div class="footer-line"><span>{footer_name}</span><span>MADE OF LITTLE THINGS</span></div>',
    unsafe_allow_html=True,
)