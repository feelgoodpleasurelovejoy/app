from IPython.display import display, HTML

# --- Main app UI loads first ---
# (Insert your existing display(background_box) call here)

# --- Then the help icon and popup overlay ---
display(HTML(r"""
<style>
  #fpl-help-icon {
    position: fixed;
    left: 90px;
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

  #fpl-help-modal {
    display: none;
    position: fixed;
    left: 90px;
    bottom: 80px;
    transform: none;
    width: 90vw;
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

  #fpl-help-close {
    background: #ffc107;
    border: none;
    padding: 6px 12px;
    font-weight: bold;
    border-radius: 8px;
    cursor: pointer;
    margin-top: 10px;
  }

  #fpl-help-modal p, #fpl-help-modal ul {
    font-size: 16px;
  }
</style>

<div id="fpl-help-icon" title="Help">?</div>

<div id="fpl-help-modal" role="dialog" aria-modal="true" aria-label="App Usage Instructions">
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
  Add a “+ number” after each (like +1.9), based on how much joy they'd add.<br>
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
  <button id="fpl-help-close">Close</button>
</div>

<script>
  const helpIcon = document.getElementById('fpl-help-icon');
  const helpModal = document.getElementById('fpl-help-modal');
  const helpClose = document.getElementById('fpl-help-close');

  helpIcon.onclick = () => {
    helpModal.style.display = 'block';
  };
  helpClose.onclick = () => {
    helpModal.style.display = 'none';
  };
</script>
"""))
