import streamlit as st
import random

card_deck = {
    1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
    8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'
}

st.title("🎴 High Card Draw Game")

name = st.text_input("Enter your name ❤️")

if name:
    st.write(f"Hello {name}! Choose your card:")

    player_card = st.slider("Pick a number (1-13)", 1, 13, 7)

    if st.button("Draw Cards 🎲"):
        computer_card = random.randint(1, 13)

        st.subheader("Results")

        st.write(f"**{name} drew:** {card_deck[player_card]}")
        st.write(f"**Computer drew:** {card_deck[computer_card]}")

        if player_card > computer_card:
            st.success(f"🏆 {name} wins!")
        elif computer_card > player_card:
            st.error("💻 Computer wins!")
        else:
            st.info("🤝 It's a tie!")