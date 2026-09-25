---
layout: default
title: 金刚般若波罗蜜经
description: 《金刚般若波罗蜜经》原文与逐品白话释义，可切换纯原文和对照阅读模式。
permalink: /classics/diamond-sutra/
---
<article class="scripture-page" data-mode="parallel">
  <header class="scripture-hero">
    <img src="{{ '/assets/scriptures/diamond-sutra-banner.png' | relative_url }}" alt="群山与松林在青松绿的薄雾中渐次展开，晨光落在静水上" fetchpriority="high">
    <div class="scripture-hero-shade" aria-hidden="true"></div>
    <div class="scripture-hero-copy">
      <p class="scripture-kicker">经典 · 般若 · 无住</p>
      <h1>金刚般若波罗蜜经</h1>
      <p><strong>应无所住而生其心</strong></p>
    </div>
    <a class="scripture-hero-back" href="{{ '/classics/' | relative_url }}">‹ 经典目录</a>
  </header>

  <section class="scripture-intro section-shell" aria-labelledby="scripture-intro-title">
    <div>
      <p class="eyebrow">一部关于般若与无住的经典</p>
      <h2 id="scripture-intro-title">不抓住答案，仍然认真生活。</h2>
    </div>
    <div class="scripture-intro-copy">
      <p>《金刚经》反复追问：怎样发心、行善、帮助众生，同时不被“我做了什么”“我得到了什么”牢牢困住。它的核心句是<strong>“应无所住而生其心”</strong>。这里所说的“空”不是一切都不存在，“无住”也不是冷漠或放弃，而是在看清变化与因缘之后，依然清醒地行动。</p>
      <p>以下原文依照你提供的《金刚经》文稿整理，保留原稿章节、措辞与标点。白话部分是无来的个人学习笔记，帮助初读时抓住段落脉络，不是权威注疏；不同流传版本可能存在文字差异。需要核对另一种电子底本时，可参阅 <a href="https://dlbs.liberal.ntu.edu.tw/BDLM/sutra/html/T08/T08n0235.htm" target="_blank" rel="noopener noreferrer">CBETA《金刚般若波罗蜜经》（T08 No. 235）</a>。</p>
    </div>
  </section>

  <section class="scripture-reader" aria-label="经文阅读">
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
      <p><strong>读法提示</strong> · 先看原文在说什么，再读白话尝试理解。若某段意思仍不确定，可以先留下问题，回到经文和可靠注疏中继续查证。</p>
    </div>

    <div id="scripture-content" class="scripture-content" aria-live="polite" aria-busy="true">
      <p class="scripture-loading">正在展开经文……</p>
    </div>
    <p id="scripture-error" class="scripture-error" hidden>经文暂时无法载入。你可以先<a href="{{ '/classics/diamond-sutra/original.txt' | relative_url }}">打开原文文本</a>继续阅读。</p>
    <div class="scripture-endnote">
      <span aria-hidden="true">☸</span>
      <p>愿读到的智慧，回到每一次真实的选择里。</p>
      <a href="{{ '/' | relative_url }}#classics">回到无来首页</a>
    </div>
  </section>
</article>

<script id="scripture-source-url" type="application/json">{{ '/classics/diamond-sutra/original.txt' | relative_url | jsonify }}</script>
<script id="scripture-notes-data" type="application/json">{{ site.data.diamond_sutra | jsonify }}</script>
<script src="{{ '/assets/js/scripture-reader.js' | relative_url }}" defer></script>
