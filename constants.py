# bidang PI constants
PO = 'PO' 
VPO_INTERNAL = 'VPOI'   
VPO_EKSTERNAL = 'VPOE'
SEKRETARIS = 'Sekretaris'
CONTROLLER = 'Controller' 
TREASURER = 'Treasurer'
KOOR_ACARA = 'koor-acara' 
SARANA_PRASARANA = 'SNP'
OPERASIONAL = 'OP' 
MATERI_MENTOR = 'MnM'
KREATIF = 'Kreatif'
RELASI = 'Relasi'

# bidang BPH constants
PROJECT = 'Project'
SPONSORSHIP = 'Sponsorship'
SEKRE = 'Kesekretariatan'
PSDM = 'PSDM'
ACARA_PUNCCAK = 'Acara-Puncak'
EKSPLORASI = 'Eksplorasi'
TRANSPORT_KONSUM = 'Transportasi-Konsumsi'
PERIZINAN = 'Perizinan'
LOGISTIK = 'Logistik'
KEAMANAN = 'Keamanan'
MEDIS = 'Medis'
MEDIA = 'Media Informasi'
KELEMBAGAAN = 'Kelembagaan'
MATERI = 'Materi'
MENTOR = 'Mentor'
MEDPAR = 'Media-Partner'
IT = 'IT' 
BROADCAST = 'Broadcast'
DEKOR_WARDROBE = 'Dekorasi-Wardrobe' 
VISDES_DOKUM = 'VisDes-Dokumentasi'

# fakultas constants
FF = 'FF'
FH = 'FH'
FIA = 'FIA'
FIB = 'FIB'
FEB = 'FEB'
FIK = 'FIK'
FASILKOM = 'FASILKOM'
FISIP = 'FISIP'
FK = 'FK'
FKG = 'FKG'
FKM = 'FKM'
FMIPA = 'FMIPA'
PSIKO = 'FPSI'
FT = 'FT'
VOKASI = 'VOKASI'

BIDANG_PI_CHOICES = [
    (PO, 'Project Officer'), 
    (VPO_INTERNAL, 'Vice Project Officer Internal'), 
    (VPO_INTERNAL, 'Vice Project Officer Eksternal'), 
    (SEKRETARIS, 'Sekretaris'), 
    (CONTROLLER, 'Controller'), 
    (TREASURER, 'Treasurer'), 
    (KOOR_ACARA, 'Koordinator Acara'), 
    (SARANA_PRASARANA, 'Sarana dan Prasarana'), 
    (OPERASIONAL, 'Operasional'), 
    (MATERI, 'Materi'), 
    (KREATIF, 'Kreatif'), 
    (RELASI, 'Relasi'),
]

BIDANG_BPH_CHOICES = [
    (PROJECT, 'Project'), 
    (SPONSORSHIP, 'Sponsorship'), 
    (SEKRE, 'Kesekretariatan'), 
    (PSDM, 'PSDM'), 
    (ACARA_PUNCCAK, 'Acara Puncak'), 
    (EKSPLORASI, 'Ekspolarsi'), 
    (TRANSPORT_KONSUM, 'Transportasi dan Konsumsi'), 
    (PERIZINAN, 'Perizinan'), 
    (LOGISTIK, 'Logistik'), 
    (KEAMANAN, 'Keamanan'), 
    (MEDIS, 'Medis'), 
    (MEDIA, 'Media'), 
    (KELEMBAGAAN, 'Kelembagaan'), 
    (MATERI, 'Materi'), 
    (MENTOR, 'Mentor'), 
    (MEDPAR, 'Media Partner'), 
    (IT, 'IT'), 
    (BROADCAST, 'Broadcast'), 
    (DEKOR_WARDROBE, 'Dekor dan Wardrobe'), 
    (VISDES_DOKUM, 'Visual Design dan Dokumentasi'),
]

BIDANG_PI = [
    PO, VPO_INTERNAL, VPO_INTERNAL, SEKRETARIS, CONTROLLER, 
    TREASURER, KOOR_ACARA, SARANA_PRASARANA, OPERASIONAL, 
    MATERI, KREATIF, RELASI
]

BIDANG_BPH = [
    PROJECT, SPONSORSHIP, SEKRE, PSDM, ACARA_PUNCCAK, EKSPLORASI, 
    TRANSPORT_KONSUM, PERIZINAN, LOGISTIK, KEAMANAN, MEDIS, MEDIA, 
    KELEMBAGAAN, MATERI, MENTOR, MEDPAR,
    IT, BROADCAST, DEKOR_WARDROBE, VISDES_DOKUM
]

FAKULTAS_CHOICES = [
    (FF, 'Fakultas Farmasi'),
    (FH, 'Fakultas Hukum'),
    (FIA, 'Fakultas Ilmu Administrasi'),
    (FIB, 'Fakultas Ilmu Budaya'),
    (FEB, 'Fakultas Ekonomi dan Bisnis'),
    (FIK, 'Fakultas Ilmu Keperawatan'),
    (FASILKOM, 'Fakultas Ilmu Komputer'),
    (FISIP, 'Fakultas Ilmu Sosial dan Ilmu Politik'),
    (FK, 'Fakultas Kedokteran'),
    (FKG, 'Fakultas Kedokteran Gigi'),
    (FKM, 'Fakultas Kesehatan Masyarakat'),
    (FMIPA, 'Fakultas Matematika dan Ilmu Pengetahuan Alam'),
    (PSIKO, 'Fakultas Psikologi'),
    (FT, 'Fakultas Teknik'),
    (VOKASI, 'Program Pendidikan Vokasi'),
]