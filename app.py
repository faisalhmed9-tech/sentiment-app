import streamlit as st
import urllib.parse
import random
import time

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام حمد الذكي 2026", page_icon="🛡️", layout="wide")

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
    </style>
    """, unsafe_allow_html=True)

# --- 2. الواجهة ---
st.title("🛡️ نظام حمد العالمي للتحليل")
st.write(f"👥 الزيارات: **{random.randint(16500, 17000):,}**")

name = st.text_input("سجل اسمك يا بطل:", placeholder="حمد")
user_text = st.text_area("فضفض لنظام حمد.. وش في خاطرك؟")

# --- 3. المنطق الذكي ---
if st.button("بدء التحليل الذكي 🚀"):
    if name and user_text:
        with st.spinner('⏳ خوارزميات حمد تفكر في كلامك...'):
            time.sleep(1.5)
        
        t = user_text.lower().strip()
        display_name = name.strip() if name.strip() else "يا وحش"

        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        
        # --- ركن الشطحات (بدون النشبة) ---
        
        # 1. شطحة الجوع
        if any(w in t for w in ["جوعان", "جوع", "اكل", "أكل"]):
            st.warning(f"🍔 يا {display_name}، نظام حمد للتحليل النفسي مو 'هنقرستيشن'! روح اطلب لك شاورما وتعال كمل.")
            
        # 2. شطحة النوم
        elif any(w in t for w in ["بنام", "نوم", "تعبان"]):
            st.info(f"😴 شكل السهر أثر عليك.. رح نم والوعد بكره، خوارزمياتي ما تبي تحلل واحد مغمض عيونه!")

        # 3. شطحة الحب
        elif "احبك" in t or "أحبك" in t:
            st.error(f"❤️ أدري إن نظامي فخم، بس خلينا أصدقاء يا {display_name}.. ركز في التحليل!")

        # --- ركن التحليل (تحفيز وإيجابية) ---
        
        elif any(w in t for w in ["حزين", "متضايق", "ضيق", "تبكي", "مهموم"]):
            st.subheader(f"✨ رسالة قوة لك يا {display_name}")
            st.info("💡 **قوة حمد:** الحزن مجرد محطة وقود لروحك، امسح دموعك وجهز نفسك لشيء عظيم جاي في الطريق. أنت أقوى من مجرد شعور عابر!")
            st.balloons()

        elif any(w in t for w in ["سعيد", "مستانس", "رايق", "بطل", "حلو"]):
            st.balloons()
            st.success(f"🔥 كفو! طاقة الإبداع عندك واصلة للسماء. استمر يا {display_name}!")

        else:
            st.info(f"⚖️ أهلاً يا {display_name}، وضعك 'سليم مستقيم'. استقرارك هذا هو بداية الإنجاز.")
        
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("لازم تسجل اسمك وكلامك عشان الخوارزميات تشتغل!")

st.markdown(f"<br><center>برمجة <b>حمد</b> © 2026</center>", unsafe_allow_html=True)
            
