import os

# CONFIGURATION
DATA_DIR = "data"     
OUTPUT_FILE = "index.html"

# TERMINAL UI TEMPLATE
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ROOT | Institutional</title>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        :root {
            /* Institutional Theme (Bloomberg/Hermes) */
            --bg-color: #121212;          
            --sidebar-bg: #1a1a1a;        
            --border-color: #333333;
            --text-main: #e0e0e0;
            --text-muted: #666666;
            --accent-color: #ff9900;      
            --hover-bg: #2a2a2a;
            --font-stack: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            --sidebar-width: 260px;
        }

        body {
            margin: 0; padding: 0; display: flex; height: 100vh; 
            background-color: var(--bg-color); color: var(--text-main); 
            font-family: var(--font-stack); overflow: hidden;
        }

        /* SIDEBAR CONTAINER */
        .sidebar {
            width: var(--sidebar-width);
            background-color: var(--sidebar-bg);
            border-right: 1px solid var(--border-color);
            display: flex; flex-direction: column; flex-shrink: 0;
            transition: width 0.3s cubic-bezier(0.25, 1, 0.5, 1);
            position: relative;
            white-space: nowrap;
            overflow: hidden; 
            z-index: 10;
        }

        /* COLLAPSED STATE (Completely Hidden) */
        .sidebar.collapsed { width: 0; border-right: none; }

        /* Header Area */
        .header {
            padding: 20px; height: 40px; 
            display: flex; align-items: center; justify-content: space-between;
            border-bottom: 1px solid var(--border-color);
        }

        .header-title { 
            font-size: 0.9em; font-weight: 700; color: var(--accent-color); 
            letter-spacing: 1px; text-transform: uppercase;
        }

        /* Navigation List */
        .nav-scroll { 
            flex: 1; overflow-y: auto; padding-bottom: 20px; 
            opacity: 1; transition: opacity 0.2s;
        }
        
        .sidebar.collapsed .nav-scroll, 
        .sidebar.collapsed .header-title { opacity: 0; pointer-events: none; }

        /* Categories */
        .category-label {
            padding: 20px 20px 8px 20px; font-size: 0.7em; font-weight: 600;
            color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px;
        }

        /* Links */
        .nav-link {
            display: block; padding: 8px 20px; text-decoration: none;
            color: var(--text-main); font-size: 0.85em; 
            border-left: 3px solid transparent;
            transition: all 0.2s; cursor: pointer;
        }

        .nav-link:hover { background-color: var(--hover-bg); color: #fff; }
        
        .nav-link.active {
            background-color: var(--hover-bg); 
            border-left: 3px solid var(--accent-color);
            color: var(--accent-color);
            font-weight: 500;
        }

        /* Tag for file type */
        .file-tag {
            font-size: 0.7em; padding: 2px 4px; border-radius: 2px; 
            margin-right: 8px; vertical-align: middle; opacity: 0.7;
        }
        .tag-html { background: #222; color: #569cd6; }
        .tag-md { background: #222; color: #ce9178; }

        /* Main Content */
        .main-content {
            flex: 1; display: flex; flex-direction: column; background-color: var(--bg-color);
            position: relative; overflow: hidden;
        }

        /* GHOST BURGER BUTTON */
        .ghost-burger {
            position: absolute; top: 15px; left: 15px; z-index: 100;
            background: transparent; border: none; color: var(--accent-color);
            font-size: 1.5em; cursor: pointer; opacity: 0.2;
            transition: opacity 0.3s ease; display: none; 
        }
        .ghost-burger:hover { opacity: 1.0; }

        /* Close Button inside header */
        .close-btn { 
            background: none; border: none; color: var(--text-muted); 
            cursor: pointer; font-size: 1.2em; padding: 5px;
            transition: color 0.2s;
        }
        .close-btn:hover { color: var(--accent-color); }

        /* VIEWS */
        iframe { width: 100%; height: 100%; border: none; display: none; background: #fff; }

        /* Markdown Container */
        #markdown-view {
            display: none; padding: 40px; overflow-y: auto; height: 100%;
            background-color: var(--bg-color); color: #ccc;
            line-height: 1.6; max-width: 900px; margin: 0 auto; box-sizing: border-box;
        }
        /* Markdown internal styling to match theme */
        #markdown-view h1, #markdown-view h2, #markdown-view h3 { color: var(--accent-color); margin-top: 1.5em; }
        #markdown-view a { color: #4daafc; text-decoration: none; }
        #markdown-view code { background: #222; padding: 2px 5px; border-radius: 3px; font-family: var(--font-stack); }
        #markdown-view pre { background: #111; padding: 15px; border: 1px solid #333; overflow-x: auto; }
        #markdown-view blockquote { border-left: 4px solid var(--accent-color); margin: 0; padding-left: 15px; color: var(--text-muted); }

        .placeholder {
            display: flex; flex-direction: column;
            align-items: center; justify-content: center; 
            height: 100%; width: 100%;
            color: var(--text-muted); 
            font-family: var(--font-stack);
        }
        .placeholder h1 { font-size: 1.2em; font-weight: 400; letter-spacing: 2px; margin-bottom: 10px; color: #444; }
        
    </style>
</head>
<body>

    <button id="ghost-burger" class="ghost-burger" onclick="openSidebar()">☰</button>

    <div class="sidebar" id="sidebar">
        <div class="header">
            <span class="header-title">Market Data</span>
            <button class="close-btn" onclick="closeSidebar()">×</button>
        </div>
        <div class="nav-scroll">
            {SIDEBAR_CONTENT}
        </div>
    </div>

    <div class="main-content">
        <iframe name="tool-frame" id="tool-frame"></iframe>
        
        <div id="markdown-view"></div>

        <div id="placeholder-text" class="placeholder">
            <h1>NO FEED SELECTED</h1>
        </div>
    </div>

    <script>
        const sidebar = document.getElementById('sidebar');
        const burger = document.getElementById('ghost-burger');
        const iframe = document.getElementById('tool-frame');
        const mdView = document.getElementById('markdown-view');
        const placeholder = document.getElementById('placeholder-text');
        const links = document.querySelectorAll('.nav-link');

        function closeSidebar() {
            sidebar.classList.add('collapsed');
            setTimeout(() => { burger.style.display = 'block'; }, 300);
        }

        function openSidebar() {
            burger.style.display = 'none';
            sidebar.classList.remove('collapsed');
        }

        // ROUTER LOGIC
        function loadFromHash() {
            const hash = window.location.hash.substring(1);
            
            // Reset Views
            iframe.style.display = 'none';
            mdView.style.display = 'none';
            placeholder.style.display = 'none';
            links.forEach(l => l.classList.remove('active'));

            if (!hash) {
                placeholder.style.display = 'flex';
                return;
            }

            // Highlight Link
            links.forEach(link => {
                if (link.getAttribute('href') === '#' + hash) link.classList.add('active');
            });

            // Handle content type
            if (hash.endsWith('.html')) {
                iframe.src = hash;
                iframe.style.display = 'block';
            } else if (hash.endsWith('.md')) {
                mdView.style.display = 'block';
                // Fetch and render MD
                fetch(hash)
                    .then(response => {
                        if (!response.ok) throw new Error("Failed to load file");
                        return response.text();
                    })
                    .then(text => {
                        mdView.innerHTML = marked.parse(text);
                    })
                    .catch(err => {
                        mdView.innerHTML = `<h2 style='color:red'>Error loading file</h2><p>${err.message}</p>`;
                    });
            }
        }

        window.addEventListener('hashchange', loadFromHash);
        window.addEventListener('load', loadFromHash);
    </script>
</body>
</html>
"""

def generate_sidebar_html(base_path):
    html_output = ""
    
    if not os.path.exists(base_path):
        return "<div class='category-label'>Data directory missing</div>"

    for root, dirs, files in sorted(os.walk(base_path)):
        dirs.sort()
        files.sort()
        rel_path = os.path.relpath(root, base_path)
        
        if any(part.startswith('.') for part in rel_path.split(os.sep)): continue

        # Scan for both HTML and MD
        valid_files = [f for f in files if f.endswith(('.html', '.md'))]
        
        if valid_files:
            if rel_path == ".":
                category_name = "General"
            else:
                parts = rel_path.split(os.sep)
                category_name = " > ".join([p.capitalize() for p in parts])
            
            html_output += f"<div class='category-label'>{category_name}</div>\n"
            
            for file in valid_files:
                file_path = os.path.join(DATA_DIR, rel_path, file) if rel_path != "." else os.path.join(DATA_DIR, file)
                web_path = file_path.replace(os.sep, '/')
                
                # Determine tag style
                ext = file.split('.')[-1]
                tag_class = f"tag-{ext}"
                
                raw_name = file.replace('.html', '').replace('.md', '').replace('_', ' ')
                display_name = raw_name.title() 
                
                # Added a tiny colored tag (HTML/MD) next to the name
                html_output += f"<a href='#{web_path}' class='nav-link'><span class='file-tag {tag_class}'>{ext.upper()}</span>{display_name}</a>\n"

    return html_output

def main():
    print(f"--- Root Builder v1.5 (MD Support) ---")
    sidebar_content = generate_sidebar_html(DATA_DIR)
    final_html = HTML_TEMPLATE.replace("{SIDEBAR_CONTENT}", sidebar_content)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final_html)
    print(f"Success! Generated {OUTPUT_FILE}")

if __name__ == "__main__":
    main()