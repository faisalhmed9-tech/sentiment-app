import streamlit as st
import urllib.parse
import random

# --- 1. إعدادات الصفحة الأساسية ---
st.set_page_config(page_title="نظام حمد الذكي 2026", page_icon="🛡️")

# --- 2. قاعدة البيانات ---
bad_words = ["كلمة1", "كلمة2", "كلمة3"] 

neg_videos = [
    "https://www.youtube.com/watch?v=2p8nreL_lTo", 
    "https://www.youtube.com/watch?v=pY9InT15v70"
]
neu_videos = [
    "https://www.youtube.com/watch?v=68pY7z-S2_Q", 
    "https://www.youtube.com/watch?v=07d2dXHYb94"
]

# --- 3. تصميم واجهة التطبيق ---
st.title("🛡️ نظام حمد العالمي للتحليل")
st.write("مرحباً بك في النسخة المطورة من نظام التحليل النفسي والذكاء الاصطناعي.")
st.markdown("---")

# إدخال بيانات المستخدم
name = st.text_input("سجل اسمك الكريم:")
gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

# التعديل حق الاسم
display_name = name.strip() if name.strip() else "يا بطل"
prefix = "الأستاذ" if gender == "ذكر" else "الأستاذة"
user_text = st.text_area(f"{prefix} {display_name}، وش شعورك اليوم؟ صف لنا حالتك..", height=150)

# --- 4. منطق التحليل والمعالجة ---
if st.button("تحليل النتيجة 🔍"):
    if name and user_text:
        t = user_text.lower()
        
        if any(word in t for word in bad_words):
            st.error("⚠️ عذراً يا بطل، النص يحتوي على كلمات غير ملائمة. فضلاً اجعل كلامك راقياً مثلك.")
        else:
            pos_keywords = ["سعيد", "مستانس", "رايق", "كفو", "بطل", "رهيب", "حلو", "ممتاز", "happy", "great", "nice"]
            neg_keywords = ["متضايق", "طفشان", "حزين", "زعلان", "تعبان", "قهر", "ضيق", "sad", "bad", "angry"]

            if any(w in t for w in pos_keywords):
                st.balloons()
                st.success(f"ما شاء الله! النتيجة إيجابية جداً! كفو يا {prefix} {name}، دوم هالروقان ✨")
                
                msg = f"أنا {prefix} {name}، حللت مشاعري في نظام حمد الذكي وطلعت النتيجة إيجابية! 🔥🚀"
                encoded_msg = urllib.parse.quote(msg)
                
                st.markdown("### 📢 شارك النتيجة مع أخوياك:")
                c1, c2, c3 = st.columns(3)
                with c1:
                    st.markdown(f'[WhatsApp](https://wa.me/?text={encoded_msg})', unsafe_allow_html=True)
                with c2:
                    st.markdown(f'[Telegram](https://t.me/share/url?url={encoded_msg}&text={encoded_msg})', unsafe_allow_html=True)
                with c3:
                    st.markdown(f'[X](https://twitter.com/intent/tweet?text={encoded_msg})', unsafe_allow_html=True)
                
                st.markdown("---")
                st.write("📸 **للمشاركة في سناب وتيك توك:**")
                st.info("انسخ النص أدناه وانشره في قصتك (Story) ليراها الجميع:")
                st.code(msg)

            elif any(w in t for w in neg_keywords):
                st.error(f"أفا يا {prefix} {name}.. النتيجة فيها شوية ضيق. لا يهمك، خذ لك بريك وشف هالمقطع يغير جوك:")
                st.video(random.choice(neg_videos))
            
            else:
                st.warning(f"أهلاً {prefix} {name}، أنت الآن في حالة اتزان (المربع الذهبي).")
                st.write("استمتع بهدوئك وتابع هذا المقطع:")
                st.video(random.choice(neu_videos))
    else:
        st.error("يا بطل، لازم تسجل اسمك وتكتب شي عشان أقدر أحلل شخصيتك!")

# --- 5. قسم التواصل والاقتراحات ---
st.markdown("---")
st.subheader("💡 عندك فكرة لتطوير النظام؟")
st.write("يا مبدع، إذا عندك فكرة أو اقتراح تبي حمد يضيفه في التحديث الجاي، تواصل معه مباشرة:")

my_insta_url = "https://www.instagram.com/hamd_9367_?igsh=MTV6eHF5ZXdndGZ1dw=="

st.markdown(f'''
<a href="{my_insta_url}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
    <div style="
        background: linear-gradient(45deg, #405DE6, #5851DB, #833AB4, #C13584, #E1306C, #FD1D1D);
        background: linear-gradient(45deg, #405DE6, #5851DB, #833AB4, #C13584, #E1306C, #FD1D1D);
        color: white;
        padding: 15px 25px;
        border-radius: 12px;
        text-align: center;
        font-weight: bold;
        font-size: 18px;
        box-shadow: 2px 4px 15px rgba(0,0,0,0.2);
        transition: 0.3s;">
        📸 أرسل فكرتك لحمد عبر انستقرام
    </div>
</a>
''', unsafe_allow_html=True)

# --- 6. تذييل الصفحة ---
st.markdown("---")
st.markdown(f"<center>تمت البرمجة بواسطة الخبير <b>حمد</b> | الإصدار 2.0 - 2026</center>", unsafe_allow_html=True)

    




    



                



        


      
