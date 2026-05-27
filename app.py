import streamlit as st
from textblob import TextBlob
import urllib.parse
import random

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="تطبيق الشهير حمد", page_icon="🤖", layout="centered")

# --- 2. قوائم اليوتيوب (روابط جديدة ومضمونة التشغيل) ---
neg_videos = [
    "https://www.youtube.com/watch?v=2p8nreL_lTo", 
    "https://www.youtube.com/watch?v=pY9InT15v70"
]
neu_videos = [
    "https://www.youtube.com/watch?v=68pY7z-S2_Q",
    "https://www.youtube.com/watch?v=07d2dXHYb94"
]

# --- 3. واجهة التطبيق ---
st.title("🤖 تطبيق الشهير حمد لتحليل المشاعر")
st.markdown("---")

name = st.text_input("سجل اسمك الكريم:")
gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

# تخصيص اللقب
prefix = "الشهير" if gender == "ذكر" else "الشهيرة"

user_text = st.text_area(f"يا {prefix} {name}، عبر عما في داخلك:", height=150)

if st.button("إجراء التحليل الذكي 🔍"):
    if name and user_text:
        # عملية التحليل
        blob = TextBlob(user_text)
        score = blob.sentiment.polarity
        
        # إحصائيات سريعة
        words_count = len(user_text.split())
        st.markdown(f"### 📊 تقرير التحليل لـ {prefix} {name}:")
        st.write(f"عدد الكلمات التي حللها حمد: {words_count}")

        # --- الحالة 1: الإيجابية (حساسية عالية للكلمات) ---
        if score > 0.0:
            st.balloons()
            st.success(f"طاقتك إيجابية مذهلة يا {prefix} {name}! ✨")
            msg = f"أنا {prefix} {name}، نتيجتي إيجابية في تطبيق 'الشهير حمد' 🔥! جربوا حظكم: https://sentiment-app-cncmahfqt2zhxibcsofljg.streamlit.app/"
            whatsapp_url = f"https://wa.me/?text={urllib.parse.quote(msg)}"
            st.markdown(f'''<a href="{whatsapp_url}" target="_blank">
                <button style="width:100%; background-color:#25D366; color:white; border:none; padding:15px; border-radius:15px; font-weight:bold; cursor:pointer;">
                📢 شارك نتيجتك الإيجابية عبر واتساب
                </button></a>''', unsafe_allow_html=True)

        # --- الحالة 2: السلبية ---
        elif score < 0.0:
            st.error(f"وسع صدرك يا {prefix} {name}.. الدنيا ما تسوى.")
            st.info("🎬 شاهد هذا المقطع ليغير مزاجك:")
            st.video(random.choice(neg_videos))

        # --- الحالة 3: المحايدة (المربع الذهبي) ---
        else:
            st.warning(f"مزاجك اليوم متزن ورايق يا {prefix} {name} ⚖️")
            st.markdown("""
                <div style="background-color:rgba(255, 215, 0, 0.1); padding:20px; border-radius:15px; border:2px solid #ffd700; text-align:center;">
                    <h4 style="color:#ffd700; margin:0;">🌟 ميزة الشخص المتزن:</h4>
                    <p style="color:white; margin:10px 0;">بما أن عقلك في حالة هدوء وتركيز، اخترنا لك هذا المقطع الثقافي:</p>
                </div>
            """, unsafe_allow_html=True)
            st.video(random.choice(neu_videos))
            
    else:
        st.error("لطفاً، اكتب اسمك وكلامك أولاً.")

# --- التذييل ---
st.markdown("---")
st.markdown(f"<center>تم التطوير بكل فخر بواسطة <b>الشهير حمد</b> | 2026</center>", unsafe_allow_html=True)



    



                



        


      
