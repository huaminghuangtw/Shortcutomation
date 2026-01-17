import json
import os
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

def get_date_from_week(year, week_number):
    """Convert year and week number to date."""
    # ISO 8601: Week 1 is the first week containing a Thursday
    # This means January 4th is always in Week 1
    jan_4 = datetime(year, 1, 4)
    week_1_start = jan_4 - timedelta(days=jan_4.weekday())
    target_date = week_1_start + timedelta(weeks=week_number - 1)
    return target_date

def parse_csv_data(csv_string):
    lines = csv_string.strip().split('\n')
    data = []
    for line in lines[1:]:  # Skip header
        parts = line.split(',')
        if len(parts) == 3:
            data.append({
                'week': int(parts[0]),
                'shortcuts': int(parts[1]),
                'actions': int(parts[2])
            })
    return data

def generate_chart(history_file, output_file):
    with open(history_file, 'r') as f:
        history_data = json.load(f)
    
    all_dates = []
    all_shortcuts = []
    all_actions = []
    
    for year_str, csv_data in sorted(history_data.items()):
        year = int(year_str)
        data = parse_csv_data(csv_data)
        
        for entry in data:
            date = get_date_from_week(year, entry['week'])
            all_dates.append(date)
            all_shortcuts.append(entry['shortcuts'])
            all_actions.append(entry['actions'])
    
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Inter', 'SF Pro Text', 'Segoe UI', 'Helvetica Neue', 'Arial']
    plt.rcParams['font.size'] = 13
    plt.rcParams['axes.linewidth'] = 1.2
    plt.rcParams['axes.labelsize'] = 15
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['xtick.labelsize'] = 13
    plt.rcParams['ytick.labelsize'] = 13
    
    fig, ax1 = plt.subplots(figsize=(16, 8), facecolor='white')
    ax1.set_facecolor('#FAFAFA')
    
    color1 = '#0A7AFF'
    color2 = '#FF3B30'
    grid_color = '#D1D1D6'
    text_color = '#000000'
    label_color = '#3A3A3C'
    
    line1 = ax1.plot(all_dates, all_shortcuts, 
                     color=color1, 
                     linewidth=3, 
                     label='Total Shortcuts',
                     zorder=4,
                     solid_capstyle='round')
    
    ax1.set_ylabel('Total Shortcuts', 
                   color=label_color, 
                   fontsize=15, 
                   fontweight=600, 
                   labelpad=12)
    ax1.tick_params(axis='y', 
                    labelcolor=label_color, 
                    colors=label_color,
                    width=1.2,
                    length=5, 
                    pad=6)
    ax1.yaxis.set_major_locator(plt.MaxNLocator(nbins=15, integer=True, prune='both'))
    
    ax1.spines['left'].set_color(label_color)
    ax1.spines['left'].set_linewidth(1.2)
    
    ax2 = ax1.twinx()
    line2 = ax2.plot(all_dates, all_actions, 
                     color=color2, 
                     linewidth=3, 
                     label='Total Actions',
                     zorder=4,
                     solid_capstyle='round')
    
    ax2.set_ylabel('Total Actions', 
                   color=label_color, 
                   fontsize=15, 
                   fontweight=600, 
                   labelpad=12)
    ax2.tick_params(axis='y', 
                    labelcolor=label_color, 
                    colors=label_color,
                    width=1.2,
                    length=5, 
                    pad=6)
    ax2.yaxis.set_major_locator(plt.MaxNLocator(nbins=15, integer=True, prune='both'))
    
    ax2.spines['right'].set_color(label_color)
    ax2.spines['right'].set_linewidth(1.2)
    
    ax1.set_xlabel('', fontsize=12)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax1.tick_params(axis='x', 
                    labelcolor=label_color, 
                    colors=label_color,
                    width=0,
                    length=0, 
                    pad=8)
    
    ax1.set_xlim(all_dates[0], all_dates[-1])
    
    ax1.grid(True, 
             axis='y', 
             color=grid_color, 
             linewidth=1, 
             linestyle='-', 
             alpha=0.5, 
             zorder=1)
    ax1.set_axisbelow(True)
    
    ax1.spines['top'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    legend = ax1.legend(lines, labels, 
                       loc='upper left',
                       bbox_to_anchor=(0.01, 0.98),
                       frameon=True,
                       fancybox=False,
                       shadow=False,
                       framealpha=0.95,
                       edgecolor=grid_color,
                       facecolor='white',
                       fontsize=11,
                       labelcolor=text_color,
                       handlelength=2.8,
                       handleheight=1.5,
                       borderpad=1,
                       labelspacing=0.8)
    legend.get_frame().set_linewidth(1.2)
    
    for line in legend.get_lines():
        line.set_linewidth(4)
    
    plt.subplots_adjust(left=0.11, right=0.89, top=0.96, bottom=0.08)
    
    plt.savefig(output_file, 
                dpi=600, 
                bbox_inches='tight',
                facecolor='white', 
                edgecolor='none',
                pad_inches=0.2)
    
    plt.close()


def main():
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    assets_dir = repo_root / 'assets'
    
    history_file = assets_dir / 'history.json'
    output_file = assets_dir / 'history-chart.png'
    
    generate_chart(history_file, output_file)


if __name__ == '__main__':
    main()
