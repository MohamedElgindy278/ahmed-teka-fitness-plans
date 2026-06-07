import os
import io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color, HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

W, H = A4

# ═══════════════════════════════════════════════
# FONTS
# ═══════════════════════════════════════════════
FONT_PATHS = [
    'C:/Windows/Fonts/arial.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
]

AR = 'Helvetica'
AR_BOLD = 'Helvetica-Bold'

for fp in FONT_PATHS:
    if os.path.exists(fp):
        try:
            pdfmetrics.registerFont(TTFont('AR', fp))
            pdfmetrics.registerFont(TTFont('ARB', fp.replace('.ttf', 'bd.ttf').replace('Sans', 'Sans-Bold').replace('Regular', 'Bold')) if 'Bold' not in fp else TTFont('ARB', fp))
            AR = 'AR'
            AR_BOLD = 'ARB'
            break
        except:
            pass

# ═══════════════════════════════════════════════
# COLORS - White + Green + Gold
# ═══════════════════════════════════════════════
BG_DARK     = HexColor('#0A1F0A')
BG_WHITE    = HexColor('#FFFFFF')
BG_CREAM    = HexColor('#F5F7F5')
CARD_BG     = HexColor('#F0F7F0')
GREEN_DARK  = HexColor('#1B5E20')
GREEN       = HexColor('#2E7D32')
GREEN_LIGHT = HexColor('#4CAF50')
GREEN_SOFT  = HexColor('#81C784')
GREEN_DIM   = HexColor('#C8E6C9')
GOLD        = HexColor('#D4AF37')
GRAY_DARK   = HexColor('#555555')
GRAY        = HexColor('#777777')
GRAY_LIGHT  = HexColor('#999999')
WHITE       = HexColor('#FFFFFF')
BLACK_SOFT  = HexColor('#1A1A1A')

# ═══════════════════════════════════════════════
# LAYOUT CONSTANTS
# ═══════════════════════════════════════════════
M           = 24
HDR_H       = 44
FTR_H       = 34
STRIPE_W    = 5
TOTAL_PAGES = 6

# ═══════════════════════════════════════════════
# PRIMITIVES
# ═══════════════════════════════════════════════

def fill_bg(c, col=None):
    c.setFillColor(col or BG_WHITE)
    c.rect(0, 0, W, H, stroke=0, fill=1)

def fill_rect(c, x, y, w, h, col):
    c.setFillColor(col)
    c.rect(x, y, w, h, stroke=0, fill=1)

def rrect(c, x, y, w, h, r, fc, sc=None, sw=0.5):
    c.setFillColor(fc)
    if sc:
        c.setStrokeColor(sc)
        c.setLineWidth(sw)
    p = c.beginPath()
    p.moveTo(x+r, y); p.lineTo(x+w-r, y)
    p.arcTo(x+w-2*r, y, x+w, y+2*r, -90, 90)
    p.lineTo(x+w, y+h-r)
    p.arcTo(x+w-2*r, y+h-2*r, x+w, y+h, 0, 90)
    p.lineTo(x+r, y+h)
    p.arcTo(x, y+h-2*r, x+2*r, y+h, 90, 90)
    p.lineTo(x, y+r)
    p.arcTo(x, y, x+2*r, y+2*r, 180, 90)
    p.close()
    c.drawPath(p, fill=1, stroke=1 if sc else 0)

def tl(c, s, x, y, f='Helvetica', sz=10, col=BLACK_SOFT):
    c.setFillColor(col); c.setFont(f, sz); c.drawString(x, y, str(s))

def tc(c, s, x, y, f='Helvetica', sz=10, col=BLACK_SOFT):
    c.setFillColor(col); c.setFont(f, sz); c.drawCentredString(x, y, str(s))

def tr(c, s, x, y, f='Helvetica', sz=10, col=BLACK_SOFT):
    c.setFillColor(col); c.setFont(f, sz); c.drawRightString(x, y, str(s))

def hline(c, x, y, w, col=GREEN, lw=1.0):
    c.setStrokeColor(col); c.setLineWidth(lw); c.line(x, y, x+w, y)

def circle(c, cx, cy, r, col):
    c.setFillColor(col); c.circle(cx, cy, r, fill=1, stroke=0)

def stripe(c, col=GREEN):
    fill_rect(c, 0, 0, STRIPE_W, H, col)

def grad_v(c, x, y, w, h, c1, c2, n=30):
    r1,g1,b1 = c1.red, c1.green, c1.blue
    r2,g2,b2 = c2.red, c2.green, c2.blue
    sh = h/n
    for i in range(n):
        t = i/n
        c.setFillColor(Color(r1+(r2-r1)*t, g1+(g2-g1)*t, b1+(b2-b1)*t))
        c.rect(x, y+h-(i+1)*sh, w, sh+0.6, stroke=0, fill=1)

def wrap(c, text, x, y, maxw, f, sz, col, lh=None):
    lh = lh or sz * 1.55
    c.setFillColor(col); c.setFont(f, sz)
    for para in str(text).split('\n\n'):
        words = para.replace('\n', ' ').split()
        line = []
        for word in words:
            if c.stringWidth(' '.join(line + [word]), f, sz) <= maxw:
                line.append(word)
            else:
                if line: c.drawString(x, y, ' '.join(line)); y -= lh
                line = [word]
        if line: c.drawString(x, y, ' '.join(line)); y -= lh
        y -= lh * 0.35
    return y

def content_area():
    x = STRIPE_W + M
    w = W - x - M
    return x, H - HDR_H - M, w

# ═══════════════════════════════════════════════
# CHROME (Header + Footer)
# ═══════════════════════════════════════════════

def chrome(c, section, pgnum, data, accent=GREEN):
    stripe(c, GREEN)
    fill_rect(c, 0, H-HDR_H, W, HDR_H, BG_CREAM)
    hline(c, 0, H-HDR_H, W, GREEN, 1.0)
    tl(c, 'AHMED', STRIPE_W+12, H-HDR_H+17, 'Helvetica-Bold', 13, GREEN)
    tl(c, 'TEKA', STRIPE_W+68, H-HDR_H+17, 'Helvetica-Bold', 13, GRAY_DARK)
    tc(c, section, W/2, H-HDR_H+17, 'Helvetica', 8.5, GRAY)
    fill_rect(c, 0, 0, W, FTR_H, BG_CREAM)
    hline(c, 0, FTR_H, W, GREEN, 0.7)
    tl(c, data.get('instagram', '@coach.teka1'), STRIPE_W+12, FTR_H/2-4, 'Helvetica', 7.5, GREEN)
    tc(c, data.get('phone', '01033047057'), W/2, FTR_H/2-4, 'Helvetica', 7.5, GRAY)
    tr(c, f'{pgnum} / {TOTAL_PAGES}', W-12, FTR_H/2-4, 'Helvetica-Bold', 8.5, accent)

# ═══════════════════════════════════════════════
# PAGE 1 - COVER
# ═══════════════════════════════════════════════

def p1_cover(c, data):
    fill_bg(c, BG_DARK)
    
    cover_photo = 'images/AhmedTeka_image1.jpeg'
    try:
        if os.path.exists(cover_photo):
            c.drawImage(cover_photo, 0, 0, W, H, preserveAspectRatio=True)
    except:
        grad_v(c, 0, 0, W, H, BG_DARK, HexColor('#0D2A0D'))
    
    c.setFillColor(Color(0, 0, 0, alpha=0.55))
    c.rect(0, 0, W, H, stroke=0, fill=1)
    stripe(c, GREEN_LIGHT)
    
    fill_rect(c, 0, H-52, W, 52, Color(0,0,0,0.85))
    hline(c, 0, H-52, W, GREEN_LIGHT, 1.2)
    tl(c, 'AHMED', STRIPE_W+16, H-32, 'Helvetica-Bold', 18, GREEN_LIGHT)
    tl(c, 'TEKA', STRIPE_W+84, H-32, 'Helvetica-Bold', 18, WHITE)
    hline(c, STRIPE_W+16, H-40, 100, GREEN_LIGHT, 0.6)
    tr(c, 'NUTRITION COACH', W-16, H-32, 'Helvetica', 8.5, GRAY_LIGHT)
    
    ty = H - 130
    c.setStrokeColor(Color(1,1,1,0.3)); c.setLineWidth(1.2)
    c.line(STRIPE_W+20, ty+30, STRIPE_W+20+50, ty+30)
    c.line(W-20-50, ty+30, W-20, ty+30)
    
    tc(c, 'NUTRITION', W/2, ty+15, 'Helvetica-Bold', 48, WHITE)
    tc(c, 'PLAN', W/2, ty-25, 'Helvetica-Bold', 48, GREEN_LIGHT)
    tc(c, 'Personalized Meal Plan', W/2, ty-50, 'Helvetica', 10, Color(1,1,1,0.6))
    
    cy = ty - 105
    rrect(c, STRIPE_W+16, cy, W-STRIPE_W-32, 54, 6, Color(0,0,0,0.78), GREEN_LIGHT, 1.0)
    fill_rect(c, STRIPE_W+16, cy, 4, 54, GREEN_LIGHT)
    tl(c, 'CLIENT', STRIPE_W+28, cy+40, 'Helvetica', 7, GREEN_SOFT)
    tl(c, str(data.get('client_name', 'CLIENT')), STRIPE_W+28, cy+16, AR_BOLD, 28, WHITE)
    tr(c, str(data.get('goal', 'FITNESS')), W-24, cy+30, 'Helvetica', 8.5, GREEN_LIGHT)
    
    by = cy - 10
    pw = (W - STRIPE_W - 36) / 3 - 5
    pills = [
        ('DURATION', data.get('duration', '12 WEEKS')),
        ('MEALS', data.get('meals_count', '4 MEALS')),
        ('START', data.get('start_date', 'JUNE 2026')),
    ]
    for i, (lbl, val) in enumerate(pills):
        px = STRIPE_W + 16 + i * (pw + 7.5)
        rrect(c, px, by-58, pw, 50, 4, Color(0,0,0,0.70), GOLD, 0.6)
        tl(c, lbl, px+10, by-24, 'Helvetica', 7, GRAY_LIGHT)
        tl(c, str(val), px+10, by-44, 'Helvetica-Bold', 12, GREEN_LIGHT)
    
    fill_rect(c, 0, 0, W, 40, Color(0,0,0,0.88))
    hline(c, 0, 40, W, GREEN_LIGHT, 0.8)
    tl(c, data.get('instagram', '@coach.teka1'), STRIPE_W+16, 15, 'Helvetica', 8, GREEN_LIGHT)
    tc(c, data.get('phone', '01033047057'), W/2, 15, 'Helvetica', 8, GRAY_LIGHT)
    tr(c, f'Coach {data.get("coach_name", "AHMED TEKA")}', W-14, 15, 'Helvetica-Bold', 9, GREEN_LIGHT)
    
    c.showPage()

# ═══════════════════════════════════════════════
# PAGE 2 - PROFILE & MACROS
# ═══════════════════════════════════════════════

def p2_profile(c, data):
    fill_bg(c, BG_CREAM)
    chrome(c, 'CLIENT PROFILE', 2, data)
    x, y, cw = content_area()
    
    tc(c, 'CLIENT PROFILE', x + cw/2, y - 10, 'Helvetica-Bold', 26, GREEN)
    tc(c, 'Personal Information & Macros', x + cw/2, y - 32, 'Helvetica', 10, GRAY)
    hline(c, x, y - 40, cw, GREEN, 1.0)
    
    py = y - 60
    info_items = [
        ('FULL NAME', data.get('full_name', 'N/A')),
        ('AGE', data.get('age', 'N/A')),
        ('WEIGHT', data.get('weight', 'N/A')),
        ('HEIGHT', data.get('height', 'N/A')),
        ('GOAL', data.get('goal', 'N/A')),
    ]
    
    bw = (cw - 15) / 2
    for i, (lbl, val) in enumerate(info_items):
        col = i % 2
        row = i // 2
        ix = x + col * (bw + 15)
        iy = py - row * 55
        
        rrect(c, ix, iy-42, bw, 40, 6, WHITE, GREEN_DIM, 0.3)
        fill_rect(c, ix, iy-42, 3, 40, GREEN)
        tl(c, lbl, ix+12, iy-14, 'Helvetica', 7, GRAY)
        tl(c, str(val), ix+12, iy-32, AR_BOLD, 13, BLACK_SOFT)
    
    ny = py - 130
    rrect(c, x, ny-45, cw, 42, 6, WHITE, GREEN_DIM, 0.5)
    tl(c, 'COACH NOTES', x+12, ny-16, 'Helvetica-Bold', 9, GREEN)
    tl(c, str(data.get('notes', ''))[:90], x+12, ny-33, AR, 8, GRAY)
    
    my = ny - 65
    tc(c, 'DAILY MACRONUTRIENTS', x + cw/2, my, 'Helvetica-Bold', 16, GREEN)
    hline(c, x, my-8, cw, GOLD, 0.8)
    
    macros = [
        ('MEALS/DAY', data.get('main_meals', '4'), 'meals', GREEN),
        ('PROTEIN', data.get('protein_g', '0'), 'g/day', GREEN_LIGHT),
        ('CARBS', data.get('carbs_g', '0'), 'g/day', GOLD),
        ('FAT', data.get('fat_g', '0'), 'g/day', GREEN_SOFT),
    ]
    
    mw = (cw - 30) / 4
    for i, (lbl, val, unit, color) in enumerate(macros):
        mx = x + i * (mw + 10)
        rrect(c, mx, my-65, mw, 58, 8, WHITE, color, 1)
        circle(c, mx + mw/2, my-22, 18, color)
        tc(c, str(val), mx + mw/2, my-27, 'Helvetica-Bold', 14, WHITE)
        tc(c, lbl, mx + mw/2, my-45, 'Helvetica', 7, GRAY)
        tc(c, unit, mx + mw/2, my-55, 'Helvetica', 6, GRAY)
    
    c.showPage()

# ═══════════════════════════════════════════════
# PAGE 3 - MEALS (Arabic)
# ═══════════════════════════════════════════════

def p3_meals(c, data):
    fill_bg(c, BG_CREAM)
    chrome(c, 'DAILY MEAL PLAN', 3, data)
    x, y, cw = content_area()
    
    c.saveState()
    c.setStrokeColor(Color(0.3, 0.5, 0.3, 0.03))
    c.setLineWidth(0.3)
    for px in range(30, int(W), 40):
        for py in range(30, int(H), 40):
            c.circle(px, py, 2, fill=0, stroke=1)
    c.restoreState()
    
    tc(c, 'DAILY MEAL PLAN', x + cw/2, y - 10, 'Helvetica-Bold', 24, GREEN)
    tc(c, 'خطة الوجبات اليومية', x + cw/2, y - 30, AR, 12, GRAY)
    hline(c, x, y - 38, cw, GREEN, 1.0)
    
    meals = data.get('meals', [])
    food_icons = ['🥣', '💪', '🍗', '🥗', '🍝', '🥤']
    
    my = y - 60
    for i, meal in enumerate(meals[:6]):
        icon = food_icons[i] if i < len(food_icons) else '🍽️'
        mh = 110
        
        rrect(c, x, my-mh, cw, mh-3, 8, WHITE, GREEN_DIM, 0.3)
        fill_rect(c, x, my-mh, 4, mh, GREEN)
        
        circle(c, x+30, my-24, 18, GREEN_DIM)
        tc(c, icon, x+30, my-27, 'Helvetica', 16, BLACK_SOFT)
        
        tl(c, str(meal.get('name', '')), x+56, my-14, AR_BOLD, 12, BLACK_SOFT)
        tl(c, str(meal.get('type', '')), x+56, my-26, AR, 8, GRAY)
        
        tl(c, f'{meal.get("calories", "0")} kcal', x+56, my-42, 'Helvetica-Bold', 18, GREEN)
        tl(c, f'P: {meal.get("protein", "0")}g  C: {meal.get("carbs", "0")}g  F: {meal.get("fat", "0")}g', x+56, my-54, 'Helvetica', 8, GRAY)
        
        ingredients = meal.get('ingredients', [])
        ing_y = my - 68
        if isinstance(ingredients, list):
            for ing in ingredients[:4]:
                tl(c, f'• {ing}', x+56, ing_y, AR, 8, GRAY)
                ing_y -= 11
        else:
            tl(c, f'• {str(ingredients)[:60]}', x+56, ing_y, AR, 8, GRAY)
        
        alt = meal.get('alternative', '')
        if alt:
            tl(c, f'🔄 {str(alt)[:65]}', x+56, ing_y-4, AR, 7, GREEN)
        
        my -= mh + 4
    
    if my > FTR_H + 60:
        rrect(c, x, my-40, cw, 36, 8, GREEN_DIM, GREEN, 1.2)
        tc(c, f'Total: {data.get("total_calories", "0")} kcal / day', x + cw/2, my-18, 'Helvetica-Bold', 14, GREEN)
    
    c.showPage()

# ═══════════════════════════════════════════════
# PAGE 4 - GUIDELINES & SUPPLEMENTS
# ═══════════════════════════════════════════════

def p4_guidelines(c, data):
    fill_bg(c, BG_CREAM)
    chrome(c, 'GUIDELINES & SUPPLEMENTS', 4, data)
    x, y, cw = content_area()
    
    tc(c, 'DAILY GUIDELINES', x + cw/2, y - 10, 'Helvetica-Bold', 24, GREEN)
    hline(c, x, y - 18, cw, GREEN, 1.0)
    
    wy = y - 40
    rrect(c, x, wy-55, cw, 50, 8, WHITE, GREEN, 1.5)
    fill_rect(c, x, wy-55, 4, 50, GREEN)
    tc(c, '💧 DAILY HYDRATION', x + cw/2, wy-18, 'Helvetica-Bold', 12, GREEN)
    tc(c, f'{data.get("water", "4-6 L")} of water per day', x + cw/2, wy-38, 'Helvetica-Bold', 20, BLACK_SOFT)
    
    gy = wy - 70
    gw = (cw - 15) / 2
    guidelines = [
        ('⏰ Meal Timing', data.get('meal_timing', '')),
        ('⚖️ Food Weighing', data.get('food_weighing', '')),
        ('🥤 Drinks', data.get('drinks', '')),
        ('🚫 Restricted', data.get('sweets', '')),
    ]
    
    for i, (title, body) in enumerate(guidelines):
        col = i % 2
        row = i // 2
        gx = x + col * (gw + 15)
        gyy = gy - row * 60
        
        rrect(c, gx, gyy-48, gw, 44, 6, WHITE, GREEN_DIM, 0.3)
        fill_rect(c, gx, gyy-48, 3, 44, GREEN)
        tl(c, title, gx+10, gyy-18, 'Helvetica-Bold', 10, GREEN)
        wrap(c, str(body)[:55], gx+10, gyy-32, gw-15, AR, 7.5, GRAY, lh=11)
    
    oy = gy - 140
    rrect(c, x, oy-34, cw, 30, 6, WHITE, GREEN_DIM, 0.5)
    tl(c, f'🐟 Omega-3: {data.get("omega", "")}', x+12, oy-14, AR, 9, GREEN)
    
    sy = oy - 50
    tc(c, 'SUPPLEMENTS', x + cw/2, sy, 'Helvetica-Bold', 14, GREEN)
    hline(c, x, sy-6, cw, GOLD, 0.5)
    
    supplements = data.get('supplements', [])
    for i, sup in enumerate(supplements[:3]):
        sr = sy - 20 - i * 35
        rrect(c, x, sr-26, cw, 24, 5, WHITE, GREEN_DIM, 0.3)
        circle(c, x+20, sr-13, 10, GREEN)
        tc(c, str(i+1), x+20, sr-16, 'Helvetica-Bold', 7, WHITE)
        tl(c, sup.get('name', ''), x+36, sr-8, 'Helvetica-Bold', 10, BLACK_SOFT)
        tl(c, f'{sup.get("dose", "")} — {sup.get("benefit", "")}'[:55], x+36, sr-20, AR, 7, GRAY)
    
    py2 = sy - 20 - len(supplements) * 35 - 15
    if py2 > FTR_H + 60:
        tc(c, 'PRE-WORKOUT PROTOCOL', x + cw/2, py2, 'Helvetica-Bold', 12, GREEN)
        hline(c, x, py2-5, cw, GOLD, 0.4)
        
        preworkout = data.get('preworkout', [])
        for i, pw in enumerate(preworkout[:2]):
            pwy = py2 - 20 - i * 30
            rrect(c, x, pwy-22, cw, 20, 4, GREEN_DIM, GREEN, 0.2)
            tl(c, f'{pw.get("time", "")}: {pw.get("item", "")}'[:70], x+10, pwy-10, AR, 8, BLACK_SOFT)
    
    c.showPage()

# ═══════════════════════════════════════════════
# PAGE 5 - RECIPES
# ═══════════════════════════════════════════════

def p5_recipes(c, data):
    fill_bg(c, BG_CREAM)
    chrome(c, 'RECIPE LIBRARY', 5, data)
    x, y, cw = content_area()
    
    tc(c, 'RECIPE LIBRARY', x + cw/2, y - 10, 'Helvetica-Bold', 24, GREEN)
    tc(c, 'وصفات صحية للبرنامج', x + cw/2, y - 30, AR, 11, GRAY)
    hline(c, x, y - 38, cw, GREEN, 1.0)
    
    recipes = data.get('recipes', [])
    rw = (cw - 20) / 3
    
    ry = y - 60
    for i, recipe in enumerate(recipes[:6]):
        col = i % 3
        row = i // 3
        rx = x + col * (rw + 10)
        ryy = ry - row * 125
        
        rrect(c, rx, ryy-110, rw, 106, 8, WHITE, GREEN_DIM, 0.3)
        
        circle(c, rx + rw/2, ryy-42, 25, GREEN_DIM)
        circle(c, rx + rw/2, ryy-42, 18, GREEN)
        tc(c, '🍳', rx + rw/2, ryy-46, 'Helvetica', 16, WHITE)
        
        tc(c, str(recipe.get('name', ''))[:18], rx + rw/2, ryy-72, AR_BOLD, 9, BLACK_SOFT)
        tc(c, str(recipe.get('desc', ''))[:25], rx + rw/2, ryy-84, AR, 7, GRAY)
        
        rrect(c, rx+10, ryy-105, rw-20, 18, 4, GREEN)
        tc(c, 'Watch Recipe', rx + rw/2, ryy-97, 'Helvetica-Bold', 7, WHITE)
        
        link = recipe.get('link', '#')
        if link and link != '#':
            c.linkURL(link, (rx+10, ryy-105, rx+rw-10, ryy-87))
    
    qy = ry - 280
    if qy > FTR_H + 60:
        rrect(c, x, qy-50, cw, 46, 8, GREEN_DIM, GREEN, 1)
        tc(c, '"Consistency is the key to lasting results."', x + cw/2, qy-18, 'Helvetica-Bold', 11, GREEN)
        tc(c, f'— {data.get("coach_name", "AHMED TEKA")}', x + cw/2, qy-34, 'Helvetica', 9, GRAY)
    
    c.showPage()

# ═══════════════════════════════════════════════
# PAGE 6 - COACH
# ═══════════════════════════════════════════════

def p6_coach(c, data):
    fill_bg(c, BG_DARK)
    
    coach_photo = 'images/AhmedTeka_image3.jpeg'
    try:
        if os.path.exists(coach_photo):
            c.drawImage(coach_photo, 0, 0, W, H, preserveAspectRatio=True)
    except:
        grad_v(c, 0, 0, W, H, BG_DARK, HexColor('#0D2A0D'))
    
    c.setFillColor(Color(0, 0, 0, alpha=0.55))
    c.rect(0, 0, W, H, stroke=0, fill=1)
    stripe(c, GREEN_LIGHT)
    
    fill_rect(c, 0, H-50, W, 50, Color(0,0,0,0.85))
    hline(c, 0, H-50, W, GREEN_LIGHT, 1.0)
    tl(c, 'AHMED', STRIPE_W+16, H-32, 'Helvetica-Bold', 18, GREEN_LIGHT)
    tl(c, 'TEKA', STRIPE_W+86, H-32, 'Helvetica-Bold', 18, WHITE)
    hline(c, STRIPE_W+16, H-39, 106, GREEN_LIGHT, 0.7)
    tr(c, 'YOUR COACH', W-16, H-32, 'Helvetica', 9, GRAY_LIGHT)
    
    cy = H * 0.55
    lw_c = 70
    c.setStrokeColor(GREEN_LIGHT); c.setLineWidth(1.5)
    c.line(W/2 - 200, cy + 25, W/2 - 200 + lw_c, cy + 25)
    c.line(W/2 + 200 - lw_c, cy + 25, W/2 + 200, cy + 25)
    
    tc(c, data.get('coach_name', 'AHMED TEKA'), W/2, cy, 'Helvetica-Bold', 48, GREEN_LIGHT)
    tc(c, 'NUTRITION COACH', W/2, cy-30, 'Helvetica', 14, WHITE)
    
    fill_rect(c, 0, 0, W, 90, Color(0,0,0,0.85))
    hline(c, 0, 90, W, GREEN_LIGHT, 0.8)
    
    btn_w = 150; btn_h = 34; gap2 = 15
    total_btns = 2*btn_w + gap2
    bx_start = W/2 - total_btns/2
    
    for i, (lbl, color) in enumerate([
        (f'@{data.get("instagram", "coach.teka1")}', GREEN_LIGHT),
        (data.get('phone', '01033047057'), GOLD),
    ]):
        bx = bx_start + i*(btn_w+gap2)
        by = 15
        rrect(c, bx, by, btn_w, btn_h, 5, Color(0,0,0,0.5), color, 1.2)
        tc(c, lbl, bx+btn_w/2, by+btn_h/2-4, 'Helvetica-Bold', 10, WHITE)
    
    tr(c, f'{TOTAL_PAGES} / {TOTAL_PAGES}', W-14, 100, 'Helvetica-Bold', 9, GREEN_LIGHT)
    
    c.showPage()

# ═══════════════════════════════════════════════
# BUILD FUNCTION
# ═══════════════════════════════════════════════

def generate_nutrition_pdf(data):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    c.setTitle('AHMED TEKA — Nutrition Plan')
    c.setAuthor(data.get('coach_name', 'AHMED TEKA'))
    c.setSubject('Professional Nutrition Plan')
    c.setCreator('Ahmed Teka Nutrition Engine')
    
    p1_cover(c, data)
    p2_profile(c, data)
    p3_meals(c, data)
    p4_guidelines(c, data)
    p5_recipes(c, data)
    p6_coach(c, data)
    
    c.save()
    pdf_bytes = buffer.getvalue()
    buffer.close()
    return pdf_bytes