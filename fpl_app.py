import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Feelgood Pleasure Lovejoy App", layout="wide")

# Joy bar CSS & HTML
def joy_bar_html(value):
    val = max(0, min(value, 10))
    height_percent = (val / 10) * 100
    return f"""
    <style>
      @keyframes pulse-glow {{
        0% {{ box-shadow: 0 0 20px 8px #ffd700cc; }}
        50% {{ box-shadow: 0 0 30px 15px #fff8a0cc; }}
        100% {{ box-shadow: 0 0 20px 8px #ffd700cc; }}
      }}
      .joybar-container {{
          width: 70px;
          height: 700px;
          background: #000;
          border-radius: 20px;
          box-shadow: inset 0 0 15px 6px #ffd700aa;
          position: relative;
          margin: auto;
          overflow: hidden;
      }}
      .joybar-fill {{
          position: absolute;
          bottom: 0;
          width: 100%;
          height: {height_percent}%;
          background: linear-gradient(to top, #FFD700, #FFFACD);
          border-radius: 20px 20px 0 0;
          animation: pulse-glow 2.5s ease-in-out infinite;
      }}
      .joy-label {{
          font-family: 'Arial Black', Arial, sans-serif;
          color: #FFD700CC;
          font-size: 22px;
          text-align: center;
          margin-bottom: 12px;
          user-select: none;
          letter-spacing: 3px;
      }}
    </style>
    <div class="joy-label">JOY</div>
    <div class="joybar-container">
      <div class="joybar-fill"></div>
    </div>
    """

# Intro text
st.markdown("""
<div style='font-family: Arial Black, sans-serif; color:black;'>
    <h2>Feelgood Pleasure Lovejoy App</h2>
    <p style='font-family:Arial;'>All is means to joy | Joy = 👑</p>
</div>
""", unsafe_allow_html=True)

# Layout
left_col, right_col = st.columns([1, 4])

with left_col:
    joy_value = st.slider("Joy Level", 0.0, 10.0, 5.0, 0.01)
    st.markdown(joy_bar_html(joy_value), unsafe_allow_html=True)

with right_col:
    st.markdown("### 🌹 10/10 Joy Life")

    if "joy10" not in st.session_state:
        st.session_state.joy10 = []
    if "big_lever" not in st.session_state:
        st.session_state.big_lever = []
    if "now" not in st.session_state:
        st.session_state.now = []

    def show_entries(entries, can_hammer=False):
        to_delete = -1
        to_upgrade = -1
        for i, entry in enumerate(entries):
            cols = st.columns([0.05, 0.75, 0.1, 0.1])
            locked = entry.get("locked", False)
            checked = cols[0].checkbox("", value=locked, key=f"{entry['id']}_chk", disabled=locked)
            if locked:
                cols[1].markdown(f"~~{entry['text']}~~")
            else:
                cols[1].markdown(entry["text"])
            if cols[2].button("🗑️", key=f"{entry['id']}_del"):
                to_delete = i
            if can_hammer:
                if cols[3].button("🔨", key=f"{entry['id']}_hammer"):
                    to_upgrade = i
            if checked and not locked:
                entry["locked"] = True
                st.experimental_rerun()

        if to_delete >= 0:
            entries.pop(to_delete)
            st.experimental_rerun()
        if to_upgrade >= 0:
            if len(st.session_state.big_lever) < 2:
                item = entries.pop(to_upgrade)
                item["locked"] = True
                st.session_state.big_lever.append(item)
                st.experimental_rerun()
            else:
                st.warning("Max 2 Big Lever entries reached.")

    # Show joy10 entries first
    show_entries(st.session_state.joy10, can_hammer=True)

    # Then show input box + add button
    with st.form("add_joy10_form"):
        new_joy10 = st.text_input("Type a 10/10 Entry", key="joy10_text")
        submitted = st.form_submit_button("Add 10/10 Entry")
        if submitted and new_joy10.strip():
            st.session_state.joy10.append({
                "id": f"joy10_{len(st.session_state.joy10)}",
                "text": new_joy10.strip(),
                "locked": False
            })
            st.experimental_rerun()

    # Big Lever
    st.markdown("### 🔨 Big Lever (max 2)")
    show_entries(st.session_state.big_lever)

    # Now
    st.markdown("### ✨ Now")

    def show_now():
        to_delete = -1
        for i, entry in enumerate(st.session_state.now):
            cols = st.columns([0.05, 0.8, 0.1])
            locked = entry.get("locked", False)
            checked = cols[0].checkbox("", value=locked, key=f"{entry['id']}_chk", disabled=locked)
            if locked:
                cols[1].markdown(f"~~{entry['text']}~~")
            else:
                cols[1].markdown(entry["text"])
            if cols[2].button("🗑️", key=f"{entry['id']}_del"):
                to_delete = i
            if checked and not locked:
                entry["locked"] = True
                st.experimental_rerun()
        if to_delete >= 0:
            st.session_state.now.pop(to_delete)
            st.experimental_rerun()

    show_now()

    with st.form("add_now_form"):
        now_text = st.text_input("Add Joy Chore", key="now_text")
        duration = st.selectbox("Duration", ["once", "daily", "weekly"], key="now_duration")
        submitted = st.form_submit_button("Add Joy Chore")
        if submitted and now_text.strip():
            st.session_state.now.append({
                "id": f"now_{len(st.session_state.now)}",
                "text": now_text.strip(),
                "duration": duration,
                "locked": False
            })
            st.experimental_rerun()

# Floating help button
st.markdown("""
<style>
.help-button {
    position: fixed;
    left: 100px;
    bottom: 20px;
    width: 38px;
    height: 38px;
    background: #17a2b8;
    color: white;
    border-radius: 50%;
    font-weight: bold;
    font-size: 28px;
    line-height: 38px;
    text-align: center;
    cursor: pointer;
    z-index: 99999;
    box-shadow: 0 0 12px #17a2b8aa;
    user-select: none;
}
.help-modal {
    position: fixed;
    left: 10%;
    bottom: 80px;
    width: 80vw;
    max-width: 380px;
    max-height: 70vh;
    background: #fffbe6;
    border: 3px solid #FFD700;
    border-radius: 16px;
    box-shadow: 0 0 25px #ffd700aa;
    padding: 20px;
    overflow-y: auto;
    z-index: 100000;
}
.help-close-btn {
    background: #ffc107;
    border: none;
    padding: 6px 12px;
    font-weight: bold;
    border-radius: 8px;
    cursor: pointer;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

if "show_help" not in st.session_state:
    st.session_state.show_help = False

if st.button("?", key="help_button"):
    st.session_state.show_help = not st.session_state.show_help

if st.session_state.show_help:
    st.markdown("""
    <div class="help-modal" role="dialog" aria-modal="true" aria-label="App Usage Instructions">
      <h3 style="margin-top:0;">How to use this app:</h3>
      <p><b>Everything is a means to joy. So joy is the king.</b><br>
      We say it three ways—feeling good, pleasure, and loving joy—to really ground it in.</p>
      <p>On the left you’ll see the joy scale, from 0 to 10. That’s your visual compass.</p>
      <p><b>Step 1: Describe your 10/10 joy life.</b><br>
      Think of your personal heaven. Hit “Add 10/10 Entry” for each one.</p>
      <p><b>Step 2: Rate where you are now.</b><br>
      Ask: How close am I today?</p>
      <p><b>Step 3: Add your “joy chores.”</b><br>
      Like brushing teeth, gym, or finishing tasks.</p>
      <p><b>Step 4: Pick your Big Lever(s).</b><br>
      What 1 or 2 items would raise your joy the most?</p>
      <p><b>Step 5: Lock it in.</b><br>
      Click each checkbox once to lock. After that:</p>
      <ul>
        <li>10/10 stays checked, strikethrough</li>
        <li>Now tasks disappear or reset daily/weekly</li>
      </ul>
      <button class="help-close-btn" onclick="document.querySelector('.help-modal').style.display='none'">Close</button>
    </div>
    """, unsafe_allow_html=True)
