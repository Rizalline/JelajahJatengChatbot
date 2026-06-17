import re
from data_destinations import FULL_DESTINATIONS

class NLPEngine:
    def __init__(self):
        self.destinations = FULL_DESTINATIONS
        self.spot_map = {}
        for prov_key, prov_data in self.destinations.items():
            for spot_key, spot_info in prov_data.get("spots", {}).items():
                self.spot_map[spot_key.lower()] = prov_key

    def detect_intent(self, text):
        text = text.lower().strip()
        
        # ── PRIORITY 1: Chat Manajemen & Greeting ──
        if re.search(r"\b(reset|clear|ulang|kembali|awal|home|mulai lagi)\b", text): 
            return "RESET"

        if re.search(r"\b(halo|hai|hey|pagi|siang|sore|malam|assalamualaikum)\b", text): 
            return "GREETING"

        if re.search(r"\b(siapa kamu|kamu siapa|namamu|apa kabar|kabar|terima kasih|makasih|thanks|pencipta|dibuat|bisa apa|fungsi)\b", text):
            return "GENERAL_QA"
            
        # ── PRIORITY 2: Fitur Spesifik Mandiri (Anti-Bajak) ──
        if re.search(r"\b(berapa lama|berapa jam|durasi|jarak|berapa km|lewat mana|estimasi|perjalanan)\b", text) or (re.search(r"\bdari\b", text) and re.search(r"\bke\b", text)):
            return "ASK_TRAVEL_ESTIMATION"
            
        if re.search(r"\b(kuliner|makan|oleh-oleh|khas|restoran|warung|jajanan)\b", text):
            return "ASK_CULINARY"
            
        if re.search(r"\b(transport|transportasi|rute|naik apa|akses|stasiun|bus|mobil|motor)\b", text):
            return "ASK_TRANSPORT"
            
        if re.search(r"\b(budget|biaya|harga|tiket|gratis|bayar|dana|ongkos)\b", text):
            return "ASK_BUDGET"
            
        if re.search(r"\b(waktu terbaik|bulan apa|jam berapa|kapan|cuaca|musim)\b", text):
            return "ASK_TIMING"
        
        # ── PRIORITY 3: Info Destinasi Umum & Rekomendasi ──
        spot_name, prov_key = self.extract_spot(text)
        if spot_name: 
            return "ASK_SPOT_DETAIL"

        dest_keys = self.extract_destinations(text)
        if dest_keys: 
            return "ASK_CITY_INFO"
            
        if re.search(r"\b(alam|gunung|pantai|air terjun|curug|danau|telaga|hutan|bukit|pinus)\b", text): 
            return "ASK_NATURE"
            
        if re.search(r"\b(semua kota|daftar kabupaten|daftar kota|seluruh jateng)\b", text):
            return "ASK_ALL_JATENG"
            
        if re.search(r"\b(rekomendasi|terbaik|bagus|wisata apa aja|semua wisata|daftar wisata|jateng|liburan)\b", text): 
            return "ASK_BEST_RECOMMENDATION"
        
        return "UNKNOWN"

    def extract_destinations(self, text):
        text_lower = text.lower()
        found_dests = []
        
        # Urutkan nama kota berdasarkan teks terpanjang (descending) 
        # Supaya "semarang kab" dicek duluan daripada "semarang" biasa
        sorted_keys = sorted(self.destinations.keys(), key=len, reverse=True)
        
        matched_indices = set()
        for dest_key in sorted_keys:
            for match in re.finditer(rf"\b{re.escape(dest_key)}\b", text_lower):
                start, end = match.span()
                # Pastikan potongan kata ini belum diklaim oleh nama kota yang lebih panjang
                if not any(idx in matched_indices for idx in range(start, end)):
                    found_dests.append(dest_key)
                    for idx in range(start, end):
                        matched_indices.add(idx)
                        
        return found_dests

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
