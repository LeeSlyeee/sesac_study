import os  # 운영체제(Operating System) 기능에 접근하기 위한 표준 라이브러리 모듈을 임포트합니다. 
           # 파일 경로 조작, 환경 변수(Environment Variable) 접근 등 시스템 상호작용에 주로 사용됩니다.

import json # JSON(JavaScript Object Notation) 데이터를 파싱(읽기)하거나 직렬화(쓰기)하는 기능을 제공하는 모듈입니다.
           # 웹 애플리케이션에서 데이터를 주고받을 때 주로 사용됩니다.

from flask import Flask # "Flask 웹 프레임워크"의 핵심인 'Flask' 클래스를 임포트합니다. 
                         # 이 클래스의 인스턴스(객체)가 곧 웹 애플리케이션 자체가 됩니다.

from flask import render_template # "Jinja2 템플릿 엔진"을 사용하여 HTML 파일을 렌더링하고 사용자에게 응답하는 함수입니다.
                                   # 서버의 데이터를 동적으로 HTML에 삽입하여 웹 페이지를 생성할 때 사용됩니다.

from flask import url_for # Flask에서 "뷰 함수 이름(엔드포인트)"을 기반으로 해당 URL을 동적으로 생성하는 함수입니다.
                           # 하드코딩된 URL 대신 사용하여 애플리케이션의 유연성을 높입니다.

from flask import request # 클라이언트(사용자 웹 브라우저)로부터 전송된 "HTTP 요청 데이터"에 접근하기 위한 객체입니다.
                           # 폼 데이터, 쿼리 파라미터, 파일 업로드 등의 정보를 다룰 때 필수적입니다.

from flask import redirect # 사용자 브라우저를 다른 URL로 "리다이렉션(재전송)"하도록 HTTP 응답을 생성하는 함수입니다.
                            # 주로 로그인 후 페이지 이동이나 폼 제출 후 결과 페이지로 이동시 사용됩니다.

from flask import send_from_directory # 특정 디렉터리 내의 "파일을 클라이언트에게 안전하게 전송"하는 함수입니다.
                                       # 이미지, CSS, JS 파일 등의 정적 파일이나 업로드된 파일을 제공할 때 유용합니다.

from werkzeug.utils import secure_filename # 파일 이름에 포함될 수 있는 "잠재적인 보안 문제(예: 경로 조작)"를 방지하기 위해 
                                           # 파일 이름을 안전하게 정리(Sanitize)해주는 함수입니다. 주로 파일 업로드 시 사용됩니다.



# Flask 애플리케이션 객체를 생성합니다.
app = Flask(__name__) 
# '__name__'은 현재 실행 중인 파이썬 모듈의 이름(보통 'app')을 나타냅니다. 
# Flask는 이를 기준으로 템플릿(templates/) 및 정적 파일(static/)의 위치를 찾습니다.



# --- 라우트 정의 시작: URL과 뷰 함수를 매핑하는 부분입니다. ---

@app.route('/') # URL 경로가 '/' (애플리케이션의 루트 또는 기본 경로)일 때의 라우트를 정의하는 데코레이터입니다.
def index():
    """기본 경로('/')에 대한 HTTP GET 요청을 처리하는 뷰 함수입니다."""
    # 단순 문자열을 HTTP 응답 본문(Response Body)으로 클라이언트(웹 브라우저)에 반환합니다.
    return 'Hi!!!' 


@app.route('/hello/<name>', # '/hello/' 뒤에 <name>이라는 '문자열' 변수를 포함하는 동적 URL 라우트를 정의합니다.
                            # Flask가 이 경로로 들어온 요청에서 <name> 값을 추출하여 뷰 함수의 인수로 전달합니다.
           methods=['GET'], # 이 라우트가 HTTP GET 메서드 요청만 처리하도록 제한합니다. 
           endpoint='hello_endpoint') # 이 뷰 함수를 참조할 때 사용할 고유한 이름(엔드포인트)을 지정합니다.
def hello(name): # 라우트에 연결된 뷰 함수입니다. URL에서 추출된 name 값이 문자열 인수로 전달됩니다.
    """동적 경로('/hello/<name>') 요청을 처리하고, URL에서 받은 이름을 포함하여 응답합니다."""
    # f-string을 사용하여 전달받은 name 값을 문자열에 삽입한 후, 최종 응답으로 반환합니다.
    return f'Hello, World! {name}' 




@app.route('/data/', endpoint='data_endpoint') # '/data/' 경로에 대한 라우트를 정의합니다.
def html():
    """정적 HTML 템플릿을 렌더링하는 뷰 함수입니다."""
    # templates 폴더 내의 'index.html' 파일을 찾아 HTML 응답으로 반환합니다.
    return render_template('index.html')


@app.route('/gugudan/<int:dan>', endpoint='gugudan_endpoint')
def gugudan(dan):
    """
    동적 URL 경로를 통해 <int:dan>으로 지정된 '정수형' 단(dan)을 인수로 받아 구구단을 계산합니다.
    (예: /gugudan/5)
    """
    result_list = [] # 구구단 계산 결과를 저장할 빈 리스트를 초기화합니다.
    
    # 1부터 9까지 반복하며 구구단을 계산합니다.
    for i in range(1, 10):
        result = dan * i
        # 각 계산 결과를 (단, 곱하는 수, 결과) 튜플 형태로 리스트에 추가합니다.
        result_list.append((dan, i, result))
        
    # 'gugudan.html' 템플릿을 렌더링하면서 계산된 데이터를 템플릿으로 전달합니다.
    return render_template(
        'gugudan.html',           # 렌더링할 템플릿 파일 이름
        dan_num = dan,            # 사용자 입력 단(dan)을 'dan_num' 변수명으로 템플릿에 전달
        gugu_list = result_list   # 계산 결과 리스트를 'gugu_list' 변수명으로 템플릿에 전달
    )
   
   
    

@app.route('/checkName/<username>', endpoint='check_name_endpoint')
def check_name_upper_lower(username):
    """
    동적 URL 경로를 통해 받은 'username'의 길이에 따라 대소문자를 변경하여 템플릿에 전달합니다.
    (예: /checkName/user)
    """
    
    # username 문자열의 길이를 확인합니다.
    if len(username) % 2 == 0:
        # 길이가 짝수이면 (나머지가 0), 문자열 전체를 대문자(UPPERCASE)로 변환합니다.
        tmp = str(username).upper()
    else: 
        # 길이가 홀수이면 (나머지가 0이 아님), 문자열 전체를 소문자(lowercase)로 변환합니다.
        tmp = str(username).lower()
        
    # 'userCheck.html' 템플릿을 렌더링하고, 변경된 문자열을 'username' 변수명으로 전달합니다.
    return render_template(
        'userCheck.html',
        username = tmp
    )
    
    



 
 # 1. JSON 파일 경로 정의 (static 폴더 내부)
# 파일 경로를 직접 지정하는 대신, Flask의 루트 경로를 기준으로 절대 경로를 생성합니다.
# app.root_path: 애플리케이션이 시작된 루트 디렉토리 경로
DATA_FILE_PATH = os.path.join(app.root_path, 'static', 'member.json')


# 2. JSON 파일 읽기 함수 정의
def load_user_data():
    """정의된 경로(static/user_data.json)에서 JSON 데이터를 로드합니다."""
    # 파일이 존재하는지 확인합니다. (절대 경로 사용)
    if not os.path.exists(DATA_FILE_PATH):
        print(f"오류: 데이터 파일 '{DATA_FILE_PATH}'을(를) 찾을 수 없습니다.")
        return {}
    
    # 파일을 읽기 모드('r')로 열고 내용을 로드합니다.
    try:
        with open(DATA_FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError:
        print(f"오류: '{DATA_FILE_PATH}' 파일의 JSON 형식이 올바르지 않습니다.")
        return {}
    except Exception as e:
        print(f"파일을 읽는 중 오류 발생: {e}")
        return {}

# 3. 애플리케이션 시작 시 데이터 로드
USER_DATA = load_user_data()


@app.route('/login', methods = ['GET', 'POST'])
def login():
    """로그인 페이지 렌더링 및 인증 로직 처리"""
    error = None 

    if request.method == 'POST':
        username_input = request.form['username']
        password_input = request.form['password']

        is_authenticated = False
        
        # 로드된 USER_DATA를 사용하여 인증 수행
        for user_info in USER_DATA.values(): 
            if user_info['id'] == username_input and user_info['pw'] == password_input:
                is_authenticated = True
                break
        
        if is_authenticated:
            return redirect(url_for('welcome', username=username_input))
        else:
            error = '잘못된 사용자 ID 또는 비밀번호입니다.'

    return render_template('login.html', error=error)
    
    

@app.route('/welcome/<username>')
def welcome(username):
    """로그인 성공 후 환영 페이지"""
    return render_template('welcome.html', username=username)

 
 
 
 
# 문의 폼 페이지 표시 및 처리
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # 요청 방식이 POST일 경우 (폼이 제출되었을 경우)
    if request.method == 'POST':
        # 폼 데이터 가져오기
        username = request.form['username']
        email = request.form['email']
        message = request.form['message']

        # 여기서는 단순히 데이터를 출력합니다.
        # 실제 애플리케이션에서는 이 데이터를 데이터베이스에 저장하거나,
        # 이메일을 보내는 등의 처리를 수행해야 합니다.
        print("--- 문의 폼 제출 내용 ---")
        print(f"사용자명: {username}")
        print(f"이메일: {email}")
        print(f"문의 내용: {message}")
        print("------------------------")

        # 처리가 완료되면 'success' 페이지로 리다이렉트
        return redirect(url_for('success'))
    
    # 요청 방식이 GET일 경우 (페이지를 처음 로드할 경우)
    return render_template('contact.html') 
 
 
 
# 문의 완료 페이지
@app.route('/contact/success')
def success():
    return render_template('success.html')
 
 
 
 
 
 
 





# 1. 파일이 저장될 경로 설정
# 주의: '/uploads'는 절대 경로일 가능성이 높으므로, 실제 서버 환경에 맞게 조정해야 합니다.
# 일반적으로는 'uploads'와 같이 상대 경로를 사용하여 프로젝트 폴더 내에 저장하는 것을 권장합니다.
UPLOAD_FOLDER = 'uploads' 

# 2. 허용할 확장자 설정 (보안 및 파일 유형 제한 목적)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip'}

# 3. Flask 앱 설정에 UPLOAD_FOLDER 적용
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 4. 파일 업로드 사이즈 제한 설정 (선택 사항, 예: 16MB)
# 주석 처리되어 있지만, 대용량 파일 업로드 시 서버 과부하 방지를 위해 활성화할 수 있습니다.
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 

# 애플리케이션의 보안 키 설정 (세션 및 플래시 메시지 등을 위해 필요)
app.secret_key = 'your_strong_secret_key' 

# 폴더가 없으면 생성 (파일 저장 경로가 실제로 존재하는지 확인)
if not os.path.exists(UPLOAD_FOLDER):
    print(f"INFO: UPLOAD_FOLDER '{UPLOAD_FOLDER}' 경로를 생성합니다.")
    os.makedirs(UPLOAD_FOLDER)

# --- 유틸리티 함수 섹션 ---

def allowed_file(filename):
    """
    파일 이름의 확장자가 허용된 목록에 있는지 확인합니다.
    Args:
        filename (str): 업로드된 파일의 원래 이름
    Returns:
        bool: 허용된 확장자이면 True, 아니면 False
    """
    # 1. 파일 이름에 '.'이 포함되어 있는지 (확장자 존재 여부) 확인
    # 2. 파일 이름에서 마지막 '.'을 기준으로 분리하여 확장자를 소문자로 추출 ([1])
    # 3. 추출된 확장자가 ALLOWED_EXTENSIONS 집합에 있는지 확인
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# --- 라우트 정의 섹션 ---

@app.route('/fileServer', methods=['GET'])
def fileServer():
    """
    파일 목록 페이지 (fileServer.html)를 렌더링하는 라우트입니다.
    업로드된 파일 목록을 가져와 템플릿에 전달합니다.
    """
    try:
        # UPLOAD_FOLDER 내의 모든 파일 목록을 가져와 files 변수에 저장
        files = os.listdir(app.config['UPLOAD_FOLDER'])
    except FileNotFoundError:
        # 폴더 경로에 문제가 있을 경우 예외 처리
        files = []
        print(f"ERROR: UPLOAD_FOLDER '{app.config['UPLOAD_FOLDER']}'를 찾을 수 없습니다.")
    
    # files 목록을 템플릿으로 전달하여 HTML에서 파일 목록을 표시하도록 함
    return render_template('fileServer.html', files=files)


@app.route('/upload', methods=['POST'])
def upload_file():
    """
    HTTP POST 요청을 받아 파일을 업로드 폴더에 저장하는 라우트입니다.
    """
    # 1. 요청에 파일 데이터('file' 필드)가 포함되어 있는지 확인
    if 'file' not in request.files:
        # 파일이 없으면 메인 페이지로 리다이렉트
        return redirect(url_for('fileServer')) # index 대신 fileServer로 수정 필요

    # 2. 파일 객체 가져오기
    file = request.files['file']

    # 3. 파일 이름이 비어있는지 (사용자가 파일을 선택하지 않았는지) 확인
    if file.filename == '':
        return redirect(url_for('fileServer')) # index 대신 fileServer로 수정 필요

    # 4. 파일 존재 및 허용된 확장자인지 확인
    if file and allowed_file(file.filename):
        # 파일 이름을 안전하게 처리 (보안: 경로 인젝션 공격 방지)
        filename = secure_filename(file.filename)
        # 파일이 저장될 최종 경로 생성
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # 실제 서버 디스크에 파일 저장
        try:
            file.save(filepath)
            print(f"INFO: 파일 저장 성공 - {filepath}")
        except Exception as e:
            print(f"ERROR: 파일 저장 실패 - {e}")
            return '파일 저장에 실패했습니다. 서버 권한을 확인하세요.', 500
        
        # 업로드 성공 후 파일 목록 페이지로 리다이렉트하여 갱신된 목록 표시
        return redirect('/fileServer') 
    
    # 5. 허용되지 않은 파일 형식일 경우
    return '업로드할 수 없는 파일 형식입니다. (허용 확장자: {})'.format(', '.join(ALLOWED_EXTENSIONS)), 400


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """
    업로드 폴더에 저장된 특정 파일을 사용자에게 서빙하는 라우트입니다.
    파일 다운로드/미리보기 기능을 담당합니다.
    """
    # send_from_directory 함수는 지정된 디렉토리(UPLOAD_FOLDER) 내에서
    # 요청된 파일 이름(filename)을 찾아 안전하게 반환 (보안 기능 내장)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    """
    HTTP POST 요청을 받아 지정된 파일을 서버에서 삭제하는 라우트입니다.
    POST를 사용하는 이유는 데이터 변경(삭제)을 안전하게 처리하기 위함입니다.
    """
    # 1. 파일 이름 안전하게 처리
    filename = secure_filename(filename)
    
    # 2. 파일의 전체 경로 생성
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # 3. 파일이 실제로 존재하는지 확인
    if os.path.exists(filepath):
        try:
            # os.remove를 사용하여 실제 파일 삭제
            os.remove(filepath)
            print(f"INFO: 파일 삭제 성공 - {filepath}")
        except Exception as e:
            # 파일 삭제 중 권한 또는 기타 오류 발생 시 처리
            print(f"ERROR: 파일 삭제 오류 - {e}")
            return f"파일 삭제 실패: 서버 권한 문제 또는 파일 사용 중 - {e}", 500
    else:
        # 파일이 존재하지 않는 경우
        print(f"WARNING: 삭제할 파일을 찾을 수 없습니다 - {filepath}")
        return "파일을 찾을 수 없습니다.", 404
    
    # 4. 삭제 후 파일 목록 페이지로 리다이렉트
    return redirect('/fileServer')













 
 
 
    


# --- url_for 테스트 블록 시작 ---
# Flask 애플리케이션의 컨텍스트 외부에서 url_for 함수를 사용하려면 반드시 이 블록이 필요합니다.
with app.test_request_context():
    # 💡 url_for 함수는 엔드포인트 이름(뷰 함수 이름)을 기반으로 URL 문자열을 동적으로 생성합니다.
    print(url_for('index')) # 결과: '/' (인수가 필요 없는 정적 라우트)
    
    # 동적 라우트('hello_endpoint')의 변수(name)를 키워드 인수로 전달합니다.
    print(url_for('hello_endpoint', name='Slyeee')) # 결과: '/hello/Slyeee'
    
    print(url_for('data_endpoint')) # 결과: '/data/'
    
    # 정수형 변수(dan)를 받는 동적 라우트에 값을 전달합니다.
    print(url_for('gugudan_endpoint', dan=1)) # 결과: '/gugudan/1'
    
    # 문자열 변수(username)를 받는 동적 라우트에 값을 전달합니다.
    print(url_for('check_name_endpoint', username="user01")) # 결과: '/checkName/user01'
# --- url_for 테스트 블록 끝 ---









# --- 라우트 정의 끝 ---

if __name__ == "__main__":
    # 이 파일이 직접 실행될 때 (서버 시작 시) 서버를 구동하는 블록입니다.
    
    # 💡 환경 변수 설정: 클라우드 환경에서 포트 설정을 유연하게 하기 위한 코드입니다.
    #    os.environ.get("PORT")를 통해 시스템 환경 변수 'PORT' 값을 읽어오고, 없으면 기본값 80을 사용합니다.
    port = int(os.environ.get("PORT", 80))
    
    # Flask 개발 서버를 시작합니다.
    app.run(host='0.0.0.0', 
            # 'host='0.0.0.0''는 외부에서 접속 가능하도록 모든 네트워크 인터페이스를 수신 대기합니다.
            port=port,  # 환경 변수 또는 기본값으로 설정된 포트에서 수신 대기합니다.
            debug=True) # 디버그 모드 활성화 (코드 변경 시 자동 재시작 및 오류 상세 정보 표시)