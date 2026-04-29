import os
import markdown_it

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{
            background: #ffffff;
            color: #000000;
            font-family: 'Courier New', Courier, monospace;
            font-size: 14px;
            margin: 0;
            padding: 20px;
        }}
        
        .nav {{
            background: #cccccc;
            border: 1px solid #000000;
            padding: 8px;
            margin-bottom: 20px;
        }}
        
        .nav a {{
            color: #0000ff;
            text-decoration: none;
            margin-right: 20px;
            font-weight: bold;
        }}
        
        .nav a:hover {{ text-decoration: underline; }}
        
        .content {{
            border: 1px solid #000000;
            padding: 20px;
            background: #ffffff;
            max-width: 900px;
            margin: 0 auto;
        }}

        a {{ color: #0000ff; }}
        
        h1 {{ font-size: 18px; }}
        h2 {{ font-size: 16px; border-bottom: 1px solid #000; padding-bottom: 5px; }}
        
        .footer {{
            margin-top: 20px;
            font-size: 11px;
            text-align: center;
            border-top: 1px solid #cccccc;
            padding-top: 10px;
            max-width: 900px;
            margin: 20px auto 0;
        }}
    </style>
</head>
<body>

<div class="nav">
    <a href="index.html">[home]</a>
    <a href="about.html">[about]</a>
    <a href="posts.html">[blog posts]</a>
    <a href="projects.html">[projects]</a>
    <a href="links.html">[things i like]</a>
</div>

<div class="content">
{content}
</div>

<div class="footer">&copy; 2024</div>

</body>
</html>"""


BLOG_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Blog Posts</title>
    <style>
        body {{
            background: #ffffff;
            color: #000000;
            font-family: 'Courier New', Courier, monospace;
            font-size: 14px;
            margin: 0;
            padding: 20px;
        }}
        
        .nav {{
            background: #cccccc;
            border: 1px solid #000000;
            padding: 8px;
            margin-bottom: 20px;
        }}
        
        .nav a {{
            color: #0000ff;
            text-decoration: none;
            margin-right: 20px;
            font-weight: bold;
        }}
        
        .nav a:hover {{ text-decoration: underline; }}
        
        .content {{
            border: 1px solid #000000;
            padding: 20px;
            background: #ffffff;
            max-width: 900px;
            margin: 0 auto;
        }}

        a {{ color: #0000ff; }}

        .blog-list {{
            margin: 0;
            padding: 0;
            list-style: none;
        }}

        .blog-list li {{
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px dotted #cccccc;
        }}

        .blog-list li:last-child {{ border-bottom: none; }}

        .blog-title {{ font-weight: bold; }}
        .blog-title a {{ color: #0000ff; text-decoration: none; }}
        .blog-title a:hover {{ text-decoration: underline; }}
        .blog-subtitle {{ font-size: 12px; color: #444444; margin-top: 3px; }}
        .blog-date {{ font-size: 11px; color: #666666; margin-top: 2px; }}
        
        .footer {{
            margin-top: 20px;
            font-size: 11px;
            text-align: center;
            border-top: 1px solid #cccccc;
            padding-top: 10px;
            max-width: 900px;
            margin: 20px auto 0;
        }}
    </style>
</head>
<body>

<div class="nav">
    <a href="index.html">[home]</a>
    <a href="about.html">[about]</a>
    <a href="blog.html">[blog posts]</a>
    <a href="projects.html">[projects]</a>
    <a href="links.html">[things i like]</a>
</div>

<div class="content">
    <h1>blog posts</h1>
    <ul class="blog-list">
        {entries}
    </ul>
</div>

<div class="footer">&copy; 2024</div>

</body>
</html>"""


ENTRY_TEMPLATE = """
<li>
    <div class="blog-title"><a href="{filename}">{title}</a></div>
    <div class="blog-subtitle">{subtitle}</div>
    <div class="blog-date">{date}</div>
</li>
"""


def parse_frontmatter(content: str):
    """Returns (metadata_dict, body_without_frontmatter)"""
    if not content.startswith('---'):
        return {}, content

    end = content.find('---', 3)
    if end == -1:
        return {}, content

    frontmatter = content[3:end].strip()
    body = content[end+3:].strip()

    meta = {}
    for line in frontmatter.split('\n'):
        if ':' in line:
            key, _, value = line.partition(':')
            meta[key.strip()] = value.strip()

    return meta, body


def to_md(mdfile: str, path: str, htmlpath: str):
    with open(mdfile + "/" + path, 'r') as f:
        content = f.read()

    meta, body = parse_frontmatter(content)

    md = markdown_it.MarkdownIt()
    rendered = md.render(body)

    title = meta.get('title', body.split('\n')[0].lstrip('#').strip())
    html = TEMPLATE.format(title=title, content=rendered)

    outpath = htmlpath + "/" + path.replace(".md", ".html")
    with open(outpath, 'w') as f:
        f.write(html)

    print(f"built: {outpath}")
    return meta, path.replace(".md", ".html")


mdpath = "post"
htmlpath = "html"

posts = []

for x in os.scandir(mdpath):
    if x.name.endswith(".md"):
        meta, filename = to_md(mdpath, x.name, htmlpath)
        tags = meta.get('tags', '')
        if 'noblog' not in tags:
            posts.append({
                'title': meta.get('title', filename),
                'subtitle': meta.get('subtitle', ''),
                'date': meta.get('date', ''),
                'filename': filename
            })

# sort by date descending
posts.sort(key=lambda p: p['date'], reverse=True)

# generate blog.html
entries = ''.join(ENTRY_TEMPLATE.format(**p) for p in posts)
blog_html = BLOG_TEMPLATE.format(entries=entries)

with open(htmlpath + "/blog.html", 'w') as f:
    f.write(blog_html)

print(f"built: {htmlpath}/blog.html")