import streamlit as st

# 웹 페이지 제목 설정
st.title("🚚 배송비 안내 프로그램")
st.write("주문 정보를 입력하시면 배송비를 포함한 총 결제금액을 계산해 드립니다.")

st.divider()  # 구분선

# 1. 회원 여부 입력 (라디오 버튼)
member = st.radio("정기 회원입니까?", ["예 (y)", "아니오 (n)"])

# 2. 주문 금액 입력 (숫자 입력창)
total = st.number_input("주문 금액은 얼마입니까? (원)", min_value=0, step=1000, value=0)

# 3. 계산하기 버튼
if st.button("결제 금액 계산하기"):
    st.subheader("📊 계산 결과")
    
    if member == "예 (y)":
        st.info("💡 정기회원으로 배송비가 면제됩니다.")
    else:
        st.warning("⚠️ 배송비 3000원이 부과됩니다.")
        total += 3000
        
    # 최종 금액 출력 (강조 효과)
    st.success(f"💰 총 결제금액은 **{total:,}원** 입니다.")