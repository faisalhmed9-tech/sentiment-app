import streamlit as st
from textblob import TextBlob
import urllib.parse
import random

# --- 1. إعدادات الصفحة الفخمة ---
st.set_page_config(page_title="تطبيق الشهير حمد", page_icon="🤖", layout="centered")

# --- 2. قوائم اليوتيوب (محتوى هادف وبدون موسيقى) ---
neg_videos = [
    "https://www.youtube.com/watch?v=M9pX_m_oZg0", 
    "https://www.youtube.com/watch?v=M6Z_D0u_Sxk"
]
neu_videos = [
    "https://www.youtube.com/watch?v=6m82_A8Y0S4", 
    "https://www.youtube.com/watch?v=S2uF6Mh6D4s",
    "https://www.youtube.com/watch?v=jP649Z78NYU"
]

# --- 3. واجهة التطبيق الرئيسية ---
st.title("🤖 تطبيق الشهير حمد لتحليل المشاعر")
st.markdown("---")

# مدخلات المستخدم
name = st.text_input("سجل اسمك الكريم:")
gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

# تخصيص اللقب واللون بناءً على الجنس
if gender == "ذكر":
    prefix, accent_color = "الشهير", "#1e90ff"
else:
    prefix, accent_color = "الشهيرة", "#ff69b4"

user_text = st.text_area(f"يا {prefix} {name}، عبر عما في داخلك وسأقوم بتحليله:", height=150)

if st.button("إجراء التحليل الذكي 🔍"):
    if name and user_text:
        # عملية التحليل البرمجي
        blob = TextBlob(user_text)
        score = blob.sentiment.polarity
        
        # إحصائيات إضافية (كلام زيادة لإبهار المستخدم)
        words_count = len(user_text.split())
        chars_count = len(user_text)
        
        st.markdown(f"### 📊 تقرير التحليل لـ {prefix} {name}:")
        
        # عرض عدادات النص
        c1, c2 = st.columns(2)
        c1.metric("عدد الكلمات", words_count)
        c2.metric("عدد الحروف", chars_count)

        # --- الحالة 1: الإيجابية 😍 ---
        if score > 0.1:
            st.balloons()
            st.success(f"طاقتك إيجابية مذهلة يا {prefix} {name}! ✨")
            st.info("💡 نصيحة حمد: السعادة تزداد عندما نشاركها، أخبر أحبابك بنتيجتك!")
            
            # زر الواتساب المباشر
            msg = f"أنا {prefix} {name}، حللت مشاعري في تطبيق 'الشهير حمد' وطلعت نتيجتي إيجابية 🔥! جربوا حظكم: https://sentiment-app-cncmahfqt2zhxibcsofljg.streamlit.app/"
            whatsapp_url = f"https://wa.me/?text={urllib.parse.quote(msg)}"
            st.markdown(f'''<a href="{whatsapp_url}" target="_blank">
                <button style="width:100%; background-color:#25D366; color:white; border:none; padding:15px; border-radius:15px; font-weight:bold; cursor:pointer;">
                📢 أرسل نتيجتك الإيجابية للأصدقاء والأقارب
                </button></a>''', unsafe_allow_html=True)

        # --- الحالة 2: السلبية 😔 ---
        elif score < -0.1:
            st.error(f"وسع صدرك يا {prefix} {name}، كل مر سيمر بإذن الله.")
            st.info("💡 نصيحة حمد: خذ استراحة قصيرة وشاهد هذا المقطع لتغيير جوك.")
            st.write("🎬 **مقطع فيديو مختار لك بعناية:**")
            st.video(random.choice(neg_videos))

        # --- الحالة 3: المحايدة ⚖️ (المربع الذهبي) ---
        else:
            st.warning(f"مزاجك اليوم 'منطقة ذهبية'.. متزن ورايق يا {prefix} {name} ⚖️")
            st.markdown("""
                <div style="background-color:rgba(255, 215, 0, 0.1); padding:20px; border-radius:15px; border:2px solid #ffd700; text-align:center;">
                    <h4 style="color:#ffd700; margin:0;">🌟 ميزة الشخص المتزن:</h4>
                    <p style="color:white; margin:10px 0;">بما أن عقلك في حالة هدوء وتركيز عالية، ننصحك بمشاهدة هذا المقطع الثقافي السريع:</p>
                </div>
            """, unsafe_allow_html=True)
            st.video(random.choice(neu_videos))
            
    else:
        st.error("لطفاً، نحتاج الاسم والنص لنبدأ التحليل!")

# --- التذييل النهائي ---
st.markdown("---")
st.markdown(f"<center>تم التطوير بكل فخر بواسطة <b>الشهير حمد</b> | 2026</center>", unsafe_allow_html=True)


    



                



        


      
