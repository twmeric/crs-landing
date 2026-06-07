# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ========== P0: 删除/替换暗示逃税的表述 ==========
replacements = [
    # Slide 1
    ("將客戶數據合法鎖定，確保「不被看見」", "協助客戶依法優化申報路徑，確保合規透明"),
    ("頂層物理安全盾牌", "頂層合規防護架構"),
    ("前線合夥人的定位是「跨境資產防禦體系的架構師」", "前線合夥人的定位是「跨境資產合規架構的專業顧問」"),
    ("我們交付的是一套經得起大數據稽查的頂層物理安全盾牌", "我們交付的是一套符合法規要求的頂層合規防護架構"),
    
    # Slide 2
    ("精準物理切斷", "合規路徑優化"),
    ("精準獵殺", "精準稽查"),
    ("境外私行/託管銀行後台自動盤點非居民賬戶的資產淨值與收益", "境外金融機構依法識別非居民賬戶並進行信息申報"),
    
    # Slide 3
    ("形同裸奔", "存在顯著合規風險"),
    ("直接刺穿公司外殼，將最終受益人（UBO）的個人身份與資產淨值全量送回內地", "依法要求穿透識別實益擁有人（UBO），相關信息將納入CRS交換範圍"),
    ("廉價中介註冊的「殼公司」，在大數據獵殺模型下形同裸奔", "未經合規設計的離岸架構，在CRS穿透規則下存在顯著合規風險"),
    
    # Slide 4
    ("將國稅局抓取數據的關鍵因子直接歸零", "將國稅局抓取數據的關鍵因子依法優化"),
    ("讓大數據天眼永遠看不見你", "讓大數據申報路徑更加合規高效"),
    ("只要其中一個因子是零，大數據天眼就永遠看不見你", "只要其中一個因子依法優化，合規申報路徑將更加清晰透明"),
    ("從底層物理公式上，把可能暴露你資產的因子合法歸零", "從底層法規框架出發，把可能影響合規效率的因子依法優化"),
    
    # Slide 5
    ("就像是在大馬路上裸奔的「被動老百姓」", "在CRS規則下屬於需要穿透申報的消極實體"),
    ("數據被合法鎖在香港本地", "數據依法在香港本地進行管理"),
    ("用合法的商業隱密外衣把數據留在香港", "用合規的商業架構將數據管理權依法配置在香港"),
    ("反客為主", "優化實體屬性"),
    ("套路", "方法論"),
    ("套路核心拆解", "架構核心邏輯"),
    
    # Slide 6
    ("❌ 走常規路徑：大數據雷達秒抓", "❌ 走常規路徑：稅務成本較高"),
    ("💎 走我們設計的管道：大數據直接免疫", "💎 走我們設計的管道：合規框架下的稅務優化"),
    ("致命後果：國稅局雷達對『分紅、利潤、薪水』極其敏感", "稅務影響：分紅、利潤、薪水屬於應稅收入，需依法申報"),
    ("分紅一出，立刻觸發 CRS 跨境通報與高達 20%~45% 的個人所得稅", "分紅收入需依法納入個人所得稅申報，適用相應稅率"),
    ("大數據天眼直接對你免疫", "在合規框架下實現稅務成本優化"),
    ("這條股東貸款還本的會計管道，幫客戶合法省下來的海外個稅", "這條股東貸款還本的合規會計安排，幫助客戶優化稅務成本"),
    
    # Slide 7
    ("徹底擦除名字", "通過法律架構進行所有權安排"),
    ("你名下資產合法歸零", "資產法律所有權轉移至信託名下"),
    ("這筆錢暫時不屬於任何特定的人", "受益權的行使需依信託契約及法規進行"),
    ("跟你個人完全切斷關係，讓他無從查起", "與個人名義持有存在法律區別，但仍需依法履行申報義務"),
    ("因為資產已經換名字了，跟你個人完全切斷關係，讓他無從查起", "因為資產法律所有權已轉移至信託，但CRS框架下信託信息仍需依法申報"),
    ("終極底牌", "重要合規工具"),
    ("信託是整個防禦地圖的「終極底牌」", "信託是整個合規架構的重要組成部分"),
    ("無法對一個在法律上「不屬於你」的資產強行徵稅", "信託架構下的資產處置仍需遵守相關稅法規定"),
    
    # Slide 8
    ("數據安全鎖死在香港", "數據依法在香港本地管理"),
    ("這就是終極的技術套路", "這就是核心的技術方法論"),
    ("技術套路", "技術方法"),
    
    # Slide 9
    ("核心病灶", "核心風險點"),
    ("潛在系統風險（核心病灶）", "潛在系統風險（核心風險點）"),
    
    # Slide 10
    ("幻覺粉碎", "認知澄清"),
    ("降維粉碎話術", "專業澄清話術"),
    ("戳破他們的幻覺", "澄清認知誤區"),
    ("等國稅局正式走稽查程序、發函要你說明海外第一桶金來源時，那就不是合規諮詢能解決的了", "發現合規漏洞後及早諮詢專業顧問，是保障資產安全的最佳方式"),
    ("只有用基金架構把數據合法鎖在香港本地，才是物理級的安全", "只有用合規的基金架構依法管理數據，才是法律層面的安全"),
    
    # Slide 11
    ("提前消滅合夥人與客戶心中最底層的疑慮", "提前解答合夥人與客戶關心的核心問題"),
    
    # Slide 12
    ("10天標準化「手術」", "標準化合規流程"),
    ("10天內完成 OFC 基金籌建、海外全權信託契約簽署、以及底層 SPV 公司股東貸款科目變更登記", "3-6個月內完成 OFC 基金籌建（視SFC審批進度）、海外全權信託契約簽署、以及底層 SPV 公司股東貸款科目變更登記"),
    ("Day 6 - 10", "Day 60 - 180"),
    ("10天內完成", "3-6個月內完成（視SFC審批進度）"),
    ("精密手術與架構落地", "精密合規與架構落地"),
    
    # Slide 13
    ("終身變現", "長期合作"),
    ("實現客戶關係的終身變現", "建立與客戶的長期合作關係"),
    
    # Slide 14
    ("合伙人零風險", "後台提供專業支持"),
    ("合夥人定位是前端「導醫」，後台專業人士才是「主刀醫生」。所有專業諮詢責任依法歸屬後台主體，合夥人高枕無憂", "合夥人定位是前端「導醫」，後台專業人士負責「主刀」。所有專業諮詢責任由後台持牌主體承擔，合夥人需確保引薦行為符合持牌要求"),
    ("合夥人高枕無憂", "合夥人獲得專業支持"),
    
    # Slide 15
    ("裸奔", "存在合規風險"),
    ("海外資產可能還在消極殼公司裡裸奔", "海外資產可能仍通過未合規優化的消極實體持有"),
    ("正處於國稅局大數據的精準捕獵範圍內", "需依法進行CRS申報與合規審查"),
]

for old, new in replacements:
    content = content.replace(old, new)

# ========== 添加免责声明到每页底部 ==========
# 在 </div> 的 action-guide-box 后面添加免责声明
# 由于结构复杂，我们在每个 slide 的 action-guide-box 后面插入

disclaimer_html = '''            <div style="margin-top: 20px; padding: 12px 16px; background: #FAF6F0; border-left: 3px solid #C5A059; font-size: 0.7rem; color: #777; line-height: 1.5; text-align: justify;">
                <strong>重要免責聲明：</strong>本材料僅供專業研究參考，不構成正式稅務、法律或投資意見。CRS、CFC、受控外國企業規則及各地稅法具有複雜性與時效性，具體個案應諮詢持牌稅務師、律師及法律顧問。任何架構調整均需以合法合規為前提，不得用於規避法定申報義務。過往未申報的境外收入應主動向稅務機關說明情況。信託及基金架構的設立需遵守各司法管轄區的反洗錢（AML）、實質經濟法規及SFC持牌要求。
            </div>'''

# 在每个 slide 的最后（</div> 前，controls-bar 之前）插入免责声明
# 找到每个 slide 的结束位置
slide_pattern = r'(<div class="slide" id="slide-\d+">.*?</div>\s*</div>)'
slides = re.findall(slide_pattern, content, re.DOTALL)

for slide in slides:
    # 在 slide 的最后一个 </div> 之前插入免责声明
    modified_slide = slide.rstrip() + "\n" + disclaimer_html + "\n        </div>"
    content = content.replace(slide, modified_slide, 1)

# ========== 添加经济实质说明到 Slide 5 ==========
economic_substance_note = '''            <div style="margin-top: 20px; padding: 15px 20px; background: #FFF8F0; border: 1px solid rgba(255,102,0,0.2); border-radius: 4px;">
                <div style="font-size: 0.8rem; font-weight: 500; color: #FF6600; margin-bottom: 6px;">⚠️ 經濟實質要求提醒</div>
                <p style="font-size: 0.75rem; color: #555; line-height: 1.6;">香港 OFC / LPF 架構的設立需滿足嚴格的經濟實質要求，包括但不限於：在香港聘用具備資格的投資經理、設立實質辦公場所、董事會會議在香港舉行、年度營運開支達到法定門檻等。未滿足經濟實質要求的架構可能面臨穿透風險及稅務當局的重新定性。</p>
            </div>'''

# 在 Slide 5 的 action-guide-box 后面添加
slide5_marker = '<div class="action-guide-box">\n                <span class="action-tag">架構核心邏輯</span>'
content = content.replace(slide5_marker, economic_substance_note + "\n" + slide5_marker, 1)

# ========== 添加 AML/KYC 提醒到 Slide 12 ==========
aml_kyc_note = '''            <div style="margin-top: 20px; padding: 15px 20px; background: #F0F8FF; border: 1px solid rgba(0,0,0,0.08); border-radius: 4px;">
                <div style="font-size: 0.8rem; font-weight: 500; color: #1A1A1A; margin-bottom: 6px;">🛡️ 反洗錢（AML）與客戶盡職調查（KYC）要求</div>
                <p style="font-size: 0.75rem; color: #555; line-height: 1.6;">所有跨境架構調整必須符合各司法管轄區的 AML/KYC 法規要求。客戶需提供資金來源證明（Source of Funds）及財富來源證明（Source of Wealth）。未經盡職調查的架構設立可能面臨法律風險及監管處罰。</p>
            </div>'''

slide12_marker = '<div class="action-guide-box">\n                <span class="action-tag">合夥人安全隔離</span>'
content = content.replace(slide12_marker, aml_kyc_note + "\n" + slide12_marker, 1)

# ========== 修改标题，更合规 ==========
content = content.replace(
    "CRS 跨境資產合規作戰地圖 | 15張淺白實戰版",
    "CRS 跨境資產合規架構指南 | 15頁專業參考版"
)
content = content.replace(
    "跨境資產防禦<br><span style=\"color: var(--hermes-orange); font-weight: 200;\">合規作戰地圖</span>",
    "跨境資產合規<br><span style=\"color: var(--hermes-orange); font-weight: 200;\">架構參考指南</span>"
)
content = content.replace(
    "面向專業合夥人的 15 步第一性原理實戰指南",
    "面向專業合夥人的 15 步合規架構參考指南"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done. Modified", len(replacements), "text replacements and added 3 new sections.")
