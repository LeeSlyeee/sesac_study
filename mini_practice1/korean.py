import platform
import matplotlib as mpl
from matplotlib import font_manager, rc

def korean_setup():
    system = platform.system()
    if system == "Windows":
        font_path = "C:/Windows/Fonts/malgun.ttf"
    elif system == "Darwin":
        font_path = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
    elif system == "Linux":
        font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
    else:
        font_path = None
    if font_path:
        font = font_manager.FontProperties(fname=font_path).get_name()
        mpl.rcParams['font.family'] = font
    else:
        print("폰트 경로를 확인해주세요.")
    mpl.rcParams['axes.unicode_minus'] = False
    
korean_setup()