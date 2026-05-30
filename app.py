import streamlit as st
import random
import time
import urllib.parse

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام حمد الذكي", layout="centered")

# --- 2. التنسيق البصري (نفس الروح اللي تحبها) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Tajawal', sans-serif; direction: rtl; text-align: right; }
    .stButton>button {
        width: 100%; border-radius: 15px; font-weight: bold;
        background: linear-gradient(90deg, #4CAF50, #2196F3);
        color: white; border: none; padding: 15px; font-size: 18px;
    }
    .result-box { padding: 30px; border-radius: 20px; margin-top: 25px; color: white; text-align: center; box-shadow: 0 10px 20px rgba(0,0,0,0.2); }
    .insta-box { text-align: center; margin-top: 30px; padding: 15px; background: #f8f9fa; border-radius: 15px; border: 1px solid #ddd; }
    .whatsapp-btn { background-color: #25D366; color: white !important; padding: 10px 20px; border-radius: 10px; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 15px; }
</style>
""", unsafe_allow_html=True)

# --- 3. المحرك الذكي (العامية + تنوع الردود) ---
def analyze_all(text, name, gender):
    text = text.lower()
    p_title = "يا بطل" if gender == "ذكر" else "يا بطلة"

    # [الحالات الشاطحة]
    if any(word in text for word in ["أحبك", "حب", "يا بعدي", "عشق"]):
        return "#FF4B2B", random.choice([f"يا بعد قلبي {p_title} {name}!", f"المحبة متبادلة يا {name}.", f"تستاهل الحب يا {name}."])
    
    elif any(word in text for word in ["جوعان", "أكل", "جعت", "ميت جوع"]):
        return "#FFA500", random.choice([f"يا {name} قم اضرب بالخمس!", f"عوافي مقدماً {p_title} {name}."])
    
    elif any(word in text for word in ["تعبان", "مرهق", "أنام", "دايخ"]):
        return "#607D8B", random.choice([f"سلامتك من التعب {p_title} {name}.", f"ارتاح يا {name}، الجسم له حق."])
    
    elif any(word in text for word in ["قوي", "وحش", "كفو", "أقدر"]):
        return "#4CAF50", random.choice([f"كفو {p_title} {name}! وحش ومحد قدك.", f"عزيمة حديد يا {name}."])

    # [تحليل المشاعر الأساسي]
    elif any(word in text for word in ["مستانس", "مروق", "وناسة", "فرحان", "مبسوظ"]):
        return "#4CAF50", random.choice([f"دوم هالروقان {p_title} {name}!", f"يا عيني على المزاج العالي يا {name}."])
    
    elif any(word in text for word in ["ضايق", "منغث", "طفشان", "زهقان", "زعلان"]):
        return "#F44336", random.choice([f"أفا يا {name}، الضيقة ما تدوم.", f"فضفض {p_title} {name}، وبكرا أجمل."])
    
    elif any(word in text for word in ["عادي", "تمام", "طيب", "ماشي"]):
        return "#808080", f"يوم هادي ومستقر يا {name}."

    else:
        return "#2196F3", f"منور {p_title} {name}، نورت البرنامج."

# --- 4. الواجهة الرسمية ---
st.title("🤖 نظام حمد الذكي")

col1, col2 = st.columns(2)
with col1:
    input_name = st.text_input("سجل اسمك للاختبار:", placeholder="")
with col2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

user_input = st.text_area("وش بخاطرك الحين؟")

if st.button("بدء التحليل 🚀"):
    if input_name.strip() and user_input.strip():
        with st.spinner("لحظة..."):
            time.sleep(1)
        color, reply = analyze_all(user_input, input_name, gender)
        
        st.markdown(f'<div class="result-box" style="background:{color};"><h2>{reply}</h2></div>', unsafe_allow_html=True)
        
        # زر الواتساب (المشاركة)
        whatsapp_msg = urllib.parse.quote(f"نتيجة تحليلي في نظام حمد الذكي: {reply}")
        st.markdown(f'<div style="text-align:center;"><a href="https://wa.me/?text={whatsapp_msg}" target="_blank" class="whatsapp-btn">مشاركة عبر الواتساب ✅</a></div>', unsafe_allow_html=True)
    else:
        st.warning("سجل بياناتك كاملة يا بطل!")

# --- 5. صندوق الاقتراحات (إنستغرام) ---
st.markdown("---")
st.markdown(f"""
    <div class="insta-box">
        <p style="color:#333; margin-bottom:10px;">عندك اقتراح لتطوير النظام؟ أرسله هنا:</p>
        <a href="https://www.instagram.com/hamd_9367_?igsh=MTV6eHF5ZXdndGZ1dw==" target="_blank" style="color:#E1306C; font-weight:bold; text-decoration:none;">
            📸 حساب حمد (صندوق الاقتراحات)
        </a>
    </div>
""", unsafe_allow_html=True)

st.caption("صنع بـ ❤️ بواسطة حمد | 2026")
