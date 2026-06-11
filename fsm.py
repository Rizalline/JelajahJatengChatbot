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
        # 1. Menjawab Sapaan ("Halo")
        if intent == "GREETING":
            self.response = "Halo juga! 👋 Saya Asisten Wisata Jawa Tengah. Ada yang bisa saya bantu? Kamu bisa mencari rekomendasi wisata alam, wisata kota, atau melihat tempat wisata terbaik di Jateng!"
            self.suggested_actions = ["Rekomendasi Wisata Terbaik", "Wisata Alam", "Wisata Semarang"]
            return

        # 2. Menjawab Permintaan Rekomendasi Umum ("Rekomendasi wisata")
        if intent == "ASK_BEST_RECOMMENDATION":
            self.response = "🏆 **Rekomendasi Wisata Terbaik di Jawa Tengah**\nBerikut adalah beberapa destinasi unggulan dari berbagai wilayah yang wajib kamu kunjungi:\n\n"
            
            # Mengambil sampel destinasi terbaik (misal dari Magelang, Semarang, Wonosobo)
            top_cities = ["magelang", "semarang", "wonosobo", "karanganyar"]
            for city_key in top_cities:
                if city_key in self.nlp.destinations:
                    city_data = self.nlp.destinations[city_key]
                    # Mengambil spot pertama dari kota tersebut sebagai perwakilan
                    first_spot_key = list(city_data["spots"].keys())[0]
                    spot = city_data["spots"][first_spot_key]
                    self.response += f"**{spot['name']} ({city_data['name']}) - Kategori: {spot['kategori'].capitalize()}**\n"
                    self.response += f"📖 {spot['desc']}\n\n"

            self.response += "*Ketik nama kota (misal: 'Semarang') untuk melihat rekomendasi spesifik di kota tersebut!*"
            self.suggested_actions = ["Wisata Alam", "Wisata Magelang", "Wisata Jepara"]
            return

        # 3. Menjawab "Rekomendasi wisata di [Kota 1] dan [Kota 2]" 
        if intent == "ASK_CITY_INFO" and dest_keys:
            self.response = "" # Kosongkan string respons di awal
            
            # Lakukan perulangan untuk setiap kota yang ditemukan dalam kalimat
            for dest_key in dest_keys:
                data = self.nlp.destinations[dest_key]
                self.response += f"📍 Kamu memilih **{data['name']}** {data['emoji']}\n\n"
                self.response += f"✅ **Kelebihan:** {data['kelebihan']}\n"
                self.response += f"❌ **Kekurangan:** {data['kekurangan']}\n\n"
                self.response += f"🌟 **Rekomendasi Wisata di {data['name']}:**\n"
                
                # Logika Mengelompokkan Spot Berdasarkan Kategori
                spots_by_cat = {}
                for s_key, s_val in data["spots"].items():
                    cat = s_val["kategori"].capitalize()
                    if cat not in spots_by_cat:
                        spots_by_cat[cat] = []
                    spots_by_cat[cat].append(s_val)
                
                # Mencetak daftar wisata yang sudah dikelompokkan
                for cat, spots in spots_by_cat.items():
                    self.response += f"\n🏷️ **Kategori: {cat}**\n"
                    for s in spots:
                        self.response += f"- **{s['name']}**: {s['desc']}\n"
                        
                self.response += "\n---\n\n" # Garis pembatas antar kota
                
                # Masukkan saran tombol untuk spot-spot yang ditemukan
                for s_key, s_val in data["spots"].items():
                    self.suggested_actions.append(s_val["name"])
                    
            self.response += "*Sebutkan nama spesifik tempat di atas jika ingin tahu detail kelebihan dan kekurangannya!*"
            return

        # Menjawab: "rekomendasi wisata jawa tengah", "semua wisata"
        if intent == "ASK_ALL_JATENG":
            self.response = "📍 **Daftar Destinasi di Jawa Tengah**\nBerikut adalah beberapa kabupaten/kota beserta kelebihan dan kekurangannya:\n\n"
            # Dibatasi 5 saja saat dilist agar chat tidak kepanjangan/lag, bisa disesuaikan
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

        # Menjawab: "rekomendasi wisata alam", "keindahan alam"
        if intent == "ASK_NATURE":
            nature_spots = self.nlp.get_nature_spots()
            self.response = "🌿 **Rekomendasi Wisata Alam Pilihan di Jawa Tengah**\n\n"
            # Tampilkan maksimal 5 wisata alam agar rapi
            for city_name, spot in nature_spots[:5]:
                self.response += f"**{spot['name']} ({city_name})**\n"
                self.response += f"📖 {spot['desc']}\n"
                self.response += f"✅ **Kelebihan:** {spot['kelebihan']}\n"
                self.response += f"❌ **Kekurangan:** {spot['kekurangan']}\n\n"
            self.suggested_actions = ["Bukit Sikunir", "Karimunjawa"]
            return

        # Menjawab: "kelebihan kota lama", "lawang sewu"
        if intent == "ASK_SPOT_DETAIL" and spot_key:
            city_data = self.nlp.destinations[spot_prov_key]
            spot_data = city_data["spots"][spot_key]
            
            self.response = f"📸 **Detail Destinasi: {spot_data['name']} ({city_data['name']})**\n\n"
            self.response += f"📝 **Deskripsi:**\n{spot_data['desc']}\n\n"
            self.response += f"✅ **Kelebihan Tempat Ini:**\n{spot_data['kelebihan']}\n\n"
            self.response += f"❌ **Kekurangan / Hal Perhatian:**\n{spot_data['kekurangan']}\n"
            
            self.suggested_actions = ["Rekomendasi Alam", "Wisata Jateng Lainnya"]
            return

        # Menjawab info jika pengguna hanya mengetik nama kota (misal: "semarang")
        if intent == "ASK_CITY_INFO" and dest_key:
            data = self.nlp.destinations[dest_key]
            self.response = f"Kamu memilih **{data['name']}** {data['emoji']}\n\n"
            self.response += f"✅ **Kelebihan:** {data['kelebihan']}\n"
            self.response += f"❌ **Kekurangan:** {data['kekurangan']}\n\n"
            self.response += "Destinasi populer di sini:\n"
            for s_key, s_val in data["spots"].items():
                self.response += f"- **{s_val['name']}**\n"
            self.response += "\nSebutkan nama tempat di atas jika ingin tahu detailnya!"
            
            for s_key, s_val in data["spots"].items():
                self.suggested_actions.append(s_val["name"])
            return

        # Fallback 
        self.response = "Maaf, saya belum menangkap maksudnya atau destinasinya belum terdaftar. Bisa gunakan kata kunci seperti 'Wisata Alam', 'Semarang', atau 'Lawang Sewu'?"