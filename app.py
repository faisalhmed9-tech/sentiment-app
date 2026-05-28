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
        border-radius: 15px; text-decoration: none; display: inline-block; margin-top: 10px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. الواجهة الرئيسية ---
st.title("🛡️ نظام حمد العالمي للتحليل الذكي")
st.write("النسخة الكاملة: تحليل | شطحات | مشاركة | طاقة إيجابية")

c1, c2 = st.columns(2)
with c1:
    name = st.text_input("سجل اسمك الكريم:", placeholder="حمد")
with c2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

user_text = st.text_area("وش يدور في خاطرك؟ فضفض (نظام حمد يسمعك)")

# إعدادات اللقب
prefix = "الأستاذ" if gender == "ذكر" else "الأستاذة"
display_name = name.strip() if name.strip() else "يا بطل"

# --- 3. المنطق البرمجي (التحليل الشامل) ---
if st.button("بدء التحليل وإطلاق القوة 🚀"):
    if name and user_text:
        with st.spinner('⏳ خوارزميات حمد تستخرج الطاقة...'):
            time.sleep(1)
        
        t = user_text.lower().strip()
        st.markdown('<div class="result-card">', unsafe_allow_html=True)

        # قوائم الكلمات
        sad_list = ["زعلان", "حزين", "ضيق", "تعبان", "متضايق", "مهموم", "مخلوق", "تبكي"]
        happy_list = ["سعيد", "مستانس", "رايق", "فرحان", "كفو", "بطل", "ممتاز", "قوي", "متفائل"]
        
        # --- ركن الشطحات (الكلمات الشاطحة) ---
        is_shatha = False
        if any(w in t for w in ["جوعان", "جوع", "اكل", "أكل"]):
            st.warning(f"🍔 يا {display_name}، نظام حمد مو مطعم! روح اشبع وتعال نحلل صح.")
            is_shatha = True
        elif any(w in t for w in ["نوم", "بنام", "نعسان", "تعب"]):
            st.info(f"😴 شكل السهر مأثر عليك يا {prefix} {display_name}.. روح ارتاح، النوم سلطان.")
            is_shatha = True
        elif any(w in t for w in ["احبك", "أحبك", "عشق"]):
            st.error(f"❤️ حبتك العافية يا {display_name}! بس خلك رزين، إحنا هنا للتحليل بس.")
            is_shatha = True

        # --- ركن التحليل (إذا ما كانت شطحة) ---
        if not is_shatha:
            final_result = ""
            
            if any(word in t for word in sad_list):
                st.subheader(f"🛡️ رسالة دعم لـ {prefix} {display_name}")
                st.info("💡 **تحليل حمد:** الزعل ما يليق فيك. أنت أقوى من الظروف، اضحك وخل الهم لغيرك!")
                st.balloons()
                final_result = f"أنا {prefix} {display_name}، نظام حمد عطاني جرعة قوة اليوم! 💪"

            elif any(word in t for word in happy_list):
                st.subheader(f"🔥 طاقة إيجابية خارقة لـ {prefix} {display_name}")
                st.success("ما شاء الله! طاقتك في السماء. استمر في الإبداع يا وحش!")
                st.balloons()
                final_result = f"أنا {prefix} {display_name}، طاقتي الإيجابية فولي في نظام حمد! 🔥"

            else:
                st.subheader(f"⚖️ وضع الاستقرار")
                st.write(f"أهلاً {prefix} {display_name}.. كلامك هادي ومتزن. جرب تفضفض أكثر!")
                final_result = f"أنا {prefix} {display_name}، جربت نظام حمد ووضعي مستقر ⚖️"

            # --- 4. ميزة المشاركة للأصدقاء والأقوياء ---
            st.markdown("---")
            st.write("✨ **أرسلها للأصدقاء والأقوياء:**")
            share_msg = urllib.parse.quote(final_result + " \nحلل مشاعرك هنا: https://fljg.streamlit.app")
            whatsapp_url = f"https://api.whatsapp.com/send?text={share_msg}"
            st.markdown(f'<a href="{whatsapp_url}" target="_blank" class="share-btn">📲 مشاركة عبر واتساب</a>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("يا حمد، سجل اسمك واكتب شعورك أول!")

st.markdown(f"<br><center>برمجة <b>حمد</b> © 2026</center>", unsafe_allow_html=True)
