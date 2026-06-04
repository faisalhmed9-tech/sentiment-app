import streamlit as st
import urllib.parse

# 1. التنسيق الفخم الثابت (كحلي ونيون)
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: white; }
    .stTextInput>div>div>input {
        background-color: #1e293b !important; color: white !important;
        border: 2px solid #38bdf8 !important; border-radius: 12px !important;
    }
    .stButton>button {
        width: 100%; background-color: #38bdf8; color: #0f172a;
        font-weight: bold; border-radius: 12px; border: none; height: 3em;
    }
    /* صناديق النتائج */
    .pos-box { padding: 20px; border-radius: 15px; border: 2px solid #22c55e; background: rgba(34,197,94,0.1); color: #4ade80; text-align: center; }
    .neg-box { padding: 20px; border-radius: 15px; border: 2px solid #ef4444; background: rgba(239,68,68,0.1); color: #f87171; text-align: center; }
    .neu-box { padding: 20px; border-radius: 15px; border: 2px solid #94a3b8; background: rgba(148,163,184,0.1); color: #cbd5e1; text-align: center; }
    .special-box { padding: 20px; border-radius: 15px; border: 2px solid #f472b6; background: rgba(244,114,182,0.1); color: #f472b6; text-align: center; }
    /* أزرار المشاركة والتواصل */
    .whatsapp-btn { background-color: #25d366; color: white; padding: 10px; border-radius: 8px; text-decoration: none; display: inline-block; margin-top: 10px; font-weight: bold; }
    .insta-footer { text-align: center; margin-top: 50px; padding: 20px; border-top: 1px solid #38bdf8; }
    </style>
    """, unsafe_allow_html=True)

st.title("النظام الذكي المتكامل 🧠")
text = st.text_input("أدخل النص (اسم، جملة، أو كلمة شاطحة):")

if st.button("بدء التحليل"):
    if text:
        # --- 1. الكلمات الشاطحة (3 إجابات لكل وحدة) ---
        if "حب" in text:
            st.markdown('<div class="special-box"><h3>💖 الكلمة: حب</h3><p>1. المشاعر مرتفعة</p><p>2. قلبك أخضر</p><p>3. أيامك مودة</p></div>', unsafe_allow_html=True)
        elif "جوع" in text:
            st.markdown('<div class="neu-box"><h3>🍔 الكلمة: جوع</h3><p>1. وقت العشاء</p><p>2. اترك الجوال وكل</p><p>3. البطن خالية</p></div>', unsafe_allow_html=True)
        elif "هياط" in text:
            st.markdown('<div class="neg-box"><h3>⚔️ الكلمة: هياط</h3><p>1. اذكر الله</p><p>2. هد اللعب</p><p>3. خلك ريلاكس</p></div>', unsafe_allow_html=True)
        
        # --- 2. تصنيف ذكر وأنثى ---
        elif text in ["محمد", "خالد", "فيصل", "حمد"]: 
            st.markdown('<div class="neu-box"><h3>👤 التصنيف: ذكر</h3></div>', unsafe_allow_html=True)
        elif text in ["سارة", "نورة", "هند"]:
            st.markdown('<div class="special-box"><h3>👤 التصنيف: أنثى</h3></div>', unsafe_allow_html=True)

        # --- 3. تحليل المشاعر (إيجابي، سلبي، محايد) ---
        elif any(word in text for word in ["كفو", "حلو", "زين", "بطل"]):
            res_msg = "إيجابي 😍\n1. كلام يفتح النفس\n2. طاقة إيجابية\n3. استمر بجمالك"
            st.markdown(f'<div class="pos-box"><h3>إيجابي 😍</h3><p>1. كلام يفتح النفس</p><p>2. طاقة إيجابية</p><p>3. استمر بجمالك</p></div>', unsafe_allow_html=True)
            st.balloons()
            # زر مشاركة واتساب
            url = f"https://wa.me/?text={urllib.parse.quote(res_msg)}"
            st.markdown(f'<a href="{url}" target="_blank" class="whatsapp-btn">📲 شارك النتيجة على واتساب</a>', unsafe_allow_html=True)
            
        elif any(word in text for word in ["سيء", "حزين", "ضيق"]):
            st.markdown('<div class="neg-box"><h3>سلبي 😔</h3><p>1. الله يبعد الضيقة</p><p>2. فتره وتعدي</p><p>3. بكرة أجمل</p></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="neu-box"><h3>محايد 😐</h3><p>1. كلام موزون</p><p>2. وضعك مستقر</p><p>3. لا يوجد انفعال</p></div>', unsafe_allow_html=True)
    else:
        st.warning("أدخل نص أولاً!")

# --- 4. قسم الانستقرام بالرابط الصحيح ---
st.markdown("""
    <div class="insta-footer">
        <a href="https://www.instagram.com/hamd_9367_?igsh=MTV6eHF5ZXdndGZ1dw==" target="_blank" style="color: #f472b6; text-decoration: none; font-weight: bold; font-size: 18px;">
            📸 تابعني على انستقرام: @hamd_9367_
        </a>
    </div>
    """, unsafe_allow_html=True)
