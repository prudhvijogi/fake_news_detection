import streamlit as st

def render_theme_toggle():
    st.markdown("""
        <div class="theme-toggle">
            <button onclick="toggleTheme()" class="theme-toggle-button">
                <span class="light-icon">☀️</span>
                <span class="dark-icon">🌙</span>
            </button>
        </div>
        <style>
            .theme-toggle {
                position: fixed;
                top: 1rem;
                right: 1rem;
                z-index: 1000;
            }
            
            .theme-toggle-button {
                background: var(--bg-secondary);
                border: 1px solid var(--border-color);
                border-radius: 50%;
                width: 40px;
                height: 40px;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                transition: all 0.2s ease;
            }
            
            .theme-toggle-button:hover {
                transform: scale(1.1);
            }
            
            .dark-icon {
                display: none;
            }
            
            [data-theme="dark"] .light-icon {
                display: none;
            }
            
            [data-theme="dark"] .dark-icon {
                display: block;
            }
        </style>
        <script>
            function toggleTheme() {
                const body = document.body;
                const currentTheme = body.getAttribute('data-theme');
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                body.setAttribute('data-theme', newTheme);
                localStorage.setItem('theme', newTheme);
            }
            
            // Set initial theme
            const savedTheme = localStorage.getItem('theme') || 'light';
            document.body.setAttribute('data-theme', savedTheme);
        </script>
    """, unsafe_allow_html=True)