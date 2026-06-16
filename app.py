import streamlit as st

# Tiêu đề ứng dụng
st.title("💰 Ứng dụng tính thuế thu nhập cá nhân")

# Nhập dữ liệu
TN = st.number_input(
    "Nhập tổng thu nhập (đồng)",
    min_value=0.0,
    value=100.0
)

i = st.number_input(
    "Nhập số người phụ thuộc(người) ",
    min_value=0.0,
    value=1.0
)

n = st.number_input(
    "Nhập số tiền bảo hiểm phải nộp(đồng)",
    min_value=0.0,
    value=1.0
)

giam_tru_ban_than = 15500000
giam_tru_npt = nguoi_phu_thuoc * 6200000


# Nút tính toán
if st.button("Tính toán"):

# Tổng các khoản được giảm trừ
tong_giam_tru = giam_tru_ban_than + giam_tru_npt + bao_hiem

# Thu nhập tính thuế
thu_nhap_tinh_thue = a - tong_giam_tru
        
if thu_nhap_tinh_thue < 0:
   thu_nhap_tinh_thue = 0
print(f"Tổng thu nhập tính thuế: {thu_nhap_tinh_thue:,.2f} đồng" )

 # Tính thuế TNCN theo biểu thuế lũy tiến từng phần
thue_tncn = 0
if thu_nhap_tinh_thue > 0:
    # Bậc 1: Đến 10 triệu
    if thu_nhap_tinh_thue <= 10000000:
     thue_tncn = thu_nhap_tinh_thue * 0.05
    # Bậc 2: Trên 10 đến 30 triệu
    elif thu_nhap_tinh_thue <= 30000000:
     thue_tncn = (10000000 * 0.05) + ((thu_nhap_tinh_thue - 10000000) * 0.10)
    # Bậc 3: Trên 30 đến 60 triệu
    elif thu_nhap_tinh_thue <= 60000000:
     thue_tncn = (10000000 * 0.05) + (20000000 * 0.10) + ((thu_nhap_tinh_thue - 30000000) * 0.20)
    # Bậc 4: Trên 60 đến 100 triệu
    elif thu_nhap_tinh_thue <= 100000000:
     thue_tncn = (10000000 * 0.05) + (20000000 * 0.10) + (30000000 * 0.20) + ((thu_nhap_tinh_thue - 60000000) * 0.30)
    # Bậc 5: Trên 100 triệu
    else:
     thue_tncn = (10000000 * 0.05) + (20000000 * 0.10) + (30000000 * 0.20) + (40000000 * 0.30) + ((thu_nhap_tinh_thue - 100000000) * 0.35)
st.success("Kết quả tính toán")

 st.write(
        f"📌 Tổng các khoản được giảm trừ **{tong_giam_tru:,.2f} đồng**"
    )

 st.write(
        f"📌 Thu nhập tính thuế **{thu_nhap_tinh_thue:,.2f} đồng**"
    )

    st.write(
        f"📌 Thuế thu nhập cá nhân phải nộp: **{thue_tncn:,.2f} đồng**"
    )

    
