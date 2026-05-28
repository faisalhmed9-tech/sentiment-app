import streamlit as st
import random
import time

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام حمد الذكي 2026", page_icon="🛡️", layout="wide")

# العداد: بنخليه يبدأ من رقمك المفضل ويزيد فعلياً
if 'real_counter' not in st.session_state:
    st.session_state.real_counter = 16989 

# الوضع الليلي والنهاري
mode = st.sidebar.toggle("🌙 الوضع الليلي", value=True)
if mode:
    bg, text_c, card_bg = "linear-gradient(135deg, #0f2027, #2c5364)", "white", "rgba(255,255,255,0.1)"
else:
    bg, text_c, card_bg = "linear-gradient(135deg, #f5f7fa, #c3cfe2)", "black", "white"

st.markdown(f"""
    <style>
    .main {{ background: {bg}; color: {text_c}; }}
    .stButton>button {{
        background: linear-gradient(to right, #1E3A8A, #3B82F6);
        color: white; border-radius: 25px; padding: 15px 30px; font-size: 20px; width: 100%;
    }}
    .result-card {{
        background-color: {card_bg}; padding: 25px; border-radius: 15px;
        border: 2px solid #3B82F6; margin-top: 20px; color: {text_c};
    }}
    .counter-box {{
        background: #1E3A8A; color: white; padding: 10px; border-radius: 10px; text-align: center; font-size: 18px; margin-bottom: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 2. الواجهة ---
st.title("🛡️ نظام حمد العالمي للتحليل")
st.markdown(f'<div class="counter-box">👥 عدد المستفيدين الفعلي: {st.session_state.real_counter}</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    name = st.text_input("سجل اسمك:", placeholder="حمد")
with c2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

user_text = st.text_area("وش شعورك الحين؟ (فضفض بالتفصيل)")

# اللقب والاسم
prefix = "الأستاذ" if gender == "ذكر" else "الأستاذة"
display_name = name.strip() if name.strip() else "يا بطل"

# --- 3. المنطق البرمجي (المعدل والمضمون) ---
if st.button("بدء التحليل الذكي 🚀"):
    if name and user_text:
        # تحديث العداد
        st.session_state.real_counter += 1
        
        with st.spinner('⏳ خوارزميات حمد تحلل مشاعرك...'):
            time.sleep(1)
        
        t = user_text.strip()
        st.markdown('<div class="result-card">', unsafe_allow_html=True)

        # --- ترتيب الشروط عشان ما يغلط النظام ---
        
        # 1. كلمات الحزن (زعلان، حزين، متضايق)
        sad_words = ["زعلان", "حزين", "متضايق", "تعبان", "ابكي", "خنقه", "ضيق"]
        # 2. كلمات السعادة (سعيد، مستانس، رايق)
        happy_words = ["سعيد", "مستانس", "رايق", "فرحان", "كفو", "حلو", "بطل"]
        # 3. الشطحات
        shathat = ["جوعان", "اكل", "بنام", "نوم", "احبك"]

        if any(word in t for word in sad_words):
            st.subheader(f"✨ رسالة قوة يا {prefix} {display_name}")
            st.info("💡 **تحليل حمد:** الضيق مجرد غمامة وتعدي. أنت أقوى من هذا الشعور بمليون مرة، اضحك وخل الهم يولي!")
            st.balloons()

        elif any(word in t for word in happy_words):
            st.subheader(f"🔥 طاقة إيجابية يا {prefix} {display_name}")
            st.success("كفووو! السعادة تليق بك، استمر في نشر هذي الطاقة وعيش لحظتك يا وحش!")
            st.balloons()

        elif any(word in t for word in shathat):
            if "اكل" in t or "جوع" in t:
                st.warning(f"🍔 يا {display_name}، اترك التحليل وروح اطلب لك وجبة دسمة وتعال!")
            elif "نوم" in t or "بنام" in t:
                st.info(f"😴 شكل النوم غلبك.. مسموح تروح تنام ونكمل بكره.")
            else:
                st.error(f"❤️ أحبك الله الذي أحببتنا فيه يا {display_name}، خلك في التحليل!")

        else:
            # منطقة المحايد (إذا ما لقى كلمات حزن أو فرح)
            questions = [
                "وش أكثر شيء سويته اليوم وخلاك تبتسم؟",
                "لو طلبنا منك نصيحة لـ 'حمد'، وش بتقول له؟",
                "وش هدفك اللي بتوصل له هذي السنة؟"
            ]
            st.subheader(f"⚖️ منطقة التفاعل الذكي")
            st.write(f"أهلاً {prefix} {display_name}، كلامك غامض شوي.. وش رايك تجاوب على سؤالي:")
            st.warning(f"❓ {random.choice(questions)}")
            st.write("*(اكتب إجابتك فوق واضغط تحليل مرة ثانية)*")
            
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("يا بطل، لازم تكتب اسمك وشعورك أول شيء!")

st.markdown(f"<br><center>برمجة <b>حمد</b> © 2026</center>", unsafe_allow_html=True)
