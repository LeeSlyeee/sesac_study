import os # 운영체제(Operating System)와 상호작용하기 위한 모듈을 임포트합니다. 
           # 주로 환경 변수(PORT)를 읽어오는 데 사용됩니다.
from flask import Flask # Flask 모듈에서 Flask 클래스를 임포트합니다. 웹 애플리케이션 객체를 생성하는 데 사용됩니다.
from flask import render_template

app = Flask(__name__) # Flask 애플리케이션 객체를 생성합니다.
                      # '__name__'은 현재 모듈의 이름으로, Flask가 리소스(템플릿, 정적 파일)를 찾을 위치를 결정하는 데 도움을 줍니다.

# --- 라우트 정의 시작 ---

@app.route('/') # 루트 URL ('/')에 대한 라우트를 정의합니다. 
                # 사용자가 애플리케이션의 기본 주소로 접근하면 바로 아래의 index 함수가 실행됩니다.
def index():
    """기본 경로('/') 요청을 처리하는 뷰 함수입니다."""
    return 'Hi!!!' # 웹 브라우저에 'Hi!!!'라는 문자열을 응답으로 반환합니다.

@app.route('/hello/<name>', # '/hello/' 뒤에 변수(variable part)를 포함하는 동적 URL에 대한 라우트를 정의합니다.
                            # <name> 부분은 URL에서 추출되어 hello 함수의 인수로 전달됩니다.
           methods=['GET'], # 이 라우트는 HTTP GET 요청만 처리하도록 지정합니다. 
           endpoint='hello_endpoint') # 이 라우트에 'hello_endpoint'라는 고유한 이름을 부여합니다.
def hello(name): # 라우트에 연결된 뷰 함수입니다. URL에서 추출된 name 값이 인수로 전달됩니다.
    """동적 경로('/hello/<name>') 요청을 처리하고, URL에서 받은 이름을 포함하여 응답합니다."""
    # f-string을 사용하여 전달받은 name 값을 포함하는 포맷팅된 문자열을 응답으로 반환합니다.
    return f'Hello, World! {name}' 


@app.route('/data/', endpoint='data_endpoint')
def html():
    return render_template('index.html')



# --- 라우트 정의 끝 ---

if __name__ == "__main__":
    # 애플리케이션이 직접 실행될 때 (import되지 않고) 서버를 구동하는 블록입니다.
    
    # 💡 환경 변수 설정: Cloud Run(또는 대부분의 PaaS)에서 컨테이너 포트 문제를 해결하기 위한 핵심 부분입니다.
    #    os.environ.get("PORT")를 통해 'PORT' 환경 변수 값을 가져옵니다.
    #    만약 환경 변수가 설정되어 있지 않다면, 기본값으로 80을 사용합니다.
    port = int(os.environ.get("PORT", 80))
    
    # Flask 개발 서버를 실행합니다.
    app.run(host='0.0.0.0', 
            # '0.0.0.0'은 모든 공개 IP 주소에서 들어오는 연결을 수신하겠다는 의미입니다.
            # 컨테이너 환경에서 외부 트래픽을 받기 위해 필수적인 설정입니다.
            port=port,  # 환경 변수에서 가져온 포트 번호(또는 기본값 80)에서 수신 대기하도록 지정합니다.
            debug=True) # 디버그 모드를 활성화합니다. 
                        # 코드를 수정하고 저장하면 서버가 자동으로 재시작되며, 오류 발생 시 웹 페이지에 상세한 디버그 정보를 표시합니다.