# Imports
import pandas as pd
from wordcloud import WordCloud
from urlextract import URLExtract
from collections import Counter
import emoji

# Initialize URL extractor
extract = URLExtract()




# ----------------------------------------------------
# Function: Fetch basic statistics
# ----------------------------------------------------
def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user]

    # Total messages
    num_messages = df.shape[0]

    words = []
    emojis = []

    for message in df['message']:
        words.extend(message.split())
        emojis.extend([c for c in message if emoji.is_emoji(c)])  # Extract emojis

    # Total words and emojis
    num_words = len(words)
    num_emojis = len(emojis)

    # Media messages
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    # Links
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    # Emoji frequency
    emoji_counter = Counter(emojis).most_common()

    return num_messages, num_words, num_media_messages, len(links), num_emojis, emoji_counter




# ----------------------------------------------------
# Function: Most active users
# ----------------------------------------------------
def most_busy_users(df):
    # Top 5 users by message count
    x = df['sender'].value_counts().head()

    # Percentage contribution of each user
    df_percent = round((df['sender'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'sender': 'percent'})

    return x, df_percent




# ----------------------------------------------------
# Function: Generate WordCloud
# ----------------------------------------------------
def create_wordcloud(selected_user, df):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user]

    # Remove media and group notifications
    temp = df[df['sender'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    # Remove stopwords from messages
    def remove_stop_words(message):
        return " ".join([word for word in message.lower().split() if word not in stop_words])

    temp['message'] = temp['message'].apply(remove_stop_words)

    # Generate WordCloud
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    
    return df_wc



# ----------------------------------------------------
# Function: Most common words (excluding stopwords)
# ----------------------------------------------------
def most_common_words(selected_user, df):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user]

    # Remove media and group notifications
    temp = df[df['sender'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    return pd.DataFrame(Counter(words).most_common(20))



# ----------------------------------------------------
# Function: Emoji frequency
# ----------------------------------------------------
def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if emoji.is_emoji(c)])

    return pd.DataFrame(Counter(emojis).most_common())



# ----------------------------------------------------
# Function: Monthly timeline of messages
# ----------------------------------------------------
def monthly_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user]

    # Group by year and month
    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    # Combine month and year into single string
    timeline['time'] = timeline['month'] + "-" + timeline['year'].astype(str)

    return timeline



# ----------------------------------------------------
# Function: Daily timeline of messages
# ----------------------------------------------------
def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user]

    return df.groupby('only_date').count()['message'].reset_index()



# ----------------------------------------------------
# Function: Weekly activity (which day most active)
# ----------------------------------------------------
def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user]

    return df['day_name'].value_counts()



# ----------------------------------------------------
# Function: Monthly activity (which month most active)
# ----------------------------------------------------
def month_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user]

    return df['month'].value_counts()



# Function: Weekly activity heatmap (Day vs Time Period)
def activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user]

    return df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)
