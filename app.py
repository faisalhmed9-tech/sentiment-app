import streamlit as st
import urllib.parse
import random

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام حمد الذكي", page_icon="🛡️", layout="centered")

# --- 2. روابط اليوتيوب وقائمة الحماية ---
bad_words = ["كلمة1", "كلمة2", "badword1"] 
neg_videos = ["https://www.youtube.com/watch?v=2p8nreL_lTo", "https://www.youtube.com/watch?v=pY9InT15v70"]
neu_videos = ["https://www.youtube.com/watch?v=68pY7z-S2_Q", "https://www.youtube.com/watch?v=07d2dXHYb94"]

# --- 3. واجهة النظام الاحترافية ---
st.title("🛡️ نظام حمد العالمي لتحليل المشاعر")
st.write("النسخة الشاملة: عربي عامي + English 🌍")
st.markdown("---")

name = st.text_input("سجل الاسم / Name:")
gender = st.radio("الجنس / Gender:", ["ذكر / Male", "أنثى / Female"], horizontal=True)
prefix = "الأستاذ" if "ذكر" in gender else "الأستاذة"

user_text = st.text_area(f"يا {prefix} {name}، عبر عن شعورك / Express your feelings:", height=150)

if st.button("بدء التحليل / Analyze 🔍"):
    if name and user_text:
        t = user_text.lower()
        
        # أولاً: نظام الحماية من الكلام السيء
        if any(word in t for word in bad_words):
            st.error("⚠️ تنبيه أمني: محتوى غير ملائم / Inappropriate content detected.")
        else:
            # ثانياً: قاموس حمد الذكي (عامي + فصحى + إنجليزي)
            
            # كلمات السعادة والرضا
            pos_keywords = [
                "سعيد", "فرحان", "مبسوط", "مستانس", "رايق", "كفو", "بطل", "خيال", "رهيب", "حلو", "جميل", "فخور", "ممتاز", "طيب",
                "happy", "good", "great", "excellent", "amazing", "awesome", "nice", "proud", "love", "wonderful"
            ]
            
            # كلمات الضيق والحزن
            neg_keywords = [
                "متضايق", "طفشان", "حزين", "زعلان", "تعبان", "قهر", "ضيق", "هم", "مخنوق", "سيء", "زفت", "كره", "بكي",
                "sad", "bad", "angry", "upset", "tired", "hate", "depressed", "worst", "annoyed", "bored"
            ]

            # فحص النتيجة
            is_positive = any(word in t for word in pos_keywords)
            is_negative = any(word in t for word in neg_keywords)

            st.markdown(f"### 📋 تقرير الحالة لـ {prefix} {name}:")

            if is_positive:
                st.balloons()
                st.success("النتيجة: مشاعر إيجابية / Positive Feelings ✨")
                msg = f"أنا {prefix} {name}، حللت مشاعري عند 'نظام حمد الذكي' وطلعت نتيجتي إيجابية! 🔥"
                whatsapp_url = f"https://wa.me/?text={urllib.parse.quote(msg)}"
                st.markdown(f'''<a href="{whatsapp_url}" target="_blank">
                    <button style="width:100%; background-color:#25D366; color:white; border:none; padding:15px; border-radius:15px; font-weight:bold; cursor:pointer;">
                    📢 مشاركة التقرير عبر WhatsApp
                    </button></a>''', unsafe_allow_html=True)

            elif is_negative:
                st.error("النتيجة: مشاعر سلبية أو ضيق / Negative Feelings.")
                st.info("نصيحة من حمد: لا تحزن، شاهد هذا المقطع المختار لك:")
                st.video(random.choice(neg_videos))

            else:
                st.warning("النتيجة: حالة ذهنية متزنة / Neutral State ⚖️")
                st.markdown("""
                    <div style="border:2px solid #ffd700; padding:20px; border-radius:15px; text-align:center; background-color:rgba(255,215,0,0.1);">
                        <h4 style="color:#ffd700; margin:0;">💎 المربع الذهبي</h4>
                        <p style="color:white; margin-top:10px;">أنت الآن في قمة الصفاء والهدوء الذهني.</p>
                    </div>
                """, unsafe_allow_html=True)
                st.video(random.choice(neu_videos))
    else:
        st.error("الرجاء إدخال الاسم والنص / Please enter name and text.")

st.markdown("---")
st.markdown(f"<center>تم التطوير بواسطة الخبير <b>حمد</b> | Developed by <b>Hamad</b> 2026</center>", unsafe_allow_html=True)




    



                



        


      
