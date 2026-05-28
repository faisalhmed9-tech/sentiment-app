import streamlit as st
import random
import time

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام حمد الذكي 2026", page_icon="🛡️", layout="wide")

# تعريف العداد في ذاكرة "السيرفر" المؤقتة
if 'real_counter' not in st.session_state:
    st.session_state.real_counter = 16989 

# خاصية لمنع التكرار لنفس الشخص
if 'has_counted' not in st.session_state:
    st.session_state.has_counted = False

# الوضع الليلي
mode = st.sidebar.toggle("🌙 الوضع الليلي", value=False)
if mode:
    bg, text_c, card_bg = "linear-gradient(135deg, #0f2027, #2c5364)", "white", "rgba(255,255,255,0.1)"
else:
    bg, text_c, card_bg = "linear-gradient(135deg, #f5f7fa, #c3cfe2)", "black", "white"

st.markdown(f"""
    <style>
    .main {{ background: {bg}; color: {text_c}; }}
    .stButton>button {{
        background: linear-gradient(to right, #1E3A8A, #3B82F6);
        color: white; border-radius: 25px; padding: 15px 30px; font-size: 20px;
    }}
    .result-card {{
        background-color: {card_bg}; padding: 25px; border-radius: 15px;
        border: 2px solid #3B82F6; margin-top: 20px;
    }}
    .counter-box {{
        background: #1E3A8A; color: white; padding: 10px; border-radius: 10px; text-align: center; font-size: 18px; margin-bottom: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 2. الواجهة ---
st.title("🛡️ نظام حمد العالمي للتحليل")

# عرض العداد
st.markdown(f'<div class="counter-box">👥 عدد المشاركين الحقيقي: {st.session_state.real_counter}</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    name = st.text_input("سجل اسمك يا بطل:", placeholder="حمد")
with c2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

user_text = st.text_area("فضفض لنظام حمد.. وش في خاطرك؟")

prefix = "الأستاذ" if gender == "ذكر" else "الأستاذة"
display_name = name.strip() if name.strip() else "يا وحش"

# --- 3. المنطق الذكي ---
if st.button("بدء التحليل الذكي 🚀"):
    if name and user_text:
        # الزيادة تحصل فقط مرة واحدة لكل دخول للموقع
        if not st.session_state.has_counted:
            st.session_state.real_counter += 1
            st.session_state.has_counted = True
        
        with st.spinner('⏳ خوارزميات حمد تفحص كلامك...'):
            time.sleep(1)
        
        t = user_text.lower().strip()
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        
        # --- ركن الردود ---
        if any(w in t for w in ["جوعان", "جوع", "اكل"]):
            st.warning(f"🍔 يا {prefix} {display_name}، نظام حمد مو هنقرستيشن! اطلب وتعال.")
        elif any(w in t for w in ["بنام", "نوم", "تعبان"]):
            st.info(f"😴 شكل السهر أثر عليك.. رح نم والوعد بكره.")
        elif "احبك" in t or "أحبك" in t:
            st.error(f"❤️ أدري إني فخم، بس خلينا أصدقاء يا {prefix} {display_name}!")
        elif any(w in t for w in ["حزين", "متضايق", "ضيق", "مهموم"]):
            st.subheader(f"✨ رسالة قوة")
            st.info(f"💡 يا {prefix} {display_name}، الحزن محطة وقود.. أنت أقوى مما تظن!")
            st.balloons()
        elif any(w in t for w in ["سعيد", "مستانس", "رايق", "حلو"]):
            st.balloons()
            st.success(f"🔥 كفو! طاقة الإبداع عندك توب يا {prefix} {display_name}.")
        else:
            questions = ["وش الشيء اللي لو سويته اليوم بيخليك فخور بنفسك؟", "لو معك تذكرة سفر الحين، وين تبي تروح؟"]
            st.subheader(f"⚖️ منطقة التفاعل")
            st.write(f"أهلاً {prefix} {display_name}، كلامك متزن.. جاوبني:")
            st.info(f"❓ {random.choice(questions)}")
            
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("سجل اسمك وكلامك أولاً!")

st.markdown(f"<br><center>برمجة <b>حمد</b> © 2026</center>", unsafe_allow_html=True)
