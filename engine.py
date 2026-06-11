import re
# Mengimpor data dari file terpisah yang akan kita buat nanti
from data_destinations import FULL_DESTINATIONS

class NLPEngine:
    def __init__(self):
        self.destinations = FULL_DESTINATIONS

        # Membangun pemetaan spot wisata otomatis
        self.spot_map = {}
        for prov_key, prov_data in self.destinations.items():
            for spot_key, spot_info in prov_data.get("spots", {}).items():
                self.spot_map[spot_key.lower()] = prov_key

    def detect_intent(self, text):
        text = text.lower().strip()
        
        # 1. Deteksi Sapaan (Halo)
        if re.search(r"\b(halo|hai|hey|pagi|siang|sore|malam|assalamualaikum)\b", text): 
            return "GREETING"

        # 2. Reset / Ulangi
        if re.search(r"\b(reset|ulang|kembali|awal|home|mulai lagi)\b", text): 
            return "RESET"
        
        # 3. Deteksi Info Kota/Kabupaten (Menggunakan extract_destinations yang baru)
        dest_keys = self.extract_destinations(text)
        if dest_keys: # Jika list tidak kosong
            return "ASK_CITY_INFO"

        # 4. Deteksi Spot Spesifik 
        spot_name, prov_key = self.extract_spot(text)
        if spot_name: 
            return "ASK_SPOT_DETAIL"
            
        # 5. Deteksi Kategori Alam 
        if re.search(r"\b(alam|gunung|pantai|air terjun|curug|danau|telaga|hutan|bukit)\b", text): 
            return "ASK_NATURE"
            
        # 6. Deteksi Rekomendasi Umum / Terbaik
        if re.search(r"\b(rekomendasi|terbaik|bagus|wisata apa aja|semua wisata|daftar wisata|jateng)\b", text): 
            return "ASK_BEST_RECOMMENDATION"
        
        return "UNKNOWN"

    # UBAH NAMA METHOD INI MENJADI extract_destinations DAN BUAT MENGEMBALIKAN LIST
    def extract_destinations(self, text):
        text_lower = text.lower()
        found_dests = [] # Buat list kosong untuk menampung semua kota yang terdeteksi
        for dest_key in self.destinations.keys():
            if re.search(rf"\b{re.escape(dest_key)}\b", text_lower):
                found_dests.append(dest_key) # Masukkan ke list, jangan langsung di-return
        return found_dests
        return None

    def extract_spot(self, text):
        text_lower = text.lower()
        for spot_key, prov_key in self.spot_map.items():
            if re.search(rf"\b{re.escape(spot_key)}\b", text_lower):
                return spot_key, prov_key
        return None, None

    def get_nature_spots(self):
        nature_spots = []
        for prov_key, prov_data in self.destinations.items():
            for spot_key, spot_info in prov_data.get("spots", {}).items():
                if spot_info["kategori"] == "alam":
                    nature_spots.append((prov_data["name"], spot_info))
        return nature_spots