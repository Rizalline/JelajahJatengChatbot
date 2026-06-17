# data_destinations.py

FULL_DESTINATIONS = {
    # ═══════════════════════════════════════════════════════════════
    # === 6 KOTA MADIYA ===
    # ═══════════════════════════════════════════════════════════════
    "semarang": {
        "emoji": "🏙️", "name": "Kota Semarang", #[cite: 3]
        "kelebihan": "Pusat kuliner, akses bandara dan stasiun mudah, perpaduan wisata sejarah yang kuat.", #[cite: 3]
        "kekurangan": "Cuaca siang hari sangat terik dan beberapa daerah pesisir rawan rob.", #[cite: 3]
        "kuliner": "Lumpia Gang Lombok, Tahu Gimbal Pak H. Edy, Soto Bangkes, dan Wingko Babat.",
        "transportasi": "Sangat mudah. Bisa via Stasiun Tawang/Poncol, Bandara Ahmad Yani, atau pakai BRT Trans Semarang.",
        "budget": "Sangat terjangkau. Tiket masuk wisata sejarah rata-rata Rp10.000 - Rp25.000. Kulineran mulai Rp15.000 per porsi.",
        "waktu_terbaik": "Sore hari pukul 16.00 WIB ke atas (hindari terik matahari siang) atau saat malam hari di Kota Lama.",
        "spots": {
            "kota lama": {
                "name": "Kota Lama Semarang", "kategori": "sejarah", #[cite: 3]
                "desc": "Kawasan cagar budaya dengan gedung peninggalan Hindia Belanda abad ke-18.", #[cite: 3]
                "kelebihan": "Sangat estetik untuk foto, banyak kafe klasik, ramah pejalan kaki.", #[cite: 3]
                "kekurangan": "Sangat panas di siang hari, parkir mobil lumayan jauh." #[cite: 3]
            },
            "lawang sewu": {
                "name": "Lawang Sewu", "kategori": "sejarah", #[cite: 3]
                "desc": "Gedung bekas kantor kereta api Hindia Belanda yang ikonik dengan ribuan pintu.", #[cite: 3]
                "kelebihan": "Penuh nilai sejarah dan arsitektur megah.", #[cite: 3]
                "kekurangan": "Sangat padat saat liburan, butuh pemandu agar mengerti sejarahnya." #[cite: 3]
            }
        }
    },
    "surakarta": {
        "emoji": "🏯", "name": "Kota Surakarta (Solo)", #[cite: 3]
        "kelebihan": "Biaya hidup dan kuliner sangat murah, kaya akan budaya keraton Jawa.", #[cite: 3]
        "kekurangan": "Lalu lintas cukup padat di jam berangkat/pulang kerja.", #[cite: 3]
        "kuliner": "Selat Solo Viens, Timlo Sastro, Nasi Liwet Bu Sri, dan Serabi Notosuman.",
        "transportasi": "Sangat mudah. Akses via Stasiun Solo Balapan/Purwosari, Bandara Adi Soemarmo, atau naik Bus BST (Batik Solo Trans).",
        "budget": "Sangat hemat. Tiket masuk museum/keraton berkisar Rp10.000 - Rp20.000. Makan besar melimpah mulai dari Rp12.000.",
        "waktu_terbaik": "Pagi hari untuk keliling Keraton/Museum, atau malam hari untuk wisata kuliner malam di daerah Galabo.",
        "spots": {
            "keraton kasunanan": {
                "name": "Keraton Kasunanan Surakarta", "kategori": "sejarah", #[cite: 3]
                "desc": "Istana resmi Kasunanan Surakarta yang menyimpan koleksi pusaka dan benda bersejarah.", #[cite: 3]
                "kelebihan": "Merasakan nuansa kerajaan Jawa asli, tiket murah.", #[cite: 3]
                "kekurangan": "Ada aturan berpakaian ketat (tidak boleh celana pendek)." #[cite: 3]
            }
        }
    },
    "magelang kota": {
        "emoji": "🌸", "name": "Kota Magelang", #[cite: 3]
        "kelebihan": "Kota kecil yang rapi, bersih, dan berhawa sejuk.", #[cite: 3]
        "kekurangan": "Pilihan wisata malam sangat terbatas.", #[cite: 3]
        "kuliner": "Kupat Tahu Pojok, Sop Senerek Bu Atmo, dan Es Murni Magelang.",
        "transportasi": "Akses darat strategis lewat jalur utama Semarang-Jogja. Bisa naik bus antarkota atau angkutan lokal.",
        "budget": "Murah meriah. Tiket masuk taman hiburan lokal berkisar Rp15.000 - Rp25.000. Biaya makan relatif murah.",
        "waktu_terbaik": "Pagi hari atau sore hari yang teduh untuk bersantai menikmati kebersihan tata kota di area Alun-alun.",
        "spots": {
            "taman kyai langgeng": {
                "name": "Taman Kyai Langgeng", "kategori": "alam", #[cite: 3]
                "desc": "Taman wisata rekreasi keluarga yang rimbun dengan wahana permainan.", #[cite: 3]
                "kelebihan": "Cocok untuk liburan keluarga dan anak-anak, banyak pepohonan.", #[cite: 3]
                "kekurangan": "Beberapa wahana terlihat sudah termakan usia." #[cite: 3]
            }
        }
    },
    "pekalongan kota": {
        "emoji": "👘", "name": "Kota Pekalongan", #[cite: 3]
        "kelebihan": "Pusatnya batik nasional, surganya belanja baju batik murah.", #[cite: 3]
        "kekurangan": "Udara cukup panas dan pesisirnya rentan banjir pasang.", #[cite: 3]
        "kuliner": "Nasi Megono, Garang Asem Masduki, dan Tauto Pekalongan (Soto bumbu tauco).",
        "transportasi": "Sangat mudah dijangkau via jalur kereta api lintas utara (Stasiun Pekalongan) atau bus via Tol Trans Jawa.",
        "budget": "Ekonomis. Tiket masuk museum sangat murah (di bawah Rp10.000). Budget selebihnya fleksibel untuk belanja batik.",
        "waktu_terbaik": "Pagi hingga siang hari, waktu terbaik di mana pasar grosir batik dan museum sedang beroperasi penuh.",
        "spots": {
            "museum batik": {
                "name": "Museum Batik Pekalongan", "kategori": "budaya", #[cite: 3]
                "desc": "Museum yang menyimpan ribuan koleksi batik dari seluruh Nusantara.", #[cite: 3]
                "kelebihan": "Sangat edukatif, bisa belajar langsung cara membatik.", #[cite: 3]
                "kekurangan": "Ruangan pameran tidak terlalu besar." #[cite: 3]
            }
        }
    },
    "salatiga": {
        "emoji": "🍃", "name": "Kota Salatiga", #[cite: 3]
        "kelebihan": "Salah satu kota paling toleran di Indonesia, udaranya sangat sejuk.", #[cite: 3]
        "kekurangan": "Pusat perbelanjaan dan wisata modern masih terbatas.", #[cite: 3]
        "kuliner": "Ronde Jago Salatiga, Enting-enting Gepuk, dan Singkong Keju D-9.",
        "transportasi": "Mudah diakses menggunakan bus AKAP rute Semarang-Solo atau exit tol Salatiga jika bawa kendaraan pribadi.",
        "budget": "Sangat ramah mahasiswa/wisatawan. Nongkrong and kuliner malam di sini tidak menguras kantong.",
        "waktu_terbaik": "Sepanjang hari karena udaranya sejuk alami, terutama malam hari untuk menikmati kehangatan wedang ronde.",
        "spots": {
            "kopeng": {
                "name": "Kopeng Treetop", "kategori": "alam", #[cite: 3]
                "desc": "Kawasan wisata alam pinus dengan aktivitas outbound dan berkemah.", #[cite: 3]
                "kelebihan": "Udara sangat dingin dan segar, wahana outbound sangat menantang.", #[cite: 3]
                "kekurangan": "Akses jalan cukup menanjak dari pusat kota." #[cite: 3]
            }
        }
    },
    "tegal kota": {
        "emoji": "☕", "name": "Kota Tegal", #[cite: 3]
        "kelebihan": "Kuliner khas yang lezat (sate batibul, teh poci) dan akses pantura yang strategis.", #[cite: 3]
        "kekurangan": "Suhu sangat panas, minim wisata alam.", #[cite: 3]
        "kuliner": "Sate Kambing Batibul (Bawah Tiga Bulan), Kupat Blengong, dan Nasi Ponggol.",
        "transportasi": "Akses utama via lintas Pantura Jawa. Bisa naik kereta api turun di Stasiun Tegal atau kendaraan pribadi via Tol.",
        "budget": "Murah untuk ukuran kota kuliner. Tiket masuk kawasan pantai berkisar Rp5.000 - Rp15.000.",
        "waktu_terbaik": "Sore hari pukul 16.00 WIB untuk menikmati hidangan laut di pantai sembari berburu sunset and minum teh poci.",
        "spots": {
            "pantai alam indah": {
                "name": "Pantai Alam Indah (PAI)", "kategori": "alam", #[cite: 3]
                "desc": "Pantai utara Jawa yang menjadi ikon rekreasi warga Tegal.", #[cite: 3]
                "kelebihan": "Akses sangat dekat dari pusat kota, banyak pedagang kuliner laut.", #[cite: 3]
                "kekurangan": "Pasir pantai tidak putih dan air laut kurang jernih." #[cite: 3]
            }
        }
    },

    # ═══════════════════════════════════════════════════════════════
    # === 29 KABUPATEN ===
    # ═══════════════════════════════════════════════════════════════
    "magelang": {
        "emoji": "🛕", "name": "Kabupaten Magelang", #[cite: 3]
        "kelebihan": "Wisata alam dan candi kelas dunia, dikelilingi banyak gunung.", #[cite: 3]
        "kekurangan": "Akses antar tempat wisata agak jauh.", #[cite: 3]
        "kuliner": "Kupat Tahu Pojok, Mangut Beong Magelang (super pedas), and Sop Senerek.",
        "transportasi": "Bisa naik bus antarkota jurusan Jogja-Magelang, lalu lanjut menggunakan transportasi lokal, sewa motor, atau ojek online.",
        "budget": "Tiket Candi Borobudur domestik mulai Rp50.000 (pelataran). Kuliner lokal sangat ramah kantong, mulai Rp12.000.",
        "waktu_terbaik": "Pagi hari sekali (pukul 06.00 WIB) untuk Borobudur, atau musim kemarau agar pemandangan gunung di Nepal Van Java tidak tertutup kabut.",
        "spots": {
            "candi borobudur": {
                "name": "Candi Borobudur", "kategori": "sejarah", #[cite: 3]
                "desc": "Candi Buddha terbesar di dunia dari abad ke-9.", #[cite: 3]
                "kelebihan": "Warisan dunia UNESCO, sangat megah dan terawat baik.", #[cite: 3]
                "kekurangan": "Tiket naik ke struktur candi lumayan mahal dan kuotanya dibatasi." #[cite: 3]
            },
            "nepal van java": {
                "name": "Nepal Van Java", "kategori": "alam", #[cite: 3]
                "desc": "Desa bertumpuk di lereng Gunung Sumbing yang mirip Nepal.", #[cite: 3]
                "kelebihan": "Pemandangan luar biasa, sangat estetik untuk foto.", #[cite: 3]
                "kekurangan": "Jalan sangat curam, rem motor matic rawan blong." #[cite: 3]
            }
        }
    },
    "wonosobo": {
        "emoji": "⛰️", "name": "Kabupaten Wonosobo", #[cite: 3]
        "kelebihan": "Hawa paling dingin di Jateng, pemandangan pegunungan memukau.", #[cite: 3]
        "kekurangan": "Sering macet di jalur utama saat libur panjang, bisa terjadi fenomena embun es ekstrem.", #[cite: 3]
        "kuliner": "Mie Ongklok Longkrang, Tempe Kemul hangat, dan buah Carica khas Dieng.",
        "transportasi": "Disarankan kendaraan pribadi/sewa yang kuat menanjak. Opsi umum bisa naik mikrobus dari Terminal Mendolo.",
        "budget": "Kategori menengah. Tiket kawasan Dieng sekitar Rp20.000 - Rp30.000. Sewa Jeep mulai dari Rp400.000.",
        "waktu_terbaik": "Bulan Juli - Agustus (Musim kemarau) untuk berburu Golden Sunrise bersih dan peluang melihat embun es di Dieng.",
        "spots": {
            "bukit sikunir": {
                "name": "Bukit Sikunir", "kategori": "alam", #[cite: 3]
                "desc": "Tempat melihat golden sunrise terbaik se-Asia Tenggara di Dieng.", #[cite: 3]
                "kelebihan": "Jalur pendakian mudah and pendek, sunrise sangat indah.", #[cite: 3]
                "kekurangan": "Suhu bisa mendekati 0 derajat celcius, lautan manusia saat akhir pekan." #[cite: 3]
            }
        }
    },
    "banjarnegara": {
        "emoji": "🌋", "name": "Kabupaten Banjarnegara", #[cite: 3]
        "kelebihan": "Berbagi kawasan Dieng dengan Wonosobo, pusat arung jeram.", #[cite: 3]
        "kekurangan": "Beberapa infrastruktur jalan antar desa belum rata.", #[cite: 3]
        "kuliner": "Dawet Ayu Banjarnegara asli, Combro Kalipalet, dan Manisan Carica Dieng.",
        "transportasi": "Akses via darat jalur tengah Jawa. Menuju Dieng atas jalurnya berkelok and menanjak tajam.",
        "budget": "Terjangkau. Tiket masuk objek wisata alam vulkanik Dieng kulon sekitar Rp20.000.",
        "waktu_terbaik": "Pagi hari sebelum bau belerang kawah terik menguap menyengat and sebelum kabut pegunungan turun.",
        "spots": {
            "kawah sikidang": {
                "name": "Kawah Sikidang", "kategori": "alam", #[cite: 3]
                "desc": "Kawah vulkanik aktif dengan lumpur mendidih yang bisa dilihat dari dekat.", #[cite: 3]
                "kelebihan": "Unik dan mudah diakses tanpa harus mendaki.", #[cite: 3]
                "kekurangan": "Bau belerang sangat menyengat, wajib pakai masker." #[cite: 3]
            }
        }
    },
    "jepara": {
        "emoji": "🏝️", "name": "Kabupaten Jepara", #[cite: 3]
        "kelebihan": "Pusat ukir kayu terbaik, memiliki wisata kepulauan berpasir putih.", #[cite: 3]
        "kekurangan": "Akses pelabuhan bisa ditutup jika ombak tinggi.", #[cite: 3]
        "kuliner": "Pindang Serani Jepara, Horok-horok, dan es dawet kuluban.",
        "transportasi": "Naik bus ke Terminal Jepara, dilanjutkan dengan kapal Express Bahari atau KMP Siginjai dari Pelabuhan Kartini ke Karimunjawa.",
        "budget": "Menengah ke atas jika menyeberang ke pulau (biaya kapal & paket snorkeling). Wisata pantai daratan utama sangat murah.",
        "waktu_terbaik": "Maret hingga Oktober (musim kemarau) saat gelombang air di Laut Jawa tenang and jernih untuk penyeberangan aman.",
        "spots": {
            "karimunjawa": {
                "name": "Taman Nasional Karimunjawa", "kategori": "alam", #[cite: 3]
                "desc": "Kepulauan dengan pantai pasir putih dan biota laut yang kaya.", #[cite: 3]
                "kelebihan": "Bisa snorkeling dengan terumbu karang indah, air sangat jernih.", #[cite: 3]
                "kekurangan": "Butuh menyeberang kapal berjam-jam, sinyal internet terbatas." #[cite: 3]
            }
        }
    },
    "karanganyar": {
        "emoji": "🌲", "name": "Kabupaten Karanganyar", #[cite: 3]
        "kelebihan": "Pusat wisata alam di lereng Gunung Lawu, banyak resto estetik.", #[cite: 3]
        "kekurangan": "Jalan pegunungan berliku dan sering diselimuti kabut tebal.", #[cite: 3]
        "kuliner": "Sate Kelinci Tawangmangu, Sate Jamur, Timlo Lawu, and Wedang Uwuh.",
        "transportasi": "Medan jalan menanjak tinggi. Disarankan bawa kendaraan pribadi yang prima atau sewa dari Kota Solo (sekitar 1 jam rute darat).",
        "budget": "Terjangkau. Tiket masuk candi bersejarah berkisar Rp10.000 - Rp20.000. Pengeluaran lain biasanya untuk kafe/resto estetik lereng Lawu.",
        "waktu_terbaik": "Pagi hari pukul 08.00 - 11.00 WIB agar mendapatkan pemandangan gunung bersih sebelum tertutup kabut tebal sore hari.",
        "spots": {
            "candi cetho": {
                "name": "Candi Cetho", "kategori": "sejarah", #[cite: 3]
                "desc": "Candi Hindu berbentuk punden berundak mirip gerbang di Bali.", #[cite: 3]
                "kelebihan": "Pemandangan dari atas candi sangat indah seperti di atas awan.", #[cite: 3]
                "kekurangan": "Tanjakan menuju candi sangat curam dan ekstrem." #[cite: 3]
            }
        }
    },
    "banyumas": {
        "emoji": "💧", "name": "Kabupaten Banyumas (Purwokerto)", #[cite: 3]
        "kelebihan": "Pusat kuliner tempe mendoan, wisata air terjun (curug) melimpah.", #[cite: 3]
        "kekurangan": "Curah hujan sangat tinggi sepanjang tahun.", #[cite: 3]
        "kuliner": "Tempe Mendoan Jumbo Sawangan, Soto Sokaraja (bumbu kacang), and Gethuk Goreng Sokaraja.",
        "transportasi": "Sangat mudah diakses lewat Stasiun Purwokerto (jalur kereta utama selatan) atau Bus via Terminal Bulupitu.",
        "budget": "Sangat ramah dompet. Tiket masuk lokawisata alam Baturraden berkisar Rp20.000 - Rp25.000.",
        "waktu_terbaik": "Pagi hari cerah untuk mengeksplorasi curug (air terjun) sebelum area kaki gunung diguyur hujan pada sore hari.",
        "spots": {
            "baturraden": {
                "name": "Lokawisata Baturraden", "kategori": "alam", #[cite: 3]
                "desc": "Kawasan wisata terpadu dengan pemandian air panas dan air terjun.", #[cite: 3]
                "kelebihan": "Udara segar, fasilitas sangat lengkap untuk keluarga.", #[cite: 3]
                "kekurangan": "Cukup ramai dan padat pengunjung di hari libur nasional." #[cite: 3]
            }
        }
    },
    "kebumen": {
        "emoji": "🌊", "name": "Kabupaten Kebumen", #[cite: 3]
        "kelebihan": "Memiliki garis pantai selatan yang sangat panjang dan indah.", #[cite: 3]
        "kekurangan": "Ombak pantai selatan sangat berbahaya untuk berenang.", #[cite: 3]
        "kuliner": "Nasi Penggel, Sate Ambal (bumbu tempe), dan cemilan Lanting Kebumen.",
        "transportasi": "Jalur darat lintas pantai selatan (Pansela) atau naik kereta api turun di Stasiun Kebumen/Kutoarjo.",
        "budget": "Murah meriah. Tiket masuk pantai-pantai eksotis berkisar Rp10.000 - Rp20.000 per orang.",
        "waktu_terbaik": "Sore hari pukul 16.00 WIB untuk menikmati lanskap pemandangan sunset dari atas bukit hijau Menganti.",
        "spots": {
            "pantai menganti": {
                "name": "Pantai Menganti", "kategori": "alam", #[cite: 3]
                "desc": "Pantai dengan pasir putih yang dikelilingi tebing-tebing karst hijau.", #[cite: 3]
                "kelebihan": "Sering dijuluki New Zealand-nya Indonesia, pemandangan luar biasa.", #[cite: 3]
                "kekurangan": "Angin sangat kencang, rute turun ke pantai cukup menantang." #[cite: 3]
            }
        }
    },
    "klaten": {
        "emoji": "🏊", "name": "Kabupaten Klaten", #[cite: 3]
        "kelebihan": "Kota seribu umbul (mata air tawar), candi-candi yang eksotis.", #[cite: 3]
        "kekurangan": "Beberapa umbul sangat padat di akhir pekan.", #[cite: 3]
        "kuliner": "Ayam Panggang Klaten, Sop Ayam Pak Min Klaten yang legendaris, and Geplak.",
        "transportasi": "Sangat mudah diakses karena terletak di antara Jogja-Solo. Bisa naik KRL Commuter Line turun di Stasiun Klaten.",
        "budget": "Sangat ekonomis. Tiket masuk umbul (mata air alami) rata-rata hanya Rp5.000 - Rp15.000 saja.",
        "waktu_terbaik": "Pagi hari pukul 07.00 - 09.00 WIB saat air umbul masih sangat jernih bening and pengunjung belum membeludak.",
        "spots": {
            "umbul ponggok": {
                "name": "Umbul Ponggok", "kategori": "alam", #[cite: 3]
                "desc": "Mata air jernih yang dijadikan tempat foto underwater dengan properti unik.", #[cite: 3]
                "kelebihan": "Bisa foto di bawah air dengan motor, TV, atau tenda.", #[cite: 3]
                "kekurangan": "Bagi yang tidak bisa berenang harus menyewa pelampung/pemandu." #[cite: 3]
            }
        }
    },
    "boyolali": {
        "emoji": "🐄", "name": "Kabupaten Boyolali", #[cite: 3]
        "kelebihan": "Kota susu yang sejuk di lereng Gunung Merapi dan Merbabu.", #[cite: 3]
        "kekurangan": "Wisata masih tersebar dan butuh kendaraan pribadi.", #[cite: 3]
        "kuliner": "Susu Segar Boyolali, Soto Daging Sapi Boyolali, and Tahu Susu.",
        "transportasi": "Akses jalur darat via Semarang-Solo. Menuju Selo atas membutuhkan performa mesin kendaraan yang kuat menanjak.",
        "budget": "Hemat. Biaya masuk tempat rekreasi lereng gunung and harga nongkrong di kafe Selo sangat aman di kantong.",
        "waktu_terbaik": "Pagi hari saat cuaca cerah benderang agar megahnya Gunung Merapi and Merbabu terlihat jelas tanpa tertutup awan mendung.",
        "spots": {
            "selo": {
                "name": "Kawasan Selo", "kategori": "alam", #[cite: 3]
                "desc": "Lembah indah yang diapit Gunung Merapi dan Merbabu.", #[cite: 3]
                "kelebihan": "Pemandangan gunung sangat dekat, cocok untuk ngopi santai.", #[cite: 3]
                "kekurangan": "Berada di zona rawan jika Merapi sedang erupsi tinggi." #[cite: 3]
            }
        }
    },
    "semarang kab": {
        "emoji": "🚂", "name": "Kabupaten Semarang (Ungaran/Ambarawa)", #[cite: 3]
        "kelebihan": "Pusat wisata sejarah kereta api dan candi ikonik peninggalan Mataram Kuno.", #[cite: 3]
        "kekurangan": "Lalu lintas utama Semarang-Solo sering macet.", #[cite: 3]
        "kuliner": "Tahu Serasi Bandungan, Sate Sapi Pak Kempleng, and Pecel Candi Gedong Songo.",
        "transportasi": "Akses jalan utama antar kota Semarang-Solo. Menuju spot atas (Bandungan) direkomendasikan memakai kendaraan pribadi atau ojek lokal.",
        "budget": "Terjangkau. Tiket masuk candi pegunungan berkisar Rp15.000 - Rp25.000. Pengeluaran opsional untuk sewa kuda trekking.",
        "waktu_terbaik": "Pagi hari sejuk agar tidak terlalu lelah and panas saat melakukan trekking berjalan kaki menanjak di kompleks candi.",
        "spots": {
            "candi gedong songo": {
                "name": "Candi Gedong Songo", "kategori": "sejarah", #[cite: 3]
                "desc": "Sembilan candi yang tersebar di lereng Gunung Ungaran.", #[cite: 3]
                "kelebihan": "Berada di ketinggian dengan view alam indah, ada penyewaan kuda.", #[cite: 3]
                "kekurangan": "Harus berjalan kaki cukup jauh/nanjak untuk melihat semua candinya." #[cite: 3]
            }
        }
    },
    "demak": {
        "emoji": "🕌", "name": "Kabupaten Demak", #[cite: 3]
        "kelebihan": "Pusat ziarah dan wisata religi Islam terkuat di Jawa Tengah.", #[cite: 3]
        "kekurangan": "Beberapa wilayah sering terdampak banjir rob parah.", #[cite: 3]
        "kuliner": "Sop Balungan Demak, Nasi Kebuli, dan Jamu Coro.",
        "transportasi": "Bersebelahan langsung dengan Semarang timur. Bisa ditempuh via jalur Pantura darat naik bus kota atau kendaraan pribadi.",
        "budget": "Sangat murah karena berorientasi wisata religi/ziarah. Tarif masuk masjid utama berbasis sedekah/infak.",
        "waktu_terbaik": "Pagi hari yang tenang atau sore hari menjelang magrib untuk mendapatkan atmosfer spiritual religi yang syahdu.",
        "spots": {
            "masjid agung demak": {
                "name": "Masjid Agung Demak", "kategori": "sejarah", #[cite: 3]
                "desc": "Salah satu masjid tertua di Indonesia, peninggalan Wali Songo.", #[cite: 3]
                "kelebihan": "Nilai spiritual dan sejarah yang sangat mendalam.", #[cite: 3]
                "kekurangan": "Area parkir utama seringkali penuh oleh bus peziarah." #[cite: 3]
            }
        }
    },
    "kudus": {
        "emoji": "🚬", "name": "Kabupaten Kudus", #[cite: 3]
        "kelebihan": "Kota kretek dengan kuliner unik (Soto Kudus) dan toleransi sejarah yang kuat.", #[cite: 3]
        "kekurangan": "Udara cukup panas di pusat kota.", #[cite: 3]
        "kuliner": "Soto Kudus mangkok kecil, Sate Kerbau (tekstur gurih unik), and Lentog Tanjung.",
        "transportasi": "Akses via bus darat jalur Pantura Timur. Sekitar 1,5 jam perjalanan kendaraan dari Kota Semarang.",
        "budget": "Ekonomis. Masuk kawasan Menara Kudus gratis/infak sukarela, jajanan tradisional di sekitarnya sangat ramah kantong.",
        "waktu_terbaik": "Sore atau malam hari saat lampu hias di komplek Menara bata merah mulai menyala, memberikan vibes estetik klasik.",
        "spots": {
            "menara kudus": {
                "name": "Masjid Menara Kudus", "kategori": "sejarah", #[cite: 3]
                "desc": "Masjid dengan menara berbentuk seperti candi Hindu, simbol toleransi Sunan Kudus.", #[cite: 3]
                "kelebihan": "Arsitektur bata merah yang sangat unik dan ikonik.", #[cite: 3]
                "kekurangan": "Jalanan sekitar menara cukup sempit." #[cite: 3]
            }
        }
    },
    "pati": {
        "emoji": "🍛", "name": "Kabupaten Pati", #[cite: 3]
        "kelebihan": "Pusat kuliner Nasi Gandul, banyak wisata agro.", #[cite: 3]
        "kekurangan": "Jarak antar kecamatan cukup jauh.", #[cite: 3]
        "kuliner": "Nasi Gandul khas Pati, Soto Kemiri, and Petis Runting.",
        "transportasi": "Berada di jalur trans nasional Pantura Timur, mudah dijangkau menggunakan armada bus antarkota atau kendaraan pribadi.",
        "budget": "Sangat terjangkau. Menikmati kuliner malam legendaris Nasi Gandul per porsi mulai dari Rp15.000.",
        "waktu_terbaik": "Sore hari yang santai, waktu yang pas untuk menikmati suasana damai di pinggiran waduk berlatar Gunung Muria.",
        "spots": {
            "waduk gunung rowo": {
                "name": "Waduk Gunung Rowo", "kategori": "alam", #[cite: 3]
                "desc": "Danau buatan peninggalan Belanda yang berlatar Gunung Muria.", #[cite: 3]
                "kelebihan": "Suasana tenang, cocok untuk makan ikan bakar di pinggir waduk.", #[cite: 3]
                "kekurangan": "Kurang terawat di beberapa sudut fasilitas." #[cite: 3]
            }
        }
    },
    "rembang": {
        "emoji": "⚓", "name": "Kabupaten Rembang", #[cite: 3]
        "kelebihan": "Wisata sejarah RA Kartini dan pesona bahari pantura.", #[cite: 3]
        "kekurangan": "Cuaca sangat terik khas pesisir utara.", #[cite: 3]
        "kuliner": "Lontong Tuyuhan, Sate Serepeh, and Sirup Buah Kawis (sirup cola khas Jawa).",
        "transportasi": "Ujung timur provinsi Jateng. Diakses via jalur utama darat Semarang-Surabaya lintas utara menggunakan bus antarkota.",
        "budget": "Murah. Tiket masuk area pantai cemara berkisar Rp5.000 - Rp10.000, kuliner laut lokal harganya bersahabat.",
        "waktu_terbaik": "Pagi hari atau sore pukul 15.30 WIB agar bisa menikmati keteduhan rimbun pohon cemara pantai dengan nyaman.",
        "spots": {
            "pantai karang jahe": {
                "name": "Pantai Karang Jahe", "kategori": "alam", #[cite: 3]
                "desc": "Pantai berpasir putih memanjang yang ditumbuhi banyak pohon cemara.", #[cite: 3]
                "kelebihan": "Pohon cemaranya rimbun, teduh, pasirnya lembut.", #[cite: 3]
                "kekurangan": "Sangat ramai pengunjung lokalan saat akhir pekan." #[cite: 3]
            }
        }
    },
    "blora": {
        "emoji": "🌳", "name": "Kabupaten Blora", #[cite: 3]
        "kelebihan": "Kota Jati dengan sate Blora yang melegenda.", #[cite: 3]
        "kekurangan": "Infrastruktur jalan di pedalaman hutan jati belum sepenuhnya baik.", #[cite: 3]
        "kuliner": "Sate Blora asli (bumbu kacang lembut disiram kuah kuning), Pecel Jati, and Kopi Santen.",
        "transportasi": "Akses via darat lintas tengah, atau bisa naik kereta api turun di Stasiun Cepu Blora.",
        "budget": "Ekonomis. Sistem makan Sate Blora dihitung per tusuk yang habis dimakan. Tiket masuk waduk sangat murah.",
        "waktu_terbaik": "Siang menjelang sore hari, waktu yang nikmat untuk menyantap hidangan kuliner ikan bakar lesehan di pinggiran waduk.",
        "spots": {
            "waduk tempuran": {
                "name": "Waduk Tempuran", "kategori": "alam", #[cite: 3]
                "desc": "Waduk yang digunakan untuk irigasi, perikanan, dan wisata kuliner.", #[cite: 3]
                "kelebihan": "Pusat kuliner ikan bakar lesehan yang lezat dan murah.", #[cite: 3]
                "kekurangan": "Debit air bisa sangat surut di musim kemarau panjang." #[cite: 3]
            }
        }
    },
    "grobogan": {
        "emoji": "🔥", "name": "Kabupaten Grobogan", #[cite: 3]
        "kelebihan": "Pusat fenomena alam unik, kuliner Swike yang terkenal.", #[cite: 3]
        "kekurangan": "Salah satu wilayah terpanas di Jawa Tengah.", #[cite: 3]
        "kuliner": "Swike Purwodadi (ada pilihan olahan ayam/enthok halal), Nasi Becek, and Sego Pager.",
        "transportasi": "Jalur lintas darat tengah penghubung Semarang-Blora. Bisa diakses via kendaraan pribadi atau bus medium.",
        "budget": "Sangat murah. Tiket masuk kawasan situs fenomena alam api abadi berkisar Rp5.000 - Rp10.000.",
        "waktu_terbaik": "Sore hari pukul 16.30 WIB menjelang gelap agar pesona nyala kobaran api alami dari tanah terlihat lebih kontras.",
        "spots": {
            "api abadi mrapen": {
                "name": "Api Abadi Mrapen", "kategori": "alam", #[cite: 3]
                "desc": "Sumber api alam yang keluar dari dalam tanah dan tidak pernah padam.", #[cite: 3]
                "kelebihan": "Fenomena alam langka, sering digunakan untuk obor event olahraga nasional.", #[cite: 3]
                "kekurangan": "Spot utama ukurannya kecil, durasi kunjungan biasanya singkat." #[cite: 3]
            }
        }
    },
    "sragen": {
        "emoji": "💀", "name": "Kabupaten Sragen", #[cite: 3]
        "kelebihan": "Menyimpan situs fosil manusia purba terlengkap di dunia.", #[cite: 3]
        "kekurangan": "Wisata alamnya kalah pamor dibanding kabupaten tetangga (Karanganyar).", #[cite: 3]
        "kuliner": "Sate Kambing Sragen, Soto Girin yang gurih, and Gado-gado khas Sragen.",
        "transportasi": "Sangat strategis. Akses kilat via Tol Trans Jawa (Exit Tol Sragen) atau via kereta api berhenti di Stasiun Sragen.",
        "budget": "Murah. Tiket masuk komplek klaster museum purbakala warisan dunia UNESCO berkisar Rp10.000 - Rp15.000.",
        "waktu_terbaik": "Pagi hingga siang hari sebelum jam operasional museum tutup, sangat ideal untuk agenda studi tur edukasi keluarga.",
        "spots": {
            "museum sangiran": {
                "name": "Museum Purbakala Sangiran", "kategori": "sejarah", #[cite: 3]
                "desc": "Situs warisan dunia tempat ditemukannya fosil manusia purba Homo Erectus.", #[cite: 3]
                "kelebihan": "Koleksi kelas dunia, sangat edukatif dan interaktif.", #[cite: 3]
                "kekurangan": "Cukup jauh dari pusat keramaian Solo." #[cite: 3]
            }
        }
    },
    "sukoharjo": {
        "emoji": "🎸", "name": "Kabupaten Sukoharjo", #[cite: 3]
        "kelebihan": "Pusat perbelanjaan dan wisata modern di Solo Raya.", #[cite: 3]
        "kekurangan": "Sangat padat penduduk dan lalu lintas, sering macet.", #[cite: 3]
        "kuliner": "Alun-alun Sukoharjo Street Food, Sego Kalong, and Nasi Liwet Solo Raya.",
        "transportasi": "Menempel ketat di selatan Kota Solo. Mudah diakses menggunakan ojek online, taksi, atau bus rute perkotaan.",
        "budget": "Kategori menengah. HTM tiket masuk wahana waterpark tematik modern berkisar Rp50.000 - Rp100.000 (tergantung weekend).",
        "waktu_terbaik": "Pagi hari pukul 08.30 WIB untuk bermain air di waterpark agar matahari tidak terlalu terik menyengat kulit.",
        "spots": {
            "pandawa water world": {
                "name": "Pandawa Water World", "kategori": "alam", #[cite: 3]
                "desc": "Taman bermain air tematik dengan tokoh-tokoh pewayangan Mahabharata.", #[cite: 3]
                "kelebihan": "Banyak wahana seru, patung pewayangannya unik.", #[cite: 3]
                "kekurangan": "Harga tiket relatif tinggi." #[cite: 3]
            }
        }
    },
    "wonogiri": {
        "emoji": "🏞️", "name": "Kabupaten Wonogiri", #[cite: 3]
        "kelebihan": "Surganya waduk besar dan kuliner bakso khas Wonogiri.", #[cite: 3]
        "kekurangan": "Jarak dari pusat provinsi cukup jauh ke arah selatan.", #[cite: 3]
        "kuliner": "Bakso Titoti Wonogiri asli, Mie Ayam Wonogiri, and Jangan Lombok (sayur pedas khas desa).",
        "transportasi": "Akses via bus antarkota rute selatan atau sensasi naik Kereta Wisata Railbus Batara Kresna rute Solo-Wonogiri.",
        "budget": "Sangat meriah. Menikmati seporsi bakso urat sapi asli Wonogiri mulai Rp15.000. HTM area bendungan sangat murah.",
        "waktu_terbaik": "Pagi hari atau sore sejuk untuk mengitari area waduk raksasa dengan perahu wisata tanpa kepanasan.",
        "spots": {
            "waduk gajah mungkur": {
                "name": "Waduk Gajah Mungkur", "kategori": "alam", #[cite: 3]
                "desc": "Bendungan raksasa yang menenggelamkan puluhan desa, ikon wisata Wonogiri.", #[cite: 3]
                "kelebihan": "Luas seperti lautan, banyak ikan nila bakar, dan perahu wisata.", #[cite: 3]
                "kekurangan": "Fasilitas bermain di pinggir waduk perlu peremajaan." #[cite: 3]
            }
        }
    },
    "purworejo": {
        "emoji": "🥥", "name": "Kabupaten Purworejo", #[cite: 3]
        "kelebihan": "Memiliki alun-alun terbesar di Jawa, wisata alam Goa yang eksotis.", #[cite: 3]
        "kekurangan": "Pengembangan wisata pantainya belum sepopuler tetangganya.", #[cite: 3]
        "kuliner": "Kue Clorot tradisional (wadah daun kelor), Dawet Hitam Jembatan Butuh, and Sate Winong.",
        "transportasi": "Akses darat jalur selatan Jawa, sangat dekat dengan Bandara YIA Kulon Progo. Bisa naik kereta turun Stasiun Kutoarjo.",
        "budget": "Ekonomis. Tiket masuk objek wisata penjelajahan gua and alam pegunungan berkisar Rp10.000 - Rp15.000.",
        "waktu_terbaik": "Pagi hari cerah. Hindari puncak musim hujan lebat agar kondisi rute trek tangga batuan di dalam gua tidak licin.",
        "spots": {
            "goa seplawan": {
                "name": "Goa Seplawan", "kategori": "alam", #[cite: 3]
                "desc": "Gua alam di pegunungan Menoreh tempat ditemukannya patung emas Siwa Parwati.", #[cite: 3]
                "kelebihan": "Stalaktitnya bagus, pemandangan dari bibir tebingnya spektakuler.", #[cite: 3]
                "kekurangan": "Akses jalan menanjak dan rawan licin saat hujan." #[cite: 3]
            }
        }
    },
    "purbalingga": {
        "emoji": "🦇", "name": "Kabupaten Purbalingga", #[cite: 3]
        "kelebihan": "Pusat bulu mata palsu, wisata gua dan curug (air terjun) sangat banyak.", #[cite: 3]
        "kekurangan": "Fasilitas transportasi umum ke wisata alam minim.", #[cite: 3]
        "kuliner": "Sroto Klamud (Soto wadah kelapa muda), Nasi Goreng Usman, and tempe mendoan kriuk.",
        "transportasi": "Bersebelahan dengan Purwokerto. Akses rute perbukitan disarankan menggunakan motor atau rental mobil.",
        "budget": "Murah and bersahabat. HTM tiket masuk komplek gua vulkanik berkisar Rp15.000 - Rp25.000 (sudah include lighting dalam gua).",
        "waktu_terbaik": "Pagi hingga siang hari. Suasana di dalam gua sejuk alami, sangat pas untuk berlindung dari potensi hujan sore hari lereng Slamet.",
        "spots": {
            "goa lawa": {
                "name": "Goa Lawa (Golaga)", "kategori": "alam", #[cite: 3]
                "desc": "Gua vulkanik di lereng Gunung Slamet yang luas dan terbentuk dari lava membeku.", #[cite: 3]
                "kelebihan": "Dihiasi lampu warna-warni yang estetik, tidak pengap.", #[cite: 3]
                "kekurangan": "Suasananya cukup gelap di beberapa lorong." #[cite: 3]
            }
        }
    },
    "cilacap": {
        "emoji": "🏰", "name": "Kabupaten Cilacap", #[cite: 3]
        "kelebihan": "Kabupaten terluas di Jateng, terkenal dengan pantai, kilang minyak, dan pulau penjara.", #[cite: 3]
        "kekurangan": "Suhu di pesisir sangat panas, jarak dari ibu kota provinsi (Semarang) sangat jauh.", #[cite: 3]
        "kuliner": "Brekecek Pathak Jahan (kuliner kepala ikan pedas), Sate Martawi (dua tusuk lidi per porsi), and Tahu Masak Cilacap.",
        "transportasi": "Akses via kereta api lintas selatan berlabuh di Stasiun Cilacap. Rute menuju spot benteng dekat dari pesisir pelabuhan.",
        "budget": "Terjangkau. Tiket masuk area cagar budaya situs militer benteng kuno berkisar Rp5.000 - Rp15.000.",
        "waktu_terbaik": "Pagi hari pukul 08.00 WIB sewaktu matahari pesisir pantai belum terlalu terik membakar and energi masih fit untuk jalan kaki.",
        "spots": {
            "benteng pendem": {
                "name": "Benteng Pendem", "kategori": "sejarah", #[cite: 3]
                "desc": "Benteng pertahanan Hindia Belanda yang dahulu tertimbun tanah pesisir.", #[cite: 3]
                "kelebihan": "Sangat luas, banyak lorong rahasia bersejarah yang bisa dieksplor.", #[cite: 3]
                "kekurangan": "Kondisi beberapa bangunan agak lembab dan kurang cahaya." #[cite: 3]
            }
        }
    },
    "temanggung": {
        "emoji": "🍂", "name": "Kabupaten Temanggung", #[cite: 3]
        "kelebihan": "Kota penghasil tembakau terbaik, diapit gunung kembar Sindoro dan Sumbing.", #[cite: 3]
        "kekurangan": "Kontur wilayah naik turun tajam.", #[cite: 3]
        "kuliner": "Sego Gono (Nasi gurih tabur daun gono), Kopi Arabika/Robusta Sindoro-Sumbing asli, and Balung Kuwuk.",
        "transportasi": "Jalur berbukit tajam di tengah provinsi. Direkomendasikan naik motor/mobil pribadi atau menggunakan jasa sewa ojek lokal wisata.",
        "budget": "Ekonomis. Tiket masuk gardu pandang and area camping alam lereng berkisar Rp15.000 - Rp25.000 per kepala.",
        "waktu_terbaik": "Subuh buta pukul 04.30 WIB demi berburu momen lautan awan and terbitnya matahari (sunrise) magis di sela gunung kembar.",
        "spots": {
            "posong": {
                "name": "Wisata Alam Posong", "kategori": "alam", #[cite: 3]
                "desc": "Gardu pandang di lereng Gunung Sindoro untuk melihat golden sunrise dan lautan awan.", #[cite: 3]
                "kelebihan": "Spot sunrise dan camping yang luar biasa, udara segar.", #[cite: 3]
                "kekurangan": "Jalan berbatu macadam menuju lokasi, tidak ramah untuk mobil ceper." #[cite: 3]
            }
        }
    },
    "kendal": {
        "emoji": "🏖️", "name": "Kabupaten Kendal", #[cite: 3]
        "kelebihan": "Bersebelahan langsung dengan Semarang, kawasan industri namun kaya wisata atas.", #[cite: 3]
        "kekurangan": "Wilayah pesisir bawah sering panas, sedangkan atas berkabut tebal.", #[cite: 3]
        "kuliner": "Sate Bumbon Kendal (kaya rempah), Momoko, and Kerupuk Petis gurih.",
        "transportasi": "Berbatasan dengan batas barat Semarang. Akses rute kebun teh atas medannya terjal and makadam, disarankan pakai roda dua yang fit.",
        "budget": "Sangat murah untuk tiket masuk wisata alam perkebunan (sekitar Rp10.000 - Rp20.000). Alokasikan dana darurat untuk ban bocor jika offroad.",
        "waktu_terbaik": "Pagi hari pukul 06.00 - 08.00 WIB untuk merasakan sensasi sejuk ekstrem kabut tipis di atas hamparan permadani kebun teh.",
        "spots": {
            "kebun teh medini": {
                "name": "Kebun Teh Medini", "kategori": "alam", #[cite: 3]
                "desc": "Hamparan kebun teh peninggalan Belanda di lereng Gunung Ungaran.", #[cite: 3]
                "kelebihan": "Udaranya sedingin kulkas, view pegunungannya sangat asri.", #[cite: 3]
                "kekurangan": "Akses jalannya mayoritas berbatu keras (offroad), ban bocor sering terjadi." #[cite: 3]
            }
        }
    },
    "batang": {
        "emoji": "🐬", "name": "Kabupaten Batang", #[cite: 3]
        "kelebihan": "Kombinasi lengkap wisata pantai dan wisata alam pegunungan.", #[cite: 3]
        "kekurangan": "Banyak dilalui jalur pantura truk besar, harus hati-hati.", #[cite: 3]
        "kuliner": "Sego Megono Batang, Lontong Lemprak, and Serabi Kalibeluk berukuran jumbo.",
        "transportasi": "Sangat mudah via jalan raya nasional Pantura atau keluar tol Trans Jawa. Kawasan pantai terhitung dekat dari pusat kota.",
        "budget": "Terjangkau. HTM pantai murah, pengeluaran bergeser ke arah menu menu kafe hits tepi pantai standar anak muda (Rp15.000 - Rp40.000).",
        "waktu_terbaik": "Sore hari pukul 16.00 WIB, waktu paling populer untuk menikmati nongkrong santai di beach cafe sembari melihat sunset.",
        "spots": {
            "pantai sigandu": {
                "name": "Pantai Sigandu & Safari Beach Jateng", "kategori": "alam", #[cite: 3]
                "desc": "Pantai utara yang kini dipenuhi kafe estetik dan taman safari mini.", #[cite: 3]
                "kelebihan": "Kafe pinggir pantainya kekinian, ada atraksi lumba-lumba edukatif.", #[cite: 3]
                "kekurangan": "Pasir pantainya tidak terlalu luas dan kurang cocok untuk berenang." #[cite: 3]
            }
        }
    },
    "pekalongan kab": {
        "emoji": "🏕️", "name": "Kabupaten Pekalongan", #[cite: 3]
        "kelebihan": "Punya dataran tinggi Petungkriyono yang merupakan hutan lindung asri.", #[cite: 3]
        "kekurangan": "Akses ke wisata alam atas cukup jauh dan berkelok.", #[cite: 3]
        "kuliner": "Pindang Tetel (kuah kluwek tetelan sapi), Apem Kesesi, and Kopi robusta alami Petungkriyono.",
        "transportasi": "Medan jalan pegunungan pedalaman sangat sempit, curam, and berliku. Wajib menggunakan motor/mobil kecil ber-engsel lincah.",
        "budget": "Murah meriah. HTM masuk spot rekreasi sungai alami batuan jernih berkisar Rp5.000 - Rp15.000.",
        "waktu_terbaik": "Pagi hari di puncak musim kemarau agar warna kejernihan air sungai biru kehijauan maksimal and jalanan tidak licin karena basah.",
        "spots": {
            "bengkelung park": {
                "name": "Bengkelung Park (Petungkriyono)", "kategori": "alam", #[cite: 3]
                "desc": "Wisata sungai berbatu jernih di kawasan hutan lindung Petungkriyono.", #[cite: 3]
                "kelebihan": "Airnya super jernih kebiruan, udaranya segar alami.", #[cite: 3]
                "kekurangan": "Jalan pegunungan yang sangat sempit." #[cite: 3]
            }
        }
    },
    "pemalang": {
        "emoji": "🍍", "name": "Kabupaten Pemalang", #[cite: 3]
        "kelebihan": "Kuliner Nasi Grombyang, wisata air dan pegunungan Nanas.", #[cite: 3]
        "kekurangan": "Banyak jalan kabupaten yang kondisinya sering rusak.", #[cite: 3]
        "kuliner": "Nasi Grombyang (nasi kuah kaldu hitam pekat gurih), Sate Loso, and Apem Comal.",
        "transportasi": "Akses utama via Pantura darat atau Tol Trans Jawa. Jalur menuju curug (air terjun) bawah gunung membutuhkan motor yang sehat.",
        "budget": "Sangat murah. Menikmati semangkok ikon kuliner Nasi Grombyang hangat berkisar Rp15.000 saja per porsi.",
        "waktu_terbaik": "Pagi hari pukul 08.00 - 10.00 WIB untuk berenang puas di air terjun mini sebelum dipadati oleh kunjungan wisatawan lokal.",
        "spots": {
            "curug sibedil": {
                "name": "Curug Sibedil", "kategori": "alam", #[cite: 3]
                "desc": "Air terjun kecil namun melebar dengan banyak pancuran bak tirai air.", #[cite: 3]
                "kelebihan": "Sangat estetik, kolam airnya jernih dan aman untuk bermain anak.", #[cite: 3]
                "kekurangan": "Areanya tidak terlalu besar, padat saat musim liburan." #[cite: 3]
            }
        }
    },
    "tegal kab": {
        "emoji": "♨️", "name": "Kabupaten Tegal (Slawi)", #[cite: 3]
        "kelebihan": "Surganya pemandian air panas alami di bawah Gunung Slamet.", #[cite: 3]
        "kekurangan": "Kemacetan parah di jalur wisata saat akhir pekan.", #[cite: 3]
        "kuliner": "Tahu Aci Slawi, Mendoan Tegal bumbu kecap pedas, and es Teh Poci Wasgitel.",
        "transportasi": "Jalur menanjak ekstrem ke arah kaki gunung, rawan macet parah pas weekend. Pastikan minyak rem and fungsi kopling mobil aman.",
        "budget": "Kategori menengah. Sewa villa bervariasi. Tiket masuk komplek pemandian air panas belerang alami berkisar Rp20.000 - Rp35.000.",
        "waktu_terbaik": "Hari biasa (weekday) di pagi hari atau malam sekalian untuk mendapatkan sensasi berendam air hangat optimal di tengah kabut dingin.",
        "spots": {
            "guci": {
                "name": "Pemandian Air Panas Guci", "kategori": "alam", #[cite: 3]
                "desc": "Kawasan wisata pemandian air panas alami pegunungan yang dipercaya menyembuhkan penyakit kulit.", #[cite: 3]
                "kelebihan": "Airnya panas langsung dari alam tidak berbau belerang, fasilitas villa menjamur.", #[cite: 3]
                "kekurangan": "Sangat-sangat macet di akhir pekan dan libur lebaran/tahun baru." #[cite: 3]
            }
        }
    },
    "brebes": {
        "emoji": "🧅", "name": "Kabupaten Brebes", #[cite: 3]
        "kelebihan": "Kabupaten penghasil telur asin dan bawang merah terbesar, punya wisata kebun teh luas.", #[cite: 3]
        "kekurangan": "Ujung barat Jawa Tengah, perjalanan ke wisata pegunungan cukup melelahkan.", #[cite: 3]
        "kuliner": "Telur Asin Brebes (original/asap/panggang), Sate Blengong (burung blengong), and Kupat Glabed.",
        "transportasi": "Gerbang barat Jateng, dilewati Tol Trans Jawa and Pantura utama. Rute menuju kebun teh atas (Kaligua) panjang, berkelok and sempit.",
        "budget": "Ekonomis. Harga beli oleh-oleh telur asin berkisar Rp4.500 - Rp6.000 per butir. Tiket agrowisata peninggalan Belanda relatif murah.",
        "waktu_terbaik": "Pagi hari pukul 07.30 WIB sebelum matahari menyengat agar puas berkeliling di dalam gua Jepang and kebun teh agrowisata Kaligua.",
        "spots": {
            "kaligua": {
                "name": "Agrowisata Kaligua", "kategori": "alam", #[cite: 3]
                "desc": "Perkebunan teh di lereng barat Gunung Slamet peninggalan kolonial Belanda.", #[cite: 3]
                "kelebihan": "Pemandangan kebun teh memanjakan mata, ada wisata sejarah goa Jepang.", #[cite: 3]
                "kekurangan": "Akses jalan panjang berkelok-kelok dan cukup sempit dari jalan utama Pantura." #[cite: 3]
            }
        }
    }
}
