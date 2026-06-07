# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Disclaimer HTML pattern
disclaimer_pattern = r'''\s*<div style="margin-top: 20px; padding: 12px 16px; background: #FAF6F0; border-left: 3px solid #C5A059; font-size: 0\.7rem; color: #777; line-height: 1\.5; text-align: justify;">\s*<strong>重要免責聲明：</strong>.*?</div>'''

# Find all disclaimers
matches = list(re.finditer(disclaimer_pattern, content, re.DOTALL))
print(f"Found {len(matches)} disclaimers")

# Remove ALL disclaimers first
content = re.sub(disclaimer_pattern, '', content, flags=re.DOTALL)

# Find Slide 1's closing </div> (the slide container, not inner elements)
# Slide 1: <div class="slide active" id="slide-1"> ... </div> followed by <div class="slide" id="slide-2">
slide1_end_marker = '</div>\n\n        <div class="slide" id="slide-2">'

# The disclaimer to add to Slide 1
disclaimer_html = '''

            <div style="margin-top: 16px; padding: 10px 14px; background: #FAF6F0; border-left: 3px solid #C5A059; font-size: 0.65rem; color: #777; line-height: 1.5; text-align: justify;">
                <strong>重要免責聲明：</strong>本材料僅供專業研究參考，不構成正式稅務、法律或投資意見。CRS、CFC、受控外國企業規則及各地稅法具有複雜性與時效性，具體個案應諮詢持牌稅務師、律師及法律顧問。任何架構調整均需以合法合規為前提，不得用於規避法定申報義務。過往未申報的境外收入應主動向稅務機關說明情況。信託及基金架構的設立需遵守各司法管轄區的反洗錢（AML）、實質經濟法規及SFC持牌要求。
            </div>'''

# Insert disclaimer before Slide 1's closing
def insert_disclaimer_before_slide2(match):
    return disclaimer_html + '\n        </div>' + '\n\n        <div class="slide" id="slide-2">'

content = re.sub(
    r'(</div>\s*\n\s*<div class="slide" id="slide-2">)',
    insert_disclaimer_before_slide2,
    content,
    count=1
)

# Fix Slide 07 structure: move the two orphan trust-layers back inside trust-box-container
# Find the broken structure in Slide 7
slide7_fix_pattern = (
    r'(<div class="trust-box-container">\s*'
    r'<div class="trust-layer">\s*'
    r'<div class="layer-title">.*?</div>\s*'
    r'<div class="layer-desc">.*?</div>\s*'
    r'</div>\s*)'
    r'(</div>\s*'
    r'<div class="trust-layer">\s*'
    r'<div class="layer-title">.*?</div>\s*'
    r'<div class="layer-desc">.*?</div>\s*'
    r'</div>\s*'
    r'<div class="trust-layer">\s*'
    r'<div class="layer-title">.*?</div>\s*'
    r'<div class="layer-desc">.*?</div>\s*'
    r'</div>\s*)'
    r'(</div>\s*<div class="action-guide-box">)'
)

# A simpler approach: just fix the specific Slide 7 structure
# Look for: trust-box-container with one trust-layer, then closing, then two more trust-layers
slide7_broken = re.search(
    r'(<div class="trust-box-container">\s*<div class="trust-layer">.*?)(</div>\s*)(<div class="trust-layer">.*?)(<div class="trust-layer">.*?</div>\s*)(</div>\s*<div class="action-guide-box">)',
    content,
    re.DOTALL
)

if slide7_broken:
    # Reconstruct: keep all three trust-layers inside trust-box-container
    fixed = (
        slide7_broken.group(1) +
        slide7_broken.group(3) +
        slide7_broken.group(4) +
        slide7_broken.group(5)
    )
    content = content.replace(slide7_broken.group(0), fixed)
    print("Fixed Slide 07 structure")
else:
    print("Slide 07 pattern not found - may already be fixed or structure changed")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done.")
