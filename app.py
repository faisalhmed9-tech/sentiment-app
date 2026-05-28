import streamlit as st
import random
import time
import urllib.parse

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام حمد الذكي 2026", page_icon="🛡️", layout="wide")

# تصميم الواجهة (CSS)
st.markdown("""
    <style>
    .main { background: linear-gradient(135deg, #0f2027, #2c5364); color: white; }
    .stButton>button {
        background: linear-gradient(to right, #1E3A8A, #3B82F6);
        color: white; border-radius: 25px; padding: 15px 30px; width: 100%; border: none; font-weight: bold;
    }
    .result-card {
        background-color: rgba(255,255,255,0.15); padding: 25px; border-radius: 20px;
        border: 2px solid #3B82F6; margin-top: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }
    .share-btn {
        background-color: #25D366; color: white; padding: 10px 20px; 
        border-radius: 15px; text-decoration: none; display: inline-block; margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. الواجهة الرئيسية ---
st.title("🛡️ نظام حمد العالمي للتحليل الذكي")
st.write("حلل مشاعرك وشارك قوتك مع الأصدقاء والأقوياء! 🔥")

c1, c2 = st.columns(2)
with c1:
    name = st.text_input("سجل اسمك الكريم:", placeholder="حمد")
with c2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

user_text = st.text_area("وش شعورك الحين؟ (فضفض بالتفصيل عشان نحللك صح)")

# إعدادات اللقب والاسم
prefix = "الأستاذ" if gender == "ذكر" else "الأستاذة"
display_name = name.strip() if name.strip() else "يا بطل"

# --- 3. المنطق البرمجي والتحليل ---
if st.button("بدء التحليل وإطلاق القوة 🚀"):
    if name and user_text:
        with st.spinner('⏳ جاري استخراج الطاقة وتحليل البيانات...'):
            time.sleep(1.2)
        
        t = user_text.lower().strip()
        st.markdown('<div class="result-card">', unsafe_allow_html=True)

        # قوائم الكلمات (دقة عالية)
        sad_list = ["زعلان", "حزين", "ضيق", "تعبان", "متضايق", "مهموم", "مخلوق", "تبكي"]
        happy_list = ["سعيد", "مستانس", "رايق", "فرحان", "كفو", "بطل", "ممتاز", "قوي", "متفائل"]
        shathat = ["جوعان", "اكل", "أكل", "نوم", "بنام", "احبك", "أحبك"]

        # النتيجة النهائية (لحفظها في رابط المشاركة)
        final_result = ""

        # أولاً: فحص الحزن
        if any(word in t for word in sad_list):
            final_result = f"أنا {prefix} {display_name}، نظام حمد حلل مشاعري ولقى إني أحتاج طاقة، وعطاني رسالة قوة!"
            st.subheader(f"🛡️ دعم خاص من حمد لـ {prefix} {display_name}")
            st.info("💡 **تحليل حمد:** الضيق مجرد غمامة وتعدي. أنت جبل ما يهزه ريح! خذ لك راحة وارجع أقوى، الدنيا ما تسوى زعلك.")
            st.balloons()

        # ثانياً: فحص السعادة والقوة الإيجابية (الأقوياء)
        elif any(word in t for word in happy_list):
            final_result = f"أنا {prefix} {display_name}، حللت في نظام حمد وطلعت طاقتي الإيجابية فولي! 🔥"
            st.subheader(f"🔥 طاقة إيجابية خارقة لـ {prefix} {display_name}")
            st.success("يا سلام! السعادة والقوة تليق بك. أنت الآن في قمة عطائك، انشر هذي الطاقة حولك يا وحش!")
            st.balloons()

        # ثالثاً: الشطحات
        elif any(word in t for word in shathat):
            if "اكل" in t or "جوع" in t:
                st.warning("🍔 اترك التحليل وروح اشبع أول يا بطل!")
            elif "نوم" in t or "بنام" in t:
                st.info("😴 شكل السهر مأثر عليك.. روح ارتاح ونكمل بكره.")
            else:
                st.error("❤️ حبتك العافية! خلك في التحليل الحين.")

        # رابعاً: المحايد
        else:
            final_result = f"أنا {prefix} {display_name}، جربت نظام حمد العالمي للتحليل، وضعك مستقر وهادي!"
            st.subheader(f"⚖️ وضع الاستقرار الذهبي")
            st.write(f"أهلاً {prefix} {display_name}.. كلامك متزن. جرب تفضفض أكثر عشان نطلع القوة اللي داخلك.")

        # --- 4. ميزة المشاركة للأصدقاء ---
        if final_result:
            st.markdown("---")
            st.write("✨ **شارك نتيجتك مع الأقوياء والأصدقاء:**")
            share_msg = urllib.parse.quote(final_result + " \nجرب حظك هنا: https://fljg.streamlit.app")
            whatsapp_url = f"https://api.whatsapp.com/send?text={share_msg}"
            st.markdown(f'<a href="{whatsapp_url}" target="_blank" class="share-btn">📲 مشاركة عبر واتساب</a>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("يا حمد، سجل اسمك واكتب شعورك أول عشان تطلع النتيجة!")

st.markdown(f"<br><center>برمجة <b>حمد</b> © 2026</center>", unsafe_allow_html=True)
        
