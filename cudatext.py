import cudatext_api as ct
import cudatext_cmd as cmds

MB_OK = 0x00000000
MB_OKCANCEL = 0x00000001
MB_ABORTRETRYIGNORE = 0x00000002
MB_YESNOCANCEL = 0x00000003
MB_YESNO = 0x00000004
MB_RETRYCANCEL = 0x00000005
MB_ICONERROR = 0x00000010
MB_ICONQUESTION = 0x00000020
MB_ICONWARNING = 0x00000030
MB_ICONINFO = 0x00000040

ID_OK = 1
ID_CANCEL = 2
ID_ABORT = 3
ID_RETRY = 4
ID_IGNORE = 5
ID_YES = 6
ID_NO = 7

SEL_NORMAL = 0
SEL_COLUMN = 1

CARET_SET_ONE = 0
CARET_ADD = 1
CARET_DELETE_ALL = 2
CARET_SET_INDEX = 100

APP_DIR_EXE = 0
APP_DIR_SETTINGS = 1
APP_DIR_DATA = 2
APP_DIR_PY = 3
APP_FILE_SESSION = 4

CONVERT_CHAR_TO_COL = 0
CONVERT_COL_TO_CHAR = 1

LINESTATE_NORMAL  = 0
LINESTATE_CHANGED = 1
LINESTATE_ADDED   = 2
LINESTATE_SAVED   = 3

COLOR_NONE = 0x1FFFFFFF

MENU_LIST = 0
MENU_LIST_ALT = 1

BOOKMARK_GET = 0
BOOKMARK_SET = 1
BOOKMARK_CLEAR = 2
BOOKMARK_CLEAR_ALL = 3
BOOKMARK_SETUP = 4
BOOKMARK_GET_LIST = 5

TAB_SPLIT_NO = 0
TAB_SPLIT_HORZ = 1
TAB_SPLIT_VERT = 2

LOG_CLEAR         = 0
LOG_ADD           = 1
LOG_SET_PANEL     = 2
LOG_SET_REGEX     = 3
LOG_SET_LINE_ID   = 4
LOG_SET_COL_ID    = 5
LOG_SET_NAME_ID   = 6
LOG_SET_FILENAME  = 7
LOG_SET_ZEROBASE  = 8
LOG_CONSOLE_CLEAR = 20
LOG_CONSOLE_ADD   = 21
LOG_CONSOLE_GET   = 22

LOG_PANEL_OUTPUT   = "0"
LOG_PANEL_VALIDATE = "1"

PROP_GUTTER_NUM     = 1
PROP_GUTTER_FOLD    = 2
PROP_GUTTER_BM      = 3
PROP_EOL            = 4
PROP_WRAP           = 5
PROP_RO             = 6
PROP_TAB_SPACES     = 7
PROP_TAB_SIZE       = 8
PROP_MARGIN         = 9
PROP_MARGIN_STRING  = 10
PROP_INSERT         = 11
PROP_MODIFIED       = 12
PROP_RULER          = 13
PROP_LINE_STATE     = 14
PROP_LEXER_FILE     = 20
PROP_LEXER_POS      = 21
PROP_LEXER_CARET    = 22
PROP_INDEX_GROUP    = 23
PROP_INDEX_TAB      = 24
PROP_UNPRINTED_SHOW        = 30
PROP_UNPRINTED_SPACES      = 31
PROP_UNPRINTED_ENDS        = 32
PROP_UNPRINTED_END_DETAILS = 33

PROC_GET_CLIP = 0
PROC_SET_CLIP = 1
PROC_GET_COMMAND = 2
PROC_SAVE_SESSION = 3
PROC_LOAD_SESSION = 4
PROC_SET_SESSION = 5
PROC_MENU_CLEAR = 6
PROC_MENU_ADD = 7
PROC_MENU_ENUM = 8

LEXER_GET_LIST    = 0
LEXER_GET_ENABLED = 1
LEXER_GET_EXT     = 2
LEXER_GET_MODIFIED= 3
LEXER_GET_LINKS   = 4
LEXER_GET_STYLES  = 5
LEXER_GET_COMMENT = 6
LEXER_SET_NAME    = 10
LEXER_SET_ENABLED = 11
LEXER_SET_EXT     = 12
LEXER_SET_LINKS   = 13
LEXER_SAVE_LIB    = 20
LEXER_DELETE      = 21
LEXER_IMPORT      = 22
LEXER_EXPORT      = 23

def app_exe_version():
    return ct.app_exe_version()
def app_api_version():
    return ct.app_api_version()
def app_path(id):
    return ct.app_path(id)
def app_proc(id, text):
    if id==PROC_MENU_ADD and '{' in text and '}' in text:
        cmd_id = text[text.index('{')+1:text.index('}')]
       #pass;                   print('app_proc: ?? text='+text)
        text   = text.replace('{'+cmd_id+'}', str(eval('cmds.'+cmd_id)))
       #pass;                   print('app_proc: ok text='+text)
    return ct.app_proc(id, text)    

def app_log(id, text):
    res = ct.app_log(id, text)
    if id==LOG_CONSOLE_GET:
        return res.splitlines()
    else:
        return res    

def msg_box(text, flags):
    return ct.msg_box(text, flags)
def msg_status(text):
    return ct.msg_status(text)
    
def dlg_input(label, defvalue):
    return ct.dlg_input(label, defvalue)
def dlg_color(value):
    return ct.dlg_color(value)    

def dlg_input_ex(number, caption,
                 label1   , text1='', label2='', text2='', label3='', text3='',
                 label4='', text4='', label5='', text5='', label6='', text6='',
                 label7='', text7='', label8='', text8='', label9='', text9='',
                 label10='', text10=''):
    result = ct.dlg_input_ex(number, caption,
                 label1, text1, label2, text2, label3, text3,
                 label4, text4, label5, text5, label6, text6,
                 label7, text7, label8, text8, label9, text9,
                 label10, text10)
    if result is None:
        return None
    else:
        return result.splitlines()
        
def dlg_menu(id, text):
    return ct.dlg_menu(id, text)        

def dlg_file(is_open, init_filename, init_dir, filters):
    res = ct.dlg_file(is_open, init_filename, init_dir, filters)
    if res is None:
        return None
    res = res.splitlines()
    if len(res)==1:
        res=res[0]
    return res

def dlg_checklist(caption, columns, items, size_x, size_y):
    items = ct.dlg_checklist(caption, columns, items, size_x, size_y)
    if not items:
        return None
    return [(s=='1') for s in items]

def file_open(filename, group=-1):
    return ct.file_open(filename, group)
def file_save():
    return ct.file_save()

def ed_handles():
    r0, r1 = ct.ed_handles()
    return range(r0, r1+1)

def ini_read(filename, section, key, value):
    return ct.ini_read(filename, section, key, value)
def ini_write(filename, section, key, value):
    return ct.ini_write(filename, section, key, value)
    
def lexer_proc(id, value):
    return ct.lexer_proc(id, value)
    

#Editor
class Editor:
    h = 0
    def __init__(self, handle):
        self.h = handle

    def get_carets(self):
        big = 4294967295 #workaround for Py engine bug. it gives this, not -1.
        res = ct.ed_get_carets(self.h)
        for item in res:
            if item[2]==big: item[2]=-1
            if item[3]==big: item[3]=-1
        return res
        
    def set_caret(self, x1, y1, x2=-1, y2=-1, id=CARET_SET_ONE):
        return ct.ed_set_caret(self.h, x1, y1, x2, y2, id)

    def get_line_count(self):
        return ct.ed_get_line_count(self.h)

    def get_text_all(self):
        items = [self.get_text_line(i) for i in range(self.get_line_count())]
        return '\n'.join(items)
        
    def set_text_all(self, text):
        return ct.ed_set_text_all(self.h, text)
    def get_text_sel(self):
        return ct.ed_get_text_sel(self.h)
    def get_text_line(self, num):
        return ct.ed_get_text_line(self.h, num)
    def set_text_line(self, num, text):
        return ct.ed_set_text_line(self.h, num, text)
    def get_text_substr(self, x1, y1, x2, y2):
        return ct.ed_get_text_substr(self.h, x1, y1, x2, y2)

    def get_sel_mode(self):
        return ct.ed_get_sel_mode(self.h)
    def get_sel_lines(self):
        return ct.ed_get_sel_lines(self.h)
    def get_sel_rect(self):
        return ct.ed_get_sel_rect(self.h)
    def set_sel_rect(self, x1, y1, x2, y2):
        return ct.ed_set_sel_rect(self.h, x1, y1, x2, y2)

    def delete(self, x1, y1, x2, y2):
        return ct.ed_delete(self.h, x1, y1, x2, y2)
    def insert(self, x1, y1, text):
        return ct.ed_insert(self.h, x1, y1, text)

    def get_filename(self):
        return ct.ed_get_filename(self.h)

    def get_tabcolor(self):
        return ct.ed_get_tabcolor(self.h)
    def set_tabcolor(self, value):
        return ct.ed_set_tabcolor(self.h, value)

    def get_enc(self):
        return ct.ed_get_enc(self.h)
    def set_enc(self, value):
        return ct.ed_set_enc(self.h, value)
    def get_top(self):
        return ct.ed_get_top(self.h)
    def set_top(self, value):
        return ct.ed_set_top(self.h, value)

    def cmd(self, value):
        return ct.ed_cmd(self.h, value)
    def focus(self):
        return ct.ed_focus(self.h)
    def bookmark(self, id, nline, nkind=1, ncolor=-1, icon=''):
        return ct.ed_bookmark(self.h, id, nline, nkind, ncolor, icon)

    def lock(self):
        return ct.ed_lock(self.h)
    def unlock(self):
        return ct.ed_unlock(self.h)

    def get_split(self):
        return ct.ed_get_split(self.h)
    def set_split(self, state, value):
        return ct.ed_set_split(self.h, state, value)
        
    def get_prop(self, id, value=''):
        return ct.ed_get_prop(self.h, id, value)
    def set_prop(self, id, value):
        return ct.ed_set_prop(self.h, id, value)
    
    def complete(self, text, len1, len2):
        return ct.ed_complete(self.h, text, len1, len2)
        
    def convert(self, id, x, y):
        return ct.ed_convert(self.h, id, x, y)
        
    def get_ranges(self):
        return ct.ed_get_ranges(self.h)
    #end

#objects
ed = Editor(0)
ed_bro = Editor(1)
