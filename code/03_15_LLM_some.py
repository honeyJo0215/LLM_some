#!/usr/bin/env python3
"""
썸 판별 LLM 모델
- 연애 초기 '썸' 단계에서 흔히 겪는 착각과 진짜 감정 신호를 데이터 기반 심리학 연구를 참고하여 설명합니다.
- 확장된 감정 분석 알고리즘과 다수의 if-else 조건을 통해 사용자가 입력한 상황을 분석합니다.
- 두 가지 모드를 제공합니다.
    1. 자유 서술 입력: 사용자가 자신의 상황을 자유롭게 기술하면, 입력된 문장을 활용해 상세한 분석 결과를 도출합니다.
    2. 질문 기반 입력: 다수의 예/아니오 질문에 답변하면, 조건별 점수를 합산하여 세밀한 분석 결과를 제공합니다.
    
※ 이 모델은 참고용 알고리즘으로, 실제 인간 감정이나 관계의 복잡성을 완벽하게 대변하지는 않습니다.
"""

def analyze_text(input_text):
    """
    자유 서술 입력에 대해 감정 분석을 진행합니다.
    확장된 긍정적 신호와 부정적 또는 애매한 신호를 체크하여 점수를 산출합니다.
    """
    positive_keywords = [
        '연락', '관심', '미소', '칭찬', '만남', '데이트', '행복', '기대',
        '사랑', '로맨스', '애정', '따뜻', '배려', '섬세', '감동', '설렘',
        '존중', '격려', '유머', '신뢰', '친밀', '공감', '감사', '낭만',
        '친절', '열정', '감탄', '기쁨', '환상', '희망', '긍정', '존중감',
        '깊은', '진심', '솔직', '조화', '열의', '관심도', '웃음', '애틋',
        '헌신', '열렬', '매력', '즐거움', '활력', '편안', '밥', '술', '아싸'
    ]
    ambiguous_keywords = [
        '친구', '그냥', '평범', '우정', '애매', '무관심', '지루', '냉정',
        '일상', '단순', '만남뿐', '관심부족', '무심', '의심', '불안',
        '혼란', '불확실', '한계', '피곤', '피상적', '표면적', '무의미', '안',
        '망함', '끊어', '여사친', '남사친', '모두', '만인', '쉬운', '아니', '원나잇',
        '인싸'
    ]
    
    score = 0
    for word in positive_keywords:
        if word in input_text:
            score += 1
    for word in ambiguous_keywords:
        if word in input_text:
            score -= 1
    return score

def detailed_text_analysis(situation, score):
    """
    자유 서술 입력을 바탕으로, 입력된 문장과 점수를 활용하여 상세 분석 결과를 생성합니다.
    """
    result_text = f"입력하신 내용:\n{situation}\n\n"
    result_text += f"계산된 감정 분석 점수: {score}\n\n"
    
    if score > 5:
        result_text += ("분석 결과:\n귀하의 서술에서는 상대방에 대한 긍정적 감정과 로맨틱한 신호가 두드러집니다. "
                        "자주 언급된 표현으로 분석을 진행한 결과, "
                        "상대방이 호감을 적극적으로 표현하고 있음을 보여줍니다. 이러한 요소는 두 사람 사이의 관계 발전 가능성이 높음을 시사합니다.")
    elif score < -5:
        result_text += ("분석 결과:\n입력하신 내용에서는 부정적 또는 모호한 감정 신호가 우세합니다. "
                        "자주 언급된 표현으로 분석을 진행한 결과, "
                        "우정 또는 피상적인 관계에 머무를 가능성이 높음을 암시합니다.")
    else:
        result_text += ("분석 결과:\n귀하의 서술은 긍정적 신호와 부정적 신호가 혼재되어 있어 상황이 다소 모호하게 나타납니다. "
                        "이 경우, 보다 구체적인 상황 파악과 추가적인 소통이 필요할 수 있으며, 단순한 결과보다는 다양한 측면에서 관계를 재검토할 필요가 있습니다.")
    
    return result_text

def determine_relationship_by_text():
    """
    자유 서술 입력을 받아 감정 분석 후, 상세 분석 결과 문자열을 반환합니다.
    """
    situation = input("자신의 상황을 자유롭게 서술해주세요 (자세하게 입력할수록 정확한 분석이 가능합니다):\n")
    score = analyze_text(situation.lower())
    detailed_result = detailed_text_analysis(situation, score)
    return detailed_result

def detailed_question_analysis(score):
    """
    예/아니오 질문 응답 결과 점수를 바탕으로 상세 분석 결과를 생성합니다.
    """
    result_text = f"예/아니오 응답을 종합한 총점: {score}\n\n"
    
    if score >= 20:
        result_text += ("분석 결과:\n응답을 종합해보면, 상대방은 일관되고 적극적인 감정 표현 및 호감의 신호를 보이고 있습니다. "
                        "자주 연락을 시도하고, 진심 어린 칭찬과 미소를 통해 긍정적인 상호작용을 이어가고 있는 것으로 보입니다. "
                        "이러한 신호들은 두 사람의 관계가 로맨틱하게 발전할 가능성이 높음을 시사합니다.")
    elif score <= 10:
        result_text += ("분석 결과:\n예/아니오 응답 결과, 상대방은 감정 표현에 있어서 다소 소극적인 모습을 보입니다. "
                        "연락 빈도, 대화 중 긍정적 신호, 약속 이행 등에서 나타난 점수를 종합해볼 때, 현재 관계는 "
                        "단순한 우정이나 피상적인 관심에 머물 가능성이 높음을 암시합니다.")
    else:
        result_text += ("분석 결과:\n응답 결과가 중간 범위로 나타났습니다. 일부 항목에서는 상대방의 관심과 호감 신호가 보이지만, "
                        "다른 항목에서는 그 신호가 미약합니다. 이러한 모호한 결과는 관계 발전 여부가 상황에 따라 달라질 수 있음을 의미하며, "
                        "추가적인 소통과 관찰이 필요할 수 있음을 보여줍니다.")
    
    return result_text

def determine_relationship_by_questions():
    """
    예/아니오 질문을 통해 점수를 산출하고, 상세 분석 결과 문자열을 반환합니다.
    """
    score = 0
    print("\n아래의 질문에 '예' 또는 '아니오'로 답해주세요.")
    
    questions = [
        ("1. 상대방이 먼저 연락하는 경우가 많습니까?", 2),
        ("2. 대화 중 긍정적인 감정 표현(칭찬, 미소 등)이 자주 있습니까?", 2),
        ("3. 만남이나 데이트 제안이 자연스럽게 이어집니까?", 2),
        ("4. 상대방의 태도가 일관되고 뚜렷합니까?", 2),
        ("5. 대화 주제에 깊이가 있고 감정적인 이야기가 오갑니까?", 2),
        ("6. 상대방이 당신의 이야기에 진심으로 공감합니까?", 2),
        ("7. 서로의 개인적인 관심사와 취미에 대해 자주 이야기합니까?", 2),
        ("8. 상대방이 당신의 기분을 세심하게 살펴줍니까?", 2),
        ("9. 만남 후 긍정적인 피드백이나 감사의 메시지를 자주 받습니까?", 2),
        ("10. 약속을 지키고 시간 약속에 충실합니까?", 2),
        ("11. 상대방의 말투와 표정에서 진심을 느낄 수 있습니까?", 2),
        ("12. 상대방이 당신의 주변 사람들에게 긍정적인 인상을 주었습니까?", 2),
        ("13. 만남의 빈도와 지속성이 자연스러운 흐름을 보입니까?", 2),
        ("14. 서로의 미래에 대해 가볍게나마 이야기합니까?", 2),
        ("15. 상대방이 작은 선물이나 관심을 표현합니까?", 2),
        ("16. 만날 때마다 서로에 대해 더 알아가고 있습니까?", 2),
        ("17. 상대방이 어려운 상황에서 지원이나 도움을 주었습니까?", 2),
        ("18. 상대방이 당신을 특별하다고 느끼게 만듭니까?", 2),
        ("19. 상대방이 당신의 성격이나 취향을 잘 이해합니까?", 2),
        ("20. 상대방의 행동에서 일관된 관심과 애정이 보입니까?", 2)
    ]
    
    for q, weight in questions:
        ans = input(q + " (예/아니오): ").strip().lower()
        if ans == "예":
            score += weight
    
    detailed_result = detailed_question_analysis(score)
    return detailed_result

def show_result_window(result_text):
    """
    Tkinter 창을 생성하여, 분석 결과를 사용자가 창을 닫을 때까지 표시합니다.
    """
    import tkinter as tk
    root = tk.Tk()
    root.title("분석 결과")
    root.geometry("600x400")
    
    # Text 위젯을 사용하여 멀티라인 텍스트 표시
    text_widget = tk.Text(root, wrap="word", font=("Arial", 12))
    text_widget.pack(expand=True, fill="both", padx=10, pady=10)
    text_widget.insert("1.0", result_text)
    text_widget.config(state="disabled")  # 읽기 전용으로 설정
    
    close_button = tk.Button(root, text="닫기", command=root.destroy)
    close_button.pack(pady=10)
    
    root.mainloop()

def main():
    print("==== 썸 판별 LLM 모델 ====")
    print("연애 초기의 '썸'과 '착각'을 구분하는 알고리즘에 오신 것을 환영합니다!")
    print("이 모델은 데이터 기반 심리학 연구와 확장된 감정 분석, if-else 조건을 활용하여 상세한 분석 결과를 도출합니다.\n")
    
    mode = input("자유 서술로 상황을 분석하시겠습니까? (자유 서술: y / 질문 방식: n): ").strip().lower()
    if mode == 'y':
        result_text = determine_relationship_by_text()
    else:
        result_text = determine_relationship_by_questions()
    
    print("\n분석이 완료되었습니다. 결과 창이 나타납니다. 창을 닫기 전까지 결과를 확인하실 수 있습니다.")
    show_result_window(result_text)

if __name__ == "__main__":
    main()
