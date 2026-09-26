---
layout: article
title: "文章标题"
date: "YYYY-MM-DDTHH:MM:SS+08:00" # 使用发布时间，精确到秒以稳定排列时间线
summary: "公众号摘要"
status: draft
permalink: /articles/YYYY-MM-DD-short-title/
cover: /articles/YYYY-MM-DD-short-title/images/cover.png
cover_alt: "封面画面说明"
---

## 正文

从一个具体的问题、经历或观察开始。

### 小标题

展开个人理解，尽量结合具体生活经验。引用经文或他人观点时注明出处，并区分引用与自己的体会。

## 结尾

回到文章开头的问题，留下简洁的收束或可实践的提醒。

## 配图安排

- 封面：`images/cover.png`（2.35:1 横版）
- 正文图 1：`images/01.png`（3:4 竖版；建议放在……）
- 正文图 2：`images/02.png`（3:4 竖版；建议放在……）
- 正文图 3：`images/03.png`（3:4 竖版；按需使用，建议放在……）
- 在正文中用公开地址插图，例如：`![图片说明](https://lumisum.github.io/wulai/articles/YYYY-MM-DD-short-title/images/01.png)`

## 发布信息

- 微信公众号标题：
- 作者 / 来源署名（如需）：
- 关键词：
- 原文链接（发布后填写）：

## 公众号导入稿

将本文保存为 `articles/YYYY-MM-DD-short-title/article.md`，并把配图放在同目录的 `images/` 下。文章定稿并标记为 `published` 后，运行 `python3 scripts/export_wechat.py`，会在本篇目录生成 `wechat.md`（内联 HTML 的公众号稿）和 `wechat.html`（可预览、可复制版本），并按时间更新 `articles/README.md`。HTML 稿的开头包含 2.35:1 封面，排版遵循 [`guides/wechat-formatting.md`](../guides/wechat-formatting.md)。
