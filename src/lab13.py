"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
import pandas as pd

# Console Windows mặc định không phải UTF-8: in tiếng Việt sẽ báo UnicodeEncodeError.
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return {
        'token': tien_token.sum(),
        'tool': tien_tool.sum(),
        'chay_lai': chay_lai,
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': tong / thanh_cong,
        'hoa_don_moi_yc': (tien_token.sum() + tien_tool.sum()) / len(reqs),
    }


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()

    # ---------- A2 · Mô hình chi phí từ trace ----------
    print('\n=== A2 · Mô hình chi phí từ trace ===')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        if ten == 'hoa_don_moi_yc':
            print(f'{ten:15s} {gia_tri:>14,.1f}')
        else:
            print(f'{ten:15s} {gia_tri:>14,.0f}')
    ty_so_hoa_don = ket_qua['cps'] / ket_qua['hoa_don_moi_yc']
    ty_trong_lam_lai = ket_qua['lam_lai'] / ket_qua['tong'] * 100
    ty_trong_xem_lai = ket_qua['xem_lai'] / ket_qua['tong'] * 100
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    chi_phi_he_thong_moi_yc = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'CPS / hoa_don_moi_yc [simulated]: {ty_so_hoa_don:.1f}x')
    print(f'Ti trong lam_lai [simulated]:     {ty_trong_lam_lai:.1f}%')
    print(f'Ti trong xem_lai [simulated]:     {ty_trong_xem_lai:.1f}%')
    print(f'Chi phi ca he thong / yc [sim]:   {chi_phi_he_thong_moi_yc:,.0f} d ({chi_phi_he_thong_moi_yc / BASELINE:.2f}x)')

    # ---------- A3 · Tách theo loại yêu cầu ----------
    print('\n=== A3 · Tách theo loại yêu cầu ===')
    print(f'{"Loai":12s} {"So YC":>6s} {"Ti le TC":>9s} {"Lan chay/YC":>12s} {"CPS [sim]":>12s} {"So 12.000d":>11s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub)
        ti_le_tc = kq['thanh_cong'] / len(sub) * 100
        lan_chay_tb = sub['so_lan_chay'].mean()
        print(f'{loai:12s} {len(sub):>6d} {ti_le_tc:>8.1f}% {lan_chay_tb:>12.2f} {kq["cps"]:>10,.0f} d {kq["cps"] / BASELINE:>10.2f}x')

    print('\nTi le status == ok theo loai va attempt:')
    runs_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    runs_loai['is_ok'] = (runs_loai['status'] == 'ok').astype(float)
    piv = runs_loai.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100
    print(piv.reindex(['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']).round(1).to_string())

    # ---------- A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ----------
    print('\n=== A4 · Chi phí cố định 40 triệu đ/tháng (noi_dia + hang_nang) ===')
    CHI_PHI_CO_DINH_THANG = 40_000_000
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    ti_le_tc_tren_toan_mau = kq_pv['thanh_cong'] / len(reqs)
    print(f'Pham vi noi_dia + hang_nang: {kq_pv["thanh_cong"]} viec thanh cong / {len(reqs)} YC mau, CPS chua co dinh = {kq_pv["cps"]:,.0f} d [simulated]')
    print(f'{"Khoi luong":22s} {"TC/thang":>10s} {"Co dinh/viec":>13s} {"CPS+CD [sim]":>13s} {"So 12.000d":>11s}')
    for ten_kl, tong_yc_thang in [('45.000 YC/thang', 45_000), ('Mot nua (22.500)', 22_500)]:
        viec_tc_thang = tong_yc_thang * ti_le_tc_tren_toan_mau
        cd_moi_viec = CHI_PHI_CO_DINH_THANG / viec_tc_thang
        cps_cong_cd = kq_pv['cps'] + cd_moi_viec
        print(f'{ten_kl:22s} {viec_tc_thang:>10,.0f} {cd_moi_viec:>11,.0f} d {cps_cong_cd:>11,.0f} d {cps_cong_cd / BASELINE:>10.2f}x')

    # ---------- Nhiệm vụ B · Bảng độ nhạy ----------
    # ---------- B1 · Đổi từng yếu tố ----------
    print('\n=== B1 · Bảng độ nhạy (đổi từng yếu tố) ===')
    kich_ban = {
        'Gia token gap doi':        dict(gia_vao=52, gia_ra=260),
        'Gia token giam mot nua':   dict(gia_vao=13, gia_ra=65),
        'Ti le xem lai gap doi':    dict(he_so_xem_lai=2),
        'Ti le xem lai giam nua':   dict(he_so_xem_lai=0.5),
        'So ca lam lai gap doi':    dict(he_so_lam_lai=2),
        'So ca lam lai giam nua':   dict(he_so_lam_lai=0.5),
        'Luong nhan vien tang 25%': dict(luong_phut=2500),
        'Toi da 2 lan chay':        dict(max_lan_chay=2),
        'Chi cho chay 1 lan':       dict(max_lan_chay=1),
    }
    goc = ket_qua['cps']
    ket_qua_b1 = {}
    print(f'{"Kich ban":26s} {"CPS [sim]":>12s} {"Thay doi":>10s}')
    print(f'{"Goc (A2)":26s} {goc:>10,.0f} d {"0.0%":>10s}')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        pct = (cps / goc - 1) * 100
        ket_qua_b1[ten] = (cps, pct)
        print(f'{ten:26s} {cps:>10,.0f} d {pct:>+9.1f}%')

    # Tự kiểm tra quy luật: giảm một nửa = -1/2 mức tăng gấp đôi
    for ten_tang, ten_giam in [
        ('Gia token gap doi', 'Gia token giam mot nua'),
        ('Ti le xem lai gap doi', 'Ti le xem lai giam nua'),
        ('So ca lam lai gap doi', 'So ca lam lai giam nua'),
    ]:
        tang = ket_qua_b1[ten_tang][1]
        giam = ket_qua_b1[ten_giam][1]
        assert abs(giam + tang / 2) < 1e-9, f'Sai quy luat tuyen tinh: {ten_tang} ({tang}) vs {ten_giam} ({giam})'
    print('Kiem tra quy luat "giam mot nua = 1/2 muc tang gap doi": DAT')

    # ---------- B2 · Đổi một cặp và xếp hạng ----------
    print('\n=== B2 · Đổi một cặp và xếp hạng ===')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    pct_cap = (cps_cap / goc - 1) * 100
    tong_rieng = ket_qua_b1['Gia token gap doi'][1] + ket_qua_b1['Ti le xem lai gap doi'][1]
    assert abs(pct_cap - tong_rieng) < 1e-9, 'Mo hinh phai cong tuyen tinh'
    print(f'Gia token x2 + Xem lai x2 [sim]: {cps_cap:,.0f} d ({pct_cap:+.1f}%, tong hai tac dong rieng: {tong_rieng:+.1f}%)')
    xep_hang = sorted(
        [
            ('So ca lam lai', ket_qua_b1['So ca lam lai gap doi'][1]),
            ('Ti le xem lai', ket_qua_b1['Ti le xem lai gap doi'][1]),
            ('Luong nhan vien (+25%)', ket_qua_b1['Luong nhan vien tang 25%'][1]),
            ('Gia token', ket_qua_b1['Gia token gap doi'][1]),
        ],
        key=lambda x: abs(x[1]),
        reverse=True,
    )
    print('Xep hang 3 yeu to anh huong manh nhat:',
          ' · '.join(f'{i}. {ten} ({pct:+.1f}%)' for i, (ten, pct) in enumerate(xep_hang[:3], 1)))

    # ---------- B3 · Giới hạn chạy lại có thật sự rẻ hơn ----------
    print('\n=== B3 · Giới hạn số lần chạy (chi phí cả hệ thống) ===')
    print(f'{"Gioi han":10s} {"Tong tro ly [sim]":>18s} {"Khong TC":>10s} {"Ca he thong [sim]":>18s} {"CPS [sim]":>12s}')
    for max_k in [1, 2, 3]:
        kq_k = mo_hinh(runs, reqs, max_lan_chay=max_k)
        khong_tc_k = len(reqs) - kq_k['thanh_cong']
        ca_he_thong_k = kq_k['tong'] + khong_tc_k * BASELINE
        print(f'{f"{max_k} lan":10s} {kq_k["tong"]:>16,.0f} d {khong_tc_k:>10d} {ca_he_thong_k:>16,.0f} d {kq_k["cps"]:>10,.0f} d')

    # ---------- B4 · Nếu phải xem lại tất cả (noi_dia + hang_nang) ----------
    print('\n=== B4 · Xem lại 100% trong phạm vi noi_dia + hang_nang ===')
    runs_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]
    so_yc_ok = runs_pv[runs_pv['status'] == 'ok']['request_id'].nunique()
    so_lam_lai_pv = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    token_tool_pv = kq_pv['token'] + kq_pv['tool']
    xem_lai_100 = so_yc_ok * 5 * LUONG_PHUT

    # Trường hợp 1: đề cho 9 phút/ca làm lại
    lam_lai_9p = so_lam_lai_pv * 9 * LUONG_PHUT
    tong_b4_9p = token_tool_pv + xem_lai_100 + lam_lai_9p
    cps_b4_9p = tong_b4_9p / kq_pv['thanh_cong']
    hoa_von_9p = (BASELINE * kq_pv['thanh_cong'] - token_tool_pv - lam_lai_9p) / (so_yc_ok * LUONG_PHUT)

    # Trường hợp 2: dùng trung bình phut_lam_lai_simulated trên toàn bộ ca làm lại
    tb_phut_lam_lai = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    lam_lai_tb = so_lam_lai_pv * tb_phut_lam_lai * LUONG_PHUT
    tong_b4_tb = token_tool_pv + xem_lai_100 + lam_lai_tb
    cps_b4_tb = tong_b4_tb / kq_pv['thanh_cong']
    hoa_von_tb = (BASELINE * kq_pv['thanh_cong'] - token_tool_pv - lam_lai_tb) / (so_yc_ok * LUONG_PHUT)

    print(f'Pham vi: {len(pham_vi)} YC, {so_yc_ok} YC co >=1 lan ok (xem lai 5p = {xem_lai_100:,.0f} d), {so_lam_lai_pv} ca lam lai, token+tool = {token_tool_pv:,.0f} d')
    print(f'Voi 9.0 phut/ca lam lai:       tong = {tong_b4_9p:>10,.0f} d -> CPS = {cps_b4_9p:>6,.0f} d ({cps_b4_9p / BASELINE:.2f}x) [sim] | hoa von <= {hoa_von_9p:.1f} phut/lan xem')
    print(f'Voi {tb_phut_lam_lai:.1f} phut/ca (TB du lieu): tong = {tong_b4_tb:>10,.0f} d -> CPS = {cps_b4_tb:>6,.0f} d ({cps_b4_tb / BASELINE:.2f}x) [sim] | hoa von <= {hoa_von_tb:.1f} phut/lan xem')

    # ---------- Nhiệm vụ D · Cỡ mẫu (CP4) ----------
    from statistics import NormalDist
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower

    P1, P2, ALPHA, POWER, ICC = 0.70, 0.75, 0.05, 0.80, 0.02
    SO_NHAN_VIEN = 40

    def co_mau(p1, p2, alpha=ALPHA, power=POWER):
        """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (công thức trong docs/du_lieu_va_cong_thuc.md)."""
        za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
        pb = (p1 + p2) / 2
        return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                          + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)

    def he_so_thiet_ke(m, icc=ICC):
        return 1 + (m - 1) * icc

    print('\n=== D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02) ===')
    n_a = co_mau(P1, P2)
    print(f'a) Chia theo yêu cầu:             {n_a:,} yêu cầu mỗi nhóm')

    de_b = he_so_thiet_ke(75)
    n_b = math.ceil(n_a * de_b)
    nv_b = math.ceil(n_b / 75)
    print(f'b) Theo nhân viên, m = 75:         DE = {de_b:.2f} -> {n_b:,} mỗi nhóm = {nv_b} nhân viên mỗi nhóm, '
          f'tổng {2 * nv_b} > {SO_NHAN_VIEN}: {"đủ" if 2 * nv_b <= SO_NHAN_VIEN else "KHÔNG đủ người"}')

    tran_c = 20 / ICC
    print(f'c) 20 nhân viên mỗi nhóm:          tối đa c/ICC = {tran_c:,.0f} {"<" if tran_c < n_a else ">="} {n_a:,}: '
          f'{"KHÔNG đạt" if tran_c < n_a else "đạt"}')

    tran_d = 6 / ICC
    print(f'd) 6 depot mỗi nhóm:               tối đa c/ICC = {tran_d:,.0f} < {n_a:,}: KHÔNG đạt, chỉ 6 cụm')

    n_e = co_mau(P1, P1 + 0.06)
    # 20m / (1 + (m - 1) ICC) >= n_e  ->  m >= n_e (1 - ICC) / (20 - n_e ICC)
    m_e = math.ceil(n_e * (1 - ICC) / (20 - n_e * ICC))
    de_e = he_so_thiet_ke(m_e)
    print(f'e) Mức chênh 6 điểm, 20 NV/nhóm:   n = {n_e:,} -> m >= {m_e} yêu cầu mỗi nhân viên, DE = {de_e:.2f}, '
          f'n hiệu dụng = {20 * m_e / de_e:,.0f}')

    # Con số bất lợi: thiết kế cho 6 điểm nhưng tác động thật chỉ 5 điểm
    h5 = proportion_effectsize(P2, P1)
    power_5 = NormalIndPower().power(effect_size=h5, nobs1=n_e, alpha=ALPHA, ratio=1.0)
    print(f'Power nếu tác động thật chỉ +5 điểm với n hiệu dụng {n_e} mỗi nhóm: {power_5:.2f}')

    # Số hiện tại để đặt ngưỡng luật dừng (đợt chạy thử, không có đối chứng)
    print('\n=== D3 · Tỉ lệ hiện tại để đặt luật dừng ===')
    mo_lai = reqs['mo_lai_trong_7_ngay'].astype(int)
    print(f'mo_lai_trong_7_ngay toàn mẫu:           {mo_lai.mean() * 100:.2f}% ({mo_lai.sum()}/{len(reqs)})')
    mo_lai_pv = pham_vi['mo_lai_trong_7_ngay'].astype(int)
    print(f'mo_lai_trong_7_ngay noi_dia + hang_nang: {mo_lai_pv.mean() * 100:.2f}% ({mo_lai_pv.sum()}/{len(pham_vi)})')
    duoc_xem = reqs[reqs['duoc_xem_lai'].astype(int) == 1]
    bo_qua = duoc_xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    print(f'Tỉ lệ bỏ qua gợi ý (sua hoặc bo):        {bo_qua.mean() * 100:.1f}% ({bo_qua.sum()}/{len(duoc_xem)})')
