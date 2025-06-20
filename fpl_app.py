import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Feelgood Pleasure Lovejoy App", layout="wide")

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

st.markdown("""
<div style='font-family: Arial Black, sans-serif; color:black;'>
    <h2>Feelgood Pleasure Lovejoy App</h2>
    <p style='font-family:Arial;'>All is means to joy | Joy = 👑</p>
</div>
""", unsafe_allow_html=True)

left_col, right_col = st.columns([1,4])

with left_col:
    joy_value = st.slider("Joy Level", 0.0, 10.0, 5.0, 0.01)
    st.markdown(joy_bar_html(joy_value), unsafe_allow_html=True)

with right_col:
    if 'joy10' not in st.session_state:
        st.session_state.joy10 = []
    if 'big_lever' not in st.session_state:
        st.session_state.big_lever = []
    if 'now' not in st.session_state:
        st.session_state.now = []
    if 'now_text' not in st.session_state:
        st.session_state.now_text = ""
    if 'now_duration' not in st.session_state:
        st.session_state.now_duration = "once"
    if 'show_help' not in st.session_state:
        st.session_state.show_help = False

    def display_entry_list(entries, can_upgrade=False):
        remove_idx = None
        move_to_big = None
        for i, entry in enumerate(entries):
            cols = st.columns([0.05, 0.8, 0.1, 0.1]) if can_upgrade else st.columns([0.05, 0.8, 0.1])
            checked = cols[0].checkbox("", key=f"{entry['id']}_chk", value=entry.get('locked', False), disabled=entry.get('locked', False))
            if entry.get('locked', False):
                cols[1].markdown(f"~~{entry['text']}~~")
            else:
                cols[1].markdown(entry['text'])

            if cols[-2].button("🗑️", key=f"{entry['id']}_del"):
                remove_idx = i

            if can_upgrade and cols[-1].button("🔨", key=f"{entry['id']}_upg"):
                move_to_big = i

            if checked and not entry.get('locked', False):
                entry['locked'] = True

        if remove_idx is not None:
            entries.pop(remove_idx)
            st.experimental_rerun()
        if move_to_big is not None:
            if len(st.session_state.big_lever) < 2:
                item = entries.pop(move_to_big)
                item['locked'] = True
                st.session_state.big_lever.append(item)
                st.experimental_rerun()
            else:
                st.warning("Max 2 Big Lever entries reached.")

    def add_joy10_callback():
        new_entry = st.session_state.new_joy10.strip()
        if new_entry:
            st.session_state.joy10.append({'id': f"joy10_{len(st.session_state.joy10)}", 'text': new_entry, 'locked': False})
            st.session_state.new_joy10 = ""

    def add_big_lever_callback():
        new_entry = st.session_state.new_big_lever.strip()
        if new_entry:
            if len(st.session_state.big_lever) < 2:
                st.session_state.big_lever.append({'id': f"big_lever_{len(st.session_state.big_lever)}", 'text': new_entry, 'locked': False})
                st.session_state.new_big_lever = ""
            else:
                st.warning("Max 2 Big Lever entries reached.")

    def add_now_callback():
        new_entry = st.session_state.now_text.strip()
        dur = st.session_state.now_duration
        if new_entry:
            st.session_state.now.append({'id': f"now_{len(st.session_state.now)}", 'text': new_entry, 'duration': dur, 'locked': False})
            st.session_state.now_text = ""

    st.markdown("### 🌹 10/10 Joy Life")
    st.text_input("Add 10/10 Entry", key="new_joy10")
    st.button("Add 10/10 Entry", on_click=add_joy10_callback)

    display_entry_list(st.session_state.joy10, can_upgrade=True)

    st.markdown("### 🔨 Big Lever (max 2)")
    st.text_input("Add Big Lever Entry", key="new_big_lever")
    st.button("Add Big Lever", on_click=add_big_lever_callback)

    display_entry_list(st.session_state.big_lever)

    st.markdown("### ✨ Now")
    st.text_input("Add Joy Chore", key="now_text", value=st.session_state.now_text)
    st.selectbox("Duration", options=["once", "daily", "weekly"], index=["once","daily","weekly"].index(st.session_state.now_duration), key="now_duration")
    st.button("Add Joy Chore", on_click=add_now_callback)

    def display_now_entries():
        remove_idx = None
        for i, entry in enumerate(st.session_state.now):
            cols = st.columns([0.05, 0.8, 0.1])
            checked = cols[0].checkbox("", key=f"{entry['id']}_chk", value=entry.get('locked', False), disabled=entry.get('locked', False))
            if entry.get('locked', False):
                cols[1].markdown(f"~~{entry['text']}~~")
            else:
                cols[1].markdown(entry['text'])
            if cols[2].button("🗑️", key=f"{entry['id']}_del"):
                remove_idx = i
            if checked and not entry.get('locked', False):
                entry['locked'] = True
        if remove_idx is not None:
            st.session_state.now.pop(remove_idx)
            st.experimental_rerun()

    display_now_entries()

    def toggle_help():
        st.session_state.show_help = not st.session_state.show_help

    if st.button("?", key="help_btn", on_click=toggle_help):
        pass

    if st.session_state.show_help:
        st.markdown("""
        <style>
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
        <div class="help-modal" role="dialog" aria-modal="true" aria-label="App Usage Instructions">
          <h3 style="margin-top:0;">How to use this app:</h3>
          <p><b>Everything is a means to joy. So joy is the king.</b><br>
          We say it three ways—feeling good, pleasure, and loving joy—to really ground it in.</p>
          <p>On the left you’ll see the joy scale, from 0 to 10. That’s your visual compass.</p>
          <p><b>Step 1: Describe your 10/10 joy life.</b><br>
          Since all is for joy, perfection = 10/10 joy, not just money, romance, or success.<br>
          Think of the real-life items that make up your personal heaven.<br>
          Hit “add 10/10 entry” for each one.</p>
          <p><b>Step 2: Rate where you are now.</b><br>
          Based on your 10/10 list, ask: How close am I today? Maybe you're at a 3, 5, 8.<br>
          Enter that number on the scale.</p>
          <p><b>Step 3: Add your “joy chores.”</b><br>
          These are the things that maintain or move your current level—<br>
          like brushing teeth, doing the dishes, going to the gym, finishing a task.<br>
          Tap “add joy chores”, and choose whether it’s daily, weekly, or once.</p>
          <p><b>Step 4: Pick your Big Lever(s).</b><br>
          Now look again at your 10/10 list.<br>
          Which 1 or 2 items would make the biggest positive impact on your score if you focused just on them?<br>
          If you'd like, add a “+ number” after each (like +1.9), based on how much joy they'd add.<br>
          Tap the hammer icon to move them to the Big Lever section.<br>
          This is where you’ll focus most—just 1 or 2 items max.</p>
          <p><b>Step 5: Lock it in.</b><br>
          Once everything’s entered, click each checkbox once to lock in the text and duration.<br>
          After that, checkboxes work normally:</p>
          <ul>
              <li>In 10/10, checked = permanent + strikethrough.</li>
              <li>In Now, one-time tasks disappear when done, recurring ones freeze until the next day/week.</li>
          </ul>
          <p>You can always delete with the trash icon.</p>
          <p><b>A note on growth:</b><br>
          Every time you hit a 9 or 10, it’s not “mission complete”—it’s a new horizon.<br>
          Each peak reveals a higher one, because joy gets richer.<br>
          Your 10/10 at age 5 isn’t your 10/10 now (no more HoHos and 20-hour video games, right?).<br>
          So: when you hit a high, re-evaluate. What’s your 10/10 today? Update your entries. Stay fresh. Stay real.<br>
          Some habits may stick around (like brushing your teeth), but joy itself evolves endlessly.<br>
          <b>Joy has no ceiling.</b></p>
          <button class="help-close-btn" onclick="document.querySelector('.help-modal').style.display='none'">Close</button>
        </div>
        """, unsafe_allow_html=True)
