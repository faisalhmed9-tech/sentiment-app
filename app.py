import streamlit as st
import urllib.parse
import random
import time
from datetime import datetime

# --- 1. إعدادات الصفحة الفخمة ---
st.set_page_config(page_title="نظام حمد العالمي 2026", page_icon="🛡️", layout="wide")

# تخصيص CSS متقدم (خلفية متدرجة وتأثيرات للأزرار)
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .stButton>button {
        background: linear-gradient(to right, #1E3A8A, #3B82F6);
        color: white;
        border-radius: 25px;
        border: none;
        padding: 15px 30px;
        font-size: 20px;
        transition: 0.5s;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. عداد الزيارات الوهمي (للهيبة) ---
if 'visits' not in st.session_state:
    st.session_state.visits = random.randint(15400, 16000)
else:
    st.session_state.visits += 1

# --- 3. واجهة التطبيق ---
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100) # أيقونة تعبيرية
with col2:
    st.title("🛡️ نظام حمد العالمي للتحليل الذكي")
    st.write(f"👥 عدد المستفيدين من النظام حتى الآن: **{st.session_state.visits:,}** بطل وبطلة")

st.markdown("---")

# إدخال البيانات
c1, c2 = st.columns(2)
with c1:
    name = st.text_input("سجل اسمك الكريم:", placeholder="مثلاً: حمد")
with c2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

# منطق حمد الذكي للاسم
display_name = name.strip() if name.strip() else "يا بطل"
prefix = "الأستاذ" if gender == "ذكر" else "الأستاذة"

user_text = st.text_area(f"يا {prefix} {display_name}، وش شعورك اليوم؟", 
                         placeholder="اكتب شعورك هنا بكل صراحة.. نظام حمد يسمعك 🎤")

# --- 4. التحليل مع تأثير "خوارزميات حمد" ---
if st.button("بدء التحليل الذكي 🚀"):
    if name and user_text:
        with st.spinner('⏳ جاري استشارة خوارزميات حمد العالمية...'):
            time.sleep(2) # تأخير بسيط ليعطي إيحاء بالتفكير
            
        t = user_text.lower()
        pos_keywords = ["سعيد", "مستانس", "رايق", "كفو", "بطل", "رهيب", "حلو", "ممتاز", "فخم"]
        neg_keywords = ["متضايق", "طفشان", "حزين", "زعلان", "تعبان", "قهر", "ضيق"]

        if any(w in t for w in pos_keywords):
            st.balloons()
            st.success(f"🎊 النتيجة: **طاقة إيجابية متفجرة!** أنت اليوم في قمة العطاء يا {prefix} {display_name}.")
            msg = f"تحليل مشاعري في نظام حمد الذكي: إيجابي 100% 🔥🚀"
            
            # أزرار مشاركة فخمة
            st.markdown(f"### 📢 بشر أخوياك بالنتيجة:")
            st.markdown(f'''
                <a href="https://wa.me/?text={urllib.parse.quote(msg)}" target="_blank" style="text-decoration:none">
                    <button style="background-color:#25D366; color:white; border-radius:10px; padding:10px; border:none; cursor:pointer;">🟢 واتساب</button>
                </a>
                <a href="https://t.me/share/url?url={urllib.parse.quote(msg)}" target="_blank" style="text-decoration:none">
                    <button style="background-color:#24A1DE; color:white; border-radius:10px; padding:10px; border:none; cursor:pointer;">🔵 تليجرام</button>
                </a>
            ''', unsafe_allow_html=True)
            st.code(msg)

        elif any(w in t for w in neg_keywords):
            st.warning(f"يا {prefix} {display_name}، الحياة تجارب.. خذ لك بريك وشف هالشي:")
            st.video("https://www.youtube.com/watch?v=2p8nreL_lTo")
        else:
            st.info("حالة اتزان (المربع الذهبي) ⚖️ أنت في وضعية الحكيم الآن.")
            st.video("https://www.youtube.com/watch?v=68pY7z-S2_Q")
    else:
        st.error("يا بطل، سجل اسمك واكتب شعورك أولاً!")

# --- 5. صندوق الاقتراحات (انستقرام حمد) ---
st.markdown("<br><br>", unsafe_allow_html=True)
my_insta = "https://www.instagram.com/hamd_9367_?igsh=MTV6eHF5ZXdndGZ1dw=="
st.markdown(f'''
    <div style="background-color: white; padding: 20px; border-radius: 15px; border-left: 5px solid #E1306C; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
        <h4>💡 هل لديك فكرة لتطوير النظام؟</h4>
        <p>مطور النظام "حمد" يرحب بكل اقتراحاتكم الإبداعية.</p>
        <a href="{my_insta}" target="_blank" style="text-decoration: none;">
            <button style="background: linear-gradient(45deg, #f09433, #bc1888); color: white; border: none; padding: 10px 20px; border-radius: 10px; cursor: pointer;">
                📸 أرسل اقتراحك الآن
            </button>
        </a>
    </div>
''', unsafe_allow_html=True)

st.markdown(f"<br><center>حقوق البرمجة محفوظة للمطور <b>حمد</b> © 2026</center>", unsafe_allow_html=True)
                         
