from __future__ import annotations

import pandas as pd
from datetime import date
from pydantic import BaseModel


class Symbol(BaseModel):
    cnm: str
    tck: str

    dt: list[date | str] = []

    gp_rum: list[int | None] = []
    gp_gm: list[float | None] = []
    gp_oim: list[float | None] = []
    gp_om: list[float | None] = []
    gp_nim: list[int | None] = []
    gp_eps: list[float | None] = []
    gp_d: list[float | None] = []
    gp_pr: list[float | None] = []
    gp_sm: list[int | None] = []
    gp_bvps: list[float | None] = []
    gp_ocf: list[int | None] = []
    gp_csp: list[int | None] = []
    gp_fcf: list[int | None] = []
    gp_fcfps: list[float | None] = []
    gp_wc: list[int | None] = []

    pm_r: list[float | None] = []
    pm_cogs: list[float | None] = []
    pm_gm: list[float | None] = []
    pm_sga: list[float | None] = []
    pm_rd: list[float | None] = []
    pm_o: list[float | None] = []
    pm_om: list[float | None] = []
    pm_nii: list[float | None] = []
    pm_ebm: list[float | None] = []

    p_trp: list[float | None] = []
    p_nm: list[float | None] = []
    p_at: list[float | None] = []
    p_roa: list[float | None] = []
    p_fl: list[float | None] = []
    p_roe: list[float | None] = []
    p_roic: list[float | None] = []
    p_ic: list[float | None] = []

    g_rp_1: list[float | None] = []
    g_rp_3: list[float | None] = []
    g_rp_5: list[float | None] = []
    g_rp_10: list[float | None] = []

    g_opi_1: list[float | None] = []
    g_opi_3: list[float | None] = []
    g_opi_5: list[float | None] = []
    g_opi_10: list[float | None] = []

    g_ni_1: list[float | None] = []
    g_ni_3: list[float | None] = []
    g_ni_5: list[float | None] = []
    g_ni_10: list[float | None] = []

    g_eps_1: list[float | None] = []
    g_eps_3: list[float | None] = []
    g_eps_5: list[float | None] = []
    g_eps_10: list[float | None] = []

    cf_ocf: list[float | None] = []
    cf_fcfgp: list[float | None] = []
    cf_ceag: list[float | None] = []
    cf_fcfos: list[float | None] = []
    cf_fcfoni: list[float | None] = []

    fh_casti: list[float | None] = []
    fh_ar: list[float | None] = []
    fh_inv: list[float | None] = []
    fh_oca: list[float | None] = []
    fh_tca: list[float | None] = []
    fh_nppe: list[float | None] = []
    fh_int: list[float | None] = []
    fh_olta: list[float | None] = []
    fh_ta: list[float | None] = []
    fh_ap: list[float | None] = []
    fh_std: list[float | None] = []
    fh_tp: list[float | None] = []
    fh_al: list[float | None] = []
    fh_ostl: list[float | None] = []
    fh_tcl: list[float | None] = []
    fh_ltd: list[float | None] = []
    fh_oltl: list[float | None] = []
    fh_tl: list[float | None] = []
    fh_tse: list[float | None] = []
    fh_tle: list[float | None] = []

    lqd_cr: list[float | None] = []
    lqd_qr: list[float | None] = []
    lqd_fl: list[float | None] = []
    lqd_doe: list[float | None] = []

    efc_dso: list[float | None] = []
    efc_di: list[float | None] = []
    efc_pp: list[float | None] = []
    efc_ccc: list[float | None] = []
    efc_rt: list[float | None] = []
    efc_it: list[float | None] = []
    efc_fat: list[float | None] = []
    efc_at: list[float | None] = []


    @property
    def df(self) -> pd.DataFrame:
        return pd.DataFrame(self.dict())
