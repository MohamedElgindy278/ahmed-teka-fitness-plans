import streamlit as st
from datetime import datetime
from workout_generator import generate_pdf

st.set_page_config(page_title='AHMED TEKA', page_icon='💪', layout='wide')

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
*{font-family:'Cairo',sans-serif!important}
.main-header{background:linear-gradient(135deg,#080B12,#1A2235);padding:1.5rem;border-radius:15px;text-align:center;border:2px solid #D4AF37;margin-bottom:2rem}
.main-header h1{color:#D4AF37;font-size:2rem;font-weight:900;margin:0}
.main-header p{color:#9BA3B2;font-size:0.9rem;margin:0}
.stButton>button{background:linear-gradient(135deg,#D4AF37,#A0832A);color:#080B12;font-weight:700;font-size:1.3rem;padding:1rem;border-radius:10px;border:none;width:100%}
.stButton>button:hover{background:linear-gradient(135deg,#E8C84A,#D4AF37);transform:translateY(-2px)}
label{color:#D4AF37!important;font-weight:600!important}
input,textarea{background-color:#1A2235!important;color:#E8E4DC!important;border:2px solid #374151!important}
.success-box{background:linear-gradient(135deg,#1C1A08,#2A2208);border:2px solid #D4AF37;border-radius:10px;padding:1.5rem;text-align:center;color:#D4AF37;font-size:1.2rem;font-weight:700}
.day-box{background:#111827;border:2px solid #D4AF37;border-radius:10px;padding:1rem;margin-bottom:1rem}
.day-box h3{color:#D4AF37;margin:0}
@media(max-width:768px){.main-header h1{font-size:1.3rem}}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>AHMED TEKA</h1><p>PREMIUM WORKOUT PLAN · PUSH // PULL // LEGS</p></div>', unsafe_allow_html=True)

with st.form('form'):
    # CLIENT INFO
    col1, col2 = st.columns(2)
    with col1:
        client_name = st.text_input('Client Name', 'MOHAMED')
        goal = st.text_input('Goal', 'HYPERTROPHY & STRENGTH')
        weight = st.text_input('Weight (kg)', '75')
    with col2:
        program = st.text_input('Program', 'PUSH // PULL // LEGS')
        volume = st.text_input('Volume', 'VOL.1')
        tagline = st.text_input('Tagline', 'ENGINEERED FOR DOMINANCE')
    
    col3, col4, col5 = st.columns(3)
    with col3:
        duration = st.text_input('Duration', '8 WEEKS')
    with col4:
        frequency = st.text_input('Frequency', '6 DAYS / WEEK')
    with col5:
        start_date = st.text_input('Start Date', datetime.now().strftime('%B %Y').upper())
    
    st.markdown('---')
    
    # COACH INFO
    col6, col7, col8 = st.columns(3)
    with col6:
        coach_name = st.text_input('Coach Name', 'AHMED TEKA')
    with col7:
        instagram = st.text_input('Instagram', '@coach.teka1')
    with col8:
        phone = st.text_input('Phone', '01033047057')
    
    instagram_link = st.text_input('Instagram Link', 'https://instagram.com/coach.teka1')
    
    # PHILOSOPHY
    philosophy = st.text_area('Philosophy', """This program is not about going through the motions. It is about training with intention, precision, and relentless focus. Every set, every rep, every second of rest is calculated to push your body beyond its limits and force adaptation.

The Push Pull Legs split allows optimal muscle recovery while maintaining high training frequency. You will train each muscle group twice per week across 6 sessions, with one full rest day for complete systemic recovery.

Adhere strictly to prescribed rest intervals. Progressive overload - adding weight or reps each week - is your primary growth driver. Track every session. Outperform yesterday.""", height=150)
    
    st.markdown('---')
    
    # PUSH DAY
    st.markdown('<div class="day-box"><h3>PUSH DAY - CHEST · SHOULDERS · TRICEPS</h3></div>', unsafe_allow_html=True)
    push_text = st.text_area('Push Exercises (one per line: NAME - SETSxREPS - REST - DESC)', 
        """CHEST PRESS MACHINE - 3x10-12 - 90s - Back flat against pad. Full ROM.
DB INCLINE CHEST PRESS - 3x10-12 - 90s - 30-45 incline. Control eccentric.
BUTTERFLY MACHINE - 3x10-12 - 90s - Peak squeeze at full contraction.
DB SHOULDER PRESS - 3x10-12 - 90s - No lock elbows. Core braced.
SEATED LATERAL RAISE - 3x12-15 - 60s - Lead with elbows. No momentum.
CABLE OVERHEAD TRICEP - 3x12-15 - 60s - Full extension at bottom.
ROPE PUSHDOWN - 3x12-15 - 60s - Elbows pinned to sides.
CABLE CRUNCH - 3x15-20 - 45s - Contraction is everything.""", height=200, key='push')
    
    # PULL DAY
    st.markdown('<div class="day-box"><h3>PULL DAY - BACK · BICEPS · REAR DELTS</h3></div>', unsafe_allow_html=True)
    pull_text = st.text_area('Pull Exercises', 
        """LAT PULLDOWN - 3x10-12 - 90s - Wide grip. Full lat stretch.
SEATED ROW V-BAR - 3x10-12 - 90s - Squeeze shoulder blades.
BACK EXTENSION - 3x12-15 - 60s - Neutral spine.
REAR DELT FLY MACHINE - 3x12-15 - 60s - Control the negative.
DUMBBELL CURL - 3x10-12 - 60s - Supinate at peak.
ROPE HAMMER CURL - 3x10-12 - 60s - Neutral grip.
INCLINE DB SHRUG - 3x12-15 - 60s - 1-second hold at top.""", height=180, key='pull')
    
    # LEGS DAY
    st.markdown('<div class="day-box"><h3>LEGS DAY - QUADS · HAMSTRINGS · GLUTES · CALVES</h3></div>', unsafe_allow_html=True)
    legs_text = st.text_area('Legs Exercises', 
        """BARBELL BACK SQUAT - 4x8-10 - 120s - Below parallel. Knees track toes.
LEG PRESS MACHINE - 3x10-12 - 90s - No knee lockout.
HACK SQUAT - 3x10-12 - 90s - Close stance. Full depth.
LEG EXTENSION - 3x12-15 - 60s - Peak squeeze. 2-second hold.
HAMSTRING CURL - 3x12-15 - 60s - Plantarflex foot at top.
BARBELL LUNGES - 3x10/leg - 90s - Drive through front heel.
SEATED CALF RAISE - 3x15-20 - 45s - Full stretch at bottom.
STANDING CALF RAISE - 2x20-25 - 45s - Single-leg variation.""", height=200, key='legs')
    
    st.markdown('---')
    
    # TIPS & QUOTE
    tips_text = st.text_area('Tips (title | body per line)', 
        """PERFECT FORM | Every rep with compromised technique reinforces a harmful pattern. Reduce load, master the movement, then progress.
PROGRESSIVE OVERLOAD | Add 2.5 kg or 2 reps each week minimum. Log every session.
SLEEP AS TRAINING | Growth hormone peaks during deep sleep. 7-9 hours nightly is not optional.
FUEL YOUR SESSIONS | Target 1.8-2.2g protein per kg bodyweight daily.
HYDRATION DAILY | Minimum 4 liters of water on training days.
MENTAL EDGE | Controlled breathing and visualization before each set increases power output.""", height=150)
    
    col9, col10 = st.columns([3,1])
    with col9:
        quote = st.text_area('Quote', 'THE BODY ACHIEVES WHAT THE MIND BELIEVES. DISCIPLINE IS THE BRIDGE BETWEEN GOALS AND GREATNESS.', height=80)
    with col10:
        quote_author = st.text_input('Author', '- Ahmed Teka')
    
    submitted = st.form_submit_button('GENERATE PREMIUM PDF', use_container_width=True)

if submitted:
    if not client_name:
        st.error('Please enter client name')
    else:
        with st.spinner('Creating premium 8-page PDF...'):
            try:
                def parse_exercises(text, day):
                    exercises = []
                    for line in text.strip().split('\n'):
                        if line.strip():
                            parts = line.split(' - ')
                            name = parts[0].strip()
                            sets_reps = parts[1].strip() if len(parts) > 1 else '3x10-12'
                            rest = parts[2].strip() if len(parts) > 2 else '90s'
                            desc = parts[3].strip() if len(parts) > 3 else 'Full ROM. Control the movement.'
                            
                            s, r = ('3', '10-12')
                            if 'x' in sets_reps:
                                sp = sets_reps.split('x')
                                s, r = sp[0].strip(), sp[1].strip()
                            
                            exercises.append({
                                'name': name, 'sets': s, 'reps': r, 'rest': rest,
                                'desc': desc, 'link': '#', 'day': day
                            })
                    return exercises
                
                exercises = []
                exercises.extend(parse_exercises(push_text, 'push_day'))
                exercises.extend(parse_exercises(pull_text, 'pull_day'))
                exercises.extend(parse_exercises(legs_text, 'legs_day'))
                
                tips = []
                for line in tips_text.strip().split('\n'):
                    if '|' in line:
                        t, b = line.split('|', 1)
                        tips.append({'title': t.strip(), 'icon': f'{len(tips)+1:02d}', 'body': b.strip()})
                
                data = {
                    'client_name': client_name, 'program': program, 'volume': volume,
                    'tagline': tagline, 'duration': duration, 'frequency': frequency,
                    'start_date': start_date, 'goal': goal, 'coach_name': coach_name,
                    'instagram': instagram, 'instagram_link': instagram_link, 'phone': phone,
                    'philosophy': philosophy, 'exercises': exercises, 'tips': tips,
                    'quote': quote, 'quote_author': quote_author,
                    'timeline': [
                        {'week': 'WEEK 1-2', 'phase': 'FOUNDATION', 'desc': 'Master form. Build mind-muscle connection. Establish baseline loads for all movements.'},
                        {'week': 'WEEK 3-4', 'phase': 'PROGRESSION', 'desc': 'Increase load by 5-10%. Volume ramps methodically. Training intensity begins to rise.'},
                        {'week': 'WEEK 5-6', 'phase': 'INTENSIFICATION', 'desc': 'Push beyond comfort zones. Drop sets introduced on the final exercise of each session.'},
                        {'week': 'WEEK 7-8', 'phase': 'PEAK OUTPUT', 'desc': 'Maximum effort on all lifts. Test your true capacity. Deload the final 3 days of week 8.'},
                    ],
                    'warmup': {
                        'cardio': '5-10 MIN LIGHT CARDIO: Treadmill or bike at 60-65% max heart rate. Goal: elevate core temperature, increase joint lubrication, prime the cardiovascular system for heavy training.',
                        'upper_note': 'Shoulder circles, band pull-aparts, arm swings, chest openers, thoracic rotations. Perform 2 full rounds before every Push and Pull session.',
                        'lower_note': 'Hip circles, leg swings, bodyweight squats, ankle rotations, glute bridges. Perform 2 full rounds before every Legs session.',
                        'upper_link': 'https://youtube.com/watch?v=upper_warmup',
                        'lower_link': 'https://youtube.com/watch?v=lower_warmup',
                        'protocol': [
                            'Never skip warm-up - injury prevention is non-negotiable',
                            'Full range of motion on every drill',
                            'Use warm-up sets: 50% > 75% > working weight',
                            'Note restricted areas and spend extra time there',
                        ],
                    },
                }
                
                pdf_bytes = generate_pdf(data)
                st.markdown('<div class="success-box">PREMIUM PDF GENERATED SUCCESSFULLY!</div>', unsafe_allow_html=True)
                st.download_button('DOWNLOAD PDF', data=pdf_bytes, file_name=f'AhmedTeka_{client_name}.pdf', mime='application/pdf', use_container_width=True)
                
            except Exception as e:
                st.error(f'Error: {str(e)}')
                import traceback
                st.code(traceback.format_exc())

st.markdown('---')
st.markdown('<p style="text-align:center;color:#6B7280">AHMED TEKA · @coach.teka1 · 01033047057</p>', unsafe_allow_html=True)