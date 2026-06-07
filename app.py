import streamlit as st
from datetime import datetime
from workout_generator import generate_pdf

st.set_page_config(page_title='Ahmed Teka - Workout Plan', page_icon='💪', layout='wide')

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
    *{font-family:'Cairo',sans-serif!important}
    .main-header{background:linear-gradient(135deg,#080B12,#1A2235);padding:1.5rem;border-radius:15px;text-align:center;border:2px solid #D4AF37;margin-bottom:1.5rem}
    .main-header h1{color:#D4AF37;font-size:1.8rem;font-weight:900}
    .main-header p{color:#9BA3B2;font-size:0.9rem}
    .stButton>button{background:linear-gradient(135deg,#D4AF37,#A0832A);color:#080B12;font-weight:700;font-size:1.2rem;padding:1rem;border-radius:10px;border:none;width:100%}
    .stButton>button:hover{background:linear-gradient(135deg,#E8C84A,#D4AF37);transform:translateY(-2px)}
    label{color:#D4AF37!important;font-weight:600!important}
    .day-box{background:#111827;border:2px solid #D4AF37;border-radius:10px;padding:1rem;margin-bottom:1rem}
    .day-box h3{color:#D4AF37;margin:0 0 0.5rem 0}
    .success-box{background:linear-gradient(135deg,#1C1A08,#2A2208);border:2px solid #D4AF37;border-radius:10px;padding:1.5rem;text-align:center;color:#D4AF37;font-size:1.2rem;font-weight:700}
    @media(max-width:768px){.main-header h1{font-size:1.3rem}}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>AHMED TEKA - Premium Workout Plan</h1><p>PUSH // PULL // LEGS - Professional Quality</p></div>', unsafe_allow_html=True)

ALL_EXERCISES = {
    'PUSH': [
        'CHEST PRESS MACHINE', 'DB INCLINE CHEST PRESS', 'BUTTERFLY MACHINE',
        'DB SHOULDER PRESS', 'SEATED LATERAL RAISE', 'CABLE OVERHEAD TRICEP',
        'ROPE PUSHDOWN', 'CABLE CRUNCH', 'BENCH PRESS', 'INCLINE BENCH PRESS',
        'PEC DECK', 'MILITARY PRESS', 'FRONT RAISE', 'TRICEP DIPS',
        'SKULL CRUSHERS', 'CLOSE GRIP BENCH', 'DECLINE PRESS'
    ],
    'PULL': [
        'LAT PULLDOWN', 'SEATED ROW - V-BAR', 'BACK EXTENSION',
        'REAR DELT FLY MACHINE', 'DUMBBELL CURL', 'ROPE HAMMER CURL',
        'INCLINE DB SHRUG', 'DEADLIFT', 'BARBELL ROW', 'T-BAR ROW',
        'SINGLE ARM ROW', 'FACE PULL', 'PREACHER CURL', 'CONCENTRATION CURL',
        'REVERSE FLY', 'SHRUGS', 'CHIN UPS'
    ],
    'LEGS': [
        'BARBELL BACK SQUAT', 'LEG PRESS MACHINE', 'HACK SQUAT',
        'LEG EXTENSION', 'HAMSTRING CURL', 'BARBELL LUNGES',
        'SEATED CALF RAISE', 'STANDING CALF RAISE', 'FRONT SQUAT',
        'ROMANIAN DEADLIFT', 'BULGARIAN SPLIT SQUAT', 'GLUTE BRIDGE',
        'LEG CURL', 'CALF PRESS', 'GOBLET SQUAT', 'STEP UPS'
    ]
}

with st.form('workout_form'):
    st.markdown('### CLIENT DATA')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        client_name = st.text_input('Client Name', value='MOHAMED')
        weight = st.text_input('Weight (kg)', value='75')
        goal = st.text_input('Goal', value='HYPERTROPHY & STRENGTH')
    with col2:
        program = st.text_input('Program', value='PUSH // PULL // LEGS')
        volume = st.text_input('Volume', value='VOL.1')
        tagline = st.text_input('Tagline', value='ENGINEERED FOR DOMINANCE')
    with col3:
        duration = st.text_input('Duration', value='8 WEEKS')
        frequency = st.text_input('Frequency', value='6 DAYS / WEEK')
        start_date = st.text_input('Start Date', value=datetime.now().strftime('%B %Y').upper())
    
    st.markdown('---')
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        coach_name = st.text_input('Coach Name', value='AHMED TEKA')
        instagram = st.text_input('Instagram', value='@coach.teka1')
    with col_c2:
        phone = st.text_input('Phone', value='01033047057')
        instagram_link = st.text_input('Instagram Link', value='https://instagram.com/coach.teka1')
    
    st.markdown('---')
    philosophy = st.text_area('PHILOSOPHY',
        value='This program is not about going through the motions. It is about training with intention, precision, and relentless focus. Every set, every rep, every second of rest is calculated to push your body beyond its limits and force adaptation.\n\nThe Push Pull Legs split allows optimal muscle recovery while maintaining high training frequency. You will train each muscle group twice per week across 6 sessions, with one full rest day for complete systemic recovery.\n\nAdhere strictly to prescribed rest intervals. Progressive overload - adding weight or reps each week - is your primary growth driver. Track every session. Outperform yesterday.',
        height=150)
    
    st.markdown('---')
    st.markdown('### EXERCISES SELECTION')
    
    st.markdown('<div class="day-box"><h3>PUSH DAY - CHEST - SHOULDERS - TRICEPS</h3></div>', unsafe_allow_html=True)
    selected_push = st.multiselect('Select PUSH exercises (max 8)', ALL_EXERCISES['PUSH'],
        default=['CHEST PRESS MACHINE', 'DB INCLINE CHEST PRESS', 'BUTTERFLY MACHINE', 'DB SHOULDER PRESS', 'SEATED LATERAL RAISE', 'CABLE OVERHEAD TRICEP', 'ROPE PUSHDOWN', 'CABLE CRUNCH'],
        max_selections=8, key='push')
    
    st.markdown('<div class="day-box"><h3>PULL DAY - BACK - BICEPS - REAR DELTS</h3></div>', unsafe_allow_html=True)
    selected_pull = st.multiselect('Select PULL exercises (max 8)', ALL_EXERCISES['PULL'],
        default=['LAT PULLDOWN', 'SEATED ROW - V-BAR', 'BACK EXTENSION', 'REAR DELT FLY MACHINE', 'DUMBBELL CURL', 'ROPE HAMMER CURL', 'INCLINE DB SHRUG'],
        max_selections=8, key='pull')
    
    st.markdown('<div class="day-box"><h3>LEGS DAY - QUADS - HAMSTRINGS - GLUTES - CALVES</h3></div>', unsafe_allow_html=True)
    selected_legs = st.multiselect('Select LEGS exercises (max 8)', ALL_EXERCISES['LEGS'],
        default=['BARBELL BACK SQUAT', 'LEG PRESS MACHINE', 'HACK SQUAT', 'LEG EXTENSION', 'HAMSTRING CURL', 'BARBELL LUNGES', 'SEATED CALF RAISE', 'STANDING CALF RAISE'],
        max_selections=8, key='legs')
    
    st.markdown('---')
    
    st.markdown('### TIPS (one per line: title | body)')
    tips_text = st.text_area('Tips', value='PERFECT FORM | Every rep with compromised technique reinforces a harmful pattern.\nPROGRESSIVE OVERLOAD | Add 2.5 kg or 2 reps each week minimum.\nSLEEP AS TRAINING | 7-9 hours nightly is where muscle protein synthesis occurs.\nFUEL YOUR SESSIONS | 1.8-2.2g protein per kg bodyweight daily.\nHYDRATION DAILY | Minimum 4 liters of water on training days.\nMENTAL EDGE | Controlled breathing and visualization increases power output.',
        height=150)
    
    col_q1, col_q2 = st.columns([3,1])
    with col_q1:
        quote = st.text_area('Quote', value='THE BODY ACHIEVES WHAT THE MIND BELIEVES. DISCIPLINE IS THE BRIDGE BETWEEN GOALS AND GREATNESS.')
    with col_q2:
        quote_author = st.text_input('Quote Author', value='- Ahmed Teka')
    
    submitted = st.form_submit_button('GENERATE PREMIUM PDF', use_container_width=True)

if submitted:
    if not client_name:
        st.error('Please enter client name')
    else:
        with st.spinner('Creating premium 8-page workout plan...'):
            try:
                exercises = []
                
                for ex_name in selected_push:
                    exercises.append({'name': ex_name, 'sets': '3', 'reps': '10-12', 'rest': '90s', 'desc': 'Full ROM. Control the movement.', 'link': '#', 'day': 'push_day'})
                for ex_name in selected_pull:
                    exercises.append({'name': ex_name, 'sets': '3', 'reps': '10-12', 'rest': '90s', 'desc': 'Full ROM. Control the movement.', 'link': '#', 'day': 'pull_day'})
                for ex_name in selected_legs:
                    exercises.append({'name': ex_name, 'sets': '4', 'reps': '8-10', 'rest': '120s', 'desc': 'Full ROM. Control the movement.', 'link': '#', 'day': 'legs_day'})
                
                tips = []
                for line in tips_text.strip().split('\n'):
                    if '|' in line:
                        title, body = line.split('|', 1)
                        tips.append({'title': title.strip(), 'icon': f'{len(tips)+1:02d}', 'body': body.strip()})
                
                data = {
                    'client_name': client_name, 'program': program, 'volume': volume,
                    'tagline': tagline, 'duration': duration, 'frequency': frequency,
                    'start_date': start_date, 'goal': goal, 'coach_name': coach_name,
                    'instagram': instagram, 'instagram_link': instagram_link, 'phone': phone,
                    'philosophy': philosophy, 'exercises': exercises, 'tips': tips,
                    'quote': quote, 'quote_author': quote_author,
                    'timeline': [
                        {'week': 'WEEK 1-2', 'phase': 'FOUNDATION', 'desc': 'Master form. Build mind-muscle connection.'},
                        {'week': 'WEEK 3-4', 'phase': 'PROGRESSION', 'desc': 'Increase load by 5-10%. Volume increases.'},
                        {'week': 'WEEK 5-6', 'phase': 'INTENSIFICATION', 'desc': 'Push beyond comfort zones.'},
                        {'week': 'WEEK 7-8', 'phase': 'PEAK OUTPUT', 'desc': 'Maximum effort on all lifts.'},
                    ],
                    'warmup': {
                        'cardio': '5-10 MIN LIGHT CARDIO: Treadmill or bike at 60-65% max heart rate.',
                        'upper_note': 'Shoulder circles, band pull-aparts, arm swings, chest openers.',
                        'lower_note': 'Hip circles, leg swings, bodyweight squats, ankle rotations.',
                        'upper_link': 'https://youtube.com/watch?v=upper_warmup',
                        'lower_link': 'https://youtube.com/watch?v=lower_warmup',
                        'protocol': [
                            'Never skip warm-up - injury prevention is non-negotiable',
                            'Full range of motion on every drill',
                            'Use warm-up sets: 50% > 75% > working weight',
                        ],
                    },
                }
                
                pdf_bytes = generate_pdf(data)
                st.markdown('<div class="success-box">PREMIUM PDF GENERATED SUCCESSFULLY!</div>', unsafe_allow_html=True)
                st.download_button('DOWNLOAD PDF', data=pdf_bytes, file_name=f'AhmedTeka_{client_name}.pdf', mime='application/pdf', use_container_width=True)
                
            except Exception as e:
                st.error(f'Error: {str(e)}')

st.markdown('---')
st.markdown('<p style="text-align:center;color:#6B7280">AHMED TEKA - @coach.teka1 - 01033047057</p>', unsafe_allow_html=True)