from flask import Flask, render_template

app = Flask(__name__)

# 가상의 분석 결과를 위한 더미 데이터
# 실제 데이터 분석 결과로 대체해야 합니다.
presentation_data = {
    "budget": "10억원",
    "candidate_regions": [
        {"gu": "도봉구", "dong": "창동", "avg_price": "5.5억", "note": "교통 및 재개발 잠재력 우수"},
        {"gu": "강서구", "dong": "화곡동", "avg_price": "6.2억", "note": "주변 인프라 및 마트 접근성 좋음"},
        {"gu": "관악구", "dong": "봉천동", "avg_price": "7.8억", "note": "대학가 인접, 지하철 이용 편리"}
    ],
    "analysis_summary": {
        "volume": "2022년 대비 2023년 거래량 감소 후, 2024년 이후 점진적 회복세",
        "price_change": "2023년 하락 후 2024년 소폭 반등"
    },
    "final_decision": {
        "gu": "도봉구",
        "dong": "창동",
        "reason": "예산 충족, GTX-C 노선 개통 예정 등 교통 호재 및 창동 아레나와 같은 대형 개발로 미래 가치가 가장 높다고 판단."
    }
}

@app.route('/')
def presentation():
    """발표 자료 템플릿을 렌더링합니다."""
    return render_template('presentation.html', data=presentation_data)

if __name__ == '__main__':
    # 디버그 모드는 개발 단계에서만 사용하고, 실제 발표 시에는 False로 설정하는 것이 좋습니다.
    app.run(debug=True)