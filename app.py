import streamlit as st
from datetime import datetime
from workout_generator import generate_pdf

st.set_page_config(page_title='AHMED TEKA - Premium Workout Plan', page_icon='💪', layout='wide')

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
*{font-family:'Cairo',sans-serif!important}
.main-header{background:linear-gradient(135deg,#080B12,#1A2235);padding:1.5rem;border-radius:15px;text-align:center;border:2px solid #D4AF37;margin-bottom:1.5rem}
.main-header h1{color:#D4AF37;font-size:2rem;font-weight:900;margin:0}
.main-header p{color:#9BA3B2;margin:0.3rem 0 0 0}
.stButton>button{background:linear-gradient(135deg,#D4AF37,#A0832A);color:#080B12;font-weight:700;font-size:1.2rem;padding:1rem;border-radius:10px;border:none;width:100%}
.gen-btn>button{background:linear-gradient(135deg,#FF6B35,#D4AF37)!important;color:#000!important;font-size:1.5rem!important;padding:1.5rem!important;font-weight:900!important;animation:pulse 1.5s infinite}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(212,175,55,0.4)}70%{box-shadow:0 0 0 25px rgba(212,175,55,0)}100%{box-shadow:0 0 0 0 rgba(212,175,55,0)}}
label{color:#D4AF37!important;font-weight:600!important}
input,textarea,select{background-color:#1A2235!important;color:#E8E4DC!important;border:2px solid #374151!important;border-radius:8px!important}
.exercise-card{background:#111827;border:1px solid #374151;border-radius:10px;padding:1rem;margin:0.5rem 0}
.exercise-card:hover{border-color:#D4AF37}
.day-header{background:linear-gradient(135deg,#1A2235,#080B12);padding:1rem;border-radius:10px;border-left:5px solid #D4AF37;margin:1rem 0}
.day-header h3{color:#D4AF37;margin:0}
.success-box{background:linear-gradient(135deg,#1C1A08,#2A2208);border:2px solid #D4AF37;border-radius:10px;padding:2rem;text-align:center;color:#D4AF37;font-size:1.5rem;font-weight:900}
.section-desc{color:#6B7280;font-size:0.85rem;margin-bottom:1rem}
.tip-card{background:#111827;border:1px solid #374151;border-radius:10px;padding:1rem;margin:0.5rem 0}
.tip-card:hover{border-color:#D4AF37}
/* White tooltip */
div[data-baseweb="tooltip"]{background-color:#FFFFFF!important;color:#080B12!important;font-weight:600!important;border:2px solid #D4AF37!important}
div[data-baseweb="tooltip"] p{color:#080B12!important;font-weight:500!important}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>🏋️ AHMED TEKA — PREMIUM WORKOUT PLAN</h1><p>Professional · Dark Premium · World-Class Quality</p></div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════
# PROGRAM CONFIGURATIONS
# ═══════════════════════════════════════════════
PROGRAM_CONFIGS = {
    'PUSH // PULL // LEGS': {
        'days': [
            {'key': 'push_day', 'label': 'PUSH', 'subtitle': 'CHEST · SHOULDERS · TRICEPS',
             'desc': 'Prioritize chest activation on horizontal movements, shoulder engagement on overhead work, and full tricep lockout on isolation exercises. Quality of contraction over quantity of weight.',
             'rest_note': 'REST 90-120 SECONDS BETWEEN ALL WORKING SETS'},
            {'key': 'pull_day', 'label': 'PULL', 'subtitle': 'BACK · BICEPS · REAR DELTS',
             'desc': 'Drive elbows — not hands — on all row variations. Maintain scapular retraction throughout. Feel the lats stretch at full extension on every pulldown and row.',
             'rest_note': 'REST 90-120 SECONDS BETWEEN ALL WORKING SETS'},
            {'key': 'legs_day', 'label': 'LEGS', 'subtitle': 'QUADS · HAMSTRINGS · GLUTES · CALVES',
             'desc': 'Heavy compound movements first. Never skip posterior chain work. Drive through the full foot on every squat variation — heel to toe engagement.',
             'rest_note': 'REST 2 FULL MINUTES AFTER SQUATS AND LEG PRESS'},
        ]
    },
    'ARNOLD SPLIT': {
        'days': [
            {'key': 'chest_back_day', 'label': 'CHEST & BACK', 'subtitle': 'CHEST · LATS · RHOMBOIDS',
             'desc': 'Superset chest and back movements for maximum pump and efficiency.',
             'rest_note': 'REST 60-90 SECONDS BETWEEN SUPERSETS'},
            {'key': 'shoulders_arms_day', 'label': 'SHOULDERS & ARMS', 'subtitle': 'DELTS · BICEPS · TRICEPS',
             'desc': 'Focus on deltoid isolation followed by arm supersets.',
             'rest_note': 'REST 45-60 SECONDS BETWEEN SETS'},
            {'key': 'legs_day', 'label': 'LEGS & CORE', 'subtitle': 'QUADS · HAMSTRINGS · CALVES · ABS',
             'desc': 'Heavy leg compounds followed by core work.',
             'rest_note': 'REST 2 MINUTES AFTER HEAVY COMPOUNDS'},
        ]
    },
    'UPPER / LOWER': {
        'days': [
            {'key': 'upper_day', 'label': 'UPPER BODY', 'subtitle': 'CHEST · BACK · SHOULDERS · ARMS',
             'desc': 'Complete upper body workout with compounds and isolation.',
             'rest_note': 'REST 90-120S ON COMPOUNDS | 60S ON ISOLATION'},
            {'key': 'lower_day', 'label': 'LOWER BODY', 'subtitle': 'QUADS · HAMSTRINGS · GLUTES · CALVES',
             'desc': 'Full lower body session with bilateral and unilateral work.',
             'rest_note': 'REST 2 MINUTES ON HEAVY SETS'},
        ]
    },
    'BRO SPLIT': {
        'days': [
            {'key': 'chest_day', 'label': 'CHEST', 'subtitle': 'PECTORALS',
             'desc': 'Full chest development with flat, incline, and isolation work.', 'rest_note': 'REST 90 SECONDS'},
            {'key': 'back_day', 'label': 'BACK', 'subtitle': 'LATS · TRAPS',
             'desc': 'Width and thickness focused back training.', 'rest_note': 'REST 90 SECONDS'},
            {'key': 'shoulders_day', 'label': 'SHOULDERS', 'subtitle': 'ALL DELTOID HEADS',
             'desc': 'Complete shoulder development.', 'rest_note': 'REST 60-90 SECONDS'},
            {'key': 'arms_day', 'label': 'ARMS', 'subtitle': 'BICEPS · TRICEPS',
             'desc': 'Isolation work for maximum arm pump.', 'rest_note': 'REST 45-60 SECONDS'},
            {'key': 'legs_day', 'label': 'LEGS', 'subtitle': 'QUADS · HAMSTRINGS · CALVES',
             'desc': 'Complete leg development.', 'rest_note': 'REST 2 MINUTES ON HEAVY SETS'},
        ]
    },
    'FULL BODY': {
        'days': [
            {'key': 'full_body_a', 'label': 'FULL BODY A', 'subtitle': 'STRENGTH FOCUS',
             'desc': 'Full body emphasizing strength on main compounds.', 'rest_note': 'REST 2-3 MINUTES'},
            {'key': 'full_body_b', 'label': 'FULL BODY B', 'subtitle': 'HYPERTROPHY FOCUS',
             'desc': 'Full body with higher volume for muscle growth.', 'rest_note': 'REST 60-90 SECONDS'},
        ]
    },
}

# ═══════════════════════════════════════════════
# SECTION 1: CLIENT INFO
# ═══════════════════════════════════════════════
st.markdown("## 📋 CLIENT INFORMATION")
st.markdown('<p class="section-desc">Basic client details — appears on the cover page of the PDF.</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    client_name = st.text_input('👤 Client Name', 'MOHAMED', help='Full name displayed on the cover page.')
    weight = st.text_input('⚖️ Weight (kg)', '75', help='Current body weight in kilograms.')
    start_date = st.text_input('📅 Start Date', datetime.now().strftime('%B %Y').upper(), help='Program start month/year. Example: JUNE 2026')
with col2:
    goal = st.text_input('🎯 Goal', 'HYPERTROPHY & STRENGTH', help='Primary training goal. Examples: HYPERTROPHY, STRENGTH, FAT LOSS')
    volume = st.text_input('📊 Volume', 'VOL.1', help='Program volume/phase identifier.')
    duration = st.text_input('⏱️ Duration', '8 WEEKS', help='Total program length. Example: 8 WEEKS, 12 WEEKS')
with col3:
    tagline = st.text_input('💬 Tagline', 'ENGINEERED FOR DOMINANCE', help='Motivational tagline on the cover.')
    frequency = st.text_input('🔄 Frequency', '6 DAYS / WEEK', help='Training days per week.')
    program_type = st.selectbox('📋 Program Type', list(PROGRAM_CONFIGS.keys()), index=0, help='Training split type. Determines the day layout in the PDF.')

# ═══════════════════════════════════════════════
# SECTION 2: COACH INFO
# ═══════════════════════════════════════════════
st.markdown("---")
st.markdown("## 🧑‍🏫 COACH INFORMATION")
st.markdown('<p class="section-desc">Your contact details — appear in the footer and last page of the PDF.</p>', unsafe_allow_html=True)

col_c1, col_c2, col_c3 = st.columns(3)
with col_c1:
    coach_name = st.text_input('Coach Name', 'AHMED TEKA', help='Your full name displayed on cover and last page.')
with col_c2:
    instagram = st.text_input('Instagram Username', '@coach.teka1', help='Your IG handle shown in footer with IG icon.')
with col_c3:
    phone = st.text_input('Phone Number', '01033047057', help='Contact number in footer of every page.')

instagram_link = st.text_input('Instagram Full Link', 'https://instagram.com/coach.teka1', help='Full clickable Instagram URL for PDF link.')

# ═══════════════════════════════════════════════
# SECTION 3: PHILOSOPHY
# ═══════════════════════════════════════════════
st.markdown("---")
st.markdown("## 📖 PROGRAM PHILOSOPHY")
st.markdown('<p class="section-desc">Appears on Page 2 (Introduction). Write your training philosophy and methodology.</p>', unsafe_allow_html=True)

philosophy = st.text_area('Training Philosophy', 
    value="This program is not about going through the motions. It is about training with intention, precision, and relentless focus. Every set, every rep, every second of rest is calculated to push your body beyond its limits and force adaptation.\n\nThe Push Pull Legs split allows optimal muscle recovery while maintaining high training frequency. You will train each muscle group twice per week across 6 sessions, with one full rest day for complete systemic recovery.\n\nAdhere strictly to prescribed rest intervals. Progressive overload — adding weight or reps each week — is your primary growth driver. Track every session. Outperform yesterday.",
    height=150, help='Comprehensive training philosophy for Page 2 of the PDF.')

# ═══════════════════════════════════════════════
# SECTION 4: EXERCISES
# ═══════════════════════════════════════════════
st.markdown("---")
st.markdown(f"## 💪 {program_type} — EXERCISES")
st.markdown('<p class="section-desc">Configure exercises for each training day. Each exercise has: Name, Sets, Reps, Rest, Description, Video Link.</p>', unsafe_allow_html=True)

config = PROGRAM_CONFIGS[program_type]
all_exercises = {}

for day_idx, day in enumerate(config['days']):
    st.markdown(f'<div class="day-header"><h3>🏆 Day {day_idx+1}: {day["label"]} — {day["subtitle"]}</h3></div>', unsafe_allow_html=True)
    
    ecol1, ecol2 = st.columns([2,1])
    with ecol1:
        day_desc = st.text_area(f'📝 Description — {day["label"]}', value=day['desc'], height=70, key=f'desc_{day["key"]}', help=f'Focus and methodology for {day["label"]} day.')
    with ecol2:
        day_rest = st.text_input(f'⏱️ Rest Note — {day["label"]}', value=day['rest_note'], key=f'rest_{day["key"]}', help=f'Rest period instructions for {day["label"]} day.')
    
    num_exercises = st.number_input(f'Number of exercises for {day["label"]}', min_value=1, max_value=20, value=8, key=f'num_{day["key"]}', help=f'How many exercises for {day["label"]} day? (Max 20)')
    
    st.markdown(f"**📋 Exercise List — {day['label']}**")
    
    # Headers
    h1, h2, h3, h4, h5, h6 = st.columns([3, 1, 1, 1, 3, 2])
    with h1: st.markdown('<p style="color:#D4AF37;font-weight:700;font-size:0.8rem">🏋️ NAME</p>', unsafe_allow_html=True)
    with h2: st.markdown('<p style="color:#D4AF37;font-weight:700;font-size:0.8rem">🔢 SETS</p>', unsafe_allow_html=True)
    with h3: st.markdown('<p style="color:#D4AF37;font-weight:700;font-size:0.8rem">🔁 REPS</p>', unsafe_allow_html=True)
    with h4: st.markdown('<p style="color:#D4AF37;font-weight:700;font-size:0.8rem">⏸️ REST</p>', unsafe_allow_html=True)
    with h5: st.markdown('<p style="color:#D4AF37;font-weight:700;font-size:0.8rem">📝 DESCRIPTION</p>', unsafe_allow_html=True)
    with h6: st.markdown('<p style="color:#D4AF37;font-weight:700;font-size:0.8rem">🔗 VIDEO LINK</p>', unsafe_allow_html=True)
    
    day_exercises = []
    for ex_idx in range(int(num_exercises)):
        c1, c2, c3, c4, c5, c6 = st.columns([3, 1, 1, 1, 3, 2])
        with c1:
            ex_name = st.text_input('Name', value='', placeholder='Ex: BENCH PRESS', key=f'n_{day["key"]}_{ex_idx}', label_visibility='collapsed')
        with c2:
            ex_sets = st.text_input('Sets', value='3', key=f's_{day["key"]}_{ex_idx}', label_visibility='collapsed')
        with c3:
            ex_reps = st.text_input('Reps', value='10-12', key=f'r_{day["key"]}_{ex_idx}', label_visibility='collapsed')
        with c4:
            ex_rest = st.text_input('Rest', value='90s', key=f'rest_{day["key"]}_{ex_idx}', label_visibility='collapsed')
        with c5:
            ex_desc = st.text_input('Desc', value='', placeholder='Full ROM. Control.', key=f'd_{day["key"]}_{ex_idx}', label_visibility='collapsed')
        with c6:
            ex_link = st.text_input('Link', value='#', key=f'l_{day["key"]}_{ex_idx}', label_visibility='collapsed')
        
        if ex_name.strip():
            day_exercises.append({
                'name': ex_name.strip(), 'sets': ex_sets.strip() or '3', 'reps': ex_reps.strip() or '10-12',
                'rest': ex_rest.strip() or '90s', 'desc': ex_desc.strip() or 'Full ROM.',
                'link': ex_link.strip() or '#', 'day': day['key']
            })
    
    all_exercises[day['key']] = {'exercises': day_exercises, 'desc': day_desc, 'rest_note': day_rest, 'label': day['label'], 'subtitle': day['subtitle']}

# ═══════════════════════════════════════════════
# SECTION 5: WARMUP (ALL FIELDS VISIBLE)
# ═══════════════════════════════════════════════
st.markdown("---")
st.markdown("## 🔥 WARM-UP PROTOCOL")
st.markdown('<p class="section-desc">Appears on Page 3 of the PDF. Configure the complete warm-up sequence.</p>', unsafe_allow_html=True)

wu_cardio = st.text_area('🏃 Cardio Phase', 
    value='5-10 MIN LIGHT CARDIO: Treadmill or bike at 60-65% max heart rate. Goal: elevate core temperature, increase joint lubrication, prime the cardiovascular system for heavy training.',
    height=70, help='Initial cardio warm-up instructions for Page 3.')

wu_col1, wu_col2 = st.columns(2)
with wu_col1:
    wu_upper = st.text_area('💪 Upper Body Warm-Up Sequence',
        value='Shoulder circles, band pull-aparts, arm swings, chest openers, thoracic rotations. Perform 2 full rounds before every Push and Pull session.',
        height=100, help='Upper body dynamic warm-up routine.')
    wu_upper_link = st.text_input('🔗 Upper Body Video Link', 'https://youtube.com/watch?v=upper_warmup', help='YouTube link for upper body warm-up video.')
with wu_col2:
    wu_lower = st.text_area('🦵 Lower Body Warm-Up Sequence',
        value='Hip circles, leg swings, bodyweight squats, ankle rotations, glute bridges. Perform 2 full rounds before every Legs session.',
        height=100, help='Lower body dynamic warm-up routine.')
    wu_lower_link = st.text_input('🔗 Lower Body Video Link', 'https://youtube.com/watch?v=lower_warmup', help='YouTube link for lower body warm-up video.')

wu_protocol = st.text_area('📋 Protocol Rules (One rule per line)',
    value='Never skip warm-up — injury prevention is non-negotiable\nFull range of motion on every drill\nUse warm-up sets: 50% > 75% > working weight\nNote restricted areas and spend extra time there',
    height=120, help='Warm-up protocol rules. Each line = one bullet point in the PDF.')

# ═══════════════════════════════════════════════
# SECTION 6: TIPS (DYNAMIC - ADD/REMOVE)
# ═══════════════════════════════════════════════
st.markdown("---")
st.markdown("## 💡 TIPS & MOTIVATION")
st.markdown('<p class="section-desc">Appears on Page 7 in a 2×3 grid. Add or remove tips as needed.</p>', unsafe_allow_html=True)

# Initialize tips count in session state
if 'tips_count' not in st.session_state:
    st.session_state.tips_count = 6

# Add/Remove buttons
col_add1, col_add2, col_add3 = st.columns([1, 1, 4])
with col_add1:
    if st.button('➕ Add Tip', use_container_width=True):
        st.session_state.tips_count += 1
        st.rerun()
with col_add2:
    if st.button('➖ Remove Tip', use_container_width=True) and st.session_state.tips_count > 1:
        st.session_state.tips_count -= 1
        st.rerun()

tips = []
tip_cols = st.columns(2)

for i in range(st.session_state.tips_count):
    with tip_cols[i % 2]:
        st.markdown(f'<div class="tip-card"><h4 style="color:#D4AF37;margin:0 0 0.5rem 0">💡 Tip #{i+1}</h4>', unsafe_allow_html=True)
        
        default_titles = ['PERFECT FORM', 'PROGRESSIVE OVERLOAD', 'SLEEP AS TRAINING', 'FUEL YOUR SESSIONS', 'HYDRATION DAILY', 'MENTAL EDGE',
                          'CONSISTENCY', 'TRACK PROGRESS', 'WARM UP PROPERLY', 'COOL DOWN', 'STRETCHING', 'MINDSET']
        default_bodies = [
            'Every rep with compromised technique reinforces a harmful pattern. Reduce load, master the movement, then progress. Record yourself regularly.',
            'Add 2.5 kg or 2 reps each week minimum. Log every session. If you are not progressing, you are regressing.',
            'Growth hormone peaks during deep sleep. 7-9 hours nightly is not optional — it is where muscle protein synthesis occurs.',
            'Target 1.8-2.2g protein per kg bodyweight daily. Eat a protein-rich meal 60-90 minutes before training. Log your nutrition.',
            'Minimum 4 liters of water on training days. Even mild dehydration reduces force output by up to 20%.',
            'Controlled breathing and visualization before each set measurably increases power output. Train the mind first. The body follows.',
            'Show up every single day. Consistency beats intensity every single time.',
            'Track every workout. What gets measured gets improved.',
            'Never skip warm-up. It prepares your body and prevents injuries.',
            'Cool down properly after each session to aid recovery.',
            'Stretch tight muscles regularly to maintain flexibility.',
            'Your mindset determines your results. Stay focused and positive.',
        ]
        
        tip_title = st.text_input(f'Title {i+1}', 
            value=default_titles[i] if i < len(default_titles) else f'Tip {i+1}',
            key=f'tip_title_{i}', 
            help=f'Title for tip #{i+1}. Keep it short and impactful.')
        
        tip_body = st.text_area(f'Body {i+1}',
            value=default_bodies[i] if i < len(default_bodies) else 'Write your tip here...',
            height=80, 
            key=f'tip_body_{i}', 
            help=f'Detailed body text for tip #{i+1}. Explain the tip in 1-2 sentences.')
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        if tip_title.strip():
            tips.append({
                'title': tip_title.strip(), 
                'icon': f'{i+1:02d}', 
                'body': tip_body.strip()
            })

st.caption(f'💡 {len(tips)} tips configured — Will appear in a {min(len(tips), 6)}-tip grid on Page 7')

# ═══════════════════════════════════════════════
# SECTION 7: QUOTE
# ═══════════════════════════════════════════════
st.markdown("---")
st.markdown("## 💬 MOTIVATIONAL QUOTE")
st.markdown('<p class="section-desc">Appears at the bottom of Page 7.</p>', unsafe_allow_html=True)

qcol1, qcol2 = st.columns([3, 1])
with qcol1:
    quote = st.text_area('Quote', 'THE BODY ACHIEVES WHAT THE MIND BELIEVES. DISCIPLINE IS THE BRIDGE BETWEEN GOALS AND GREATNESS.', height=100, help='Main motivational quote on Page 7.')
with qcol2:
    quote_author = st.text_input('Author', '— Ahmed Teka', help='Quote author attribution.')

# ═══════════════════════════════════════════════
# GENERATE BUTTON
# ═══════════════════════════════════════════════
st.markdown("---")
st.markdown('<div class="gen-btn">', unsafe_allow_html=True)
gen_clicked = st.button('🔥 GENERATE PREMIUM 8-PAGE PDF NOW 🔥', use_container_width=True, key='generate')
st.markdown('</div>', unsafe_allow_html=True)

if gen_clicked:
    if not client_name:
        st.error('❌ Please enter the client name.')
    else:
        with st.spinner('⚡ Creating premium 8-page workout plan...'):
            try:
                all_ex_list = []
                for dk, dd in all_exercises.items():
                    all_ex_list.extend(dd['exercises'])
                
                if not all_ex_list:
                    for dk, dd in all_exercises.items():
                        for i in range(3):
                            all_ex_list.append({'name': f'{dd["label"]} EX {i+1}', 'sets': '3', 'reps': '10-12', 'rest': '90s', 'desc': 'Full ROM.', 'link': '#', 'day': dk})
                
                if len(tips) < 6:
                    defaults = ['PERFECT FORM', 'PROGRESSIVE OVERLOAD', 'SLEEP AS TRAINING', 'FUEL YOUR SESSIONS', 'HYDRATION DAILY', 'MENTAL EDGE']
                    for i, t in enumerate(defaults):
                        if len(tips) <= i:
                            tips.append({'title': t, 'icon': f'{i+1:02d}', 'body': 'Focus on quality over quantity.'})
                
                data = {
                    'client_name': client_name, 'program': program_type, 'volume': volume,
                    'tagline': tagline, 'duration': duration, 'frequency': frequency,
                    'start_date': start_date, 'goal': goal, 'coach_name': coach_name,
                    'instagram': instagram, 'instagram_link': instagram_link, 'phone': phone,
                    'philosophy': philosophy, 'exercises': all_ex_list, 'tips': tips[:6],
                    'quote': quote, 'quote_author': quote_author,
                    'timeline': [
                        {'week': 'WEEK 1-2', 'phase': 'FOUNDATION', 'desc': 'Master form. Build mind-muscle connection.'},
                        {'week': 'WEEK 3-4', 'phase': 'PROGRESSION', 'desc': 'Increase load by 5-10%.'},
                        {'week': 'WEEK 5-6', 'phase': 'INTENSIFICATION', 'desc': 'Push beyond comfort zones.'},
                        {'week': 'WEEK 7-8', 'phase': 'PEAK OUTPUT', 'desc': 'Maximum effort. Deload final 3 days.'},
                    ],
                    'warmup': {
                        'cardio': wu_cardio, 'upper_note': wu_upper, 'lower_note': wu_lower,
                        'upper_link': wu_upper_link, 'lower_link': wu_lower_link,
                        'protocol': [p.strip() for p in wu_protocol.split('\n') if p.strip()],
                    },
                }
                
                pdf_bytes = generate_pdf(data)
                st.markdown(f'<div class="success-box">🔥 PDF GENERATED SUCCESSFULLY! 🔥<br><small>Client: {client_name} | Program: {program_type} | {len(all_ex_list)} Exercises | 8 Pages</small></div>', unsafe_allow_html=True)
                st.download_button('📥 DOWNLOAD PREMIUM PDF', data=pdf_bytes, file_name=f'AhmedTeka_{client_name.replace(" ","_")}.pdf', mime='application/pdf', use_container_width=True)
                
            except Exception as e:
                st.error(f'❌ Error: {str(e)}')
                import traceback
                st.code(traceback.format_exc())

st.markdown('---')
st.markdown("""
<div style="text-align:center;color:#6B7280;padding:1rem">
    <p style="font-size:1.1rem;color:#D4AF37;font-weight:700">© AHMED TEKA — PREMIUM WORKOUT PLANS</p>
    <p>📸 @coach.teka1 | 📞 01033047057</p>
</div>
""", unsafe_allow_html=True)