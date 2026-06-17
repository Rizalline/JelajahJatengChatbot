from enum import Enum, auto
from engine import NLPEngine

class State(Enum):
    CONSULTING = auto()

class TravelGuideFSM:
    def __init__(self):
        self.state = State.CONSULTING 
        self.nlp = NLPEngine()
        self.response = ""
        self.suggested_actions = []

    def get_response(self):
        return self.response

    def step(self, user_input=""):
        user_input = user_input.strip()
        if not user_input: return

        intent = self.nlp.detect_intent(user_input)
        dest_keys = self.nlp.extract_destinations(user_input) 
        spot_key, spot_prov_key = self.nlp.extract_spot(user_input)

        self.suggested_actions = []

        if intent == "RESET":
            self.response = "Halo! Saya Asisten Travel Jawa Tengah 🗺️\nMau cari rekomendasi wisata alam, wisata kota, atau melihat daftar semua kota di Jateng?"
            self.suggested_actions = ["Wisata Jawa Tengah", "Rekomendasi Alam", "Kota Lama"]
            return

        if intent == "GREETING":
            self.response = "Halo juga! 👋 Saya Asisten Wisata Jawa Tengah. Ada yang bisa saya bantu? Kamu bisa mencari rekomendasi wisata alam, wisata kota, atau melihat tempat wisata terbaik di Jateng!"
            self.suggested_actions = ["Rekomendasi Wisata Terbaik", "Wisata Alam", "Wisata Semarang"]
            return

        # ── FITUR BARU: Menjawab Pertanyaan Umum Manusia ──
        if intent == "GENERAL_QA":
            low_input = user_input.lower()
            if "siapa" in low_input or "namamu" in low_input:
                self.response = "Saya adalah **Jelajah Jateng Bot** 🤖, asisten virtual ramah yang siap menemani dan memberikan rekomendasi liburan terbaik di Jawa Tengah!"
            elif "kabar" in low_input:
                self.response = "Kabar saya luar biasa baik! Selalu bersemangat membantu rencana liburanmu. Bagaimana kabarmu hari ini? Semoga sehat selalu ya! 😊"
            elif "terima kasih" in low_input or "makasih" in low_input or "thanks" in low_input:
                self.response = "Sama-sama! ✨ Senang sekali bisa membantumu. Kalau butuh rekomendasi wisata lagi, panggil saya kapan saja ya!"
            elif "pencipta" in low_input or "dibuat" in low_input:
                self.response = "Saya dikembangkan oleh tim hebat: **Rizal Efendi** dan **Iir Dwi Septiani** sebagai tugas Asisten Pariwisata Cerdas Jawa Tengah! 🚀"
            elif "bisa apa" in low_input or "fungsi" in low_input:
                self.response = "Saya bisa membantumu mencari rekomendasi wisata alam/sejarah, memberikan info detail kelebihan/kekurangan tempat wisata, hingga merencanakan itinerary di Jawa Tengah! 🗺️"
            else:
                self.response = "Wah, pertanyaan yang bagus! Sebagai asisten pariwisata virtual, saya paling ahli seputar jalan-jalan di Jateng. Ada destinasi kota yang ingin kamu cari hari ini? 🏞️"
            return

        if intent == "ASK_BEST_RECOMMENDATION":
            self.response = "🏆 **Rekomendasi Wisata Terbaik di Jawa Tengah**\nBerikut adalah beberapa destinasi unggulan dari berbagai wilayah yang wajib kamu kunjungi:\n\n"
            
            top_cities = ["magelang", "semarang", "wonosobo", "karanganyar"]
            for city_key in top_cities:
                if city_key in self.nlp.destinations:
                    city_data = self.nlp.destinations[city_key]
                    first_spot_key = list(city_data["spots"].keys())[0]
                    spot = city_data["spots"][first_spot_key]
                    self.response += f"**{spot['name']} ({city_data['name']}) - Kategori: {spot['kategori'].capitalize()}**\n"
                    self.response += f"📖 {spot['desc']}\n\n"

            self.response += "*Ketik nama kota (misal: 'Semarang') untuk melihat rekomendasi spesifik di kota tersebut!*"
            self.suggested_actions = ["Wisata Alam", "Wisata Magelang", "Wisata Jepara"]
            return

        if intent == "ASK_CITY_INFO" and dest_keys:
            self.response = "" 
            
            for dest_key in dest_keys:
                data = self.nlp.destinations[dest_key]
                self.response += f"📍 Kamu memilih **{data['name']}** {data['emoji']}\n\n"
                self.response += f"✅ **Kelebihan:** {data['kelebihan']}\n"
                self.response += f"❌ **Kekurangan:** {data['kekurangan']}\n\n"
                self.response += f"🌟 **Rekomendasi Wisata di {data['name']}:**\n"
                
                spots_by_cat = {}
                for s_key, s_val in data["spots"].items():
                    cat = s_val["kategori"].capitalize()
                    if cat not in spots_by_cat:
                        spots_by_cat[cat] = []
                    spots_by_cat[cat].append(s_val)
                
                for cat, spots in spots_by_cat.items():
                    self.response += f"\n🏷️ **Kategori: {cat}**\n"
                    for s in spots:
                        self.response += f"- **{s['name']}**: {s['desc']}\n"
                        
                self.response += "\n---\n\n" 
                
                for s_key, s_val in data["spots"].items():
                    self.suggested_actions.append(s_val["name"])
                    
            self.response += "*Sebutkan nama spesifik tempat di atas jika ingin tahu detail kelebihan dan kekurangannya!*"
            return

        if intent == "ASK_ALL_JATENG":
            self.response = "📍 **Daftar Destinasi di Jawa Tengah**\nBerikut adalah beberapa kabupaten/kota beserta kelebihan dan kekurangannya:\n\n"
            count = 0
            for key, data in self.nlp.destinations.items():
                if count >= 5: break 
                self.response += f"**{data['emoji']} {data['name']}**\n"
                self.response += f"✅ **Kelebihan:** {data['kelebihan']}\n"
                self.response += f"❌ **Kekurangan:** {data['kekurangan']}\n\n"
                count += 1
            self.response += "*...dan masih banyak lagi (total 35 Kota/Kabupaten)! Sebutkan spesifik kota yang ingin kamu tuju.*"
            self.suggested_actions = ["Wisata Semarang", "Wisata Magelang", "Wisata Alam"]
            return

        if intent == "ASK_NATURE":
            nature_spots = self.nlp.get_nature_spots()
            self.response = "🌿 **Rekomendasi Wisata Alam Pilihan di Jawa Tengah**\n\n"
            for city_name, spot in nature_spots[:5]:
                self.response += f"**{spot['name']} ({city_name})**\n"
                self.response += f"📖 {spot['desc']}\n"
                self.response += f"✅ **Kelebihan:** {spot['kelebihan']}\n"
                self.response += f"❌ **Kekurangan:** {spot['kekurangan']}\n\n"
            self.suggested_actions = ["Bukit Sikunir", "Karimunjawa"]
            return

        if intent == "ASK_SPOT_DETAIL" and spot_key:
            city_data = self.nlp.destinations[spot_prov_key]
            spot_data = city_data["spots"][spot_key]
            
            self.response = f"📸 **Detail Destinasi: {spot_data['name']} ({city_data['name']})**\n\n"
            self.response += f"📝 **Deskripsi:**\n{spot_data['desc']}\n\n"
            self.response += f"✅ **Kelebihan Tempat Ini:**\n{spot_data['kelebihan']}\n\n"
            self.response += f"❌ **Kekurangan / Hal Perhatian:**\n{spot_data['kekurangan']}\n"
            
            self.suggested_actions = ["Rekomendasi Alam", "Wisata Jateng Lainnya"]
            return

        # 1. HANDLING INTENT KULINER
        if intent == "ASK_CULINARY":
            if dest_keys:
                self.response = "🍽️ **Rekomendasi Kuliner & Oleh-Oleh Khas**\n\n"
                for dest_key in dest_keys:
                    data = self.nlp.destinations[dest_key]
                    info = data.get("kuliner", "Maaf, data kuliner untuk kota ini belum lengkap.")
                    self.response += f"📍 **{data['name']}**:\n{info}\n\n"
            else:
                self.response = "🍽️ Kamu ingin tahu rekomendasi kuliner di kota mana? Coba ketik contohnya: *'kuliner khas Semarang'* atau *'makanan khas Wonosobo'*."
                self.suggested_actions = ["Kuliner Semarang", "Kuliner Wonosobo", "Kuliner Magelang"]
            return

        # 2. HANDLING INTENT TRANSPORTASI
        if intent == "ASK_TRANSPORT":
            if dest_keys:
                self.response = "🚌 **Panduan Transportasi & Rute Akses**\n\n"
                for dest_key in dest_keys:
                    data = self.nlp.destinations[dest_key]
                    info = data.get("transportasi", "Maaf, informasi rute untuk kota ini belum lengkap.")
                    self.response += f"📍 **{data['name']}**:\n{info}\n\n"
            else:
                self.response = "🚌 Info rute transportasi ke mana yang ingin kamu tanyakan? Coba ketik: *'transportasi ke Wonosobo'* atau *'cara ke Semarang naik apa'*."
                self.suggested_actions = ["Akses ke Wonosobo", "Transportasi Semarang"]
            return
        
        if intent == "ASK_TRAVEL_ESTIMATION":
            # 1. Deteksi kota apa saja yang ada di dalam text input
            extracted_cities = self.nlp.extract_destinations(text) # Mengambil list kota yang terdeteksi
            
            if len(extracted_cities) < 2:
                self.response = "🚗 Kamu ingin tahu estimasi perjalanan ke mana nih? Coba ketik lengkap dengan format: *'Dari Tegal ke Magelang berapa lama?'*"
                return
            
            # Tentukan asal dan tujuan berdasarkan urutan kata "dari" dan "ke"
            # Default asumsi: indeks 0 adalah asal, indeks 1 adalah tujuan
            origin_key = extracted_cities[0]
            dest_key = extracted_cities[1]
            
            # Cek urutan teks asli untuk memastikan akurasi asal-tujuan
            if text.find(dest_key) < text.find(origin_key):
                origin_key, dest_key = dest_key, origin_key

            origin_name = self.nlp.destinations[origin_key]["name"]
            dest_name = self.nlp.destinations[dest_key]["name"]

            # 2. Mapping Pembagian Zona 35 Kabupaten/Kota Jawa Tengah
            CITY_ZONES = {
                "semarang": "pusat", "semarang kab": "pusat", "salatiga": "pusat", "kendal": "pusat",
                "tegal": "pantura_barat", "tegal kota": "pantura_barat", "brebes": "pantura_barat", "pemalang": "pantura_barat", "pekalongan": "pantura_barat", "pekalongan kota": "pantura_barat", "batang": "pantura_barat",
                "demak": "pantura_timur", "kudus": "pantura_timur", "pati": "pantura_timur", "rembang": "pantura_timur", "blora": "pantura_timur", "grobogan": "pantura_timur",
                "cilacap": "banyumasan", "banyumas": "banyumasan", "purbalingga": "banyumasan", "banjarnegara": "banyumasan", "kebumen": "banyumasan",
                "surakarta": "soloraya", "boyolali": "soloraya", "sukoharjo": "soloraya", "karanganyar": "soloraya", "sragen": "soloraya", "klaten": "soloraya", "wonogiri": "soloraya",
                "magelang": "kedu", "magelang kota": "kedu", "temanggung": "kedu", "wonosobo": "kedu", "purworejo": "kedu"
            }

            zone_origin = CITY_ZONES.get(origin_key, "unknown")
            zone_dest = CITY_ZONES.get(dest_key, "unknown")

            # 3. Matrix Waktu & Saran Rute Utama Antar-Zona
            # Format key: (zona_asal, zona_tujuan) -> (Waktu, Saran Jalan)
            ROUTE_MATRIX = {
                ("pantura_barat", "kedu"): ("3.5 - 4.5 Jam", "Via Tol Trans Jawa (Keluar di Gerbang Tol Bawen), lalu lanjut menyusuri jalur utama Ambarawa - Magelang."),
                ("pantura_barat", "pusat"): ("2 - 2.5 Jam", "Full via Tol Trans Jawa dari arah barat langsung lurus menuju Exit Tol Krapyak/Jatingaleh Semarang."),
                ("pantura_barat", "soloraya"): ("3 - 3.5 Jam", "Full via Tol Trans Jawa langsung bablas ke arah timur menuju Exit Tol Colomadu/Solo."),
                ("banyumasan", "kedu"): ("2.5 - 3.5 Jam", "Via jalur darat tengah pegunungan melewati Purbalingga - Banjarnegara - Wonosobo (jalur tengah)."),
                ("pusat", "kedu"): ("1.5 - 2 Jam", "Via jalur utama Semarang - Yogyakarta atau bisa memanfaatkan Tol Solo-Semarang lalu keluar di Bawen."),
                ("soloraya", "kedu"): ("1.5 - 2.5 Jam", "Bisa lewat jalur utama Solo - Jogja (Klaten) atau jalur alternatif Selo (Boyolali) di celah Gunung Merapi-Merbabu."),
                ("pantura_timur", "kedu"): ("3.5 - 4.5 Jam", "Lewat jalur Pantura ke arah Semarang, lalu lanjut via Tol Semarang dan keluar di Bawen menuju Magelang.")
            }

            # Cek rute bolak-balik di matrix
            route_data = ROUTE_MATRIX.get((zone_origin, zone_dest)) or ROUTE_MATRIX.get((zone_dest, zone_origin))

            # 4. Formulasi Balasan Bot
            if origin_key == dest_key:
                self.response = f"🚗 **{origin_name}** ke **{dest_name}** kan berada di wilayah yang sama! Estimasinya sekitar 15 - 45 menit tergantung lokasi spesifik objek wisatanya."
            elif route_data:
                waktu, rute = route_data
                self.response = (
                    f"🚗 **Estimasi Perjalanan Antarkota**\n\n"
                    f"📍 **Rute:** Dari {origin_name} menuju {dest_name}\n"
                    f"⏱️ **Perkiraan Waktu:** Kurang lebih **{waktu}** (Kondisi lalu lintas normal)\n"
                    f"🛣️ **Saran Jalur:** {rute}\n\n"
                    f"_Tips: Pastikan kondisi rem dan bahan bakar kendaraanmu aman sebelum berangkat ya!_"
                )
            else:
                # Fallback jika kombinasi zonanya belum didaftarkan di matrix atas
                self.response = f"🚗 Perjalanan dari **{origin_name}** ke **{dest_name}** diperkirakan memakan waktu sekitar **3 - 5 Jam** lintas kabupaten menggunakan jalur darat utama Jawa Tengah."
            
            return

        # 3. HANDLING INTENT BUDGET / BIAYA
        if intent == "ASK_BUDGET":
            if dest_keys:
                self.response = "💰 **Estimasi Biaya & Tiket Wisata**\n\n"
                for dest_key in dest_keys:
                    data = self.nlp.destinations[dest_key]
                    info = data.get("budget", "Maaf, info estimasi biaya untuk kota ini belum lengkap.")
                    self.response += f"📍 **{data['name']}**:\n{info}\n\n"
            else:
                self.response = "💰 Info budget & harga tiket kota mana yang ingin kamu cek? Contoh: *'harga tiket wisata Magelang'* atau *'biaya liburan di Semarang'*."
                self.suggested_actions = ["Harga Tiket Magelang", "Budget Semarang"]
            return

        # 4. HANDLING INTENT WAKTU TERBAIK
        if intent == "ASK_TIMING":
            if dest_keys:
                self.response = "⏰ **Waktu & Kunjungan Terbaik**\n\n"
                for dest_key in dest_keys:
                    data = self.nlp.destinations[dest_key]
                    info = data.get("waktu_terbaik", "Maaf, info waktu terbaik berkunjung belum lengkap.")
                    self.response += f"📍 **{data['name']}**:\n{info}\n\n"
            else:
                self.response = "⏰ Kamu ingin tahu waktu berkunjung terbaik ke mana? Silakan ketik: *'waktu terbaik ke Dieng Wonosobo'* atau *'kapan jam pas ke Semarang'*."
                self.suggested_actions = ["Waktu Terbaik Wonosobo", "Waktu Terbaik Magelang"]
            return

        self.response = "Maaf, saya belum menangkap maksudnya atau destinasinya belum terdaftar. Bisa gunakan kata kunci seperti 'Wisata Alam', 'Semarang', atau 'Lawang Sewu'?"
