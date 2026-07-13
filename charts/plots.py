import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Design tokens matching warm neutral palette
BG_COLOR = 'rgba(0,0,0,0)'
GRID_COLOR = '#E6DED3'
TEXT_COLOR = '#2C2C2C'
SUBTEXT_COLOR = '#777777'
ACCENT_COLOR = '#5D7357'     # Sage Green (Positive/Forecast)
ALERT_COLOR = '#A65A52'      # Muted Terracotta (Negative/Anomaly)
WARNING_COLOR = '#B78C4C'    # Muted Gold (Warning)

layout_defaults = dict(
    paper_bgcolor=BG_COLOR,
    plot_bgcolor=BG_COLOR,
    font=dict(family='Inter, sans-serif', size=11, color=TEXT_COLOR),
    margin=dict(l=40, r=40, t=30, b=45),
    xaxis=dict(
        gridcolor=GRID_COLOR, linecolor=GRID_COLOR, 
        tickfont=dict(color=TEXT_COLOR), zeroline=False
    ),
    yaxis=dict(
        gridcolor=GRID_COLOR, linecolor=GRID_COLOR, 
        tickfont=dict(color=TEXT_COLOR), zeroline=False
    )
)

def plot_monthly_sales_trend(df_monthly, df_forecast=None, forecast_dates=None):
    fig = go.Figure()
    # Actuals
    fig.add_trace(go.Scatter(
        x=df_monthly['Order Date'], y=df_monthly['Sales'],
        mode='lines', name='Actual Historical Sales',
        line=dict(color=TEXT_COLOR, width=2)
    ))
    # Forecast
    if df_forecast is not None and forecast_dates is not None:
        fig.add_trace(go.Scatter(
            x=forecast_dates, y=df_forecast,
            mode='lines', name='Projected Sales',
            line=dict(color=ACCENT_COLOR, width=1.8, dash='dash')
        ))
    fig.update_layout(
        **layout_defaults,
        showlegend=True,
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )
    return fig

def plot_regional_comparison(df):
    reg_sales = df.groupby('Region')['Sales'].sum().reset_index()
    fig = px.bar(
        reg_sales, x='Region', y='Sales',
        color_discrete_sequence=[ACCENT_COLOR]
    )
    fig.update_layout(**layout_defaults)
    fig.update_xaxes(gridcolor='rgba(0,0,0,0)', linecolor=GRID_COLOR)
    return fig

def plot_category_distribution(df):
    cat_sales = df.groupby('Category')['Sales'].sum().reset_index()
    fig = px.bar(
        cat_sales, x='Sales', y='Category', orientation='h',
        color_discrete_sequence=[WARNING_COLOR]
    )
    fig.update_layout(**layout_defaults)
    fig.update_yaxes(gridcolor='rgba(0,0,0,0)', linecolor=GRID_COLOR)
    return fig

def plot_forecast_chart(last_actuals, forecast_dates, forecast_values, model_name):
    fig = go.Figure()
    # Last 12 months actuals
    fig.add_trace(go.Scatter(
        x=last_actuals['Order Date'], y=last_actuals['Sales'],
        mode='lines', name='Actual (Last 12 Months)',
        line=dict(color=TEXT_COLOR, width=2)
    ))
    # Projections
    fig.add_trace(go.Scatter(
        x=forecast_dates, y=forecast_values,
        mode='lines+markers', name=f'{model_name} Projection',
        line=dict(color=ACCENT_COLOR, width=2, dash='dot')
    ))
    fig.update_layout(
        **layout_defaults,
        showlegend=True,
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )
    return fig

def plot_anomaly_timeline(df_weekly, anomaly_dates, anomaly_sales):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_weekly['Order Date'], y=df_weekly['Sales'],
        mode='lines', name='Weekly Sales Baseline',
        line=dict(color=TEXT_COLOR, width=1.2)
    ))
    fig.add_trace(go.Scatter(
        x=anomaly_dates, y=anomaly_sales,
        mode='markers', name='Flagged Anomaly',
        marker=dict(color=ALERT_COLOR, size=8, symbol='circle')
    ))
    fig.update_layout(
        **layout_defaults,
        showlegend=True,
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )
    return fig

def plot_cluster_scatter(cl_df):
    fig = px.scatter(
        cl_df, x='PCA1', y='PCA2', color=cl_df['Cluster'].astype(str),
        hover_data=['Sub-Categories', 'TotalVolume', 'YoYGrowth', 'AOV'],
        labels={'Cluster': 'Demand Cluster'},
        color_discrete_sequence=[ACCENT_COLOR, ALERT_COLOR, WARNING_COLOR, SUBTEXT_COLOR]
    )
    fig.update_traces(marker=dict(size=12, line=dict(width=1, color=TEXT_COLOR)))
    fig.update_layout(
        **layout_defaults
    )
    return fig
