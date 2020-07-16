from django.test import TestCase

# Create your tests here.

"""
from django.db.models import Q 
# Q함수는 OR조건으로 데이터를 조회하기 위한 장고가 제공하는 함수

kw = request.GET.get('kw', '')  # 검색어

if kw:
    question_list = question_list.filter(
        Q(subject__icontains=kw) |  # 제목검색
        Q(content__icontains=kw) |  # 내용검색
        Q(author__username__icontains=kw) |  # 질문 글쓴이검색
        Q(answer__author__username__icontains=kw)  # 답글 글쓴이검색
    ).distinct() 

    # filter 함수뒤에 사용된 distinct 함수는 조회결과에 중복이 있을 경우 중복을 제거하고 리턴하게 해 주는 함수

    이렇게 POST방식으로 검색과 페이징이 적용되면 웹브라우저에서 "새로고침" 또는 "뒤로가기" 버튼을 클릭할 때 "만료된 페이지입니다."라는 오류를 만나게 된다. 왜냐하면 POST방식은 동일한 POST요청이 발생할 경우 중복요청을 방지하기 위해 "만료된 페이지입니다." 오류를 발생시키기 때문이다. 2페이지에서 3페이지로 갔다가 웹브라우저 뒤로가기 버튼을 클릭했을 때 2페이지로 가는것이 아니라 오류가 발생된다면 엉망이 될 것이다.

    
    게시판을 조회하는 index함수를 호출할 때는 GET방식을 사용해야 한다. 앞으로 추가될 정렬기능에 대한 파라미터 so도 GET방식으로 요청될 것이다.
"""    