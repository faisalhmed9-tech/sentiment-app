import streamlit as st
import random
import time
import urllib.parse

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام حمد الذكي", layout="centered")

# --- 2. التنسيق البصري الفخم ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Tajawal', sans-serif; direction: rtl; text-align: right; }
    .stApp { background-color: #0f172a; color: white; }
    
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #1e293b !important; 
        color: #ffffff !important;
        border: 2px solid #38bdf8 !important; 
        border-radius: 12px !important;
    }
    
    input::placeholder, textarea::placeholder {
        color: #94a3b8 !important;
        opacity: 1;
    }
    
    .stButton>button {
        width: 100%; border-radius: 15px; font-weight: bold;
        background: linear-gradient(90deg, #38bdf8, #2196F3);
        color: white; border: none; padding: 15px; font-size: 18px;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(56, 189, 248, 0.4);
    }
    .result-box { padding: 30px; border-radius: 20px; margin-top: 25px; color: white; text-align: center; box-shadow: 0 10px 20px rgba(0,0,0,0.4); }
    .insta-box { text-align: center; margin-top: 30px; padding: 15px; background: rgba(30, 41, 59, 0.5); border-radius: 15px; border: 1px solid #38bdf8; }
    .whatsapp-btn { background-color: #25D366; color: white !important; padding: 12px 25px; border-radius: 10px; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 15px; transition: 0.3s; }
    .whatsapp-btn:hover { background-color: #20ba5a; transform: scale(1.05); }
</style>
""", unsafe_allow_html=True)

# --- 3. المحرك الذكي (3 ردود لكل حالة) ---
def analyze_all(text, name, gender):
    text = text.lower()
    p_title = "يا بطل" if gender == "ذكر" else "يا بطلة"

    # [الحالات الشاطحة]
    if any(word in text for word in ["أحبك", "حب", "يا بعدي", "عشق"]):
        res = random.choice([
            f"يا بعد قلبي {p_title} {name}!",
            f"المحبة متبادلة وكلنا نحبك يا {name}.",
            f"تستاهل كل خير وحب يا {name}."
        ])
        return "#f472b6", res 
    
    elif any(word in text for word in ["جوعان", "أكل", "جعت", "ميت جوع", "جوع"]):
        res = random.choice([
            f"يا {name} قم اضرب بالخمس ولا يردك شيء!",
            f"عوافي مقدماً {p_title} {name}، البطن أهم.",
            f"العصافير بدت تزقزق.. روح تعشى يا {name}."
        ])
        return "#FFA500", res 
    
    elif any(word in text for word in ["تعبان", "مريض", "مصدع", "تعبانة", "مريضة", "راسي"]):
        res = random.choice([
            f"سلامتك ألف سلامة يا {name}، خطاك السوء يا رب.",
            f"طهور إن شاء الله {p_title} {name}، ارتاح واشرب شيء دافي.",
            f"قدامك العافية يا {name}، لا تجهد نفسك اليوم."
        ])
        return "#8b5cf6", res 
    
    elif any(word in text for word in ["هياط", "مهايط", "أنا القوي"]):
        res = random.choice([
            f"اذكر الله يا {name} وهد اللعب شوي.",
            f"ما يحتاج هياط يا {p_title} {name}، الكل عارف قدرك.",
            f"خلك ريلاكس يا {name}، الأمور سهالات."
        ])
        return "#ef4444", res 

    # [تحليل المشاعر الأساسي]
    elif any(word in text for word in ["مستانس", "مروق", "وناسة", "فرحان", "مبسوط", "حلو", "كفو"]):
        res = random.choice([
            f"دوم هالروقان {p_title} {name}! كلام يفتح النفس.",
            f"يا عيني على المزاج العالي والطاقة الإيجابية.",
            f"عسى أيامك كلها سعادة يا {name}.. استمر!"
        ])
        return "#22c55e", res 
    
    elif any(word in text for word in ["متضايق", "مغثوث", "طفشان", "زهقان", "زعلان", "سيء"]):
        res = random.choice([
            f"أفا يا {name}، الضيقة ما تدوم وبكرا أجمل.",
            f"خذ نفس عميق يا {p_title} {name}، وهونها وتهون.",
            f"الله يبعد عنك الكدر، اضحك يا {name} الدنيا فانية."
        ])
        return "#ef4444", res 
    
    else:
        return "#38bdf8", f"منور {p_title} {name}، وضعك مستقر ومحايد."

# --- 4. الواجهة الرسمية ---
st.title("🤖 نظام حمد الذكي")

col1, col2 = st.columns(2)
with col1:
    input_name = st.text_input("سجل اسمك للاختبار:", placeholder="مثلاً: حمد")
with col2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

user_input = st.text_area("وش بخاطرك الحين؟", placeholder="اكتب مشاعرك هنا...")

if st.button("بدء التحليل 🚀"):
    if input_name.strip() and user_input.strip():
        with st.spinner("لحظة..."):
            time.sleep(1)
        color, reply = analyze_all(user_input, input_name, gender)
        
        st.markdown(f'<div class="result-box" style="background:{color};"><h2>{reply}</h2></div>', unsafe_allow_html=True)
        
        # زر الواتساب (المشاركة المصلحة)
        whatsapp_msg = urllib.parse.quote(f"نتيجة تحليلي في نظام حمد الذكي: {reply}")
        whatsapp_url = f"https://api.whatsapp.com/send?text={whatsapp_msg}"
        st.markdown(f'<div style="text-align:center;"><a href="{whatsapp_url}" target="_blank" class="whatsapp-btn">مشاركة عبر الواتساب ✅</a></div>', unsafe_allow_html=True)
    else:
        st.warning("سجل بياناتك كاملة يا بطل!")

# --- 5. صندوق الاقتراحات (إنستغرامك المربوط) ---
st.markdown("---")
st.markdown(f"""
    <div class="insta-box">
        <p style="color:white; margin-bottom:10px;">عندك اقتراح لتطوير النظام؟ أرسله هنا:</p>
        <a href="https://www.instagram.com/hamd_9367_?igsh=MTV6eHF5ZXdndGZ1dw==" target="_blank" style="color:#38bdf8; font-weight:bold; text-decoration:none;">
            📸 حساب حمد (صندوق الاقتراحات)
        </a>
    </div>
""", unsafe_allow_html=True)

st.caption("صنع بـ ❤️ بواسطة حمد | 2026")
