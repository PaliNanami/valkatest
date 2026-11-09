import os
import re

print("--- Checking HTML Image Sources ---")
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

srcs = re.findall(r'src=["\'](.*?)["\']', html)
for src in srcs:
    if not src.startswith('http') and not src.startswith('data:'):
        exists = os.path.exists(src)
        print(f"HTML src: {src} -> Exists: {exists}")
        if not exists:
            print(f"WARNING: MISSING {src}")

print("\n--- Checking CSS Image URLs ---")
for css_file in ['css/styles.css', 'css/components.css']:
    with open(css_file, 'r', encoding='utf-8') as f:
        css = f.read()
    urls = re.findall(r'url\([\'"]?(.*?)[\'"]?\)', css)
    for u in urls:
        if not u.startswith('http') and not u.startswith('data:'):
            resolved = os.path.normpath(os.path.join('css', u))
            exists = os.path.exists(resolved)
            print(f"CSS url ({css_file}): {u} -> Resolved {resolved} -> Exists: {exists}")
            if not exists:
                print(f"WARNING: MISSING {resolved}")

print("\n--- Checking DATA.JS Image URLs ---")
with open('js/data.js', 'r', encoding='utf-8') as f:
    data_content = f.read()

data_imgs = re.findall(r'assets/images/[a-zA-Z0-9_\-\./]+', data_content)
for img in set(data_imgs):
    exists = os.path.exists(img)
    print(f"DATA img: {img} -> Exists: {exists}")
    if not exists:
        print(f"WARNING: MISSING {img}")

print("\nAsset Verification Completed Successfully!")
