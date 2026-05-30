import streamlit as st
import random
import time

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام حمد الذكي", layout="centered")

# --- 2. التصميم (CSS) - الألوان والخطوط الفخمة ---
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
</style>
""", unsafe_allow_html=True)

# --- 3. محرك التحليل الشامل (العامية + تنوع الردود + الجنس) ---
def analyze_all(text, name, gender):
    text = text.lower()
    
    # تحديد اللقب والمنادى بناءً على الجنس
    p_title = "يا بطل" if gender == "ذكر" else "يا بطلة"
    s_title = "الأستاذ" if gender == "ذكر" else "الأستاذة"

    # [1] قسم الحب ❤️
    if any(word in text for word in ["أحبك", "حب", "يا بعدي", "عشق", "غالي"]):
        replies = [f"يا بعد قلبي {p_title} {name}!", f"المحبة متبادلة يا {name}، كلك ذوق.", f"تستاهل كل الحب والتقدير يا {name}."]
        return "#FF4B2B", random.choice(replies)

    # [2] قسم الجوع 🍔
    elif any(word in text for word in ["جوعان", "أكل", "جعت", "ميت جوع"]):
        replies = [f"يا {name} الجوع كافر! قم اضرب بالخمس.", f"عوافي مقدماً {p_title} {name}، لا تنسى تعزمنا.", f"الجوع شين يا {name}، رح روّق بوجبة دسمة."]
        return "#FFA500", random.choice(replies)

    # [3] قسم التعب 😫
    elif any(word in text for word in ["تعبان", "مرهق", "أبي أنام", "دايخ"]):
        replies = [f"سلامتك من التعب {p_title} {name}.", f"ارتاح يا {name}، جسمك له حق عليك.", f"نوم العوافي مقدماً يا {name}، ريح باللع."]
        return "#607D8B", random.choice(replies)

    # [4] قسم القوة 🔥
    elif any(word in text for word in ["قوي", "وحش", "كفو", "أقدر", "عزيمة"]):
        replies = [f"كفو {p_title} {name}! وحش ومحد قدك.", f"هذي العزيمة اللي نعرفها فيك يا {name}.", f"قوي وتبقى قوي يا {name}، استمر!"]
        return "#4CAF50", random.choice(replies)

    # [5] المود: إيجابي 🟢
    elif any(word in text for word in ["مستانس", "مروق", "وناسة", "فرحان", "مبسوط"]):
        replies = [f"دوم هالضحكة والروقان {p_title} {name}!", f"يا عيني على المزاج العالي يا {name}.", f"كفو! خلك دايم مروق ومنعش يا {name}."]
        return "#4CAF50", random.choice(replies)
    
    # [6] المود: سلبي 🔴
    elif any(word in text for word in ["ضايق", "منغث", "طفشان", "زهقان", "زعلان", "نفسية"]):
        replies = [f"أفا يا {name}، الضيقة ما تدوم وبكرا أجمل.", f"فضفض {p_title} {name}، كلنا نمر بأيام كذا وتعدي.", f"لا يضيق صدرك يا {name}، الدنيا ما تسوى."]
        return "#F44336", random.choice(replies)
    
    # [7] المود: محايد ⚪
    elif any(word in text for word in ["عادي", "تمام", "طيب", "ماشي"]):
        replies = [f"يوم هادي ومستقر {s_title} {name}.", f"أهم شي إنك بخير ومرتاح البال يا {name}.", f"الله يكتب لك الخير في يومك يا {name}."]
        return "#808080", random.choice(replies)

    # الرد التلقائي (منور)
    else:
        return "#2196F3", f"منور {p_title} {name}، نورت البرنامج بطلتك."

# --- 4. واجهة التطبيق ---
st.title("🤖 نظام حمد الذكي")
st.write("حلل مزاجك (إيجابي، سلبي، محايد) أو شطحاتك (حب، جوع، تعب، قوة)!")

# إدخال البيانات
col1, col2 = st.columns(2)
with col1:
    input_name = st.text_input("سجل اسمك للاختبار:", placeholder="")
with col2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

user_input = st.text_area("وش بخاطرك الحين؟ (شطّح بالعامية):", placeholder="")

if st.button("بدء التحليل وإطلاق القوة 🚀"):
    if not input_name.strip() or not user_input.strip():
        st.warning("يا بطل سجل اسمك وكلامك أولاً!")
    else:
        with st.spinner("جاري قراءة أفكارك..."):
            time.sleep(1)
        
        color, reply = analyze_all(user_input, input_name, gender)
        
        st.markdown(f"""
        <div class="result-box" style="background:{color};">
            <p style="font-size: 24px; font-weight: bold; margin:0;">{reply}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.caption(f"صنع بـ ❤️ بواسطة حمد | 2026")
             
