import
            st.balloons()
            st.success(f"🎊 النتيجة: **طاقة إيجابية متفجرة!** أنت اليوم في قمة العطاء يا {prefix} {display_name}.")
            msg = f"تحليل مشاعري في نظام حمد الذكي: إيجابي 100% 🔥🚀"
            
            # أزرار مشاركة فخمة
            st.markdown(f"### 📢 بشر أخوياك بالنتيجة:")
            st.markdown(f'''
                <a href="https://wa.me/?text={urllib.parse.quote(msg)}" target="_blank" style="text-decoration:none">
                    <button style="background-color:#25D366; color:white; border-radius:10px; padding:10px; border:none; cursor:pointer;">🟢 واتساب</button>
                </a>
                <a href="https://t.me/share/url?url={urllib.parse.quote(msg)}" target="_blank" style="text-decoration:none">
                    <button style="background-color:#24A1DE; color:white; border-radius:10px; padding:10px; border:none; cursor:pointer;">🔵 تليجرام</button>
                </a>
            ''', unsafe_allow_html=True)
            st.code(msg)

        elif any(w in t for w in neg_keywords):
            st.warning(f"يا {prefix} {display_name}، الحياة تجارب.. خذ لك بريك وشف هالشي:")
            st.video("https://www.youtube.com/watch?v=2p8nreL_lTo")
        else:
            st.info("حالة اتزان (المربع الذهبي) ⚖️ أنت في وضعية الحكيم الآن.")
            st.video("https://www.youtube.com/watch?v=68pY7z-S2_Q")
    else:
        st.error("يا بطل، سجل اسمك واكتب شعورك أولاً!")

# --- 5. صندوق الاقتراحات (انستقرام حمد) ---
st.markdown("<br><br>", unsafe_allow_html=True)
my_insta = "https://www.instagram.com/hamd_9367_?igsh=MTV6eHF5ZXdndGZ1dw=="
st.markdown(f'''
    <div style="background-color: white; padding: 20px; border-radius: 15px; border-left: 5px solid #E1306C; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
        <h4>💡 هل لديك فكرة لتطوير النظام؟</h4>
        <p>مطور النظام "حمد" يرحب بكل اقتراحاتكم الإبداعية.</p>
        <a href="{my_insta}" target="_blank" style="text-decoration: none;">
            <button style="background: linear-gradient(45deg, #f09433, #bc1888); color: white; border: none; padding: 10px 20px; border-radius: 10px; cursor: pointer;">
                📸 أرسل اقتراحك الآن
            </button>
        </a>
    </div>
''', unsafe_allow_html=True)

st.markdown(f"<br><center>حقوق البرمجة محفوظة للمطور <b>حمد</b> © 2026</center>", unsafe_allow_html=True)

