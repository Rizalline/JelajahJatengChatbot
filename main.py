import streamlit as st
from fsm import TravelGuideFSM
from engine import NLPEngine

# ═══════════════════════════════════════════════════════════════
# 1. KONFIGURASI HALAMAN
# ═══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Jelajah Jawa Tengah",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════════
# 2. STATE INITIALIZATION (MANAJEMEN STATE)
# ═══════════════════════════════════════════════════════════════
if 'bot' not in st.session_state:
    st.session_state.bot = TravelGuideFSM()
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [{"role": "assistant", "content": "Halo! Mau cari rekomendasi liburan ke mana hari ini?"}]
if 'show_chat' not in st.session_state:
    st.session_state.show_chat = False 
if 'selected_prov' not in st.session_state:
    st.session_state.selected_prov = None
if 'page' not in st.session_state:
    st.session_state.page = "Destinasi" # State untuk halaman aktif

nlp = NLPEngine()
nlp_data = nlp.destinations

def send_to_chat(text):
    st.session_state.chat_history.append({"role": "user", "content": text})
    st.session_state.bot.step(text)
    bot_reply = st.session_state.bot.get_response()
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
    st.session_state.show_chat = True

# ═══════════════════════════════════════════════════════════════
# 3. KUSTOM CSS & TEMA
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --primary: #00966C;
    --primary-dark: #007A57;
    --bg-light: #F8F9FA;
    --text-main: #1A1A2E;
    --text-muted: #666666;
    --border-color: #E5E7EB;
}

* { font-family: 'Inter', sans-serif; }

/* Reset Padding Streamlit */
[data-testid="stAppViewContainer"] > .main > .block-container {
    padding-top: 2rem !important; padding-left: 0rem !important; padding-right: 0rem !important;
    max-width: 100% !important;
}
[data-testid="collapsedControl"], header, #MainMenu { display: none !important; }

/* ── HERO SECTION ── */
.hero {
    background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.6)), url('https://images.unsplash.com/photo-1553603227-2358aabe8eb8?auto=format&fit=crop&w=1920&q=80') center/cover;
    padding: 70px 20px 80px 20px;
    text-align: center; color: white; margin-top: 10px;
}
.hero h1 { font-size: 3rem; font-weight: 800; margin-bottom: 15px; letter-spacing: -0.5px; line-height: 1.2; }
.hero p { font-size: 1.1rem; max-width: 600px; margin: 0 auto 30px auto; color: #E2E8F0; }

/* ── CONTENT AREA ── */
.section-wrapper { max-width: 1200px; margin: 0 auto; padding: 40px 40px; }
.section-title { margin-bottom: 30px; }
.section-title h2 { margin: 0; font-size: 26px; color: var(--text-main); font-weight: 800; }
.section-title p { margin: 8px 0 0 0; color: var(--text-muted); font-size: 15px; }

/* Card Style */
.prov-card {
    background: white; border: 1px solid var(--border-color); border-radius: 16px; 
    padding: 24px; height: 160px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    display: flex; flex-direction: column; justify-content: flex-start;
    margin-bottom: 12px; transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.prov-card:hover { transform: translateY(-3px); box-shadow: 0 8px 15px rgba(0,0,0,0.05); }
.prov-ttl { font-size: 18px; font-weight: 700; color: var(--text-main); margin: 0 0 10px 0; display: flex; align-items: center; gap: 8px;}
.prov-exc { font-size: 14px; color: var(--text-muted); line-height: 1.6; margin: 0; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }

/* ── FLOATING CHAT WIDGET (JENDELA CHAT) ── */
div[data-testid="stVerticalBlock"]:has(.chat-widget-marker):not(:has(div[data-testid="stVerticalBlock"]:has(.chat-widget-marker))) {
    position: fixed !important; 
    top: 90px !important; 
    right: 30px !important; 
    width: 360px !important; 
    background: white !important;
    border-radius: 16px !important; 
    box-shadow: 0 10px 40px rgba(0,0,0,0.2) !important; 
    z-index: 9999 !important;
    overflow: hidden !important; 
    border: 1px solid var(--border-color) !important;
}
.chat-header { background-color: var(--primary); color: white; padding: 16px; display: flex; align-items: center; gap: 10px; }
.chat-header .dot { width: 10px; height: 10px; background-color: #A5D6A7; border-radius: 50%; box-shadow: 0 0 5px rgba(165, 214, 167, 0.8);}
.chat-header span { font-size: 15px; font-weight: 700; }
.bot-bubble { background: #F3F4F6; color: var(--text-main); padding: 12px 16px; border-radius: 0 16px 16px 16px; font-size: 14px; max-width: 85%; align-self: flex-start; margin-bottom: 12px; line-height: 1.5; box-shadow: 0 1px 2px rgba(0,0,0,0.05);}
.user-bubble { background: var(--primary); color: white; padding: 12px 16px; border-radius: 16px 0 16px 16px; font-size: 14px; max-width: 85%; align-self: flex-end; margin-left: auto; margin-bottom: 12px; line-height: 1.5; box-shadow: 0 1px 2px rgba(0,150,108,0.2);}

/* ── TOMBOL TANYA BOT (PRIMARY BUTTON STREAMLIT) ── */
button[kind="primary"] {
    background-color: var(--primary) !important; 
    color: white !important;
    font-weight: bold !important; 
    border: none !important;
    transition: all 0.2s ease !important;
}
button[kind="primary"]:hover { 
    background-color: var(--primary-dark) !important; 
}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# 4. NAVBAR INTERAKTIF
# ═══════════════════════════════════════════════════════════════
st.markdown('<div class="section-wrapper" style="padding-top: 0px; padding-bottom: 0px;">', unsafe_allow_html=True)

# Membagi menjadi 5 kolom agar muat untuk tombol Chatbot di sisi paling kanan
col_logo, col_nav1, col_nav2, col_nav3, col_chat = st.columns([2.5, 1, 1, 1, 1.2])

with col_logo:
    st.markdown('<div style="font-size: 22px; font-weight: 800; color: #1A1A2E; margin-top: 5px;"><span style="color: #00966C;">✈️ JELAJAH</span>JATENG</div>', unsafe_allow_html=True)
with col_nav1:
    if st.button("🗺️ Destinasi", use_container_width=True): 
        st.session_state.page = "Destinasi"
        st.rerun()
with col_nav2:
    if st.button("📖 Panduan Chatbot", use_container_width=True): 
        st.session_state.page = "Panduan"
        st.rerun()
with col_nav3:
    if st.button("👥 Tentang Kami", use_container_width=True): 
        st.session_state.page = "Tentang"
        st.rerun()
with col_chat:
    # Menggunakan type="primary" bawaan Streamlit agar style spesifik bekerja tanpa merusak layout kolom
    fab_label = "✖ Tutup Bot" if st.session_state.show_chat else "💬 Tanya Bot"
    if st.button(fab_label, key="toggle_chat_widget", use_container_width=True, type="primary"):
        st.session_state.show_chat = not st.session_state.show_chat
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<hr style='margin: 0;'>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# 5. KONTEN HALAMAN (ROUTING)
# ═══════════════════════════════════════════════════════════════

if st.session_state.page == "Destinasi":
    # Skenario A: Detail Wisata
    if st.session_state.selected_prov:
        prov_key = st.session_state.selected_prov
        prov_data = nlp_data[prov_key]
        
        st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
        if st.button("← Kembali ke Daftar Destinasi"):
            st.session_state.selected_prov = None
            st.rerun()
            
        st.markdown(f'<div class="section-title" style="margin-top:20px;"><h2>{prov_data["emoji"]} {prov_data["name"]}</h2></div>', unsafe_allow_html=True)
            
        col_left, col_right = st.columns([2.5, 1])
        with col_left:
            st.subheader("Ringkasan Wilayah")
            st.markdown(f"✅ **Kelebihan:** {prov_data.get('kelebihan', '-')}")
            st.markdown(f"❌ **Kekurangan:** {prov_data.get('kekurangan', '-')}")
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("📸 Destinasi Populer")
            for spot_key, spot_info in prov_data["spots"].items():
                with st.expander(f"{spot_info['name']} ({spot_info['kategori'].capitalize()})"):
                    st.write(f"**Deskripsi:** {spot_info['desc']}")
                    st.markdown(f"✅ **Kelebihan:** {spot_info['kelebihan']}")
                    st.markdown(f"❌ **Kekurangan:** {spot_info['kekurangan']}")

        with col_right:
            st.info("💡 Instruksi cepat untuk Asisten:")
            if st.button(f"🗺️ Buat Itinerary", use_container_width=True):
                send_to_chat(f"buatkan jadwal {prov_data['name']} 3 hari")
                st.rerun()
            if st.button(f"📜 Cek Aturan & Adat", use_container_width=True):
                send_to_chat(f"aturan di {prov_data['name']}")
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # Skenario B: Grid Destinasi
    else:
        st.markdown("""
        <div class="hero">
            <h1>Temukan Keindahan Tersembunyi<br>di Jawa Tengah.</h1>
            <p>Eksplorasi wisata di seluruh Jawa Tengah atau gunakan fitur Asisten (Menu Kanan Atas) untuk merencanakan liburan dengan cepat dan akurat.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
        col_title, col_search = st.columns([1, 1])
        with col_title:
            st.markdown('<div class="section-title"><h2>🏝️ Destinasi Pilihan</h2></div>', unsafe_allow_html=True)
        with col_search:
            search_input = st.text_input("Pencarian", placeholder="Cari kota (cth: Semarang, Wonosobo)...", label_visibility="collapsed")
        
        filtered_provs = [(k, v) for k, v in nlp_data.items() if not search_input or search_input.lower() in v["name"].lower()]
                
        if not filtered_provs:
            st.warning("Destinasi yang Anda cari tidak ditemukan.")
        else:
            cols = st.columns(3)
            for i, (k, v) in enumerate(filtered_provs):
                col = cols[i % 3]
                with col:
                    st.markdown(f"""
                    <div class="prov-card">
                        <div class="prov-ttl">{v['emoji']} {v['name']}</div>
                        <p class="prov-exc">{v.get('kelebihan', '')}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"Lihat Detail", key=f"btn_{k}", use_container_width=True):
                        st.session_state.selected_prov = k
                        st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "Panduan":
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
    st.title("📖 Panduan Penggunaan Chatbot")
    st.markdown("""
    Selamat datang di Asisten Wisata Jelajah Jateng! Chatbot kami dirancang menggunakan NLP (Natural Language Processing) untuk merespons kebutuhan liburan Anda dengan cerdas.
    
    Berikut adalah beberapa contoh interaksi yang bisa Anda gunakan:
    * **Mencari Rekomendasi Terbaik:** Ketik *"rekomendasi wisata terbaik"* atau *"wisata apa aja di Jateng"*.
    * **Mencari Berdasarkan Kategori:** Ketik *"rekomendasi wisata alam"* atau *"wisata sejarah"*.
    * **Mencari di Kota Spesifik (Bisa Lebih dari Satu):** Ketik *"rekomendasi wisata di Kendal dan Semarang"*.
    * **Informasi Detail Spot:** Ketik *"apa kelebihan dan kekurangan Lawang Sewu?"*.
    * **Perencanaan Itinerary:** Ketik *"buatkan jadwal liburan di Magelang selama 3 hari"*.
    
    👉 **Cara Mulai:** Klik tombol **💬 Tanya Bot** di menu navigasi atas untuk mulai berinteraksi!
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "Tentang":
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
    st.title("👥 Tentang Kami")
    st.markdown("""
    Aplikasi **Jelajah Jateng** dikembangkan sebagai Asisten Pariwisata Cerdas. Kami bertujuan untuk mendigitalkan dan memudahkan wisatawan dalam menemukan surga-surga tersembunyi di seluruh penjuru Jawa Tengah.
    
    **Sistem ini dibangun dan dikembangkan oleh:**
    * **Rizal Efendi** (23670033)
    * **Iir Dwi Septiani** (NPM: 23670001)
    """)
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# 6. LOGIKA FLOATING CHAT WIDGET
# ═══════════════════════════════════════════════════════════════

# Jendela Chatbot
if st.session_state.show_chat:
    with st.container():
        # Menggunakan <span> agar tidak mengambil tinggi/space kosong di UI
        st.markdown('<span class="chat-widget-marker"></span>', unsafe_allow_html=True)
        st.markdown("""
        <div class="chat-header">
            <div class="dot"></div><span>Asisten Wisata </span>
        </div>
        """, unsafe_allow_html=True)

        msg_container = st.container(height=350)
        with msg_container:
            for msg in st.session_state.chat_history:
                if msg["role"] == "user":
                    st.markdown(f'<div class="user-bubble">{msg["content"]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="bot-bubble">{msg["content"]}</div>', unsafe_allow_html=True)

        with st.form("chat_input_form", clear_on_submit=True):
            c1, c2 = st.columns([3.5, 1])
            with c1:
                user_input = st.text_input("msg", placeholder="Ketik pesan...", label_visibility="collapsed")
            with c2:
                submitted = st.form_submit_button("Kirim", use_container_width=True)
            
            if submitted and user_input.strip():
                st.session_state.chat_history.append({"role": "user", "content": user_input})
                st.session_state.bot.step(user_input)
                bot_reply = st.session_state.bot.get_response()
                st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
                st.rerun()