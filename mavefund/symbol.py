from __future__ import annotations

import pandas as pd
from datetime import date
from pydantic import BaseModel
from typing import Optional, Union


class Symbol(BaseModel):
    company_name: str

    symbol: str

    symbol_dates: list[date | str]

    gp_revenue_usd_mil: list[int | None]
    gp_gross_margin: list[float | None]
    gp_operating_income_usd_mil: list[float | None]
    gp_operating_margin: list[float | None]
    gp_net_income_usd_mil: list[int | None]
    gp_earnings_per_share_usd: list[float | None]
    gp_dividends_usd: list[float | None]
    gp_payout_ratio: list[float | None]
    gp_shares_mil: list[int | None]
    gp_book_value_per_share_usd: list[float | None]
    gp_operation_cash_flow_usd_mil: list[int | None]
    gp_cap_spending_usd_mil: list[int | None]
    gp_free_cash_flow_usd_mil: list[int | None]
    gp_free_cash_flow_per_share_usd: list[float | None]
    gp_working_capital_usd_mil: list[int | None]

    pm_revenue: list[float | None]
    pm_cogs: list[float | None]
    pm_gross_margin: list[float | None]
    pm_sg_and_a: list[float | None]
    pm_r_and_d: list[float | None]
    pm_other: list[float | None]
    pm_operating_margin: list[float | None]
    pm_net_interest_income_and_other: list[float | None]
    pm_ebt_margin: list[float | None]

    p_tax_rate_perc: list[float | None]
    p_net_margin_perc: list[float | None]
    p_asset_turnover: list[float | None]
    p_return_on_assets: list[float | None]
    p_financial_leverage: list[float | None]
    p_return_on_equity: list[float | None]
    p_return_on_invested_capital: list[float | None]
    p_interest_coverage: list[float | None]

    g_revenue_perc_over_1_year_average: list[float | None]
    g_revenue_perc_over_3_years_average: list[float | None]
    g_revenue_perc_over_5_years_average: list[float | None]
    g_revenue_perc_over_10_years_average: list[float | None]
    g_operating_income_perc_over_1_year_average: list[float | None]
    g_operating_income_perc_over_3_years_average: list[float | None]
    g_operating_income_perc_over_5_years_average: list[float | None]
    g_operating_income_perc_over_10_years_average: list[float | None]
    g_net_income_perc_over_1_year_average: list[float | None]
    g_net_income_perc_over_3_years_average: list[float | None]
    g_net_income_perc_over_5_years_average: list[float | None]
    g_net_income_perc_over_10_years_average: list[float | None]
    g_eps_perc_over_1_year_average: list[float | None]
    g_eps_perc_over_3_years_average: list[float | None]
    g_eps_perc_over_5_years_average: list[float | None]
    g_eps_perc_over_10_years_average: list[float | None]

    cf_operating_cash_flow_growth_perc_yoy: list[float | None]
    cf_free_cash_flow_growth_perc_yoy: list[float | None]
    cf_cap_ex_as_growth_perc_of_sales: list[float | None]
    cf_free_cash_flow_over_sales_perc: list[float | None]
    cf_free_cash_flow_over_net_income: list[float | None]

    fh_cash_and_short_term_investments: list[float | None]
    fh_accounts_receivable: list[float | None]
    fh_inventory: list[float | None]
    fh_other_current_assets: list[float | None]
    fh_total_current_assets: list[float | None]
    fh_net_pp_and_e: list[float | None]
    fh_intangibles: list[float | None]
    fh_other_long_term_assets: list[float | None]
    fh_total_assets: list[float | None]
    fh_accounts_payable: list[float | None]
    fh_short_term_debt: list[float | None]
    fh_taxes_payable: list[float | None]
    fh_accrued_liabilities: list[float | None]
    fh_other_short_term_liabilities: list[float | None]
    fh_total_current_liabilities: list[float | None]
    fh_long_term_debt: list[float | None]
    fh_other_long_term_liabilities: list[float | None]
    fh_total_liabilities: list[float | None]
    fh_total_stockholders_equity: list[float | None]
    fh_total_liabilities_and_equity: list[float | None]

    lqd_current_ratio: list[float | None]
    lqd_quick_ratio: list[float | None]
    lqd_financial_leverage: list[float | None]
    lqd_debt_over_equity: list[float | None]

    efc_days_sales_outstanding: list[float | None]
    efc_days_inventory: list[float | None]
    efc_payable_period: list[float | None]
    efc_cash_conversion_cycle: list[float | None]
    efc_receivable_turnover: list[float | None]
    efc_inventory_turnover: list[float | None]
    efc_fixed_asset_turnover: list[float | None]
    efc_asset_turnover: list[float | None]

    @classmethod
    def from_symbol_dto(cls, symbol_dto: SymbolDto) -> Symbol:
        return cls(
            company_name=symbol_dto.cnm,
            symbol=symbol_dto.tck,

            symbol_dates=symbol_dto.dt,

            gp_revenue_usd_mil=symbol_dto.gp_rum,
            gp_gross_margin=symbol_dto.gp_gm,
            gp_operating_income_usd_mil=symbol_dto.gp_oim,
            gp_operating_margin=symbol_dto.gp_om,
            gp_net_income_usd_mil=symbol_dto.gp_nim,
            gp_earnings_per_share_usd=symbol_dto.gp_eps,
            gp_dividends_usd=symbol_dto.gp_d,
            gp_payout_ratio=symbol_dto.gp_pr,
            gp_shares_mil=symbol_dto.gp_sm,
            gp_book_value_per_share_usd=symbol_dto.gp_bvps,
            gp_operation_cash_flow_usd_mil=symbol_dto.gp_ocf,
            gp_cap_spending_usd_mil=symbol_dto.gp_csp,
            gp_free_cash_flow_usd_mil=symbol_dto.gp_fcf,
            gp_free_cash_flow_per_share_usd=symbol_dto.gp_fcfps,
            gp_working_capital_usd_mil=symbol_dto.gp_wc,

            pm_revenue=symbol_dto.pm_r,
            pm_cogs=symbol_dto.pm_cogs,
            pm_gross_margin=symbol_dto.pm_gm,
            pm_sg_and_a=symbol_dto.pm_sga,
            pm_r_and_d=symbol_dto.pm_rd,
            pm_other=symbol_dto.pm_o,
            pm_operating_margin=symbol_dto.pm_om,
            pm_net_interest_income_and_other=symbol_dto.pm_nii,
            pm_ebt_margin=symbol_dto.pm_ebm,

            p_tax_rate_perc=symbol_dto.p_trp,
            p_net_margin_perc=symbol_dto.p_nm,
            p_asset_turnover=symbol_dto.p_at,
            p_return_on_assets=symbol_dto.p_roa,
            p_financial_leverage=symbol_dto.p_fl,
            p_return_on_equity=symbol_dto.p_roe,
            p_return_on_invested_capital=symbol_dto.p_roic,
            p_interest_coverage=symbol_dto.p_ic,

            g_revenue_perc_over_1_year_average=symbol_dto.g_rp_1,
            g_revenue_perc_over_3_years_average=symbol_dto.g_rp_3,
            g_revenue_perc_over_5_years_average=symbol_dto.g_rp_5,
            g_revenue_perc_over_10_years_average=symbol_dto.g_rp_10,
            g_operating_income_perc_over_1_year_average=symbol_dto.g_opi_1,
            g_operating_income_perc_over_3_years_average=symbol_dto.g_opi_3,
            g_operating_income_perc_over_5_years_average=symbol_dto.g_opi_5,
            g_operating_income_perc_over_10_years_average=symbol_dto.g_opi_10,
            g_net_income_perc_over_1_year_average=symbol_dto.g_ni_1,
            g_net_income_perc_over_3_years_average=symbol_dto.g_ni_3,
            g_net_income_perc_over_5_years_average=symbol_dto.g_ni_5,
            g_net_income_perc_over_10_years_average=symbol_dto.g_ni_10,
            g_eps_perc_over_1_year_average=symbol_dto.g_eps_1,
            g_eps_perc_over_3_years_average=symbol_dto.g_eps_3,
            g_eps_perc_over_5_years_average=symbol_dto.g_eps_5,
            g_eps_perc_over_10_years_average=symbol_dto.g_eps_10,

            cf_operating_cash_flow_growth_perc_yoy=symbol_dto.cf_ocf,
            cf_free_cash_flow_growth_perc_yoy=symbol_dto.cf_fcfgp,
            cf_cap_ex_as_growth_perc_of_sales=symbol_dto.cf_ceag,
            cf_free_cash_flow_over_sales_perc=symbol_dto.cf_fcfos,
            cf_free_cash_flow_over_net_income=symbol_dto.cf_fcfoni,

            fh_cash_and_short_term_investments=symbol_dto.fh_casti,
            fh_accounts_receivable=symbol_dto.fh_ar,
            fh_inventory=symbol_dto.fh_inv,
            fh_other_current_assets=symbol_dto.fh_oca,
            fh_total_current_assets=symbol_dto.fh_tca,
            fh_net_pp_and_e=symbol_dto.fh_nppe,
            fh_intangibles=symbol_dto.fh_int,
            fh_other_long_term_assets=symbol_dto.fh_olta,
            fh_total_assets=symbol_dto.fh_ta,
            fh_accounts_payable=symbol_dto.fh_ap,
            fh_short_term_debt=symbol_dto.fh_std,
            fh_taxes_payable=symbol_dto.fh_tp,
            fh_accrued_liabilities=symbol_dto.fh_al,
            fh_other_short_term_liabilities=symbol_dto.fh_ostl,
            fh_total_current_liabilities=symbol_dto.fh_tcl,
            fh_long_term_debt=symbol_dto.fh_ltd,
            fh_other_long_term_liabilities=symbol_dto.fh_oltl,
            fh_total_liabilities=symbol_dto.fh_tl,
            fh_total_stockholders_equity=symbol_dto.fh_tse,
            fh_total_liabilities_and_equity=symbol_dto.fh_tle,

            lqd_current_ratio=symbol_dto.lqd_cr,
            lqd_quick_ratio=symbol_dto.lqd_qr,
            lqd_financial_leverage=symbol_dto.lqd_fl,
            lqd_debt_over_equity=symbol_dto.lqd_doe,

            efc_days_sales_outstanding=symbol_dto.efc_dso,
            efc_days_inventory=symbol_dto.efc_di,
            efc_payable_period=symbol_dto.efc_pp,
            efc_cash_conversion_cycle=symbol_dto.efc_ccc,
            efc_receivable_turnover=symbol_dto.efc_rt,
            efc_inventory_turnover=symbol_dto.efc_it,
            efc_fixed_asset_turnover=symbol_dto.efc_fat,
            efc_asset_turnover=symbol_dto.efc_at,
        )

    @property
    def df(self) -> pd.DataFrame:
        return pd.DataFrame(self.dict())


class SymbolDto(BaseModel):
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

    def to_symbol(self) -> Symbol:
        return Symbol.from_symbol_dto(self)
