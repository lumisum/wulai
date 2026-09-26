#!/usr/bin/env python3
"""Export published articles as inline-styled WeChat Markdown and HTML."""

from __future__ import annotations

import html
import re
from pathlib import Path
from urllib.parse import urljoin


ROOT = Path(__file__).resolve().parents[1]
SITE_BASE = "https://lumisum.github.io/wulai/"

PARAGRAPH_STYLE = (
    "margin:0 0 20px;color:#354039;font-size:15px;line-height:1.95;"
    "letter-spacing:0.25px;"
)
HEADING_STYLE = (
    "margin:34px 0 18px;padding-left:12px;border-left:3px solid #AB8966;"
    "color:#18372F;font-size:18px;font-weight:700;line-height:1.65;"
)
SUBHEADING_STYLE = (
    "margin:26px 0 14px;color:#365344;font-size:16px;font-weight:700;"
    "line-height:1.6;"
)
QUOTE_STYLE = (
    "margin:24px 0;padding:15px 17px;border-left:3px solid #AB8966;"
    "background-color:#F5F5EF;color:#365344;font-size:15px;line-height:1.9;"
)
STRONG_STYLE = "color:#315B49;font-weight:700;"
HIGHLIGHT_STYLE = (
    "color:#315B49;background-color:#EFF2EA;font-weight:700;padding:1px 3px;"
)
LINK_STYLE = "color:#315B49;text-decoration:underline;"
IMAGE_STYLE = "display:block;width:100%;max-width:100%;height:auto;margin:0 auto;"
KICKER_STYLE = (
    "margin:2px 0 12px;color:#8C724C;font-size:12px;line-height:1.5;"
    "letter-spacing:2px;text-align:center;"
)
TITLE_STYLE = (
    "margin:0 auto 12px;color:#18372F;font-size:24px;font-weight:700;"
    "line-height:1.5;text-align:center;letter-spacing:0.4px;"
)
SUMMARY_STYLE = (
    "margin:0 auto 8px;color:#68736A;font-size:14px;line-height:1.8;"
    "text-align:center;"
)
DIVIDER_URL = urljoin(SITE_BASE, "assets/wulai-wechat-divider.png")

HIGHLIGHTS = {
    "2026-09-24-fuxue-yu-qingshang": [
        "情商最难的地方也许不在技巧，而在心。",
        "慈悲不是替别人找借口，更不是取消边界，而是在行为之外，再多看见一点。",
        "不让自己成为情绪传递链条里的中转站。",
        "情商发生在人与人之间；而它的根，也许一直长在自己的心里。",
    ],
    "2026-09-24-rulai-heyi-cheng-fozu": [
        "让原本混沌的东西变得可见。",
        "这就是“定义”的力量。",
        "定义世界本身也可以是一种修行。",
        "先靠定义看清，再靠无住，不被定义困死。",
    ],
    "2026-09-24-musk-de-yuanli": [
        "愿力不是让你更用力，而是让你的力能够持续聚焦。",
        "愿在上，行在下。",
        "执行力决定一支箭能够射多远，愿力决定千万支箭最终射向哪里。",
        "愿力不是让人更拼命。它是让一个人的力，开始形成合力。",
    ],
    "2026-09-25-ruguo-fotuo-kanjian-pi": [
        "确定和自性不是一回事。",
        "有效，不等于有自性；确定，也不等于有自性。",
        "关系中的绝对确定，和脱离关系的独立自性，并不是一回事。",
        "不要把已经得到的答案，变成最后一个不能再追问的答案。",
    ],
    "2026-09-26-fotuo-jiaoyu-luohouluo": [
        "他没有让儿子永远依赖一个正确的父亲，而是在训练儿子成为能够自己判断的人。",
        "善意里有没有悄悄混进控制。",
        "我是在帮助孩子形成自己的判断，还是努力让他成为我认为正确的样子？",
        "这两件事，也许就是教育和控制之间最重要的分界线。",
    ],
}

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n(.*)\Z", re.S)
FIELD_RE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*?)\s*$")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
TOKEN_RE = re.compile(
    r"==(.+?)==|\*\*(.+?)\*\*|\*(.+?)\*|`([^`]+)`|\[([^\]]+)\]\(([^)]+)\)"
)


def parse_frontmatter(source: str) -> tuple[dict[str, str], str]:
    match = FRONTMATTER_RE.match(source)
    if not match:
        raise ValueError("article.md is missing YAML frontmatter")

    metadata: dict[str, str] = {}
    for line in match.group(1).splitlines():
        field = FIELD_RE.match(line)
        if not field:
            continue
        value = field.group(2)
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        metadata[field.group(1)] = value.replace('\\"', '"')
    return metadata, match.group(2).strip()


def mark_highlights(text: str, phrases: list[str]) -> str:
    for phrase in sorted(phrases, key=len, reverse=True):
        bold_phrase = f"**{phrase}**"
        if bold_phrase in text:
            text = text.replace(bold_phrase, f"=={phrase}==", 1)
        elif phrase in text:
            text = text.replace(phrase, f"=={phrase}==", 1)
    return text


def render_inline(text: str) -> str:
    parts: list[str] = []
    cursor = 0
    for match in TOKEN_RE.finditer(text):
        parts.append(html.escape(text[cursor : match.start()], quote=False))
        highlighted, strong, emphasis, code, link_text, link_url = match.groups()
        if highlighted is not None:
            parts.append(
                f'<strong style="{HIGHLIGHT_STYLE}">{html.escape(highlighted, quote=False)}</strong>'
            )
        elif strong is not None:
            parts.append(
                f'<strong style="{STRONG_STYLE}">{html.escape(strong, quote=False)}</strong>'
            )
        elif emphasis is not None:
            parts.append(f"<em>{html.escape(emphasis, quote=False)}</em>")
        elif code is not None:
            parts.append(
                f'<span style="color:#5D685F;background-color:#F3F2EC;">'
                f"{html.escape(code, quote=False)}</span>"
            )
        else:
            safe_url = html.escape(link_url, quote=True)
            parts.append(
                f'<a href="{safe_url}" style="{LINK_STYLE}">'
                f"{html.escape(link_text, quote=False)}</a>"
            )
        cursor = match.end()
    parts.append(html.escape(text[cursor:], quote=False))
    return "".join(parts)


def render_image(block: str, image_base_url: str) -> str | None:
    match = IMAGE_RE.fullmatch(block.strip())
    if not match:
        return None
    alt, source = match.groups()
    image_url = urljoin(image_base_url, source)
    return (
        f'<p style="margin:26px 0;">'
        f'<img src="{html.escape(image_url, quote=True)}" '
        f'alt="{html.escape(alt, quote=True)}" style="{IMAGE_STYLE}">'
        "</p>"
    )


def render_divider() -> str:
    return (
        '<p style="margin:14px auto 24px;text-align:center;line-height:0;">'
        f'<img src="{html.escape(DIVIDER_URL, quote=True)}" alt="" '
        'style="display:block;width:100%;max-width:100%;height:auto;margin:0 auto;">'
        "</p>"
    )


def render_article_header(title: str, summary: str, cover: str) -> str:
    cover_url = urljoin(SITE_BASE, cover.lstrip("/"))
    blocks = [
        '<p style="margin:0 0 24px;line-height:0;">'
        f'<img src="{html.escape(cover_url, quote=True)}" alt="{html.escape(title, quote=True)}" '
        'style="display:block;width:100%;max-width:100%;height:auto;margin:0 auto;">'
        "</p>",
        '<div style="padding:0 24px 8px;">',
        f'<p style="{KICKER_STYLE}">无来 · 修学随笔</p>',
        f'<p style="{TITLE_STYLE}">{html.escape(title, quote=False)}</p>',
    ]
    if summary:
        blocks.append(f'<p style="{SUMMARY_STYLE}">{html.escape(summary, quote=False)}</p>')
    blocks.append(render_divider())
    return "\n".join(blocks)


def render_article_end() -> str:
    return (
        render_divider()
        + '<p style="margin:0 0 8px;color:#365344;font-size:14px;line-height:1.8;'
        'text-align:center;">愿把所思所学，带回眼前的生活。</p>'
        '<p style="margin:0;color:#AB8966;font-size:12px;letter-spacing:2px;'
        'text-align:center;">无来 · 修学随笔</p></div>'
    )


def render_body(markdown: str, image_base_url: str, highlights: list[str]) -> str:
    blocks: list[str] = []
    for raw_block in re.split(r"\n\s*\n", markdown.strip()):
        block = raw_block.strip()
        if not block:
            continue
        image = render_image(block, image_base_url)
        if image:
            blocks.append(image)
            continue

        heading = re.match(r"^(#{1,3})\s+(.+)$", block)
        if heading:
            label = heading.group(2).strip()
            if label in {"正文", "结尾"}:
                continue
            style = HEADING_STYLE if len(heading.group(1)) == 1 or len(heading.group(1)) == 2 else SUBHEADING_STYLE
            blocks.append(
                f'<p style="{style}"><span style="color:#AB8966;font-size:12px;">◦</span> '
                f'{render_inline(label)}</p>'
            )
            continue

        if block.startswith("- ") or block.startswith("* "):
            items = [line[2:].strip() for line in block.splitlines() if line.startswith(("- ", "* "))]
            rendered_items = "".join(
                f'<li style="{PARAGRAPH_STYLE}">{render_inline(item)}</li>' for item in items
            )
            blocks.append(
                f'<ul style="margin:0 0 20px;padding-left:1.4em;color:#354039;">{rendered_items}</ul>'
            )
            continue

        if re.match(r"^\d+[.)]\s+", block):
            items = [re.sub(r"^\d+[.)]\s+", "", line.strip()) for line in block.splitlines() if re.match(r"^\d+[.)]\s+", line.strip())]
            rendered_items = "".join(
                f'<li style="{PARAGRAPH_STYLE}">{render_inline(item)}</li>' for item in items
            )
            blocks.append(
                f'<ol style="margin:0 0 20px;padding-left:1.4em;color:#354039;">{rendered_items}</ol>'
            )
            continue

        if block.startswith("> ") or block == ">":
            quoted = " ".join(re.sub(r"^>\s?", "", line.strip()) for line in block.splitlines())
            quoted = mark_highlights(quoted, highlights)
            blocks.append(f'<p style="{QUOTE_STYLE}">{render_inline(quoted)}</p>')
            continue

        text = " ".join(line.strip() for line in block.splitlines())
        text = mark_highlights(text, highlights)
        blocks.append(f'<p style="{PARAGRAPH_STYLE}">{render_inline(text)}</p>')
    return "\n".join(blocks)


def make_markdown_export(title: str, summary: str, markup: str) -> str:
    return (
        "<!--\n"
        "无来微信公众号图文排版稿。封面已置于正文开头；公众号标题和摘要字段可另行填写。\n"
        f"标题：{title}\n"
        f"摘要：{summary}\n"
        "正文图片和装饰图为网站公开链接；粘贴后请检查图片，必要时在公众号后台重新上传。\n"
        "-->\n\n"
        f"{markup}\n"
    )


def make_html_export(title: str, markup: str) -> str:
    return "\n".join(
        [
            "<!doctype html>",
            '<html lang="zh-CN">',
            "<head>",
            '  <meta charset="utf-8">',
            '  <meta name="viewport" content="width=device-width, initial-scale=1">',
            f"  <title>{html.escape(title)}</title>",
            "</head>",
            '<body style="margin:0;background-color:#F4F4EE;">',
            '  <div style="max-width:677px;margin:0 auto;padding:0 0 36px;background-color:#FFFFFF;">',
            f"{markup}",
            "  </div>",
            "</body>",
            "</html>",
            "",
        ]
    )


def write_article_index(article_paths: list[Path]) -> None:
    records = []
    for article_path in article_paths:
        metadata, _ = parse_frontmatter(article_path.read_text(encoding="utf-8"))
        if metadata.get("status") != "published":
            continue
        slug = article_path.parent.name
        records.append((metadata.get("date", ""), metadata.get("title", slug), slug))
    records.sort(reverse=True)
    rows = [
        "# 文章与公众号导入稿",
        "",
        "按发布时间排列。每篇文章各有一个目录，内含原文、配图和可复制的 HTML 稿。",
        "",
        "| 日期 | 文章 | 原文 Markdown | 公众号 HTML | 排版 Markdown |",
        "| --- | --- | --- | --- | --- |",
    ]
    for date, title, slug in records:
        day = date[:10] if date else "—"
        safe_title = title.replace("|", "\\|")
        rows.append(
            f"| {day} | {safe_title} | [{slug}/article.md]({slug}/article.md) "
            f"| [{slug}/wechat.html]({slug}/wechat.html) "
            f"| [{slug}/wechat.md]({slug}/wechat.md) |"
        )
    (ROOT / "articles" / "README.md").write_text("\n".join(rows) + "\n", encoding="utf-8")


def export_article(source_path: Path) -> bool:
    metadata, body = parse_frontmatter(source_path.read_text(encoding="utf-8"))
    if metadata.get("status") != "published":
        return False
    title = metadata.get("title", "无来修学随笔")
    summary = metadata.get("summary", "")
    cover = metadata.get("cover", "")
    highlights = HIGHLIGHTS.get(source_path.parent.name, [])
    relative_article_dir = source_path.parent.relative_to(ROOT).as_posix()
    image_base_url = urljoin(SITE_BASE, f"{relative_article_dir}/images/")
    markup = "\n".join(
        part for part in [
            render_article_header(title, summary, cover),
            render_body(body, image_base_url, highlights),
            render_article_end(),
        ] if part
    )
    (source_path.parent / "wechat.md").write_text(
        make_markdown_export(title, summary, markup), encoding="utf-8"
    )
    (source_path.parent / "wechat.html").write_text(
        make_html_export(title, markup), encoding="utf-8"
    )
    return True


def main() -> None:
    articles = sorted((ROOT / "articles").glob("*/article.md"))
    exported = sum(export_article(article) for article in articles)
    write_article_index(articles)
    print(f"Generated WeChat imports for {exported} published articles.")


if __name__ == "__main__":
    main()
