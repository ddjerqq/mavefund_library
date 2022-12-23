# MaveFund API Client Library

<img alt="logo" height="120" src="mavefund.jpg" title="mavefund logo" />

The official library for [mavefund](https://mavefund.com) used to download data from
the API as pandas dataframes for easy accessibility.

created and maintained by [ddjerqq](https://github.com/ddjerqq)

## Installation

Run this in your terminal:
```bash
pip install mavefund
```

## Getting started

* To use the library you need to acquire an API key from [the official website](https://mavefund.com)
* After that import the library into your python code

```python
import mavefund as mf
with mf.Client(api_key="YOUR KEY") as client:
    apple_df = client("AAPL")
# access the dataframe here
```

## Documentation

### [Client](https://github.com/ddjerqq/mavefund_library/blob/master/mavefund/client.py)
#### creation:
There are two ways to create a client, a context manager and a regular object.

```python
from mavefund import Client

# context manager (recommended)
with Client(api_key="KEY") as client:
    apple_df = client("AAPL")

    
# regular object
client = Client("KEY")
df = client("AAPL")
client.close()
```

### [Symbol Mapping](https://github.com/ddjerqq/mavefund_library/blob/master/mavefund/symbol.py)

#### General

    cnm -> company_name
    tck -> symbol
    dt -> symbol_date

#### GrowthProfitability

    gp_rum    -> gp_revenue_usd_mil
    gp_gm     -> gp_gross_margin
    gp_oim    -> gp_operating_income_usd_mil
    gp_om     -> gp_operating_margin
    gp_nim    -> gp_net_income_usd_mil
    gp_eps    -> gp_earnings_per_share_usd
    gp_d      -> gp_dividends_usd
    gp_pr     -> gp_payout_ratio
    gp_sm     -> gp_shares_mil
    gp_bvps   -> gp_book_value_per_share_usd
    gp_ocf    -> gp_operation_cash_flow_usd_mil
    gp_csp    -> gp_cap_spending_usd_mil
    gp_fcf    -> gp_free_cash_flow_usd_mil
    gp_fcfps  -> gp_free_cash_flow_per_share_usd
    gp_wc     -> gp_working_capital_usd_mil
    
#### ProfitabilityMargin

    pm_r      -> pm_revenue
    pm_cogs   -> pm_cogs
    pm_gm     -> pm_gross_margin
    pm_sga    -> pm_sg_and_a
    pm_rd     -> pm_r_and_d
    pm_o      -> pm_other
    pm_om     -> pm_operating_margin
    pm_nii    -> pm_net_interest_income_and_other
    pm_ebm    -> pm_ebt_margin

#### Profitability

    p_trp     -> p_tax_rate_perc
    p_nm      -> p_net_margin_perc
    p_at      -> p_asset_turnover
    p_roa     -> p_return_on_assets
    p_fl      -> p_financial_leverage
    p_roe     -> p_return_on_equity
    p_roic    -> p_return_on_invested_capital
    p_ic      -> p_interest_coverage

#### Growth

    g_rp_1    -> g_revenue_perc_over_1_year_average
    g_rp_3    -> g_revenue_perc_over_3_years_average
    g_rp_5    -> g_revenue_perc_over_5_years_average
    g_rp_10   -> g_revenue_perc_over_10_years_average

    g_opi_1   -> g_operating_income_perc_over_1_year_average
    g_opi_3   -> g_operating_income_perc_over_3_years_average
    g_opi_5   -> g_operating_income_perc_over_5_years_average
    g_opi_10  -> g_operating_income_perc_over_10_years_average

    g_ni_1    -> g_net_income_perc_over_1_year_average
    g_ni_3    -> g_net_income_perc_over_3_years_average
    g_ni_5    -> g_net_income_perc_over_5_years_average
    g_ni_10   -> g_net_income_perc_over_10_years_average

    g_eps_1   -> g_eps_perc_over_1_year_average
    g_eps_3   -> g_eps_perc_over_3_years_average
    g_eps_5   -> g_eps_perc_over_5_years_average
    g_eps_10  -> g_eps_perc_over_10_years_average

#### CashFlow

    cf_ocf    -> cf_operating_cash_flow_growth_perc_yoy
    cf_fcfgp  -> cf_free_cash_flow_growth_perc_yoy
    cf_ceag   -> cf_cap_ex_as_growth_perc_of_sales
    cf_fcfos  -> cf_free_cash_flow_over_sales_perc
    cf_fcfoni -> cf_free_cash_flow_over_net_income

#### FinancialHealth

    fh_casti  -> fh_cash_and_short_term_investments
    fh_ar     -> fh_accounts_receivable
    fh_inv    -> fh_inventory
    fh_oca    -> fh_other_current_assets
    fh_tca    -> fh_total_current_assets
    fh_nppe   -> fh_net_pp_and_e
    fh_int    -> fh_intangibles
    fh_olta   -> fh_other_long_term_assets
    fh_ta     -> fh_total_assets
    fh_ap     -> fh_accounts_payable
    fh_std    -> fh_short_term_debt
    fh_tp     -> fh_taxes_payable
    fh_al     -> fh_accrued_liabilities
    fh_ostl   -> fh_other_short_term_liabilities
    fh_tcl    -> fh_total_current_liabilities
    fh_ltd    -> fh_long_term_debt
    fh_oltl   -> fh_other_long_term_liabilities
    fh_tl     -> fh_total_liabilities
    fh_tse    -> fh_total_stockholders_equity
    fh_tle    -> fh_total_liabilities_and_equity

#### Liquidity

    lqd_cr    -> lqd_current_ratio
    lqd_qr    -> lqd_quick_ratio
    lqd_fl    -> lqd_financial_leverage
    lqd_doe   -> lqd_debt_over_equity

#### Efficiency

    efc_dso   -> efc_days_sales_outstanding
    efc_di    -> efc_days_inventory
    efc_pp    -> efc_payable_period
    efc_ccc   -> efc_cash_conversion_cycle
    efc_rt    -> efc_receivable_turnover
    efc_it    -> efc_inventory_turnover
    efc_fat   -> efc_fixed_asset_turnover
    efc_at    -> efc_asset_turnover
