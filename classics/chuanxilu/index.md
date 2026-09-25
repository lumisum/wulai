---
layout: default
title: 传习录
description: 王守仁《传习录》三卷原文与分节白话学习笔记，可切换只读原文或原文对照释义。
permalink: /classics/chuanxilu/
---
<article class="scripture-page" data-mode="parallel">
  <header class="scripture-hero">
    <img src="{{ '/assets/scriptures/chuanxilu-banner.png' | relative_url }}" alt="明代学者王阳明在山间书斋执笔沉思，窗外是青松与晨雾。" fetchpriority="high">
    <div class="scripture-hero-shade" aria-hidden="true"></div>
    <div class="scripture-hero-copy">
      <p class="scripture-kicker">心学 · 知行 · 致良知</p>
      <h1>传习录</h1>
      <p><strong>知行合一 · 致良知</strong></p>
    </div>
    <a class="scripture-hero-back" href="{{ '/classics/' | relative_url }}">‹ 经典目录</a>
  </header>

  <section class="scripture-intro section-shell" aria-labelledby="scripture-intro-title">
    <div>
      <p class="eyebrow">王守仁与门人的问答、书信与记录</p>
      <h2 id="scripture-intro-title">把心学放回提问与行动之中。</h2>
    </div>
    <div class="scripture-intro-copy">
      <p>《传习录》由王守仁的门人记录、整理，包含问答、书信、序跋等，分为上、中、下三卷。知行合一、致良知、格物等概念在具体对话和论辩中展开；按问题与记录分节阅读，更容易看见每段话在回应什么。白话释义是无来的个人读书笔记，不是学术校注。</p>
      <p>原文底本：维基文库《传习录》三卷本，作者王守仁（明）。网页文本依原有卷次和记录标题转换为简体并分段，移除网页脚注标记；改编文本依 CC BY-SA 4.0 分享，请注明来源并以相同方式共享。<a href="https://github.com/lumisum/wulai/blob/main/classics/chuanxilu/SOURCE.md" target="_blank" rel="noopener noreferrer">查看底本、整理方式与许可说明</a> · <a href="https://zh.wikisource.org/wiki/傳習錄" target="_blank" rel="noopener noreferrer">维基文库原作</a></p>
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
    <p id="scripture-error" class="scripture-error" hidden>原文暂时无法载入。你可以先<a href="{{ '/classics/chuanxilu/original.txt' | relative_url }}">打开原文文本</a>继续阅读。</p>
    <div class="scripture-endnote">
      <span aria-hidden="true">☸</span>
      <p>愿所读的智慧，回到每一次真实的选择里。</p>
      <a href="{{ '/' | relative_url }}#classics">回到无来首页</a>
    </div>
  </section>
</article>
<script id="scripture-source-url" type="application/json">{{ '/classics/chuanxilu/original.txt' | relative_url | jsonify }}</script>
<script id="scripture-reader-config" type="application/json">{"sectionUnit":"节"}</script>
<script id="scripture-notes-data" type="application/json">{{ site.data.chuanxilu | jsonify }}</script>
<script src="{{ '/assets/js/scripture-reader.js' | relative_url }}" defer></script>
