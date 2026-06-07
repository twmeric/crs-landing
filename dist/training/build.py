# -*- coding: utf-8 -*-
# Part 1: HTML head + CSS + Hero + Quiz + Principle
part1 = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CRS 合作方销售赋能站</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;600&family=Noto+Sans+SC:wght@300;400;500;600&display=swap" rel="stylesheet">
  <style>
    :root { --hermes-orange: #FF6600; --charcoal: #1A1A1A; --ivory: #F5F0EB; --gold: #C5A059; --gray: #7F7F7F; --border: rgba(26,26,26,0.12); --card-bg: #FAF8F5; }
    * { margin:0; padding:0; box-sizing:border-box; }
    html { scroll-behavior:smooth; }
    body { font-family: "Noto Sans SC", -apple-system, BlinkMacSystemFont, sans-serif; background: var(--ivory); color: var(--charcoal); line-height: 1.8; font-size: 15px; }
    .reveal { opacity:0; transform:translateY(30px); transition:all 0.8s cubic-bezier(0.22,1,0.36,1); }
    .reveal.visible { opacity:1; transform:translateY(0); }
    .section { max-width: 1000px; margin: 0 auto; padding: 70px 5%; }
    .section-header { text-align: center; margin-bottom: 48px; }
    .section-header h2 { font-family: "Noto Serif SC", serif; font-size: clamp(1.3rem, 2.5vw, 1.7rem); font-weight: 400; letter-spacing: 0.1em; margin-bottom: 12px; }
    .section-header p { font-size: 0.85rem; color: var(--gray); max-width: 520px; margin: 0 auto; }
    .gold-line { width: 36px; height: 1px; background: var(--gold); margin: 16px auto; }

    .hero { min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 80px 5%; position: relative; }
    .hero-tag { font-size: 0.7rem; font-weight: 600; letter-spacing: 0.15em; text-transform: uppercase; color: var(--hermes-orange); margin-bottom: 20px; }
    .hero h1 { font-family: "Noto Serif SC", serif; font-size: clamp(1.8rem, 4vw, 2.8rem); font-weight: 300; letter-spacing: 0.12em; line-height: 1.3; margin-bottom: 16px; }
    .hero p { font-size: 0.95rem; color: var(--gray); max-width: 520px; margin-bottom: 40px; }

    .data-flow { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; justify-content: center; font-size: 0.82rem; margin: 30px 0; max-width: 800px; }
    .flow-node { background: var(--charcoal); color: var(--ivory); padding: 10px 18px; border-radius: 6px; font-weight: 500; white-space: nowrap; }
    .flow-pipe { color: var(--gold); font-size: 1.1rem; letter-spacing: 0.05em; }
    .flow-highlight { color: var(--hermes-orange); font-size: 0.75rem; margin-top: 8px; width: 100%; }

    .quiz-wrap { background: #fff; border: 1px solid var(--border); border-radius: 12px; padding: 36px 32px; max-width: 720px; margin: 0 auto; }
    .quiz-step { display: none; animation: fadeIn 0.4s ease; }
    .quiz-step.active { display: block; }
    @keyframes fadeIn { from { opacity:0; transform:translateY(10px);} to { opacity:1; transform:translateY(0);} }
    .quiz-q { font-family: "Noto Serif SC", serif; font-size: 1.05rem; font-weight: 400; margin-bottom: 18px; letter-spacing: 0.04em; }
    .quiz-q-num { display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; background: var(--charcoal); color: var(--ivory); font-size: 0.75rem; font-weight: 600; margin-right: 10px; font-family: "Noto Sans SC", sans-serif; }
    .quiz-option { display: block; padding: 12px 16px; margin-bottom: 10px; border: 1px solid var(--border); border-radius: 8px; cursor: pointer; font-size: 0.88rem; transition: all 0.25s; background: transparent; color: inherit; text-align: left; width: 100%; }
    .quiz-option:hover { border-color: var(--hermes-orange); background: rgba(255,102,0,0.03); }
    .quiz-option.selected { border-color: var(--hermes-orange); background: rgba(255,102,0,0.06); }
    .quiz-nav { display: flex; justify-content: space-between; margin-top: 24px; }
    .btn { padding: 10px 24px; border-radius: 4px; font-size: 0.82rem; font-weight: 500; letter-spacing: 0.06em; cursor: pointer; border: none; transition: all 0.3s; }
    .btn-primary { background: var(--charcoal); color: var(--ivory); }
    .btn-primary:hover { background: var(--hermes-orange); }
    .btn-ghost { background: transparent; color: var(--charcoal); border: 1px solid var(--border); }
    .btn-ghost:hover { border-color: var(--hermes-orange); color: var(--hermes-orange); }
    .btn:disabled { opacity: 0.4; cursor: not-allowed; }
    .quiz-result { display: none; text-align: center; animation: fadeIn 0.5s ease; }
    .quiz-result.active { display: block; }
    .result-badge { display: inline-block; padding: 8px 24px; border-radius: 4px; font-size: 0.9rem; font-weight: 600; letter-spacing: 0.08em; margin-bottom: 16px; }
    .result-low { background: #E8F5E9; color: #2D6A4F; }
    .result-mid { background: #E3F2FD; color: #1565C0; }
    .result-high { background: #FFF3E0; color: #E65100; }
    .result-veryhigh { background: #FBE9E7; color: #B8401E; }
    .result-rec { background: var(--card-bg); border-left: 3px solid var(--gold); padding: 16px 20px; text-align: left; margin-top: 20px; font-size: 0.88rem; line-height: 1.8; }
    .progress-bar { height: 3px; background: var(--border); border-radius: 2px; margin-bottom: 24px; overflow: hidden; }
    .progress-fill { height: 100%; background: var(--hermes-orange); transition: width 0.4s ease; width: 0%; }

    .compare-table { width: 100%; border-collapse: collapse; font-size: 0.88rem; margin: 20px 0; }
    .compare-table th { text-align: left; padding: 12px; font-weight: 600; font-size: 0.78rem; letter-spacing: 0.06em; text-transform: uppercase; color: var(--gray); border-bottom: 2px solid var(--charcoal); background: transparent; }
    .compare-table td { padding: 14px 12px; border-bottom: 1px solid var(--border); vertical-align: top; }
    .compare-table td:first-child { font-weight: 500; color: var(--charcoal); width: 20%; }

    .scenario-list { display: flex; flex-direction: column; gap: 20px; }
    .scenario-card { background: #fff; border: 1px solid var(--border); border-radius: 10px; overflow: hidden; transition: all 0.4s; }
    .scenario-card:hover { box-shadow: 0 16px 40px rgba(26,26,26,0.06); border-color: var(--hermes-orange); }
    .scenario-header { padding: 20px 24px; display: flex; align-items: center; gap: 14px; cursor: pointer; background: var(--card-bg); border-bottom: 1px solid var(--border); }
    .scenario-num { font-family: "Noto Serif SC", serif; font-size: 1.6rem; font-weight: 300; color: var(--gold); line-height: 1; min-width: 36px; }
    .scenario-title { font-family: "Noto Serif SC", serif; font-size: 1.05rem; font-weight: 400; letter-spacing: 0.04em; flex: 1; }
    .scenario-tag { font-size: 0.65rem; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; padding: 3px 10px; border-radius: 4px; background: var(--ivory); color: var(--gray); white-space: nowrap; }
    .scenario-body { max-height: 0; overflow: hidden; transition: max-height 0.5s cubic-bezier(0.22,1,0.36,1); }
    .scenario-card.open .scenario-body { max-height: 1200px; }
    .scenario-arrow { font-size: 0.8rem; color: var(--gray); transition: transform 0.3s; }
    .scenario-card.open .scenario-arrow { transform: rotate(180deg); }
    .scenario-inner { padding: 24px; }
    .script-box { background: var(--card-bg); border-left: 3px solid var(--gold); padding: 18px 20px; margin: 14px 0; font-size: 0.88rem; line-height: 1.9; }
    .script-step { margin-bottom: 10px; }
    .script-step strong { color: var(--charcoal); font-weight: 600; }
    .rebuttal-box { background: #FBE9E7; border-left: 3px solid var(--hermes-orange); padding: 14px 18px; margin: 14px 0; font-size: 0.85rem; line-height: 1.8; }
    .rebuttal-box .client { color: #B8401E; font-weight: 500; margin-bottom: 6px; }
    .rebuttal-box .reply { color: #333; }

    .quotes-grid { display: grid; grid-template-columns: 1fr; gap: 16px; }
    .quote-card { background: #fff; border: 1px solid var(--border); border-radius: 8px; padding: 24px 28px; position: relative; font-family: "Noto Serif SC", serif; font-size: 1.05rem; line-height: 1.8; color: var(--charcoal); transition: all 0.3s; }
    .quote-card:hover { border-color: var(--hermes-orange); box-shadow: 0 8px 24px rgba(26,26,26,0.06); }
    .quote-card::before { content: "\\201C"; font-size: 3rem; line-height: 1; color: var(--gold); opacity: 0.3; position: absolute; top: 8px; left: 16px; font-family: Georgia, serif; }
    .quote-num { position: absolute; top: 12px; right: 16px; font-size: 0.7rem; font-weight: 600; color: var(--gold); letter-spacing: 0.1em; font-family: "Noto Sans SC", sans-serif; }

    .checklist-card { max-width: 520px; margin: 0 auto; background: #fff; border: 1px solid var(--border); border-radius: 10px; padding: 32px 28px; box-shadow: 0 12px 30px rgba(26,26,26,0.06); }
    .checklist-title { font-family: "Noto Serif SC", serif; font-size: 1.15rem; font-weight: 400; letter-spacing: 0.08em; text-align: center; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid var(--border); }
    .checklist-item { display: flex; align-items: flex-start; gap: 12px; padding: 10px 0; font-size: 0.88rem; line-height: 1.7; border-bottom: 1px dashed var(--border); }
    .checklist-item:last-child { border-bottom: none; }
    .checklist-box { width: 18px; height: 18px; border: 2px solid var(--charcoal); border-radius: 3px; flex-shrink: 0; margin-top: 3px; }
    .checklist-summary { text-align: center; margin-top: 20px; padding-top: 16px; border-top: 1px solid var(--border); font-size: 0.82rem; color: var(--gray); font-style: italic; }

    footer { text-align: center; padding: 30px 5%; font-size: 0.72rem; color: var(--gray); letter-spacing: 0.05em; border-top: 1px solid var(--border); }

    @media (max-width: 768px) {
      .section { padding: 48px 5%; }
      .hero { min-height: auto; padding: 60px 5% 40px; }
      .hero h1 { font-size: 1.6rem; }
      .data-flow { gap: 6px; font-size: 0.72rem; }
      .flow-node { padding: 8px 12px; }
      .quiz-wrap { padding: 24px 18px; }
      .compare-table { font-size: 0.78rem; }
      .compare-table th, .compare-table td { padding: 10px 8px; }
      .scenario-header { padding: 16px 18px; }
      .scenario-inner { padding: 18px; }
      .script-box, .rebuttal-box { padding: 14px 16px; font-size: 0.85rem; }
      .quote-card { padding: 20px 22px; font-size: 0.95rem; }
      .checklist-card { padding: 24px 20px; }
    }

    @media print {
      .reveal, .reveal.visible { opacity: 1 !important; transform: none !important; transition: none !important; }
      .hero { min-height: auto; padding: 30px 5%; }
      .section { padding: 30px 5%; page-break-inside: avoid; }
      .scenario-body { max-height: none !important; overflow: visible !important; }
      .scenario-card { break-inside: avoid; page-break-inside: avoid; }
      .checklist-card { break-inside: avoid; }
      .quote-card { break-inside: avoid; }
      body { background: #fff !important; }
      .quiz-wrap { display: none; }
      .gold-line { margin: 10px auto; }
    }
  </style>
</head>
<body>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(part1)

print("Part 1 written.")
