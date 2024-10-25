import streamlit as st
import pandas as pd
import plotly.express as px
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# Database connection function
def get_connection():
    return psycopg2.connect(
        host=os.getenv("HOST"),  # Adjust if needed
        database=os.getenv("DATABASE"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        port = os.getenv("PORT_NO")
    )

# Helper to get scores from PostgreSQL
def get_scores():
    conn = get_connection()
    df = pd.read_sql("SELECT player_name, score FROM player_scores", conn)
    conn.close()
    return df

# Function to reset the game: Drop and recreate tables
def reset_game():
    conn = get_connection()
    cur = conn.cursor()
    
    # Drop existing tables
    cur.execute("DROP TABLE IF EXISTS player_scores;")
    cur.execute("DROP TABLE IF EXISTS player_progress;")
    
    # Recreate tables
    cur.execute("""
        CREATE TABLE player_scores (
            player_name VARCHAR(50) PRIMARY KEY,
            score INT DEFAULT 0);
        INSERT INTO player_scores (player_name) 
        VALUES ('Semilore'), ('Tomisin'), ('Joel'), ('Monica'), ('Lekan');
    """)
    
    cur.execute("""
        CREATE TABLE player_progress (
            player_name VARCHAR PRIMARY KEY,
            current_question_index INT DEFAULT 0,
            answered_questions JSONB DEFAULT '[]',
            questions_answered_count INT DEFAULT 0);
    """)
    
    conn.commit()
    cur.close()
    conn.close()

# Title of the dashboard
st.title("Game Night Dashboard")
st.divider()

scores_data = get_scores()

fig = px.bar(
    scores_data,
    x="player_name",
    y="score",
    color="player_name",
    text="score",
    title="Real-Time Player Scores",
)
fig.update_traces(textposition='outside')
fig.update_layout(yaxis_title="Score", xaxis_title="Player", showlegend=False)

st.plotly_chart(fig, use_container_width=True)

st.divider()
reset_col, refresh_col = st.columns(2)
# Button to reset the game
with reset_col:
    if st.button("Reset Game"):
        reset_game()
        st.success("Game has been reset successfully!")
        st.rerun()  # Reload the app to reflect changes
        
with refresh_col:
    if st.button("Refresh Score"):
        st.rerun()


