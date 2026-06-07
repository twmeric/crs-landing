# -*- coding: utf-8 -*-
# This script appends part 2 to the existing index.html

scenarios = [
    {
        "num": "01",
        "title": "已有离岸公司",
        "tag": "BVI / 开曼 / 香港壳",
        "profile": "客户持有BVI或开曼壳公司，用于持股、收租或持有海外资产。公司除了注册地址外没有实质经营，银行账户直接关联个人。",
        "trigger": "银行KYC更新通知、账户突然被要求补充UBO信息、转账额度被限制",
        "script": [
            ("开场", "张总，您那间BVI公司最近有没有收到银行的KYC更新表格？"),
            ("痛点", "现在银行后台会自动判断公司是Passive NFE还是FI。如果是Passive，就会穿透到您个人，把账户信息自动送回内地。"),
            ("数据冲击", "去年香港向内地自动交换了超过100万条账户信息，这不是抽查，是批量传输。"),
            ("软性邀约", "要不要找个时间，我帮您看看现在的架构在CRS眼里是什么状态？不收费，就当做个体检。"),
        ],
        "rebuttal": [
            ("我的壳公司又不在内地，内地税务局管不到。", "张总，CRS管的不是'公司在哪'，而是'信息交换'。您的香港银行每年5月会自动把您BVI公司的账户余额和受益人信息打包送回内地税务局。这不是内地税务局'管不管得到'的问题，是数据已经自动到家门口了。"),
        ],
    },
    {
        "num": "02",
        "title": "香港物业持有者",
        "tag": "房产 / 租金 / 套现",
        "profile": "客户在香港有1套以上房产，用于收租或准备出售变现。租金收入直接汇入个人账户，或未做合规申报。",
        "trigger": "发现租金收入越来越透明、准备出售房产、收到税务局关于海外收入的询问",
        "script": [
            ("开场", "张总，您那几套香港物业的租金，现在还是直接打进个人账户吗？"),
            ("痛点", "香港物业租金属于香港来源收入，香港税务局会征收物业税。同时，如果客户仍是内地税务居民，这笔租金在内地也需申报。两边都看得见。"),
            ("数据冲击", "香港税务局和内地税务局之间已经有CRS数据交换通道。您在香港收的每一笔租金，内地系统都能收到对应信息。"),
            ("软性邀约", "我们可以帮您设计一个合规的租金架构，让税务成本最优化。要不要先做一个初步评估？"),
        ],
        "rebuttal": [
            ("我在香港交税了，内地应该不用再交吧？", "张总，香港和内地的税制是独立的。在香港交了物业税，不代表内地就豁免了。如果您仍是内地税务居民，全球收入都需申报。不过两地之间有税收抵免安排，关键是看架构怎么设计才能合法合规地优化整体税负。"),
        ],
    },
    {
        "num": "03",
        "title": "刚拿香港身份",
        "tag": "高才通 / 优才 / 投资",
        "profile": "客户刚通过高才通、优才或投资移民拿到香港身份，误以为拿了香港身份证就等于税务豁免。核心企业、家人和常住地仍在内地。",
        "trigger": "刚获批香港身份、准备申请永居、担心内地税务局是否还管自己",
        "script": [
            ("开场", "张总，恭喜您拿到香港身份！不过我多嘴问一句，您的主要公司和家人都还在内地吧？"),
            ("痛点", "税法看的是'核心利益中心地'，不是'身份证'。只要您的主要事业、家人还在内地，在法律上您依然是内地的全球征税对象。"),
            ("数据冲击", "很多客户以为拿了香港身份就安全了，结果CRS交换回来的数据显示他仍是内地税务居民，两边都要申报，反而更麻烦。"),
            ("软性邀约", "身份规划和税务规划是两回事。我们可以帮您看看现在的税务居民身份认定情况，再决定怎么配合身份做最优安排。"),
        ],
        "rebuttal": [
            ("我已经拿了香港身份证，内地税务局还能管我？", "张总，税务局不管您拿哪里的身份证，管的是您的'习惯性住所'和'核心利益中心'。只要您每年在内地待超过183天，或者主要收入来自内地企业，您就仍然是内地税务居民。香港身份是入境处发的，税务身份是税务局定的，这是两套系统。"),
        ],
    },
    {
        "num": "04",
        "title": "跨境电商老板",
        "tag": "外汇 / 平台收款 / 资金回流",
        "profile": "客户经营跨境电商或跨境贸易，通过第三方平台收款，资金频繁在境内外流动。收款路径复杂，缺乏合规申报。",
        "trigger": "平台要求补充税务信息、外汇额度受限、资金回流路径被银行询问",
        "script": [
            ("开场", "张总，您现在亚马逊/Shopify的货款，是怎么回流到内地的？走第三方平台还是直接结汇？"),
            ("痛点", "跨境电商的资金流特别容易被大数据标记。如果收款路径没有设计好，一笔大额结汇就可能触发反洗钱预警和税务关注。"),
            ("数据冲击", "去年金税四期上线后，银行系统已经和税务系统打通。单笔超过一定额度的跨境资金流动，会自动推送给税务局做比对。"),
            ("软性邀约", "我们可以帮您设计一条合规的资金回流通道，既满足经营需要，又能优化税务成本。要不要先聊聊您的收款结构？"),
        ],
        "rebuttal": [
            ("我做的是正当生意，税务局不会管我吧？", "张总，正当生意和合规申报是两回事。您做生意当然正当，但如果收款没有走合规的申报路径，税务局看到的可能是'大额资金流入但无对应申报'。这就不是生意正不正当的问题，是申报链条完不完整的问题。"),
        ],
    },
    {
        "num": "05",
        "title": "准备二代接班",
        "tag": "家族传承 / 资产分散 / 股权",
        "profile": "家族企业创始人准备将资产和企业传给下一代。资产分散在多个法域，股权结构复杂，缺乏系统性的传承规划。",
        "trigger": "子女即将成年或回国接班、创始人考虑退休、家族资产需要重组",
        "script": [
            ("开场", "张总，您现在家族的资产分布，如果让您儿子/女儿接班，他能一句话说清楚家里有哪些资产、分别在哪些地方吗？"),
            ("痛点", "接班最大的风险不是子女能力不够，是资产结构太乱。创始人自己可能都记不清楚每家离岸公司的作用，下一代更是一头雾水。"),
            ("数据冲击", "没有顶层设计的家族资产，在CRS时代就像裸奔。每家公司的账户信息每年都会被交换，如果架构没有提前梳理好，接班的时候税务局比子女还清楚家里有多少钱。"),
            ("软性邀约", "我们可以帮您做一个家族资产的'健康体检'，把分布在各地的资产梳理清楚，再设计一个既合规又方便传承的顶层架构。"),
        ],
        "rebuttal": [
            ("我还在考虑，不急着做。", "张总，传承规划最怕的就是'临时抱佛脚'。等到您决定退休的时候再梳理，可能面临几个问题：第一，时间紧，很多架构调整需要3-6个月；第二，身体状况变化可能导致税务居民身份认定复杂化；第三，CRS数据已经在持续交换，拖得越久，历史数据暴露得越多。现在做，是'从容布局'；以后做，是'被动救火'。"),
        ],
    },
    {
        "num": "06",
        "title": "海外上市/融资",
        "tag": "IPO / VIE / 股权激励",
        "profile": "客户的企业准备海外上市或已经搭建VIE架构，有复杂的股权结构和股权激励计划。创始人个人资产与企业资产混同。",
        "trigger": "启动IPO流程、投资人要求尽调、准备发放股权激励",
        "script": [
            ("开场", "张总，您现在VIE架构里的开曼公司，个人持股部分有没有做过税务规划？"),
            ("痛点", "海外上市最大的税务地雷在上市前。如果创始人个人持股没有提前规划，上市套现时可能面临巨额的个税冲击。而且CRS会让您的持股信息完全透明。"),
            ("数据冲击", "上市后，您的开曼公司股东信息、持股数量、分红记录，都会通过CRS通道交换回内地。如果之前没有做合规架构，到时候想补救都来不及。"),
            ("软性邀约", "我们可以帮您做一个上市前的税务架构诊断，看看现在的持股方式在上市后会产生多少税务成本，再设计优化方案。"),
        ],
        "rebuttal": [
            ("我的投资人/律师已经帮我做好了。", "张总，投资人和律师主要关注的是上市合规和公司治理，税务优化通常不是他们的核心能力。很多VIE架构在上市前没有考虑创始人个人的税务居民身份和CRS影响，结果上市后创始人套现时发现税负比预期高出一倍。这不是质疑您的团队，是多一层专业保障。"),
        ],
    },
    {
        "num": "07",
        "title": "中西部内企老板",
        "tag": "不熟悉资本市场 / 资产主要在内地",
        "profile": "来自中西部地区的传统企业老板，不熟悉离岸架构和资本市场。资产主要在内地，但子女留学或企业有出海打算，开始有跨境需求。",
        "trigger": "子女准备出国留学、企业接到海外订单、身边朋友开始聊海外配置",
        "script": [
            ("开场", "张总，您身边有没有朋友最近把一部分资产放到香港或新加坡去了？他们有没有跟您聊过CRS的事情？"),
            ("痛点", "中西部很多企业老板以前完全不需要关心海外税务，但现在子女一留学、企业一出海，就突然暴露在CRS的射程之内了。最可怕的是，很多人完全不知道游戏规则已经变了。"),
            ("数据冲击", "现在不是只有大老板才会被CRS覆盖。只要您在香港或海外有任何银行账户——哪怕只有几十万——银行都会依法把信息交换回内地。"),
            ("软性邀约", "您现在可能还没有海外账户，但如果您有出海的打算，提前了解规则比临时抱佛脚要划算得多。我们可以先做一个免费的'出海前税务体检'，看看您如果走出去，会碰到哪些税务关卡。"),
        ],
        "rebuttal": [
            ("我是做实业的，不搞那些虚的，应该跟我没关系。", "张总，我完全理解您的想法。但CRS不是针对'搞虚的'的人，它是针对所有有海外金融账户的人。您现在可能没有海外账户，但如果您以后要给留学的孩子汇学费、或者企业要做海外贸易、或者想在香港开个公司接订单——只要您在海外有任何银行账户，就会自动进入CRS交换范围。这不是'搞不搞虚的'的问题，是'做不做海外生意'的问题。"),
        ],
    },
    {
        "num": "08",
        "title": "初创公司老板",
        "tag": "融资计划 / 股权复杂 / 提前规划",
        "profile": "科技或新经济领域初创公司创始人，有融资计划或已经获得多轮融资。股权结构复杂（含期权池、代持等），创始人个人资产与公司资产混同。",
        "trigger": "启动A轮/B轮融资、投资人要求税务尽调、考虑设立海外架构",
        "script": [
            ("开场", "张总，您现在公司的股权架构，如果下一轮投资人要做税务尽调，您觉得能通过吗？"),
            ("痛点", "很多初创公司早期为了省事，股权结构做得非常简单——创始人直接个人持股。但到融资的时候，投资人一看您的个人税务居民身份和CRS状态，可能会要求您先做合规调整，否则影响估值。"),
            ("数据冲击", "现在越来越多的投资协议里加入了'税务合规陈述'条款。如果您的个人持股没有提前规划，投资人可能会要求您出具税务合规证明，或者在估值上打折。"),
            ("软性邀约", "我们可以帮您做一个'融资前税务健康检查'，看看现在的股权结构在投资人眼里是什么状态，再设计一个既合规又不影响融资节奏的优化方案。"),
        ],
        "rebuttal": [
            ("我们公司还小，等做大再考虑这些。", "张总，税务架构最大的特点就是'越早做越便宜，越晚做越贵'。公司小的时候，股权结构简单，调整成本低；等公司做大了，股东多了、估值高了，任何股权变动都可能触发巨额的税务成本。很多独角兽的创始人最后悔的就是：早期省了几万块的架构设计费，后期多交了几千万的税。"),
        ],
    },
]

quotes = [
    "CRS不是来抓你的，是来交换数据的。抓你的是内地税务局的大数据比对系统。",
    "您在香港的银行账户，每年5月就像寄明信片一样，自动寄给内地税务局。",
    "现在的问题不是'我有没有事'，而是'我的数据已经在路上了，我准备好了吗？'",
    "BVI壳公司不是保险箱，是玻璃房——银行后台一眼就能看穿里面的主人是谁。",
    "拿到香港身份≠拿到税务豁免，税务局看的是你的'核心利益中心'，不是你的身份证。",
]

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Scenarios
html += '''
<!-- ========== SCENARIOS ========== -->
<section class="section" id="scenarios">
  <div class="section-header reveal">
    <h2>八大客户场景 × 话术模板</h2>
    <div class="gold-line"></div>
    <p>点击展开查看完整话术（含客户反驳及应对）</p>
  </div>

  <div class="scenario-list reveal">
'''

for s in scenarios:
    html += f'''    <div class="scenario-card">
      <div class="scenario-header" onclick="toggleScenario(this)">
        <span class="scenario-num">{s['num']}</span>
        <span class="scenario-title">{s['title']}</span>
        <span class="scenario-tag">{s['tag']}</span>
        <span class="scenario-arrow">▼</span>
      </div>
      <div class="scenario-body">
        <div class="scenario-inner">
          <p style="font-size:0.82rem;color:#555;margin-bottom:14px;line-height:1.7;"><strong style="color:var(--charcoal);">客户画像：</strong>{s['profile']}</p>
          <p style="font-size:0.82rem;color:#555;margin-bottom:16px;line-height:1.7;"><strong style="color:var(--charcoal);">触发信号：</strong>{s['trigger']}</p>

          <div class="script-box">
'''
    for step, text in s['script']:
        html += f'            <div class="script-step"><strong>{step}：</strong>{text}</div>\n'
    html += '''          </div>

'''
    for client, reply in s['rebuttal']:
        html += f'''          <div class="rebuttal-box">
            <div class="client">❌ 客户说：「{client}」</div>
            <div class="reply">✅ 应对：{reply}</div>
          </div>
'''
    html += '''        </div>
      </div>
    </div>
'''

html += '''  </div>
</section>
'''

# Quotes
html += '''
<!-- ========== QUOTES ========== -->
<section class="section" id="quotes">
  <div class="section-header reveal">
    <h2>五个 "aha moment" 金句</h2>
    <div class="gold-line"></div>
    <p>可在任何场景中插入，让客户瞬间意识到问题的严重性</p>
  </div>

  <div class="quotes-grid reveal">
'''

for i, q in enumerate(quotes, 1):
    html += f'''    <div class="quote-card">
      <span class="quote-num">0{i}</span>
      <p style="padding-left:16px;">{q}</p>
    </div>
'''

html += '''  </div>
</section>
'''

# Checklist
html += '''
<!-- ========== CHECKLIST ========== -->
<section class="section" id="checklist">
  <div class="section-header reveal">
    <h2>合作方行动清单</h2>
    <div class="gold-line"></div>
    <p>见客户前的自检表 · 可截图打印</p>
  </div>

  <div class="checklist-card reveal">
    <div class="checklist-title">CRS 合作方 · 见客户前自检清单</div>
    <div class="checklist-item">
      <div class="checklist-box"></div>
      <div>知道客户的税务居民身份<br><small style="color:var(--gray);">内地 / 香港 / 双重 / 多重</small></div>
    </div>
    <div class="checklist-item">
      <div class="checklist-box"></div>
      <div>了解客户是否有海外公司或境外资产<br><small style="color:var(--gray);">BVI / 香港物业 / 离岸账户 / 海外上市架构</small></div>
    </div>
    <div class="checklist-item">
      <div class="checklist-box"></div>
      <div>准备了一个「数据冲击点」<br><small style="color:var(--gray);">如：去年香港向内地交换了多少条账户信息</small></div>
    </div>
    <div class="checklist-item">
      <div class="checklist-box"></div>
      <div>设计了一个「软性邀约」结尾<br><small style="color:var(--gray);">免费体检 / 初步诊断 / 风险评估</small></div>
    </div>
    <div class="checklist-item">
      <div class="checklist-box"></div>
      <div>记住：不要卖方案，卖的是<br><small style="color:var(--gray);">「让客户意识到自己有问题」</small></div>
    </div>
    <div class="checklist-summary">
      打印提示：按 Ctrl+P（或 Cmd+P）即可打印本页 · 行动清单区块已优化打印样式
    </div>
  </div>
</section>
'''

# Footer
html += '''
<!-- ========== FOOTER ========== -->
<footer>
  本资料仅供专业研究参考，不构成正式税务或法律意见 | 重要决策请核实原始法规<br>
  具体个案应咨询持牌税务师、律师及法律顾问 | 任何架构调整均需以合法合规为前提
</footer>

<script>
  // Scroll reveal
  const reveals = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('visible'); });
  }, { threshold: 0.1 });
  reveals.forEach(el => observer.observe(el));

  // Scenario accordion
  function toggleScenario(header) {
    const card = header.parentElement;
    card.classList.toggle('open');
  }

  // Quiz logic
  let currentStep = 0;
  const totalSteps = 5;
  let answers = [];
  const scenarioNames = ["已有离岸公司", "香港物业持有者", "刚拿香港身份", "跨境电商老板", "准备二代接班", "海外上市/融资", "中西部内企老板", "初创公司老板"];

  function updateProgress() {
    const pct = ((currentStep) / totalSteps) * 100;
    document.getElementById('quizProgress').style.width = pct + '%';
  }

  function showStep(n) {
    document.querySelectorAll('.quiz-step').forEach(s => s.classList.remove('active'));
    const steps = document.querySelectorAll('.quiz-step');
    if (steps[n]) steps[n].classList.add('active');
    currentStep = n;
    updateProgress();
  }

  function calcResult() {
    let weights = [0,0,0,0,0,0,0,0];
    answers.forEach(a => {
      const w = a.weights.split(',').map(Number);
      w.forEach((v, i) => weights[i] += v);
    });
    const maxIdx = weights.indexOf(Math.max(...weights));
    const total = weights.reduce((a,b)=>a+b,0);
    let level, badgeClass, title, desc, timing;
    if (total <= 4) {
      level = '低风险'; badgeClass = 'result-low'; title = '🟢 低风险客户';
      desc = '客户目前CRS暴露面较小，但建议提前了解规则，为未来的跨境需求做好准备。';
      timing = '建议在本季度末前进行一次初步沟通，建立信任关系。';
    } else if (total <= 8) {
      level = '中风险'; badgeClass = 'result-mid'; title = '🔵 中风险客户';
      desc = '客户已有一定的CRS暴露面，需要关注其资金流动和税务身份状态。';
      timing = '建议在1个月内安排初步诊断，帮助客户认识潜在风险。';
    } else if (total <= 12) {
      level = '高风险'; badgeClass = 'result-high'; title = '🟠 高风险客户';
      desc = '客户的CRS暴露面显著，存在被大数据比对命中的可能，需尽快启动合规评估。';
      timing = '建议立即安排见面沟通，时间窗口有限。';
    } else {
      level = '极高风险'; badgeClass = 'result-veryhigh'; title = '🔴 极高风险客户';
      desc = '客户处于CRS穿透的核心区域，数据交换风险极高，需紧急启动合规架构设计。';
      timing = '建议本周内安排紧急会面，客户的合规窗口正在关闭。';
    }

    document.getElementById('resultBadge').textContent = level;
    document.getElementById('resultBadge').className = 'result-badge ' + badgeClass;
    document.getElementById('resultTitle').textContent = title;
    document.getElementById('resultDesc').textContent = desc;
    document.getElementById('resultRec').innerHTML =
      '<strong>推荐话术场景：</strong>场景 ' + String(maxIdx+1).padStart(2,'0') + ' · ' + scenarioNames[maxIdx] + '<br>' +
      '<strong>介入时机：</strong>' + timing;
    document.getElementById('quizResult').classList.add('active');
  }

  function resetQuiz() {
    answers = [];
    currentStep = 0;
    document.querySelectorAll('.quiz-option').forEach(btn => btn.classList.remove('selected'));
    document.getElementById('quizResult').classList.remove('active');
    showStep(0);
    document.querySelectorAll('.quiz-step').forEach(s => {
      const next = s.querySelector('.btn-primary');
      if (next) next.disabled = true;
    });
  }

  document.querySelectorAll('.quiz-step').forEach((step, stepIdx) => {
    const options = step.querySelectorAll('.quiz-option');
    const nextBtn = step.querySelector('.btn-primary');
    const prevBtn = step.querySelector('.btn-ghost');

    options.forEach(btn => {
      btn.addEventListener('click', () => {
        options.forEach(b => b.classList.remove('selected'));
        btn.classList.add('selected');
        answers[stepIdx] = { value: btn.dataset.value, weights: btn.dataset.weights };
        if (nextBtn) nextBtn.disabled = false;
      });
    });

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (stepIdx < totalSteps - 1) {
          showStep(stepIdx + 1);
        } else {
          document.querySelectorAll('.quiz-step').forEach(s => s.classList.remove('active'));
          document.querySelector('.progress-bar').style.display = 'none';
          calcResult();
        }
      });
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        if (stepIdx > 0) showStep(stepIdx - 1);
      });
    }
  });

  updateProgress();
</script>

</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done. index.html generated successfully.")
