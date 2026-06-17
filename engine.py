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
        
        if re.search(r"\b(reset|ulang|kembali|awal|home|mulai lagi)\b", text): 
            return "RESET"

        if re.search(r"\b(halo|hai|hey|pagi|siang|sore|malam|assalamualaikum)\b", text): 
            return "GREETING"

        if re.search(r"\b(siapa kamu|kamu siapa|namamu|apa kabar|kabar|terima kasih|makasih|thanks|pencipta|dibuat oleh|bisa apa|fungsi bot)\b", text):
            return "GENERAL_QA"
            
        if re.search(r"\b(berapa lama|berapa jam|durasi|jarak|berapa km|lewat mana|estimasi|perjalanan)\b", text) or (re.search(r"\bdari\b", text) and re.search(r"\bke\b", text)):
            return "ASK_TRAVEL_ESTIMATION"
        
        # ── FITUR BARU: DETEKSI INTENT KULINER, TRANSPORT, BUDGET, TIMING ──
        if re.search(r"\b(kuliner|makan|oleh-oleh|khas|restoran|warung|jajanan|lumpia|mie ongklok)\b", text):
            return "ASK_CULINARY"
            
        if re.search(r"\b(transport|transportasi|rute|naik apa|akses|stasiun|bandara|terminal|bus|jalan|gojek|grab|mobil|motor)\b", text):
            return "ASK_TRANSPORT"
            
        if re.search(r"\b(budget|biaya|harga|tiket|gratis|bayar|dana|ongkos|rupiah|murah|mahal)\b", text):
            return "ASK_BUDGET"
            
        if re.search(r"\b(waktu terbaik|bulan apa|jam berapa|kapan|cuaca|musim|kapan pas|jam berkunjung)\b", text):
            return "ASK_TIMING"
        
        # Deteksi info kota & spot tetap berada di bawah chitchat & spesifik info
        dest_keys = self.extract_destinations(text)
        if dest_keys: 
            return "ASK_CITY_INFO"

        spot_name, prov_key = self.extract_spot(text)
        if spot_name: 
            return "ASK_SPOT_DETAIL"
            
        if re.search(r"\b(alam|gunung|pantai|air terjun|curug|danau|telaga|hutan|bukit)\b", text): 
            return "ASK_NATURE"
            
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
