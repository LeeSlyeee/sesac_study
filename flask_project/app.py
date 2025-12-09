from flask import Flask # Flask 모듈에서 Flask 클래스를 임포트합니다. 웹 애플리케이션 객체를 생성하는 데 사용됩니다.

app = Flask(__name__) # Flask 애플리케이션 객체를 생성합니다.
                      # '__name__'은 현재 모듈의 이름으로, Flask가 리소스(템플릿, 정적 파일)를 찾을 위치를 결정하는 데 도움을 줍니다.

# --- 라우트 정의 시작 ---

@app.route('/') # 루트 URL ('/')에 대한 라우트를 정의합니다. 
                # 사용자가 이 URL로 접근하면 바로 아래의 index 함수가 실행됩니다.
def index():
    return 'Hi!!!' # 함수가 실행될 때 웹 브라우저에 'Hi!!!'라는 문자열을 응답으로 반환합니다.

@app.route('/hello/<name>', # '/hello/' 뒤에 변수(variable part)를 포함하는 URL에 대한 라우트를 정의합니다.
                            # <name> 부분은 URL에서 추출되어 hello 함수의 인수로 전달됩니다.
             methods=['GET'], # 이 라우트는 HTTP GET 요청만 처리하도록 지정합니다. (선택 사항이지만 명시적으로 지정)
             endpoint='hello_endpoint') # 이 라우트에 'hello_endpoint'라는 고유한 이름을 부여합니다.
                                        # URL을 동적으로 생성하거나(url_for 함수) 뷰 함수를 참조할 때 사용될 수 있습니다.
def hello(name): # 라우트에 연결된 뷰 함수입니다. URL에서 추출된 name 값이 인수로 전달됩니다.
    return f'Hello, World! {name}' # 전달받은 name 값을 포함하여 포맷팅된 문자열을 응답으로 반환합니다.

# --- 라우트 정의 끝 ---

app.run(port=8080, # 개발 서버를 실행합니다. 'port=8080'은 서버가 8080 포트에서 수신 대기하도록 지정합니다.
        debug=True) # 디버그 모드를 활성화합니다. 
                    # 코드를 수정하고 저장하면 서버가 자동으로 재시작되며, 오류 발생 시 상세한 디버그 정보를 웹 페이지에 표시합니다.