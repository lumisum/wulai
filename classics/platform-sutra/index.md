---
layout: default
title: 六祖坛经
description: 《六祖坛经》CBETA 十品主文与逐品白话学习笔记，可切换只读原文或对照释义。
permalink: /classics/platform-sutra/
---
<article class="scripture-page" data-mode="parallel">
  <header class="scripture-hero">
    <img src="{{ '/assets/scriptures/platform-sutra-banner.png' | relative_url }}" alt="唐代禅者在松林寺院的木杵旁劳作，晨光从屋檐间落下。" fetchpriority="high">
    <div class="scripture-hero-shade" aria-hidden="true"></div>
    <div class="scripture-hero-copy">
      <p class="scripture-kicker">禅宗 · 般若 · 无住</p>
      <h1>六祖坛经</h1>
      <p><strong>无相 · 无念 · 无住</strong></p>
    </div>
    <a class="scripture-hero-back" href="{{ '/classics/' | relative_url }}">‹ 经典目录</a>
  </header>

  <section class="scripture-intro section-shell" aria-labelledby="scripture-intro-title">
    <div>
      <p class="eyebrow">一部从修行与日用展开的经典</p>
      <h2 id="scripture-intro-title">看见六祖的教法如何落到日常。</h2>
    </div>
    <div class="scripture-intro-copy">
      <p>本页依据《六祖大师法宝坛经》十品主文整理，叙述惠能求法、说法与弟子问答，围绕般若、无相、无念、无住、定慧与修行展开。经文按 CBETA 十品结构呈现，并配以无来的逐品白话学习笔记，帮助初读时抓住脉络。</p>
      <p>经文底本：CBETA《六祖大师法宝坛经》（大正藏 T48 No. 2008，元宗宝编）。本页收录十品主文；卷首序赞和后附碑铭等材料暂不纳入阅读正文。经文从 CBETA XML 提取并转换为简体，原档保留 CBETA 来源与版本头部。CBETA 资料限定非营利用途；此文本按 CC BY-NC-SA 4.0 分享，本页整理文本亦以相同方式分享。不同传本的版本、章节标题与字句可能有异。<a href="{{ '/classics/platform-sutra/source/T48n2008.xml' | relative_url }}">查看本地 CBETA XML 原档</a> · <a href="https://cbeta.org/copyright" target="_blank" rel="noopener noreferrer">CBETA 授权说明</a> · <a href="https://github.com/cbeta-org/xml-p5/blob/master/T/T48/T48n2008.xml" target="_blank" rel="noopener noreferrer">CBETA 在线底本</a></p>
    </div>
  </section>

  <section class="scripture-reader" aria-label="经典原文阅读">
    <div class="scripture-controls">
      <div class="reader-mode" role="group" aria-label="选择阅读模式">
        <button type="button" class="reader-mode-button" data-reader-mode="original" aria-pressed="false">只看原文</button>
        <button type="button" class="reader-mode-button" data-reader-mode="parallel" aria-pressed="true">原文 + 白话释义</button>
      </div>
      <div class="reader-audio-control" data-audio-state="loading" role="group" aria-label="静心背景音乐">
        <audio id="scripture-audio" src="{{ '/assets/audio/wulai-reading.mp3' | relative_url }}" loop preload="none"></audio>
        <button type="button" class="reader-audio-toggle" data-audio-toggle aria-pressed="false" aria-label="播放背景音乐">
          <span aria-hidden="true">♫</span><span data-audio-toggle-label>开启音乐</span>
        </button>
        <label class="reader-audio-volume">
          <span>音量</span>
          <input type="range" data-audio-volume min="0" max="0.25" step="0.01" value="0.08" aria-label="背景音乐音量">
          <output data-audio-volume-value>8%</output>
        </label>
        <span class="reader-audio-status" data-audio-status aria-live="polite">正在尝试自动播放</span>
      </div>
      <div class="reader-tools" aria-label="阅读工具">
        <button type="button" data-font-step="-1" aria-label="缩小字号">A−</button>
        <button type="button" data-font-step="1" aria-label="放大字号">A+</button>
        <button type="button" data-index-toggle aria-expanded="false" aria-controls="scripture-index">章节目录 <span aria-hidden="true">⌄</span></button>
      </div>
    </div>
    <div class="scripture-progress" aria-hidden="true">
      <span id="scripture-chapter-count">正在载入章节</span>
      <span class="scripture-progress-track"><span id="scripture-progress-bar"></span></span>
      <span>静心阅读</span>
    </div>
    <nav id="scripture-index" class="scripture-index-nav" aria-label="章节目录" hidden>
      <ol id="scripture-index-list"></ol>
    </nav>
    <div class="scripture-reading-note" data-parallel-note>
      <span class="reading-note-mark" aria-hidden="true">☸</span>
      <p><strong>读法提示</strong> · 先读原文，再看白话学习笔记如何拆解意思。遇到仍不确定的地方，可以先留下问题，回到经文、原典或可靠注疏继续查证。</p>
    </div>
    <div id="scripture-content" class="scripture-content" aria-live="polite" aria-busy="true">
      <p class="scripture-loading">正在展开原文……</p>
    </div>
    <p id="scripture-error" class="scripture-error" hidden>原文暂时无法载入。你可以先<a href="{{ '/classics/platform-sutra/original.txt' | relative_url }}">打开原文文本</a>继续阅读。</p>
    <div class="scripture-endnote">
      <span aria-hidden="true">☸</span>
      <p>愿所读的智慧，回到每一次真实的选择里。</p>
      <a href="{{ '/' | relative_url }}#classics">回到无来首页</a>
    </div>
  </section>
</article>
<script id="scripture-source-url" type="application/json">{{ '/classics/platform-sutra/original.txt' | relative_url | jsonify }}</script>
<script id="scripture-reader-config" type="application/json">{"sectionUnit":"品"}</script>
<script id="scripture-notes-data" type="application/json">{{ site.data.platform_sutra | jsonify }}</script>
<script src="{{ '/assets/js/scripture-reader.js' | relative_url }}" defer></script>
