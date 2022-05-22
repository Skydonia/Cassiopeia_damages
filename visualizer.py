from plotly.subplots import make_subplots
import plotly.graph_objects as go


def Visualize(df_list, output_path, subplot_titles):
    fig = make_subplots(rows=len(df_list) // 2, cols=2,
                        subplot_titles=subplot_titles)
    for i, df in enumerate(df_list):
        damage_sources = [e for e in df.columns if e not in ['target_magic_rest', 'total']]
        for damage_source in damage_sources:
            fig.add_trace(go.Scatter(
                name=damage_source,
                x=df['target_magic_rest'],
                y=df[damage_source],
                stackgroup='one', legendgroup=subplot_titles[i]),
                row=i // 2 + 1, col=i % 2 + 1)
    fig.update_layout(
        legend_tracegroupgap=600//len(df_list),
        title_text=f"Simulation (1Q + 4E) Cassiopeia set 3 items report",
        **{f'xaxis{i + 1}_title': 'Target magic resist' for i, df in enumerate(df_list)},
        **{f'yaxis{i + 1}_title': 'Damages' for i, df in enumerate(df_list)})
    # template="plotly_dark"
    fig.write_html(output_path)
    return
