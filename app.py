import streamlit as st
from datetime import datetime
from workout_generator import generate_pdf

st.set_page_config(page_title='AHMED TEKA - Premium Workout Plan', page_icon='💪', layout='wide')

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
*{font-family:'Cairo',sans-serif!important}
.main-header{background:linear-gradient(135deg,#080B12,#1A2235);padding:1.5rem;border-radius:15px;text-align:center;border:2px solid #D4AF37;margin-bottom:1rem}
.main-header h1{color:#D4AF37;font-size:2rem;font-weight:900;margin:0}
.main-header p{color:#9BA3B2;margin:0}
.section-title{color:#D4AF37;font-size:1.3rem;font-weight:700;margin:1rem 0;padding:0.5rem 1rem;background:#111827;border-left:4px solid #D4AF37;border-radius:5px;cursor:pointer}
.stButton>button{background:linear-gradient(135deg,#D4AF37,#A0832A);color:#080B12;font-weight:700;font-size:1.2rem;padding:1rem;border-radius:10px;border:none;width:100%}
.stButton>button:hover{background:linear-gradient(135deg,#E8C84A,#D4AF37)}
label{color:#D4AF37!important;font-weight:600!important}
input,textarea{background-color:#1A2235!important;color:#E8E4DC!important;border:2px solid #374151!important;border-radius:8px!important}
.success-box{background:linear-gradient(135deg,#1C1A08,#2A2208);border:2px solid #D4AF37;border-radius:10px;padding:1.5rem;text-align:center;color:#D4AF37;font-size:1.2rem;font-weight:700}
.info-box{background:#0C1020;border:1px solid #374151;border-radius:8px;padding:1rem;margin:0.5rem 0}
.info-box h4{color:#D4AF37;margin:0 0 0.5rem 0}
.help-text{color:#6B7280;font-size:0.8rem;margin-top:0.2rem}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>AHMED TEKA</h1><p>PREMIUM WORKOUT PLAN GENERATOR</p></div>', unsafe_allow_html=True)

# Initialize session state for sections
if 'show_client' not in st.session_state:
    st.session_state.show_client = True
if 'show_philosophy' not in st.session_state:
    st.session_state.show_philosophy = False
if 'show_warmup' not in st.session_state:
    st.session_state.show_warmup = False
if 'show_push' not in st.session_state:
    st.session_state.show_push = False
if 'show_pull' not in st.session_state:
    st.session_state.show_pull = False
if 'show_legs' not in st.session_state:
    st.session_state.show_legs = False
if 'show_tips' not in st.session_state:
    st.session_state.show_tips = False

# ═══════════════════════════════════════════════
# SECTION 1: CLIENT INFO (Always visible)
# ═══════════════════════════════════════════════
st.markdown("## BASIC INFORMATION")
st.caption("Fill in the client details below. These will appear on the cover page.")

col1, col2, col3 = st.columns(3)
with col1:
    client_name = st.text_input('👤 Client Name', value='MOHAMED', help='Full name as it will appear on the PDF cover')
    weight = st.text_input('⚖️ Weight (kg)', value='75', help='Client current weight')
    start_date = st.text_input('📅 Start Date', value=datetime.now().strftime('%B %Y').upper(), help='Program start month/year')
with col2:
    goal = st.text_input('🎯 Goal', value='HYPERTROPHY & STRENGTH', help='Main training goal')
    program = st.text_input('📋 Program Type', value='PUSH // PULL // LEGS', help='Program split type')
    volume = st.text_input('📊 Volume', value='VOL.1', help='Program volume/phase')
with col3:
    tagline = st.text_input('💬 Tagline', value='ENGINEERED FOR DOMINANCE', help='Motto/tagline on cover')
    duration = st.text_input('⏱️ Duration', value='8 WEEKS', help='Total program length')
    frequency = st.text_input('🔄 Frequency', value='6 DAYS / WEEK', help='Training days per week')

st.markdown("---")

# COACH INFO
st.markdown("## COACH INFORMATION")
st.caption("Your contact details for the PDF footer and last page.")

col_c1, col_c2, col_c3 = st.columns(3)
with col_c1:
    coach_name = st.text_input('🧑‍🏫 Coach Name', value='AHMED TEKA', help='Your name as the coach')
with col_c2:
    instagram = st.text_input('📸 Instagram Username', value='@coach.teka1', help='Your IG handle')
with col_c3:
    phone = st.text_input('📞 Phone Number', value='01033047057', help='Your contact number')

instagram_link = st.text_input('🔗 Instagram Full Link', value='https://instagram.com/coach.teka1', help='Full clickable IG link')

st.markdown("---")

# ═══════════════════════════════════════════════
# SECTION 2: PHILOSOPHY (Collapsible)
# ═══════════════════════════════════════════════
col_ph1, col_ph2 = st.columns([10,1])
with col_ph1:
    if st.button('📖 PROGRAM PHILOSOPHY — Click to expand/collapse', use_container_width=True, key='btn_philosophy'):
        st.session_state.show_philosophy = not st.session_state.show_philosophy

if st.session_state.show_philosophy:
    st.info('💡 This text appears on Page 2 (Introduction). Write your training philosophy here.')
    philosophy = st.text_area('Philosophy Text', 
        value="This program is not about going through the motions. It is about training with intention, precision, and relentless focus. Every set, every rep, every second of rest is calculated to push your body beyond its limits and force adaptation.\n\nThe Push Pull Legs split allows optimal muscle recovery while maintaining high training frequency. You will train each muscle group twice per week across 6 sessions, with one full rest day for complete systemic recovery.\n\nAdhere strictly to prescribed rest intervals. Progressive overload — adding weight or reps each week — is your primary growth driver. Track every session. Outperform yesterday.",
        height=200, key='philosophy')
    
    st.markdown("### Program Timeline")
    st.caption("Edit the 4 phases of the program timeline.")
    
    tl_col1, tl_col2 = st.columns(2)
    with tl_col1:
        tl1_week = st.text_input('Phase 1 - Week Range', 'WEEK 1-2')
        tl1_phase = st.text_input('Phase 1 - Name', 'FOUNDATION')
        tl1_desc = st.text_area('Phase 1 - Description', 'Master form. Build mind-muscle connection. Establish baseline loads for all movements.', height=70, key='tl1')
        
        tl2_week = st.text_input('Phase 2 - Week Range', 'WEEK 3-4')
        tl2_phase = st.text_input('Phase 2 - Name', 'PROGRESSION')
        tl2_desc = st.text_area('Phase 2 - Description', 'Increase load by 5-10%. Volume ramps methodically. Training intensity begins to rise.', height=70, key='tl2')
    with tl_col2:
        tl3_week = st.text_input('Phase 3 - Week Range', 'WEEK 5-6')
        tl3_phase = st.text_input('Phase 3 - Name', 'INTENSIFICATION')
        tl3_desc = st.text_area('Phase 3 - Description', 'Push beyond comfort zones. Drop sets introduced on the final exercise of each session.', height=70, key='tl3')
        
        tl4_week = st.text_input('Phase 4 - Week Range', 'WEEK 7-8')
        tl4_phase = st.text_input('Phase 4 - Name', 'PEAK OUTPUT')
        tl4_desc = st.text_area('Phase 4 - Description', 'Maximum effort on all lifts. Test your true capacity. Deload the final 3 days of week 8.', height=70, key='tl4')

st.markdown("---")

# ═══════════════════════════════════════════════
# SECTION 3: WARMUP (Collapsible)
# ═══════════════════════════════════════════════
if st.button('🔥 WARM-UP PROTOCOL — Click to expand/collapse', use_container_width=True, key='btn_warmup'):
    st.session_state.show_warmup = not st.session_state.show_warmup

if st.session_state.show_warmup:
    st.info('🏃 This section appears on Page 3 (Warm-Up Protocol).')
    
    wu_cardio = st.text_area('Cardio Instructions', 
        value='5-10 MIN LIGHT CARDIO: Treadmill or bike at 60-65% max heart rate. Goal: elevate core temperature, increase joint lubrication, prime the cardiovascular system for heavy training.',
        height=80, key='wu_cardio')
    
    wc1, wc2 = st.columns(2)
    with wc1:
        wu_upper = st.text_area('Upper Body Warm-Up', 
            value='Shoulder circles, band pull-aparts, arm swings, chest openers, thoracic rotations. Perform 2 full rounds before every Push and Pull session.',
            height=100, key='wu_upper')
        wu_upper_link = st.text_input('Upper Body Video Link', 'https://youtube.com/watch?v=upper_warmup')
    with wc2:
        wu_lower = st.text_area('Lower Body Warm-Up',
            value='Hip circles, leg swings, bodyweight squats, ankle rotations, glute bridges. Perform 2 full rounds before every Legs session.',
            height=100, key='wu_lower')
        wu_lower_link = st.text_input('Lower Body Video Link', 'https://youtube.com/watch?v=lower_warmup')
    
    wu_protocol = st.text_area('Protocol Rules (one per line)',
        value='Never skip warm-up — injury prevention is non-negotiable\nFull range of motion on every drill\nUse warm-up sets: 50% > 75% > working weight\nNote restricted areas and spend extra time there',
        height=120, key='wu_protocol')

st.markdown("---")

# ═══════════════════════════════════════════════
# SECTION 4: PUSH DAY (Collapsible)
# ═══════════════════════════════════════════════
if st.button('💪 PUSH DAY — Chest · Shoulders · Triceps — Click to expand', use_container_width=True, key='btn_push'):
    st.session_state.show_push = not st.session_state.show_push

if st.session_state.show_push:
    st.info('🎯 Page 4 in the PDF. Enter exercises in format: NAME - SETSxREPS - REST - DESCRIPTION')
    st.markdown("**Example:** `CHEST PRESS MACHINE - 3x10-12 - 90s - Back flat against pad. Full ROM.`")
    push_text = st.text_area('Push Day Exercises (max 8)', 
        value="CHEST PRESS MACHINE - 3x10-12 - 90s - Back flat against pad. Full ROM - lockout to full stretch.\nDB INCLINE CHEST PRESS - 3x10-12 - 90s - 30-45 incline. Elbows slightly tucked. Control the eccentric.\nBUTTERFLY MACHINE - 3x10-12 - 90s - Peak squeeze at full contraction. 3-second eccentric phase.\nDB SHOULDER PRESS - 3x10-12 - 90s - Do not lock elbows at top. Core braced throughout.\nSEATED LATERAL RAISE - 3x12-15 - 60s - Lead with elbows. Slight forward lean. No momentum.\nCABLE OVERHEAD TRICEP - 3x12-15 - 60s - Hinge forward slightly. Full extension at bottom.\nROPE PUSHDOWN - 3x12-15 - 60s - Flare the rope outward at lockout. Elbows pinned to sides.\nCABLE CRUNCH - 3x15-20 - 45s - Round spine toward hips. Contraction is everything here.",
        height=250, key='push')
    push_rest = st.text_input('Push Day Rest Note', 'REST 90-120 SECONDS BETWEEN ALL WORKING SETS')
    push_desc = st.text_area('Push Day Description', 'Prioritize chest activation on horizontal movements, shoulder engagement on overhead work, and full tricep lockout on isolation exercises. Quality of contraction over quantity of weight.', height=80, key='push_desc')

st.markdown("---")

# ═══════════════════════════════════════════════
# SECTION 5: PULL DAY (Collapsible)
# ═══════════════════════════════════════════════
if st.button('🏋️ PULL DAY — Back · Biceps · Rear Delts — Click to expand', use_container_width=True, key='btn_pull'):
    st.session_state.show_pull = not st.session_state.show_pull

if st.session_state.show_pull:
    st.info('🎯 Page 5 in the PDF.')
    st.markdown("**Example:** `LAT PULLDOWN - 3x10-12 - 90s - Wide grip. Full lat stretch.`")
    pull_text = st.text_area('Pull Day Exercises (max 8)',
        value="LAT PULLDOWN - 3x10-12 - 90s - Wide grip. Pull to upper chest. Full lat stretch at top.\nSEATED ROW V-BAR - 3x10-12 - 90s - Chest tall. Squeeze shoulder blades hard at contraction.\nBACK EXTENSION - 3x12-15 - 60s - Neutral spine. Engage glutes and lumbar simultaneously.\nREAR DELT FLY MACHINE - 3x12-15 - 60s - Arms parallel to floor. Control the negative.\nDUMBBELL CURL - 3x10-12 - 60s - Supinate at peak. Elbows stationary.\nROPE HAMMER CURL - 3x10-12 - 60s - Neutral grip. Targets brachialis.\nINCLINE DB SHRUG - 3x12-15 - 60s - Straight elevation. 1-second hold at top.",
        height=250, key='pull')
    pull_rest = st.text_input('Pull Day Rest Note', 'REST 90-120 SECONDS BETWEEN ALL WORKING SETS')
    pull_desc = st.text_area('Pull Day Description', 'Drive elbows — not hands — on all row variations. Maintain scapular retraction throughout. Feel the lats stretch at full extension on every pulldown and row.', height=80, key='pull_desc')

st.markdown("---")

# ═══════════════════════════════════════════════
# SECTION 6: LEGS DAY (Collapsible)
# ═══════════════════════════════════════════════
if st.button('🦵 LEGS DAY — Quads · Hamstrings · Glutes · Calves — Click to expand', use_container_width=True, key='btn_legs'):
    st.session_state.show_legs = not st.session_state.show_legs

if st.session_state.show_legs:
    st.info('🎯 Page 6 in the PDF.')
    st.markdown("**Example:** `BARBELL BACK SQUAT - 4x8-10 - 120s - Below parallel. Knees track toes.`")
    legs_text = st.text_area('Legs Day Exercises (max 8)',
        value="BARBELL BACK SQUAT - 4x8-10 - 120s - Below parallel depth. Knees track over toes. Brace hard.\nLEG PRESS MACHINE - 3x10-12 - 90s - High foot placement targets glutes. No knee lockout.\nHACK SQUAT - 3x10-12 - 90s - Close stance for quad emphasis. Full controlled depth.\nLEG EXTENSION - 3x12-15 - 60s - Peak squeeze. 2-second hold at full extension.\nHAMSTRING CURL - 3x12-15 - 60s - Plantarflex foot at top for maximal engagement.\nBARBELL LUNGES - 3x10/leg - 90s - Long stride, upright torso. Drive through front heel.\nSEATED CALF RAISE - 3x15-20 - 45s - Full stretch at bottom. Slow tempo.\nSTANDING CALF RAISE - 2x20-25 - 45s - Single-leg variation for imbalance correction.",
        height=250, key='legs')
    legs_rest = st.text_input('Legs Day Rest Note', 'REST 2 FULL MINUTES AFTER SQUATS AND LEG PRESS')
    legs_desc = st.text_area('Legs Day Description', 'Heavy compound movements first. Never skip posterior chain work. Drive through the full foot on every squat variation — heel to toe engagement.', height=80, key='legs_desc')

st.markdown("---")

# ═══════════════════════════════════════════════
# SECTION 7: TIPS (Collapsible)
# ═══════════════════════════════════════════════
if st.button('💡 TIPS & MOTIVATION — Click to expand/collapse', use_container_width=True, key='btn_tips'):
    st.session_state.show_tips = not st.session_state.show_tips

if st.session_state.show_tips:
    st.info('📝 Page 7 in the PDF. Format: TITLE | BODY (one per line)')
    tips_text = st.text_area('Tips (title | body per line)',
        value="PERFECT FORM | Every rep with compromised technique reinforces a harmful pattern. Reduce load, master the movement, then progress. Record yourself regularly.\nPROGRESSIVE OVERLOAD | Add 2.5 kg or 2 reps each week minimum. Log every session. If you are not progressing, you are regressing.\nSLEEP AS TRAINING | Growth hormone peaks during deep sleep. 7-9 hours nightly is not optional — it is where muscle protein synthesis occurs.\nFUEL YOUR SESSIONS | Target 1.8-2.2g protein per kg bodyweight daily. Eat a protein-rich meal 60-90 minutes before training.\nHYDRATION DAILY | Minimum 4 liters of water on training days. Even mild dehydration reduces force output by up to 20%.\nMENTAL EDGE | Controlled breathing and visualization before each set measurably increases power output.",
        height=200, key='tips')
    
    cq1, cq2 = st.columns([3,1])
    with cq1:
        quote = st.text_area('Motivational Quote', 'THE BODY ACHIEVES WHAT THE MIND BELIEVES. DISCIPLINE IS THE BRIDGE BETWEEN GOALS AND GREATNESS.', height=100)
    with cq2:
        quote_author = st.text_input('Quote Author', '— Ahmed Teka')

st.markdown("---")

# ═══════════════════════════════════════════════
# GENERATE BUTTON
# ═══════════════════════════════════════════════
if st.button('🚀 GENERATE PREMIUM 8-PAGE PDF', use_container_width=True):
    if not client_name:
        st.error('❌ Please enter the client name at minimum.')
    else:
        with st.spinner('🔄 Creating your premium 8-page workout plan PDF...'):
            try:
                def parse_ex(text, day):
                    exs = []
                    for line in text.strip().split('\n'):
                        if line.strip():
                            parts = line.split(' - ')
                            name = parts[0].strip()
                            sr = parts[1].strip() if len(parts) > 1 else '3x10-12'
                            rest = parts[2].strip() if len(parts) > 2 else '90s'
                            desc = parts[3].strip() if len(parts) > 3 else 'Full ROM.'
                            s, r = ('3', '10-12')
                            if 'x' in sr:
                                sp = sr.split('x')
                                s, r = sp[0].strip(), sp[1].strip()
                            exs.append({'name': name, 'sets': s, 'reps': r, 'rest': rest, 'desc': desc, 'link': '#', 'day': day})
                    return exs
                
                exercises = []
                if st.session_state.show_push:
                    exercises.extend(parse_ex(push_text, 'push_day'))
                else:
                    # default push
                    exercises.extend([{'name':'CHEST PRESS MACHINE','sets':'3','reps':'10-12','rest':'90s','desc':'Full ROM.','link':'#','day':'push_day'},{'name':'DB SHOULDER PRESS','sets':'3','reps':'10-12','rest':'90s','desc':'No lock elbows.','link':'#','day':'push_day'},{'name':'ROPE PUSHDOWN','sets':'3','reps':'12-15','rest':'60s','desc':'Elbows pinned.','link':'#','day':'push_day'}])
                
                if st.session_state.show_pull:
                    exercises.extend(parse_ex(pull_text, 'pull_day'))
                else:
                    exercises.extend([{'name':'LAT PULLDOWN','sets':'3','reps':'10-12','rest':'90s','desc':'Wide grip.','link':'#','day':'pull_day'},{'name':'SEATED ROW','sets':'3','reps':'10-12','rest':'90s','desc':'Squeeze blades.','link':'#','day':'pull_day'},{'name':'DUMBBELL CURL','sets':'3','reps':'10-12','rest':'60s','desc':'Supinate at peak.','link':'#','day':'pull_day'}])
                
                if st.session_state.show_legs:
                    exercises.extend(parse_ex(legs_text, 'legs_day'))
                else:
                    exercises.extend([{'name':'BARBELL BACK SQUAT','sets':'4','reps':'8-10','rest':'120s','desc':'Below parallel.','link':'#','day':'legs_day'},{'name':'LEG PRESS','sets':'3','reps':'10-12','rest':'90s','desc':'No lockout.','link':'#','day':'legs_day'},{'name':'LEG EXTENSION','sets':'3','reps':'12-15','rest':'60s','desc':'Peak squeeze.','link':'#','day':'legs_day'}])
                
                tips = []
                if st.session_state.show_tips:
                    for line in tips_text.strip().split('\n'):
                        if '|' in line:
                            t, b = line.split('|', 1)
                            tips.append({'title': t.strip(), 'icon': f'{len(tips)+1:02d}', 'body': b.strip()})
                else:
                    tips = [{'title':'PERFECT FORM','icon':'01','body':'Master form first.'},{'title':'PROGRESSIVE OVERLOAD','icon':'02','body':'Add weight weekly.'},{'title':'SLEEP','icon':'03','body':'7-9 hours nightly.'},{'title':'NUTRITION','icon':'04','body':'1.8-2.2g protein/kg.'},{'title':'HYDRATION','icon':'05','body':'4L water daily.'},{'title':'MENTAL EDGE','icon':'06','body':'Visualize success.'}]
                
                data = {
                    'client_name': client_name, 'program': program, 'volume': volume,
                    'tagline': tagline, 'duration': duration, 'frequency': frequency,
                    'start_date': start_date, 'goal': goal, 'coach_name': coach_name,
                    'instagram': instagram, 'instagram_link': instagram_link, 'phone': phone,
                    'philosophy': philosophy if st.session_state.show_philosophy else 'Train with intention and precision.',
                    'exercises': exercises, 'tips': tips,
                    'quote': quote if st.session_state.show_tips else 'DISCIPLINE IS THE BRIDGE.',
                    'quote_author': quote_author if st.session_state.show_tips else '- Ahmed Teka',
                    'timeline': [
                        {'week': tl1_week if st.session_state.show_philosophy else 'WEEK 1-2', 'phase': tl1_phase if st.session_state.show_philosophy else 'FOUNDATION', 'desc': tl1_desc if st.session_state.show_philosophy else 'Master form.'},
                        {'week': tl2_week if st.session_state.show_philosophy else 'WEEK 3-4', 'phase': tl2_phase if st.session_state.show_philosophy else 'PROGRESSION', 'desc': tl2_desc if st.session_state.show_philosophy else 'Increase load.'},
                        {'week': tl3_week if st.session_state.show_philosophy else 'WEEK 5-6', 'phase': tl3_phase if st.session_state.show_philosophy else 'INTENSIFICATION', 'desc': tl3_desc if st.session_state.show_philosophy else 'Push beyond.'},
                        {'week': tl4_week if st.session_state.show_philosophy else 'WEEK 7-8', 'phase': tl4_phase if st.session_state.show_philosophy else 'PEAK OUTPUT', 'desc': tl4_desc if st.session_state.show_philosophy else 'Maximum effort.'},
                    ],
                    'warmup': {
                        'cardio': wu_cardio if st.session_state.show_warmup else '5-10 MIN LIGHT CARDIO',
                        'upper_note': wu_upper if st.session_state.show_warmup else 'Shoulder circles, arm swings.',
                        'lower_note': wu_lower if st.session_state.show_warmup else 'Hip circles, leg swings.',
                        'upper_link': wu_upper_link if st.session_state.show_warmup else '#',
                        'lower_link': wu_lower_link if st.session_state.show_warmup else '#',
                        'protocol': wu_protocol.split('\n') if st.session_state.show_warmup else ['Never skip warm-up', 'Full ROM on every drill'],
                    },
                }
                
                pdf_bytes = generate_pdf(data)
                st.markdown('<div class="success-box">✅ PREMIUM PDF GENERATED SUCCESSFULLY!</div>', unsafe_allow_html=True)
                st.download_button('📥 DOWNLOAD PDF', data=pdf_bytes, file_name=f'AhmedTeka_{client_name}.pdf', mime='application/pdf', use_container_width=True)
                
            except Exception as e:
                st.error(f'Error: {str(e)}')
                import traceback
                st.code(traceback.format_exc())

st.markdown('---')
st.markdown('<p style="text-align:center;color:#6B7280">© AHMED TEKA · @coach.teka1 · 01033047057</p>', unsafe_allow_html=True)