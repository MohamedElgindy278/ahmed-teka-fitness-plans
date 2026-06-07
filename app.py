import streamlit as st
from datetime import datetime
from workout_generator import generate_pdf

st.set_page_config(page_title='Ahmed Teka - Workout Plan',page_icon='💪',layout='wide',initial_sidebar_state='collapsed')

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
    *{font-family:'Cairo',sans-serif!important}
    .main-header{background:linear-gradient(135deg,#080B12,#1A2235);padding:2rem;border-radius:15px;text-align:center;border:2px solid #D4AF37;margin-bottom:2rem}
    .main-header h1{color:#D4AF37;font-size:2.5rem;font-weight:900;margin:0}
    .stButton>button{background:linear-gradient(135deg,#D4AF37,#A0832A);color:#080B12;font-weight:700;font-size:1.3rem;padding:1rem 3rem;border-radius:10px;border:none;width:100%;transition:all 0.3s ease}
    .stButton>button:hover{background:linear-gradient(135deg,#E8C84A,#D4AF37);transform:translateY(-2px);box-shadow:0 10px 20px rgba(212,175,55,0.3)}
    .stTextInput>div>div>input,.stSelectbox>div>div>select,.stTextArea>div>div>textarea{background-color:#1A2235;color:#E8E4DC;border:2px solid #374151;border-radius:10px;font-size:1.1rem;padding:0.75rem}
    label{color:#D4AF37!important;font-weight:600!important;font-size:1.1rem!important}
    .success-message{background:linear-gradient(135deg,#1C1A08,#2A2208);border:2px solid #D4AF37;border-radius:10px;padding:1.5rem;text-align:center;color:#D4AF37;font-size:1.2rem;font-weight:700}
    @media(max-width:768px){.main-header h1{font-size:1.8rem}.stButton>button{font-size:1.1rem;padding:0.75rem 2rem}}
</style>
""",unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>🏋️ Ahmed Teka - Workout Plan Generator</h1><p>Premium Professional Workout Plan</p></div>',unsafe_allow_html=True)

with st.form('workout_form'):
    st.markdown('### 📋 أدخل بياناتك')
    col1,col2=st.columns(2)
    with col1:
        client_name=st.text_input('👤 اسم العميل',placeholder='أدخل اسمك الكامل')
        weight=st.text_input('⚖️ الوزن (كجم)',placeholder='مثال: 75')
        goal=st.selectbox('🎯 الهدف',['تضخيم عضلي','تنشيف','زيادة قوة','لياقة عامة','تحسين صحة'])
    with col2:
        program=st.selectbox('📅 نوع البرنامج',['Push / Pull / Legs','Upper / Lower','Full Body','Bro Split'])
        frequency=st.selectbox('🔄 عدد أيام التمرين',['3 أيام','4 أيام','5 أيام','6 أيام'])
        duration=st.selectbox('⏳ مدة البرنامج',['4 أسابيع','6 أسابيع','8 أسابيع','12 أسبوع'])
    st.markdown('---')
    st.markdown('### 💪 التمارين المفضلة')
    exercises_text=st.text_area('أدخل التمارين (تمرين في كل سطر)',placeholder='Bench Press - 3x10\nSquats - 4x8\nDeadlifts - 3x5',height=150)
    st.markdown('---')
    submitted=st.form_submit_button('🚀 توليد خطة التمرين PDF',use_container_width=True)

if submitted:
    if not client_name:
        st.error('⚠️ الرجاء إدخال اسم العميل')
    else:
        with st.spinner('🔄 جاري إنشاء خطة التمرين...'):
            try:
                exercises_list=[]
                if exercises_text.strip():
                    for line in exercises_text.strip().split('\n'):
                        if line.strip():
                            parts=line.split('-')
                            name=parts[0].strip()
                            sets_reps=parts[1].strip() if len(parts)>1 else '3x10'
                            s,r=(sets_reps.split('x') if 'x' in sets_reps else ('3','10'))
                            exercises_list.append({'name':name,'sets':s.strip(),'reps':r.strip(),'rest':'90s','desc':f'تمرين {name}','link':'#','day':'push_day'})
                if not exercises_list:
                    exercises_list=[
                        {'name':'Bench Press','sets':'3','reps':'10-12','rest':'90s','desc':'صدر','link':'#','day':'push_day'},
                        {'name':'Shoulder Press','sets':'3','reps':'10-12','rest':'90s','desc':'أكتاف','link':'#','day':'push_day'},
                        {'name':'Pull Ups','sets':'3','reps':'8-12','rest':'90s','desc':'ظهر','link':'#','day':'pull_day'},
                        {'name':'Barbell Rows','sets':'3','reps':'10-12','rest':'90s','desc':'ظهر','link':'#','day':'pull_day'},
                        {'name':'Squats','sets':'4','reps':'8-10','rest':'120s','desc':'أرجل','link':'#','day':'legs_day'},
                        {'name':'Leg Press','sets':'3','reps':'10-12','rest':'90s','desc':'أرجل','link':'#','day':'legs_day'},
                    ]
                data={
                    'client_name':client_name,'weight':weight or 'غير محدد','goal':goal,'program':program,
                    'frequency':frequency,'duration':duration,'exercises':exercises_list,
                    'tagline':'ENGINEERED FOR DOMINANCE','volume':'VOL.1',
                    'start_date':datetime.now().strftime('%B %Y').upper(),
                    'coach_name':'AHMED TEKA','instagram':'@coach.teka1',
                    'instagram_link':'https://instagram.com/coach.teka1','phone':'01033047057',
                    'philosophy':f'برنامج تدريبي لـ {client_name}.\nالهدف: {goal}\nالمدة: {duration}',
                }
                pdf_bytes=generate_pdf(data)
                st.markdown('<div class="success-message">✅ تم إنشاء الخطة بنجاح!</div>',unsafe_allow_html=True)
                st.download_button('📥 تحميل PDF',data=pdf_bytes,file_name=f'Workout_{client_name}.pdf',mime='application/pdf',use_container_width=True)
            except Exception as e:
                st.error(f'❌ خطأ: {str(e)}')

st.markdown('---')
st.markdown('<div style="text-align:center;color:#6B7280;padding:1rem"><p>© 2024 Ahmed Teka</p><p>📸 @coach.teka1 | 📞 01033047057</p></div>',unsafe_allow_html=True)
