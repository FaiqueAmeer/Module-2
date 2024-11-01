import pandas as pd

# Load and clean the data
twitch_data = pd.read_csv('Twitch_game_data.csv', encoding='ISO-8859-1')
twitch_data = twitch_data.dropna(subset=['Game'])
twitch_data['Month'] = twitch_data['Month'].astype(int)
twitch_data['Year'] = twitch_data['Year'].astype(int)
twitch_data['Hours_watched'] = twitch_data['Hours_watched'].astype(int)
twitch_data['Peak_viewers'] = twitch_data['Peak_viewers'].astype(int)
twitch_data['Avg_viewer_ratio'] = twitch_data['Avg_viewer_ratio'].astype(float)

# Calculate top games by engagement metrics
top_hours_watched = twitch_data.groupby('Game')['Hours_watched'].sum().nlargest(5)
top_peak_viewers = twitch_data.groupby('Game')['Peak_viewers'].max().nlargest(5)
top_avg_viewer_ratio = twitch_data.groupby('Game')['Avg_viewer_ratio'].mean().nlargest(5)

# Display the results
print("Top Games by Total Hours Watched:\n", top_hours_watched)
print("\nTop Games by Peak Viewers:\n", top_peak_viewers)
print("\nTop Games by Average Viewer Ratio:\n", top_avg_viewer_ratio)