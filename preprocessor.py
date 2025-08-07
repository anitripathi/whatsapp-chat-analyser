import re
import pandas as pd

def preprocess(data):
    # Regex pattern to extract: date, time, AM/PM, sender, message
    pattern = r'(\d{1,2}/\d{1,2}/\d{2}),\s(\d{1,2}:\d{2})\s?(AM|PM)\s-\s(.*?):\s(.*)'

    matches = re.findall(pattern, data)

    if not matches:
        return pd.DataFrame()

    full_datetime = [f"{date}, {time} {ampm}" for date, time, ampm, _, _ in matches]
    senders = [sender for _, _, _, sender, _ in matches]
    message_content = [msg for _, _, _, _, msg in matches]

    df = pd.DataFrame({
        'datetime_raw': full_datetime,
        'sender': senders,
        'message': message_content
    })

    df['date'] = pd.to_datetime(df['datetime_raw'], format='%m/%d/%y, %I:%M %p')

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['month_num'] = df['date'].dt.month
    df['day_name'] = df['date'].dt.day_name()
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['only_date'] = df['date'].dt.date

    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append("23-00")
        elif hour == 0:
            period.append("00-1")
        else:
            period.append(f"{hour}-{hour+1}")
    df['period'] = period

    return df
