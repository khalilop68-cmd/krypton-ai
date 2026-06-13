import streamlit as st
import google.generativeai as genai

try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("يرجى التأكد من إضافة GOOGLE_API_KEY في الـ Secrets")

st.title("Krypton AI Engine")

user_query = st.text_input("اسأل عن أعقد القوانين، المعادلات، أو التحليلات الفلسفية هنا:")

if st.button("تشغيل الذكاء الخارق وربح المال 🎯"):
    if user_query:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(user_query)
        st.success("تم التحليل والاستنتاج بنجاح حسب المنهجيات التعليمية المطلوب:")
        st.write(response.text)
    else:
        st.warning("يرجى كتابة سؤال أولاً!")
