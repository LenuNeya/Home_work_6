CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ('a','b', 'v', 'h', 'd', 'e', 'e', 'zh', 'z', 'y', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u',
               'f', 'kh', 'ts', 'ch', 'sh', 'sch', '', 'y', '', 'e', 'yu', 'ia', 'ye', 'i', 'yi', 'g')

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

FOLDERS = {
    'images': {'jpeg', 'png', 'jpg', 'svg', 'bmp'},
    'video': {'avi', 'mp4', 'mov', 'mkv'},
    'documents': {'doc', 'docx', 'txt', 'pdf', 'xlsx', 'xls', 'pptx', 'csv'},
    'audio': {'mp3', 'ogg', 'wavV', 'amr'},
    'archives': {'zip', 'gz', 'tar'}
}