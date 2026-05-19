import streamlit as st
import random
import time

card_deck = {
    1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
    8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'
}

st.set_page_config(page_title="High Card Game", page_icon="🎴")

st.title("🎴 High Card Draw Game")

name = st.text_input("Enter your name ❤️")

# Function to create a fake card UI
def card_ui(title, value, color):
    st.markdown(
        f"""
        <div style="
            border:2px solid {color};
            border-radius:15px;
            padding:20px;
            text-align:center;
            font-size:40px;
            font-weight:bold;
            background-color:#111;
            color:{color};
            margin-bottom:10px;
        ">
        {value}
        </div>
        """,
        unsafe_allow_html=True
    )

if name:
    st.write(f"Hello **{name}** 👋")

    player_card = st.slider("Pick your card power (1-13)", 1, 13, 7)

    if st.button("🎲 Draw Cards"):
        placeholder = st.empty()

        # Fake animation effect
        for _ in range(6):
            with placeholder.container():
                st.write("Shuffling cards... 🔄")
                card_ui("Shuffling", random.choice(list(card_deck.values())), "#888")
            time.sleep(0.2)

        computer_card = random.randint(1, 13)

        st.markdown("---")
        st.subheader("🃏 Final Result")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**{name}**")
            card_ui("Player", card_deck[player_card], "#00ffcc")

        with col2:
            st.write("**Computer**")
            card_ui("CPU", card_deck[computer_card], "#ff5555")

        st.markdown("---")

        # Result
        if player_card > computer_card:
            st.success(f"🏆 {name} wins!")
        elif computer_card > player_card:
            st.error("💻 Computer wins!")
        else:
            st.info("🤝 It's a tie!")