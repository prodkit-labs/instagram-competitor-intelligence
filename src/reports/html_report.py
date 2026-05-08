import html
import re


def _split_table_row(line):
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _is_table_divider(line):
    cells = _split_table_row(line)
    return all(re.match(r"^:?-{3,}:?$", cell) for cell in cells)


def _render_table(lines):
    header = _split_table_row(lines[0])
    body = [_split_table_row(line) for line in lines[2:]]
    cells = "".join(f"<th>{html.escape(cell)}</th>" for cell in header)
    rows = [f"<thead><tr>{cells}</tr></thead>", "<tbody>"]
    for row in body:
        row_cells = "".join(f"<td>{html.escape(cell)}</td>" for cell in row)
        rows.append(f"<tr>{row_cells}</tr>")
    rows.append("</tbody>")
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def markdown_to_simple_html(markdown):
    rows = []
    in_list = False
    table_lines = []

    def flush_table():
        nonlocal table_lines
        if table_lines:
            if len(table_lines) >= 2 and _is_table_divider(table_lines[1]):
                rows.append(_render_table(table_lines))
            else:
                for table_line in table_lines:
                    rows.append(f"<p>{html.escape(table_line)}</p>")
            table_lines = []

    for line in markdown.splitlines():
        if line.startswith("|"):
            if in_list:
                rows.append("</ul>")
                in_list = False
            table_lines.append(line)
            continue

        flush_table()

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
        elif re.match(r"^\d+\. ", line):
            rows.append(f"<p>{html.escape(line)}</p>")
        elif not line.strip():
            if in_list:
                rows.append("</ul>")
                in_list = False
        else:
            rows.append(f"<p>{html.escape(line)}</p>")
    flush_table()
    if in_list:
        rows.append("</ul>")

    return """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Instagram Competitor Report</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; line-height: 1.55; max-width: 1080px; margin: 40px auto; padding: 0 20px; color: #17202a; }
    h1 { font-size: 34px; margin-bottom: 8px; }
    h2 { margin-top: 32px; border-bottom: 1px solid #e5e7eb; padding-bottom: 6px; }
    table { border-collapse: collapse; width: 100%; margin: 14px 0 24px; font-size: 14px; }
    th, td { border: 1px solid #e5e7eb; padding: 9px 10px; text-align: left; vertical-align: top; }
    th { background: #f8fafc; font-weight: 650; }
    tr:nth-child(even) td { background: #fbfdff; }
    td:nth-child(2), td:nth-child(4), td:nth-child(5), td:nth-child(6) { white-space: nowrap; }
    code { background: #f1f5f9; padding: 2px 4px; border-radius: 4px; }
  </style>
</head>
<body>
""" + "\n".join(rows) + "\n</body>\n</html>\n"
