import marimo

__generated_with = "0.23.8"
app = marimo.App(width="full")

@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import re
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.ticker as mticker
    return matplotlib, mo, np, pd, plt, re, mticker


@app.cell
def _(mo):
    mo.md("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

    :root {
      --bg:      #ffffff;
      --surface: #ffffff;
      --card:    #f5f5f5;
      --border:  #cccccc;
      --accent:  #1a56cc;
      --accent2: #c0392b;
      --green:   #1a7a3a;
      --muted:   #555555;
      --text:    #111111;
      --heading: #000000;
    }

    body, .marimo {
      background: #ffffff !important;
      color: #111111 !important;
      font-family: 'DM Sans', sans-serif !important;
    }

    .marimo-carousel { width:100%; max-width:1100px; margin:0 auto; }

    .slide {
      min-height:78vh; background:#ffffff;
      border:1px solid var(--border); border-radius:18px;
      padding:56px 72px; display:flex; flex-direction:column;
      justify-content:flex-start; position:relative;
      overflow:hidden; box-sizing:border-box;
    }
    .slide::before { display:none; }
    .slide-title {
      background:#f7f9ff;
      justify-content:center; text-align:center;
    }
    .slide-section {
      background:#f7f9ff;
      justify-content:center; align-items:center; text-align:center;
    }

    .kicker {
      font-family:'DM Mono',monospace; font-size:11px; font-weight:500;
      letter-spacing:.18em; text-transform:uppercase;
      color:var(--accent); margin-bottom:18px;
    }
    h1.display {
      font-family:'DM Serif Display',serif; font-size:52px;
      line-height:1.12; color:#000000; margin:0 0 22px;
    }
    h2.slide-heading {
      font-family:'DM Serif Display',serif; font-size:36px;
      color:#000000; margin:0 0 32px; line-height:1.15;
    }
    h3.section-label {
      font-family:'DM Serif Display',serif; font-size:44px;
      color:#000000; margin:0;
    }
    p.subtitle {
      font-size:18px; color:#444444; max-width:640px;
      margin:0 auto 32px; line-height:1.65;
    }
    p.body-text { font-size:16px; color:#111111; line-height:1.75; margin:0 0 14px; }

    .chip-row { display:flex; flex-wrap:wrap; gap:10px; margin-top:16px; }
    .chip {
      font-family:'DM Mono',monospace; font-size:12px;
      background:#f0f0f0; border:1px solid #bbbbbb;
      border-radius:6px; padding:5px 12px; color:#333333;
    }
    .chip.accent  { border-color:var(--accent);  color:var(--accent); background:#eef2ff; }
    .chip.accent2 { border-color:var(--accent2); color:var(--accent2); background:#fff0f0; }

    .stat-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:18px; margin-top:10px; }
    .stat-card {
      background:#f5f5f5; border:1px solid #cccccc;
      border-radius:12px; padding:28px 24px; text-align:center;
    }
    .stat-card .value { font-family:'DM Serif Display',serif; font-size:40px; color:var(--accent); display:block; }
    .stat-card .label { font-size:13px; color:#555555; margin-top:6px; line-height:1.45; }
    .stat-card.orange .value { color:var(--accent2); }
    .stat-card.green  .value { color:var(--green); }

    .two-col { display:grid; grid-template-columns:1fr 1fr; gap:32px; margin-top:8px; }
    .col-box {
      background:#f5f5f5; border:1px solid #cccccc;
      border-radius:12px; padding:28px 24px;
    }
    .col-box h4 {
      font-family:'DM Mono',monospace; font-size:11px;
      letter-spacing:.15em; text-transform:uppercase;
      color:var(--accent); margin:0 0 14px;
    }

    ul.slide-list { list-style:none; padding:0; margin:0; }
    ul.slide-list li {
      font-size:15px; color:#111111; padding:9px 0;
      border-bottom:1px solid #dddddd;
      display:flex; align-items:flex-start; gap:12px; line-height:1.55;
    }
    ul.slide-list li:last-child { border-bottom:none; }
    ul.slide-list li::before {
      content:'→'; color:var(--accent); font-family:'DM Mono',monospace;
      font-size:13px; flex-shrink:0; margin-top:1px;
    }

    .outcome-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:14px; margin-top:10px; }
    .outcome-pill {
      background:#f5f5f5; border:1px solid #cccccc;
      border-radius:8px; padding:14px 18px; font-size:14px;
      color:#111111; display:flex; align-items:center; gap:10px;
    }
    .outcome-pill .dot { width:8px; height:8px; border-radius:50%; flex-shrink:0; }
    .dot-blue   { background:#1a56cc; }
    .dot-orange { background:#c0392b; }
    .dot-green  { background:#1a7a3a; }
    .dot-muted  { background:#999999; }

    .code-block {
      background:#f5f5f5; border:1px solid #cccccc;
      border-radius:10px; padding:20px 24px;
      font-family:'DM Mono',monospace; font-size:13px;
      color:#111111; line-height:1.7; margin-top:10px;
    }
    .code-block .kw { color:#c0392b; }
    .code-block .cm { color:#666666; font-style:italic; }
    .code-block .st { color:#1a7a3a; }

    .step-list { list-style:none; padding:0; margin:0; }
    .step-list li {
      display:flex; gap:20px; align-items:flex-start;
      padding:16px 0; border-bottom:1px solid #dddddd;
      font-size:15px; color:#111111; line-height:1.6;
    }
    .step-list li:last-child { border-bottom:none; }
    .step-num {
      font-family:'DM Mono',monospace; font-size:11px; font-weight:500;
      color:var(--accent); background:#eef2ff;
      border:1px solid var(--accent); border-radius:6px;
      padding:3px 9px; flex-shrink:0; margin-top:2px;
    }

    .callout {
      background:#eef2ff; border-left:3px solid var(--accent);
      border-radius:0 10px 10px 0; padding:18px 22px; margin-top:18px;
      font-size:15px; color:#111111; line-height:1.65;
    }
    .callout.orange { background:#fff0ee; border-color:var(--accent2); }
    .callout.green  { background:#eeffee; border-color:var(--green); }

    .hdiv { border:none; border-top:1px solid #dddddd; margin:24px 0; }

    .slide-footer {
      margin-top:auto; padding-top:24px;
      font-family:'DM Mono',monospace; font-size:11px;
      color:#aaaaaa; letter-spacing:.06em;
      display:flex; justify-content:space-between;
    }

    /* ── Interactive tab styles ── */
    .ctrl-label {
      font-family:'DM Mono',monospace; font-size:10px;
      letter-spacing:.14em; text-transform:uppercase;
      color:var(--accent); margin-bottom:8px;
    }
    .reg-table-wrap {
      background:#f5f5f5; border:1px solid #cccccc;
      border-radius:12px; padding:24px 28px; margin-top:28px;
      overflow-x:auto;
    }
    .reg-table-wrap h4 {
      font-family:'DM Mono',monospace; font-size:11px;
      letter-spacing:.15em; text-transform:uppercase;
      color:var(--accent); margin:0 0 16px;
    }
    table.reg-table {
      width:100%; border-collapse:collapse;
      font-size:13px; font-family:'DM Mono',monospace;
    }
    table.reg-table th {
      text-align:right; padding:6px 14px;
      border-bottom:2px solid #aaaaaa;
      color:#333333; font-weight:600; white-space:nowrap;
    }
    table.reg-table th:first-child { text-align:left; }
    table.reg-table td {
      text-align:right; padding:6px 14px;
      border-bottom:1px solid #dddddd;
      color:#111111;
    }
    table.reg-table td:first-child { text-align:left; color:#444444; }
    table.reg-table tr:hover td { background:#eeeeee; }
    table.reg-table tr.did-row td { font-weight:500; color:#000000; }
    table.reg-table tr.did-row td.sig { color:var(--accent2); font-weight:700; }
    .sig-note {
      font-family:'DM Mono',monospace; font-size:10px;
      color:#666666; margin-top:10px;
    }
    .error-box {
      background:#fff0f0; border:1px solid #e0a0a0;
      border-radius:10px; padding:18px 22px; margin-top:20px;
      font-size:14px; color:#aa0000;
      font-family:'DM Mono',monospace;
    }
    </style>
    """)
    return



@app.cell
def _(np, pd, re):
    TREATMENT_YEAR = 13

    MENU_OF_REGRESSANDS = [
        'Poverty Percent All Ages',
        'Poverty Percent Under Age 18',
        'Poverty Percent Ages 5-17',
        'FI Rate',
        'Child FI Rate',
        '% FI Children Below 185 FPL',
        'Cost Per Meal',
        'Weighted Annual Food Budget Shortfall',
        'Num FI Persons',
    ]
    PLACEBO_OUTCOMES = ['Labor Force']
    ALL_OUTCOMES = MENU_OF_REGRESSANDS + PLACEBO_OUTCOMES

    POSSIBLE_CONTROLS = [
        'Unemployment Rate (%)',
        'Num FI Persons',
        'Labor Force',
    ]

    def build_panel(df_raw, snap_quantile=0.30):
        """Return a fully-prepared panel dataframe indexed by (entity, Year)."""
        df = df_raw.copy()
        df['entity'] = df['Postal'].astype(str) + ' ' + df['Name'].astype(str)
        df['rel_time'] = df['Year'] - TREATMENT_YEAR

        event_dummies = pd.get_dummies(df['rel_time'], prefix='evt', drop_first=False)
        event_dummies = event_dummies.drop(columns=['evt_-1'], errors='ignore')
        df = pd.concat([df, event_dummies], axis=1)

        snap_pre = df[df['rel_time'] < 0].groupby('entity')['SNAP'].mean().rename('snap_pre_mean')
  
        threshold = snap_pre.quantile(snap_quantile)
        treated_entities = snap_pre[snap_pre >= threshold].index
        df['treated'] = df['entity'].isin(treated_entities).astype(int)
        evt_cols = [c for c in df.columns if c.startswith('evt_')]
        for col in evt_cols:
            df[f'did_{col}'] = df['treated'] * df[col]

        df = df.set_index(['entity', 'Year'])
        df = df.drop(index='DC District of Columbia', level='entity', errors='ignore')

        obs = df.groupby(level='entity').size()
        balanced = obs[obs > 6].index
        df = df[df.index.get_level_values('entity').isin(balanced)]
        return df

    def run_regression(df, regressand, log_left=False, controls=None):
        from linearmodels.panel import PanelOLS
        did_cols = [c for c in df.columns if c.startswith('did_evt_')]
        if not did_cols:
            raise ValueError('No DiD columns found — check panel build.')
        ctrl_cols = [c for c in (controls or []) if c in df.columns and c != regressand]
        y = df[regressand].copy()
        if log_left:
            y = np.log(y.replace(0, np.nan))
        X = df[did_cols + ctrl_cols].copy()
        mask = y.notna() & X.notna().all(axis=1)
        y, X = y[mask], X[mask]
        model = PanelOLS(dependent=y, exog=X,
                         entity_effects=True, time_effects=True,
                         drop_absorbed=True)
        return model.fit(cov_type='clustered', cluster_entity=True)

    def build_event_fig(result, regressand, log_left=False):
        """Return a matplotlib Figure for the event study."""
        params = result.params
        ci = result.conf_int()
        pat = re.compile(r'did_evt_(-?\d+)')
        times, coefs, lower, upper = [], [], [], []
        for k in params.index:
            m = pat.search(k)
            if m:
                t = int(m.group(1))
                times.append(t)
                coefs.append(float(params[k]))
                lower.append(float(ci.loc[k, 'lower']))
                upper.append(float(ci.loc[k, 'upper']))
        times += [-1];  coefs += [0.0];  lower += [0.0];  upper += [0.0]
        order = sorted(range(len(times)), key=lambda i: times[i])
        times = [times[i]  for i in order]
        coefs = [coefs[i]  for i in order]
        lower = [lower[i]  for i in order]
        upper = [upper[i]  for i in order]

        fig, ax = plt.subplots(figsize=(11, 5))

        ax.fill_between(times, lower, upper, alpha=0.2, color='steelblue', label='95% CI')
        ax.plot(times, coefs, marker='o', color='steelblue', linewidth=1.5, markersize=5)
        ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
        ax.axvline(-0.5, color='red', linewidth=1, linestyle=':', label='Lapse (2013)')

        ax.set_xlabel('Event time (years relative to 2013 lapse)')
        ylabel = f'DiD coeff — log({regressand})' if log_left else f'DiD coeff — {regressand}'
        ax.set_ylabel(ylabel)
        ax.set_title(f'Event Study: SNAP Lapse Effect on {regressand}')
        ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
        ax.legend()

        if log_left:
            ax2 = ax.twinx()
            y_min, y_max = ax.get_ylim()
            ax2.set_ylim((np.exp(y_min) - 1) * 100, (np.exp(y_max) - 1) * 100)
            ax2.set_ylabel('Approx. % change')
            ax2.yaxis.set_major_formatter(
                mticker.FuncFormatter(lambda x, _: f'{x:.1f}%'))

        plt.tight_layout()
        return fig

    def result_to_table_rows(result, regressand):
        """Return list-of-dicts suitable for rendering; mark DiD rows."""
        params  = result.params
        stderr  = result.std_errors
        tstat   = result.tstats
        pval    = result.pvalues
        ci      = result.conf_int()
        rows = []
        pat = re.compile(r'did_evt_(-?\d+)')
        for k in params.index:
            is_did = bool(pat.search(k))
            p = float(pval[k])
            stars = ('***' if p < 0.01 else
                     '**'  if p < 0.05 else
                     '*'   if p < 0.10 else '')
            rows.append({
                '_var':   k,
                '_is_did': is_did,
                'Coef.':  f'{float(params[k]):.4f}{stars}',
                'Std. Err.': f'{float(stderr[k]):.4f}',
                't':       f'{float(tstat[k]):.2f}',
                'P>|t|':   f'{p:.4f}',
                '[0.025':  f'{float(ci.loc[k,"lower"]):.4f}',
                '0.975]':  f'{float(ci.loc[k,"upper"]):.4f}',
            })
        return rows

    return (
        ALL_OUTCOMES, MENU_OF_REGRESSANDS, PLACEBO_OUTCOMES,
        POSSIBLE_CONTROLS, TREATMENT_YEAR,
        build_event_fig, build_panel, result_to_table_rows, run_regression,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Cell 4 — load raw CSV (users must set CSV_PATH)
# ─────────────────────────────────────────────────────────────────────────────
@app.cell
def _(mo):
    path_input = mo.ui.text(
        value='Dataset Operations/dataset.csv',
        label='CSV path',
        full_width=True,
    )
    mo.vstack([
        mo.md("### Dataset path"),
        mo.md("Set the path to your `dataset.csv` before using the interactive tab."),
        path_input,
    ])
    return (path_input,)


@app.cell
def _(path_input, mo, pd):
    import os as _os
    _csv_path = path_input.value.strip()
    if _os.path.exists(_csv_path):
        _df_raw = pd.read_csv(_csv_path)
        load_status = mo.callout(
            mo.md(f"**Loaded** `{_csv_path}` — {len(_df_raw):,} rows, {_df_raw.shape[1]} columns."),
            kind="success",
        )
        _load_ok = True
    else:
        _df_raw = None
        load_status = mo.callout(
            mo.md(f"File not found: `{_csv_path}`. Set the correct path above."),
            kind="warn",
        )
        _load_ok = False

    df_raw = _df_raw
    load_ok = _load_ok
    load_status
    return df_raw, load_ok, load_status



@app.cell
def _(MENU_OF_REGRESSANDS, PLACEBO_OUTCOMES, POSSIBLE_CONTROLS, mo):
    ctrl_regressand = mo.ui.dropdown(
        options=MENU_OF_REGRESSANDS + PLACEBO_OUTCOMES,
        value=MENU_OF_REGRESSANDS[0],
        label="Outcome (regressand)",
        full_width=True)
    ctrl_quantile = mo.ui.slider(
        start=0.05, stop=0.95, step=0.05, value=0.30,
        show_value=True,
        label="SNAP treatment quantile cutoff",
        full_width=True)
    ctrl_controls = mo.ui.multiselect(
        options=POSSIBLE_CONTROLS,
        value=['Unemployment Rate (%)'],
        label="Additional controls",
        full_width=True)
    ctrl_log = mo.ui.switch(value=False, label="Log-scale (left axis)")

    return ctrl_controls, ctrl_log, ctrl_quantile, ctrl_regressand

@app.cell
def _(
    build_event_fig, build_panel, ctrl_controls, ctrl_log,
    ctrl_quantile, ctrl_regressand, df_raw, load_ok,
    mo, plt, result_to_table_rows, run_regression,
):
    def _make_reg_table_html(rows):
        cols = ['Coef.', 'Std. Err.', 't', 'P>|t|', '[0.025', '0.975]']
        header = '<tr><th>Variable</th>' + ''.join(f'<th>{c}</th>' for c in cols) + '</tr>'
        body_rows = []
        for r in rows:
            td_class = ' class="did-row"' if r['_is_did'] else ''
            p_val = float(r['P>|t|'])
            sig_cls = ' class="sig"' if r['_is_did'] and p_val < 0.10 else ''
            coef_td = f'<td{sig_cls}>{r["Coef."]}</td>'
            cells = ''.join(f'<td>{r[c]}</td>' for c in cols[1:])
            body_rows.append(f'<tr{td_class}><td>{r["_var"]}</td>{coef_td}{cells}</tr>')
        sig_note = (
            '<p class="sig-note">*** p&lt;0.01 &nbsp; ** p&lt;0.05 &nbsp; * p&lt;0.10 &nbsp;'
            '— DiD rows highlighted; significant DiD coefficients in orange</p>'
        )
        return (
            '<div class="reg-table-wrap">'
            '<h4>Regression output — clustered SE (entity)</h4>'
            f'<table class="reg-table"><thead>{header}</thead><tbody>'
            + ''.join(body_rows)
            + f'</tbody></table>{sig_note}</div>'
        )

    if not load_ok or df_raw is None:
        _did_output = mo.callout(
            mo.md("Load a dataset first using the path input above."),
            kind="warn"
        )
    else:
        _regressand = ctrl_regressand.value
        _quantile   = ctrl_quantile.value
        _controls   = list(ctrl_controls.value) if ctrl_controls.value else []
        _log        = ctrl_log.value

        try:
            _df = build_panel(df_raw, snap_quantile=_quantile)
            if _regressand not in _df.columns:
                raise ValueError(f'Column "{_regressand}" not found in dataset.')
            _safe_ctrl = [c for c in _controls if c != _regressand and c in _df.columns]

            _result = run_regression(_df, _regressand, log_left=_log, controls=_safe_ctrl)
            _fig    = build_event_fig(_result, _regressand, log_left=_log)

            _n_treated = int(_df['treated'].groupby(level='entity').first().sum())
            _n_total   = int(_df['treated'].groupby(level='entity').first().count())
            _pct       = f'{_n_treated / _n_total * 100:.0f}%'

            _chip_html = (
                f'<div class="chip-row" style="margin-bottom:20px">'
                f'<span class="chip accent">quantile cutoff = {_quantile:.2f}</span>'
                f'<span class="chip accent2">treated: {_n_treated} / {_n_total} counties ({_pct})</span>'
                f'<span class="chip">{"log " if _log else ""}{_regressand}</span>'
                + (''.join(f'<span class="chip">+ {c}</span>' for c in _safe_ctrl) if _safe_ctrl else '')
                + '</div>'
            )

            _rows      = result_to_table_rows(_result, _regressand)
            _tbl_html  = _make_reg_table_html(_rows)

            _did_output = mo.vstack([
                mo.md(_chip_html),
                mo.mpl.interactive(_fig),
                mo.md(_tbl_html),
            ])
            plt.close(_fig)

        except Exception as _e:
            _did_output = mo.md(f'<div class="error-box">⚠ {type(_e).__name__}: {_e}</div>')

    _did_output
    return

@app.cell
def _(ctrl_controls, ctrl_log, ctrl_quantile, ctrl_regressand, mo):
    slide_title = mo.md("""
    <div class="slide slide-title">
      <div class="kicker">Econometric Analysis · Event Study · Panel Data</div>
      <h1 class="display">The 2013 SNAP Lapse<br><em>&amp; Food Insecurity</em></h1>
      <p class="subtitle">
        A Difference-in-Differences event study estimating the causal effect
        of the 2013 federal SNAP benefit reduction on county-level food insecurity
        and poverty outcomes across the United States.
      </p>
      <div class="chip-row" style="justify-content:center">
        <span class="chip accent">PanelOLS · Two-Way FE</span>
        <span class="chip accent2">Clustered SE</span>
        <span class="chip">County × Year Panel</span>
        <span class="chip">Pre-trends Tested</span>
      </div>
      <div class="slide-footer"><span>SNAP Event Study</span><span>Slide 1 / 9</span></div>
    </div>
    """)

    slide_background = mo.md("""
    <div class="slide">
      <div class="kicker">Motivation</div>
      <h2 class="slide-heading">Background &amp; Research Question</h2>
      <div class="two-col">
        <div class="col-box">
          <h4>The 2013 SNAP Lapse</h4>
          <ul class="slide-list">
            <li>In November 2013, a temporary boost to SNAP benefits from the 2009 Recovery Act expired.</li>
            <li>Benefits fell by roughly $36/month for a family of four — about 5% of the average benefit.</li>
            <li>The lapse was federal and <em>uniform</em>, creating sharp variation across counties by prior reliance.</li>
          </ul>
        </div>
        <div class="col-box">
          <h4>Research Question</h4>
          <ul class="slide-list">
            <li>Did counties more reliant on SNAP <em>before</em> 2013 see worse food insecurity outcomes after?</li>
            <li>Does the effect appear in poverty rates, food insecurity rates, and budget shortfalls?</li>
            <li>Are pre-treatment trends parallel? (Identification check)</li>
          </ul>
        </div>
      </div>
      <div class="callout">
        <strong>Key insight:</strong> Because the lapse was nationwide, treatment intensity is defined
        by pre-period SNAP take-up rates — counties above the chosen percentile
        of mean pre-2013 SNAP participation are classified as <em>treated</em>.
      </div>
      <div class="slide-footer"><span>SNAP Event Study</span><span>Slide 2 / 9</span></div>
    </div>
    """)

    slide_data = mo.md("""
    <div class="slide">
      <div class="kicker">Data</div>
      <h2 class="slide-heading">Dataset &amp; Sample Construction</h2>
      <div class="stat-grid">
        <div class="stat-card"><span class="value">County</span>
          <div class="label">Unit of observation (entity index)</div></div>
        <div class="stat-card orange"><span class="value">2013</span>
          <div class="label">Treatment year (SNAP lapse event)</div></div>
        <div class="stat-card green"><span class="value">70%</span>
          <div class="label">Treated counties (≥ 30th pctile SNAP)</div></div>
        <div class="stat-card"><span class="value">&gt;6</span>
          <div class="label">Min. time periods required per county</div></div>
      </div>
      <hr class="hdiv">
      <h4 style="font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.15em;text-transform:uppercase;color:var(--accent);margin:0 0 14px">Sample Restrictions</h4>
      <ul class="slide-list">
        <li>DC (District of Columbia) dropped — singular entity, not representative of county structure.</li>
        <li>Unbalanced counties with fewer than 7 observations excluded to ensure clean pre/post windows.</li>
        <li>Treatment threshold tunable via the interactive tab (default: 30th percentile).</li>
        <li>Unemployment Rate (%) included as default control in main specifications.</li>
      </ul>
      <div class="slide-footer"><span>SNAP Event Study</span><span>Slide 3 / 9</span></div>
    </div>
    """)

    slide_design = mo.md("""
    <div class="slide">
      <div class="kicker">Identification Strategy</div>
      <h2 class="slide-heading">DiD Event Study Design</h2>
      <ol class="step-list">
        <li><span class="step-num">01</span>
          <div><strong>Define treatment.</strong> Compute each county's mean SNAP participation over all pre-2013 years.
          Counties at or above the chosen percentile are <em>treated</em>; the rest are controls.</div></li>
        <li><span class="step-num">02</span>
          <div><strong>Create event-time dummies.</strong>
          <code style="font-family:'DM Mono',monospace;background:var(--card);padding:1px 6px;border-radius:4px">rel_time = Year − 2013</code>.
          Dummies <code style="font-family:'DM Mono',monospace;background:var(--card);padding:1px 6px;border-radius:4px">evt_t</code>
          for each period; <code style="font-family:'DM Mono',monospace;background:var(--card);padding:1px 6px;border-radius:4px">evt_−1</code> omitted as baseline.</div></li>
        <li><span class="step-num">03</span>
          <div><strong>Interact with treatment.</strong>
          DiD regressors <code style="font-family:'DM Mono',monospace;background:var(--card);padding:1px 6px;border-radius:4px">did_evt_t = treated × evt_t</code>
          capture the differential effect of the lapse at each event-time period.</div></li>
        <li><span class="step-num">04</span>
          <div><strong>Two-Way Fixed Effects PanelOLS.</strong> Entity (county) FE absorb time-invariant heterogeneity.
          Time (year) FE absorb common shocks. Errors clustered at the entity level.</div></li>
      </ol>
      <div class="callout orange">
        <strong>Estimand:</strong> The coefficient on <em>did_evt_t</em> for t ≥ 0 measures the ATT in
        post-lapse years, relative to the omitted pre-lapse period t = −1.
      </div>
      <div class="slide-footer"><span>SNAP Event Study</span><span>Slide 4 / 9</span></div>
    </div>
    """)

    slide_outcomes = mo.md("""
    <div class="slide">
      <div class="kicker">Outcome Variables</div>
      <h2 class="slide-heading">Menu of Regressands</h2>
      <p class="body-text">Nine primary outcomes are estimated; one placebo is used for falsification.</p>
      <div style="margin-bottom:18px">
        <div class="kicker" style="margin-bottom:10px">Primary Outcomes</div>
        <div class="outcome-grid">
          <div class="outcome-pill"><span class="dot dot-blue"></span>Poverty Percent, All Ages</div>
          <div class="outcome-pill"><span class="dot dot-blue"></span>Poverty Percent, Under 18</div>
          <div class="outcome-pill"><span class="dot dot-blue"></span>Poverty Percent, Ages 5–17</div>
          <div class="outcome-pill"><span class="dot dot-orange"></span>Food Insecurity Rate (FI Rate)</div>
          <div class="outcome-pill"><span class="dot dot-orange"></span>Child Food Insecurity Rate</div>
          <div class="outcome-pill"><span class="dot dot-orange"></span>% FI Children Below 185% FPL</div>
          <div class="outcome-pill"><span class="dot dot-green"></span>Cost Per Meal</div>
          <div class="outcome-pill"><span class="dot dot-green"></span>Weighted Annual Food Budget Shortfall</div>
          <div class="outcome-pill"><span class="dot dot-green"></span>Number of FI Persons</div>
        </div>
      </div>
      <div class="outcome-grid">
        <div class="outcome-pill"><span class="dot dot-muted"></span><em>Placebo: Labor Force (falsification test)</em></div>
      </div>
      <div class="callout">
        <strong>Log specification:</strong> Any outcome can be estimated in log form via the
        interactive tab to recover approximate percentage changes, with right-axis rescaling
        via <code style="font-family:'DM Mono',monospace;background:rgba(0,0,0,.3);padding:1px 6px;border-radius:4px">exp(β) − 1</code>.
      </div>
      <div class="slide-footer"><span>SNAP Event Study</span><span>Slide 5 / 9</span></div>
    </div>
    """)

    slide_model = mo.md("""
    <div class="slide">
      <div class="kicker">Estimation</div>
      <h2 class="slide-heading">Model &amp; Implementation</h2>
      <div class="two-col">
        <div>
          <h4 style="font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.15em;text-transform:uppercase;color:var(--accent);margin:0 0 12px">Regression Spec</h4>
          <div class="code-block">
            y<sub>it</sub> = α<sub>i</sub> + λ<sub>t</sub><br>
            &nbsp;&nbsp;&nbsp;+ Σ<sub>t≠−1</sub> β<sub>t</sub>·(Treated<sub>i</sub> × 𝟙[τ=t])<br>
            &nbsp;&nbsp;&nbsp;+ γ·Controls<sub>it</sub> + ε<sub>it</sub>
          </div>
          <ul class="slide-list" style="margin-top:14px">
            <li>α<sub>i</sub>: county fixed effects</li>
            <li>λ<sub>t</sub>: year fixed effects</li>
            <li>Errors clustered by county</li>
          </ul>
        </div>
        <div>
          <h4 style="font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.15em;text-transform:uppercase;color:var(--accent);margin:0 0 12px">Python Implementation</h4>
          <div class="code-block">
            <span class="cm"># linearmodels PanelOLS</span><br>
            model = <span class="kw">PanelOLS</span>(<br>
            &nbsp;&nbsp;dependent=y,<br>
            &nbsp;&nbsp;exog=X,<br>
            &nbsp;&nbsp;entity_effects=<span class="kw">True</span>,<br>
            &nbsp;&nbsp;time_effects=<span class="kw">True</span>,<br>
            &nbsp;&nbsp;drop_absorbed=<span class="kw">True</span><br>
            )<br>
            result = model.fit(<br>
            &nbsp;&nbsp;cov_type=<span class="st">'clustered'</span>,<br>
            &nbsp;&nbsp;cluster_entity=<span class="kw">True</span><br>
            )
          </div>
        </div>
      </div>
      <div class="slide-footer"><span>SNAP Event Study</span><span>Slide 6 / 9</span></div>
    </div>
    """)





    _controls_panel = mo.vstack([
        mo.hstack([
            mo.vstack([
                mo.md('<div class="ctrl-label">Outcome (regressand)</div>'),
                ctrl_regressand,
            ]),
            mo.vstack([
                mo.md('<div class="ctrl-label">SNAP quantile cutoff</div>'),
                ctrl_quantile,
            ]),
        ], gap=1.5),
        mo.hstack([
            mo.vstack([
                mo.md('<div class="ctrl-label">Additional controls</div>'),
                ctrl_controls,
            ]),
            mo.vstack([
                mo.md('<div class="ctrl-label">Options</div>'),
                ctrl_log,
            ]),
        ], gap=1.5),
    ], gap=1)

    slide_interactive = mo.vstack([
        mo.md("""
        <div style="padding:40px 56px 0">
          <div class="kicker">Interactive</div>
          <h2 class="slide-heading">DiD Event Study Explorer</h2>
        </div>
        <div style="padding:0 56px 40px">
        """),
        _controls_panel,
        mo.md("</div>"),
    ])

    mo.carousel([slide_interactive])