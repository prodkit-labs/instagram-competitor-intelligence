import html
import re


def markdown_to_simple_html(markdown):
    rows = []
    in_list = False
    for line in markdown.splitlines():
        if line.startswith("# "):
            rows.append(f"<h1>{html.escape(line[2:])}</h1>")
        elif line.startswith("## "):
            if in_list:
                rows.append("</ul>")
                in_list = False
            rows.append(f"<h2>{html.escape(line[3:])}</h2>")
        elif line.startswith("- "):
            if not in_list:
                rows.append("<ul>")
                in_list = True
            rows.append(f"<li>{html.escape(line[2:])}</li>")
        elif line.startswith("|"):
            if in_list:
                rows.append("</ul>")
                in_list = False
            rows.append(f"<pre>{html.escape(line)}</pre>")
        elif re.match(r"^\d+\. ", line):
            rows.append(f"<p>{html.escape(line)}</p>")
        elif not line.strip():
            if in_list:
                rows.append("</ul>")
                in_list = False
        else:
            rows.append(f"<p>{html.escape(line)}</p>")
    if in_list:
        rows.append("</ul>")

    return """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Instagram Competitor Report</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; line-height: 1.55; max-width: 960px; margin: 40px auto; padding: 0 20px; color: #17202a; }
    h1 { font-size: 34px; margin-bottom: 8px; }
    h2 { margin-top: 32px; border-bottom: 1px solid #e5e7eb; padding-bottom: 6px; }
    pre { background: #f8fafc; padding: 8px 10px; border-radius: 6px; overflow-x: auto; }
    code { background: #f1f5f9; padding: 2px 4px; border-radius: 4px; }
  </style>
</head>
<body>
""" + "\n".join(rows) + "\n</body>\n</html>\n"
