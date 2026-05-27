import streamlit as st
import urllib.parse
import random

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام حمد العالمي", page_icon="🛡️", layout="centered")

# --- 2. البيانات المساعدة ---
bad_words = ["كلمة1", "كلمة2", "سب"] 
neg_videos = ["https://www.youtube.com/watch?v=2p8nreL_lTo", "https://www.youtube.com/watch?v=pY9InT15v70"]
neu_videos = ["https://www.youtube.com/watch?v=68pY7z-S2_Q", "https://www.youtube.com/watch?v=07d2dXHYb94"]

# --- 3. واجهة التطبيق الرئيسية ---
st.title("🛡️ نظام حمد العالمي الذكي")
st.markdown("---")

# نظام التبويبات للتنظيم
tab1, tab2 = st.tabs(["🔍 تحليل المشاعر", "🧹 مركز التنظيف"])

with tab1:
    # إدخال البيانات مع تصحيح اختيار الجنس
    name = st.text_input("سجل الاسم / Name:")
    gender_choice = st.radio("الجنس / Gender:", ["ذكر", "أنثى"], horizontal=True)
    
    # تحديد اللقب بدقة
    prefix = "الأستاذ" if gender_choice == "ذكر" else "الأستاذة"

    user_text = st.text_area(f"يا {prefix} {name}، اكتب شعورك هنا:", height=120)

    if st.button("تحليل الآن 🔍"):
        if name and user_text:
            t = user_text.lower()
            
            # 1. فحص الحماية
            if any(word in t for word in bad_words):
                st.error("⚠️ تنبيه أمني: تم اكتشاف لغة غير ملائمة.")
            else:
                # 2. القاموس الشامل (عامي + إنجليزي)
                pos = ["سعيد", "مستانس", "رايق", "كفو", "بطل", "خيال", "رهيب", "حلو", "happy", "great", "cool"]
                neg = ["متضايق", "طفشان", "حزين", "زعلان", "تعبان", "قهر", "ضيق", "sad", "bad", "upset"]

                # 3. عرض النتائج
                if any(w in t for w in pos):
                    st.balloons()
                    st.success(f"النتيجة: مشاعر إيجابية! كفو يا {prefix} {name} ✨")
                    msg = f"أنا {prefix} {name}، جربت نظام حمد وطلعت نتيجتي إيجابية! 🔥"
                    whatsapp_url = f"https://wa.me/?text={urllib.parse.quote(msg)}"
                    st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="width:100%; background-color:#25D366; color:white; border:none; padding:15px; border-radius:15px; font-weight:bold; cursor:pointer;">📢 شارك النتيجة واتساب</button></a>', unsafe_allow_html=True)
                
                elif any(w in t for w in neg):
                    st.error(f"النتيجة: ضيق بسيط.. عسى ما شر يا {prefix} {name}؟")
                    st.info("نصيحة حمد ليرتاح بالك:")
                    st.video(random.choice(neg_videos))
                
                else:
                    st.warning("النتيجة: حالة المربع الذهبي (اتزان هادئ)")
                    st.markdown('<div style="border:2px solid #ffd700; padding:15px; border-radius:10px; text-align:center; background-color:rgba(255,215,0,0.1);">🌟 قمة الصفاء الذهني 🌟</div>', unsafe_allow_html=True)
                    st.video(random.choice(neu_videos))
        else:
            st.error("الرجاء كتابة الاسم والنص.")

with tab2:
    st.header("🧹 مركز حمد لتنظيف التواصل الاجتماعي")
    st.write("هذا القسم مصمم لمساعدتك على تنظيف حساباتك وحماية خصوصيتك.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("سناب شات")
    with col2:
        st.button("تيك توك")
    with col3:
        st.button("تلجرام")
    
    st.info("💡 سيتم إضافة روابط التنظيف المباشرة في التحديث القادم.")

st.markdown("---")
st.markdown(f"<center>برمجة وتطوير الخبير <b>حمد</b> | 2026</center>", unsafe_allow_html=True)
    




    



                



        


      
