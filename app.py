import streamlit as st
import time
import random
import urllib.parse

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام حمد الذكي", layout="centered", initial_sidebar_state="collapsed")

# --- 2. CSS حق التصميم (تعديلات حمد الاحترافية) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
    /* توحيد الخط والاتجاه */
    html, body, [class*="st-"] {
        font-family: 'Tajawal', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* تنسيق العنوان والنصوص عشان ما تنعكس */
    .header-container {
        direction: rtl;
        text-align: right;
        margin-bottom: 20px;
    }

    /* زر التحليل (التدرج اللوني اللي صممته أنت) */
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        font-weight: bold;
        background: linear-gradient(90deg, #4CAF50, #2196F3);
        color: white;
        border: none;
        padding: 12px;
        font-size: 18px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }

    /* صندوق النتيجة الفخم */
    .result-box {
        background: #1e1e1e;
        padding: 25px;
        border-radius: 15px;
        border-right: 5px solid #4CAF50;
        margin-top: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        color: white;
        direction: rtl;
        text-align: right;
    }

    /* زر الواتساب الأخضر */
    .whatsapp-btn {
        display: block;
        width: 100%;
        background-color: #25D366;
        color: white !important;
        padding: 12px;
        border-radius: 15px;
        text-align: center;
        text-decoration: none;
        margin-top: 15px;
        font-weight: bold;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. واجهة التطبيق (الكلام الأصلي بدون عكس) ---
st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.title("🤖 نظام حمد الذكي")
st.write("وش يدور في خاطرك: فضفض وسوف يتم تحليلك!")
st.markdown('</div>', unsafe_allow_html=True)

# خانة النص
user_input = st.text_area("اكتب شعورك هنا:", height=120, placeholder="مثال: طفشان، تعبان، مبسوط...")

# دالة التحليل
def analyze_feeling(text):
    text = text.strip()
    if any(word in text for word in ["طفشان", "زهقان", "ملل", "طفش"]):
        return "طفشان", "😴"
    elif any(word in text for word in ["تعبان", "مرهق", "سهر", "تعب", "نوم"]):
        return "تعبان", "🥱"
    elif any(word in text for word in ["مبسوط", "فرحان", "تمام", "رايق"]):
        return "مبسوط", "😄"
    elif any(word in text for word in ["زعلان", "حزين", "ضايق"]):
        return "زعلان", "😢"
    elif any(word in text for word in ["احبك", "أحبك"]):
        return "حب", "❤️"
    else:
        return "عادي", "😐"

# --- 4. منطق العمل عند الضغط على الزر ---
if st.button("بدء التحليل وإطلاق القوة 🚀"):
    if not user_input.strip():
        st.warning("اكتب شي أول يا بطل! ما ينفع نحلل بياض.")
    else:
        with st.spinner("جاري استخراج البيانات وتحليل قوتك..."):
            time.sleep(1.5)
        
        feeling, emoji = analyze_feeling(user_input)
        
        # تحديد اللقب (الأستاذ / الأستاذة) بناءً على النص
        if any(w in user_input for w in ["أستاذة", "استاذه", "بنت", "دكتورة", "معلمة"]):
            address = "يا الأستاذة"
        else:
            address = "يا الأستاذ"
            
        # صياغة الرد (نفس أسلوبك اللي تحبه)
        if feeling == "تعبان" or feeling == "عادي":
            res_text = f"{emoji} شكل السهر مأثر عليك {address}.. روح ارتاح، النوم سلطان."
        elif feeling == "مبسوط":
            res_text = f"{emoji} كفو {address}! دوم هالوناسة والروقان يا بطل."
        elif feeling == "طفشان":
            res_text = f"{emoji} الطفش بداية الإبداع {address}، غير جو وبترجع أقوى."
        elif feeling == "حب":
            res_text = f"{emoji} حبتك العافية {address}! القلب وما يهوى."
        else:
            res_text = f"{emoji} هدي اللعب {address}، الأمور بتزين والوضع مستقر."

        # عرض النتيجة في الصندوق
        st.markdown(f'<div class="result-box"><h3>{res_text}</h3></div>', unsafe_allow_html=True)
        
        # الاحتفال
        st.balloons()
        
        # رابط المشاركة
        share_msg = urllib.parse.quote(res_text + " \nحلل شعورك في نظام حمد الذكي: https://fljg.streamlit.app")
        whatsapp_url = f"https://wa.me/?text={share_msg}"
        st.markdown(f'<a href="{whatsapp_url}" target="_blank" class="whatsapp-btn">📤 شارك النتيجة على واتساب</a>', unsafe_allow_html=True)

# --- 5. التذييل (Footer) ---
st.markdown("---")
st.markdown('<div style="text-align:center; color:gray;">صنع بـ ❤️ بواسطة حمد | 2026</div>', unsafe_allow_html=True)
            
