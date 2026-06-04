#!/usr/bin/env python3
"""Parse TOPIK II Exam 35 Reading - manual fix for complex questions."""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load existing JSON
with open(r'D:\A Web\the-free-korean\src\content\topik\thi-thu\topik2-thi-thu-35.json', 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

reading = exam_data['sections'][1]['questions']

# Manually fix questions that need passage text
# For Q5-8: passage is an image, just note it
for qid in [5, 6, 7, 8]:
    q = next((q for q in reading if q['id'] == qid), None)
    if q:
        q['question_ko'] = '[Hình ảnh/đoạn văn - xem đề thi gốc]'
        # Keep existing choices

# For Q9-12: passage is image/text that needs context
for qid in [9, 10, 11, 12]:
    q = next((q for q in reading if q['id'] == qid), None)
    if q:
        q['question_ko'] = '[Đoạn văn/đồ thị - xem đề thi gốc]'
        # Keep existing choices

# For Q19-20: passage about fruit
passage_19_20 = "과일을 빨리 익히기 위해 화학 물질이 사용되기도 한다.그러나 화학 물질로 익힌 과일은 겉은 익었지만 속이 잘 익지 않은 경우가 많다.그래서 화학 물질로 익힌 과일은 대개 자연적으로 숙성된 과일에 비해 맛과 향이 떨어진다.( )화학 물질이 과일 껍질에 남게 될 수도 있다.이런 과일을 지속적으로 먹으면 건강에 문제가 생기게 된다."

q19 = next((q for q in reading if q['id'] == 19), None)
if q19:
    q19['question_ko'] = passage_19_20 + "\n\n19. ( )에 들어갈 알맞은 것을 고르십시오."
    q19['choices'] = ["또한", "또한", "그래도", "그러면"]

q20 = next((q for q in reading if q['id'] == 20), None)
if q20:
    q20['question_ko'] = passage_19_20 + "\n\n20. 이 글의 내용과 같은 것을 고르십시오."
    q20['choices'] = [
        "과일을 껍질까지 먹으면 건강에 좋다.",
        "과일 향을 좋게 만드는 화학 물질이 있다.",
        "화학 물질을 사용하면 과일이 속까지 잘 익는다.",
        "자연 숙성 과일이 인공 숙성 과일보다 맛이 더 낫다."
    ]

# For Q21-22: passage about choices
passage_21_22 = "사람들은 보통 선택을 할 때 여러 가지 중에서 고르면 더 좋은 선택을 할 수 있을 것이라고 생각한다.그래서 선택이 필요할 때 정보를 많이 수집하려고 노력한다.그러나 선택의 수가 늘어나면 고민의 양도 함께 증가한다.( )결정을 내리지 못하는 상황이 되는 것이다.후회 없는 선택을 위한 노력이 오히려 선택을 방해하는 결과를 불러오게 된다."

q21 = next((q for q in reading if q['id'] == 21), None)
if q21:
    q21['question_ko'] = passage_21_22 + "\n\n21. ( )에 들어갈 알맞은 것을 고르십시오."
    q21['choices'] = ["골치만 아프고", "콧대만 높아지고", "눈치만 빨라지고", "비행기만 태우고"]

q22 = next((q for q in reading if q['id'] == 22), None)
if q22:
    q22['question_ko'] = passage_21_22 + "\n\n22. 이 글의 중심 생각을 고르십시오."
    q22['choices'] = [
        "고민할수록 더 좋은 선택을 할 수 있다.",
        "선택의 폭이 넓어지면 결정이 더 어려워진다.",
        "선택을 할 때는 먼저 방해 요인을 없애야 한다.",
        "후회 없는 선택을 하려면 풍부한 정보가 필요하다."
    ]

# For Q23-24: passage about company
passage_23_24 = "내가 운영하는 회사의 사정이 점점 더 어려워졌다.공장에 불이 나서 피해를 입은 데다가 매출까지 크게 감소한 것이다.어쩔 수 없이 직원 수를 줄여야 했다.나는 직원들을 한자리에 불러 모아 놓고도 한참을 아무 말도 할 수 없었다.눈을 지그시 감고 겨우 입을 떼려는 순간 \"사장님!\"한 직원이 나를 불렀다.그 직원은 흰 봉투를 내 앞으로 내밀면서 말했다.\"그동안 어려운 회사 살림 때문에 고생 많으셨습니다.어려워진 회사에 도움이 될까 싶어서 저희들이 월급의 10퍼센트씩을 모았습니다.적은 돈이지만 회사 운영에 도움이 되었으면 합니다.\"순간 나는 마치 천하를 얻은 듯 마음이 든든해졌다."

q23 = next((q for q in reading if q['id'] == 23), None)
if q23:
    q23['question_ko'] = passage_23_24 + "\n\n23. 밑줄 친 부분에 나타난 나의 심정으로 알맞은 것을 고르십시오."
    q23['choices'] = ["곤란하다", "섭섭하다", "부끄럽다", "당황하다"]

q24 = next((q for q in reading if q['id'] == 24), None)
if q24:
    q24['question_ko'] = passage_23_24 + "\n\n24. 이 글의 내용과 같은 것을 고르십시오."
    q24['choices'] = [
        "화재가 발생한 후 회사의 사정이 좋아졌다.",
        "나는 회사에서 일할 새로운 직원들을 뽑았다.",
        "직원들이 월급의 일부를 걷어 회사를 도왔다.",
        "흰 봉투 안에는 직원들이 쓴 편지가 들어 있었다."
    ]

# For Q41: special question about book
q41 = next((q for q in reading if q['id'] == 41), None)
if q41:
    q41['question_ko'] = "지난 10년간 '한국형 리더십'에 남다른 관심을 쏟아 온 박선호 박사는 세종에게서 배우다 라는 신간을 내놓았다.( ㉠ ) 세종에게서 배우다 는 세종의 리더십을 배워 잘 활용할 수 있도록 돕는 일종의 경영서이다.( ㉡ )세종은 여러 분야에서 리더로서의 면모를 보여 주었다.만일 그에게 탁월한 리더십이 없었더라면 한글 창제와 같은 업적은 불가능했을지도 모른다.( ㉢ )신분이나 지역을 따지지 않고 오직 개인의 역량만을 기준으로 사람을 뽑아 썼다.( ㉣ )\n\n<보기>\n세종의 남다른 리더십은 인재의 등용에서도 잘 나타난다.\n\n41. 다음 문장이 들어가기에 가장 알맞은 곳을 고르십시오."
    q41['choices'] = ["㉠", "㉡", "㉢", "㉣"]

# For Q42-43: passage about diving
passage_42_43 = "초등학교 3학년쯤으로 보이는 남자 아이가 가장 높은 다이빙대에 올라갔다.성인도 호기로 올라갔다가 그냥 내려오곤 하는 곳이었다.소년은 무서워서 뛰어내리지도,뒤돌아 내려가지도 못하고 다이빙대 끝과 계단 사이를 한참 왔다 갔다 했다.그러자 부모로 보이는 사람이 내려오라는 손짓을 했다.아이는 계속 망설였다.수영장의 모든 사람이 이 모습을 지켜보고 있었다.그때였다.스피커에서 수영장 관리자로 추정되는 사람의 목소리가 나오기 시작했다.나는 당연히 아이의 부모에게 '어서 아이를 데리고 내려오라.'고 말할 줄 알았다.그런데 그는 전혀 다른 말을 했다.\"넌 할 수 있어!내가 도와줄게.이제 셋을 셀 거야.겁내지 말고 뛰어내리면 돼!\"그리고 큰 소리로 숫자를 세기 시작했다.수영장에 있던 모든 사람도 스피커 소리를 따라 큰 소리로 숫자를 따라 셌다.(중략)\n아이는 다이빙대 끝을 박차고 허공에 손을 휘저으며 뛰어내렸다.아이가 물로 떨어지는 몇 초 동안,모든 것은 잠시 숨을 멈추었다.바람도 공기도 나뭇잎의 흔들림까지.이윽고 '풍덩'하는 소리와 함께 세상은 다시 깨어났다.박수 소리가 수영장을 울렸다.나도 손뿐 아니라 마음 깊은 곳에서 박수를 보냈다."

q42 = next((q for q in reading if q['id'] == 42), None)
if q42:
    q42['question_ko'] = passage_42_43 + "\n\n42. 밑줄 친 부분에 나타난 사람들의 태도로 알맞은 것을 고르십시오."
    q42['choices'] = ["격려하고 있다", "위로하고 있다", "안도하고 있다", "원망하고 있다"]

q43 = next((q for q in reading if q['id'] == 43), None)
if q43:
    q43['question_ko'] = passage_42_43 + "\n\n43. 이 글의 내용과 같은 것을 고르십시오."
    q43['choices'] = [
        "아이가 올라간 다이빙대는 어린이 전용으로 만들어졌다.",
        "아이가 뛰어내려 물속으로 들어가자 사람들이 박수를 쳤다.",
        "방송을 통해 아이의 부모가 아이에게 내려오라고 소리쳤다.",
        "아이의 부모는 관리자에게 아이를 데려와 달라고 부탁했다."
    ]

# For Q44-45: passage about emissions
passage_44_45 = "환경부는 '온실가스 배출권 거래제'의 시행을 앞두고 향후 3년간 온실가스 총량을 정해 업종별로 할당한다는 계획을 발표했다.이 제도는 지구온난화의 원인인 온실가스를 줄이기 위한 것으로 업체별로 일정한 배출량을 정해 놓고 기준보다 많거나 모자라는 경우 배출권을 사고팔 수 있게 하는 제도이다.그런데 기업의 성장률을 고려하지 않고 할당량을 정하는 방식에 대해 문제가 있다는 지적이 있다.( )기업은 배출권을 구입해야 하는데 경영 악화로 공장을 가동하지 않는 기업은 도리어 배출권 판매 이익을 취할 수 있기 때문이다.새 제도의 정착을 위해 모두가 납득할 수 있는 합리적인 시행 방안이 마련되어야 할 것이다."

q44 = next((q for q in reading if q['id'] == 44), None)
if q44:
    q44['question_ko'] = passage_44_45 + "\n\n44. 이 글의 주제로 알맞은 것을 고르십시오."
    q44['choices'] = [
        "기업이 동의하지 않는 제도의 시행은 지양해야 한다.",
        "배출권 할당은 기업의 사정에 따라 조정되어야 한다.",
        "배출권 할당은 의도적인 거래를 염두에 두어야 한다.",
        "현실성을 고려한 환경 보호 대책이 마련되어야 한다."
    ]

q45 = next((q for q in reading if q['id'] == 45), None)
if q45:
    q45['question_ko'] = passage_44_45 + "\n\n45. ( )에 들어갈 내용으로 알맞은 것을 고르십시오."
    q45['choices'] = [
        "배출량이 할당된 양에 못 미친",
        "온실가스 총량을 신고하지 않은",
        "매출이 늘어 공장 가동률이 높아진",
        "경영진의 배출량 감소 의지가 강한"
    ]

# For Q46-47: passage about merger
passage_46_47 = "만년 2위를 면하지 못하던 포털 사이트 '둠'과 모바일 서비스 시장의 떠오르는 샛별 '코코'가 합병을 결정하면서 IT업계의 지각 변동이 예고된다.이를 두고 재계의 예측은 양분된다.( ㉠ )그 하나는 둠의 콘텐츠와 코코의 서비스 경쟁력이 결합했을 때 최상의 시너지 효과를 발휘할 것이라고 보는 입장이다.( ㉡ )다른 하나는 현재보다 그 역량이 줄어들 것이라고 보는 입장이다.( ㉢ )혼자서 하는 일에는 최선을 다하던 사람도 공동 작업에서는 그렇지 않을 수 있기 때문이다.( ㉣ )여기에 코코의 경우 소규모 기업으로 시장 상황에 발 빠르게 대처한다는 게 강점이었는데,몸집이 커지면 그것이 어렵게 될 것이라는 점도 이유로 들었다."

q46 = next((q for q in reading if q['id'] == 46), None)
if q46:
    q46['question_ko'] = passage_46_47 + "\n\n<보기>\n이는 합병 기업이 각자의 강점을 합친 것 이상의 역량을 발휘했을 때 가능하다.\n\n46. 다음 문장이 들어가기에 가장 알맞은 곳을 고르십시오."
    q46['choices'] = ["㉠", "㉡", "㉢", "㉣"]

q47 = next((q for q in reading if q['id'] == 47), None)
if q47:
    q47['question_ko'] = passage_46_47 + "\n\n47. 이 글의 내용과 같은 것을 고르십시오."
    q47['choices'] = [
        "양 기업의 합병은 코코의 경영 부진에 의한 것이다.",
        "양 기업의 규모는 동종 업계에서 우열을 가리기 어렵다.",
        "코코는 그동안 신속한 업무 처리로 재계의 인정을 받아 왔다.",
        "둠과 코코의 합병에 대한 예측들은 긍정적이라는 공통점이 있다."
    ]

# For Q48-50: passage about privacy
passage_48_50 = "인터넷 공간에서의 개인 정보 삭제에 관한 법안 제정이 뜨거운 쟁점으로 부각되고 있다.유럽에서는 이러한 법안이 통과되었고 미국에서도 제한적으로 적용하기로 결정되었다.우리 사회에서도 그간 피해 사례가 잘 알려져 있기 때문인지 찬성 쪽으로 공감대가 형성되어 있는 듯하다.그러나 이는 이면에 잠재한 부정적 측면을 고려하지 않은 성급한 동조이다.이 법안이 실행되었을 때 나타날 수 있는 부작용을 생각해 보라.삭제된 정보가 흉악 범에 관한 것이라면,특정 기업의 부조리나 공직자의 비리를 고발한 기사라면…….법 시행의 결과가 개인뿐만 아니라 사회,국가의 불행으로 이어지지 않는다고 누가 자신할 수 있겠는가?예컨대 누군가가 후속 범죄의 대상이 될 수도 있고 과거의 행적을 조작한 후보자가 선거에서 당선될 수도 있다.개인의 권리를 존중하려는 의도가 ( )장치가 되어서는 안 될 것이다."

q48 = next((q for q in reading if q['id'] == 48), None)
if q48:
    q48['question_ko'] = passage_48_50 + "\n\n48. 필자가 이 글을 쓴 목적을 고르십시오."
    q48['choices'] = [
        "법 제정의 공론화를 촉구하기 위해",
        "법 제정의 반대 근거를 제시하기 위해",
        "법 시행의 피해 사례를 알려 주기 위해",
        "법 시행의 적절한 시기를 제안하기 위해"
    ]

q49 = next((q for q in reading if q['id'] == 49), None)
if q49:
    q49['question_ko'] = passage_48_50 + "\n\n49. ( )에 들어갈 내용으로 알맞은 것을 고르십시오."
    q49['choices'] = [
        "공공의 피해를 유발하는",
        "국민의 자유를 침해하는",
        "소통의 단절을 조장하는",
        "사회의 통합을 저해하는"
    ]

q50 = next((q for q in reading if q['id'] == 50), None)
if q50:
    q50['question_ko'] = passage_48_50 + "\n\n50. 밑줄 친 부분에 나타난 필자의 태도로 알맞은 것을 고르십시오."
    q50['choices'] = [
        "이 법으로 피해를 입은 사람들을 동정하고 있다.",
        "이 법의 제정 단계에서의 문제점을 지적하고 있다.",
        "이 법이 실패했던 해외 사례에 대해 비판하고 있다.",
        "이 법의 시행이 가져올 부작용에 대해 염려하고 있다."
    ]

# Save updated JSON
exam_data['sections'][1]['questions'] = reading

with open(r'D:\A Web\the-free-korean\src\content\topik\thi-thu\topik2-thi-thu-35.json', 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

# Verify
with open(r'D:\A Web\the-free-korean\src\content\topik\thi-thu\topik2-thi-thu-35.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

reading = data['sections'][1]['questions']
with_text = sum(1 for q in reading if q['question_ko'])
with_choices = sum(1 for q in reading if q['choices'])

print(f"✅ Reading section updated!")
print(f"   Total: {len(reading)} questions")
print(f"   With text: {with_text}")
print(f"   With choices: {with_choices}")

# Show empty
empty = [q['id'] for q in reading if not q['question_ko']]
if empty:
    print(f"   Still empty: {empty}")
else:
    print(f"   All questions have text! ✅")
