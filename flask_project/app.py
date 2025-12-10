import os  # 운영체제(Operating System)와 상호작용하기 위한 표준 라이브러리 모듈을 임포트합니다. 
           # 주로 환경 변수(Environment Variable)를 읽어오는 데 사용됩니다.
import json
from flask import Flask # Flask 웹 프레임워크의 핵심인 Flask 클래스를 임포트합니다. 이 클래스를 사용하여 애플리케이션 객체를 생성합니다.
from flask import render_template # Jinja2 템플릿 엔진을 사용하여 HTML 파일을 렌더링하고 사용자에게 응답하는 함수를 임포트합니다.
from flask import url_for # Flask에서 뷰 함수 이름(엔드포인트)을 기반으로 URL을 동적으로 생성하는 함수를 임포트합니다.
from flask import request
from flask import redirect


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

 
    


# --- url_for 테스트 블록 시작 ---
# Flask 애플리케이션의 컨텍스트 외부에서 url_for 함수를 사용하려면 반드시 이 블록이 필요합니다.
with app.test_request_context():
    # 💡 url_for 함수는 엔드포인트 이름(뷰 함수 이름)을 기반으로 URL 문자열을 동적으로 생성합니다.
    print(url_for('index')) # 결과: '/' (인수가 필요 없는 정적 라우트)
    
    # 동적 라우트('hello_endpoint')의 변수(name)를 키워드 인수로 전달합니다.
    print(url_for('hello_endpoint', name="Slyeee")) # 결과: '/hello/Slyeee'
    
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