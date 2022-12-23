from __future__ import annotations

import pandas as pd
from datetime import date
from pydantic import BaseModel
from typing import Optional, Union


class Symbol(BaseModel):
    cnm: str
    tck: str

    dt: list[Union[date, str]] = []

    gp_rum: list[Optional[int]] = []
    gp_gm: list[Optional[float]] = []
    gp_oim: list[Optional[float]] = []
    gp_om: list[Optional[float]] = []
    gp_nim: list[Optional[int]] = []
    gp_eps: list[Optional[float]] = []
    gp_d: list[Optional[float]] = []
    gp_pr: list[Optional[float]] = []
    gp_sm: list[Optional[int]] = []
    gp_bvps: list[Optional[float]] = []
    gp_ocf: list[Optional[int]] = []
    gp_csp: list[Optional[int]] = []
    gp_fcf: list[Optional[int]] = []
    gp_fcfps: list[Optional[float]] = []
    gp_wc: list[Optional[int]] = []

    pm_r: list[Optional[float]] = []
    pm_cogs: list[Optional[float]] = []
    pm_gm: list[Optional[float]] = []
    pm_sga: list[Optional[float]] = []
    pm_rd: list[Optional[float]] = []
    pm_o: list[Optional[float]] = []
    pm_om: list[Optional[float]] = []
    pm_nii: list[Optional[float]] = []
    pm_ebm: list[Optional[float]] = []

    p_trp: list[Optional[float]] = []
    p_nm: list[Optional[float]] = []
    p_at: list[Optional[float]] = []
    p_roa: list[Optional[float]] = []
    p_fl: list[Optional[float]] = []
    p_roe: list[Optional[float]] = []
    p_roic: list[Optional[float]] = []
    p_ic: list[Optional[float]] = []

    g_rp_1: list[Optional[float]] = []
    g_rp_3: list[Optional[float]] = []
    g_rp_5: list[Optional[float]] = []
    g_rp_10: list[Optional[float]] = []

    g_opi_1: list[Optional[float]] = []
    g_opi_3: list[Optional[float]] = []
    g_opi_5: list[Optional[float]] = []
    g_opi_10: list[Optional[float]] = []

    g_ni_1: list[Optional[float]] = []
    g_ni_3: list[Optional[float]] = []
    g_ni_5: list[Optional[float]] = []
    g_ni_10: list[Optional[float]] = []

    g_eps_1: list[Optional[float]] = []
    g_eps_3: list[Optional[float]] = []
    g_eps_5: list[Optional[float]] = []
    g_eps_10: list[Optional[float]] = []

    cf_ocf: list[Optional[float]] = []
    cf_fcfgp: list[Optional[float]] = []
    cf_ceag: list[Optional[float]] = []
    cf_fcfos: list[Optional[float]] = []
    cf_fcfoni: list[Optional[float]] = []

    fh_casti: list[Optional[float]] = []
    fh_ar: list[Optional[float]] = []
    fh_inv: list[Optional[float]] = []
    fh_oca: list[Optional[float]] = []
    fh_tca: list[Optional[float]] = []
    fh_nppe: list[Optional[float]] = []
    fh_int: list[Optional[float]] = []
    fh_olta: list[Optional[float]] = []
    fh_ta: list[Optional[float]] = []
    fh_ap: list[Optional[float]] = []
    fh_std: list[Optional[float]] = []
    fh_tp: list[Optional[float]] = []
    fh_al: list[Optional[float]] = []
    fh_ostl: list[Optional[float]] = []
    fh_tcl: list[Optional[float]] = []
    fh_ltd: list[Optional[float]] = []
    fh_oltl: list[Optional[float]] = []
    fh_tl: list[Optional[float]] = []
    fh_tse: list[Optional[float]] = []
    fh_tle: list[Optional[float]] = []

    lqd_cr: list[Optional[float]] = []
    lqd_qr: list[Optional[float]] = []
    lqd_fl: list[Optional[float]] = []
    lqd_doe: list[Optional[float]] = []

    efc_dso: list[Optional[float]] = []
    efc_di: list[Optional[float]] = []
    efc_pp: list[Optional[float]] = []
    efc_ccc: list[Optional[float]] = []
    efc_rt: list[Optional[float]] = []
    efc_it: list[Optional[float]] = []
    efc_fat: list[Optional[float]] = []
    efc_at: list[Optional[float]] = []


    @property
    def df(self) -> pd.DataFrame:
        return pd.DataFrame(self.dict())
