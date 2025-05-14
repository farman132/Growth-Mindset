import streamlit as st

st.set_page_config(page_title="Growth Mindset App", layout="centered")
st.title("🌱 Growth Mindset Coach")

menu = st.sidebar.radio("Menu Chuno:", ["Home", "Quiz", "Tips", "Reflection", "Motivation"])

if menu == "Home":
    st.header("👋 Welcome!")
    st.write("""
    Is app ka maqsad hai aapki soch (mindset) ko positive bananay mein madad karna.

    **Growth Mindset** ka matlab hai:
    - Apni galtiyon se seekhna
    - Challenges ko accept karna
    - Aur har waqt improve karte rehna

    Aao mil kar apni soch ko behtar banayein!
    """)
    st.image("https://miro.medium.com/v2/resize:fit:1200/format:webp/1*B6jKURDZn1XZKjb5t5JrNQ.jpeg", use_column_width=True)

elif menu == "Quiz":
    st.header("🧠 Mindset Quiz")
    st.write("Neeche diye gaye sawalat ka jawab dein:")

    q1 = st.radio("1. Mein mushkil kaam se ghabrata hoon.", ["Haan", "Nahi"])
    q2 = st.radio("2. Ghaltiyan meri failure ka saboot hain.", ["Haan", "Nahi"])
    q3 = st.radio("3. Mein naye skills seekh sakta hoon.", ["Haan", "Nahi"])
    q4 = st.radio("4. Agar mein fail ho jaun to dobara koshish karta hoon.", ["Haan", "Nahi"])
    q5 = st.radio("5. Mein samajhta hoon ke zehni salahiyatain fix hoti hain.", ["Haan", "Nahi"])

    if st.button("🔍 Result Check Karein"):
        score = 0
        if q1 == "Nahi": score += 1
        if q2 == "Nahi": score += 1
        if q3 == "Haan": score += 1
        if q4 == "Haan": score += 1
        if q5 == "Nahi": score += 1

        st.subheader("🎯 Aapka Result:")
        if score >= 4:
            st.success("Aap ka mindset growth based hai! Keep it up! 💪")
        else:
            st.warning("Aap thoda fixed mindset rakhte hain. Lekin aap seekh sakte hain!")

elif menu == "Tips":
    st.header("📌 Tips for Growth Mindset")
    st.write("""
    💡 **Behtar soch aur learning ke liye kuch tips:**

    - Har challenge ek seekhne ka moka hai
    - Ghaltiyan improvement ka chance hoti hain
    - Mehnat aur lagan se sab kuch seekha ja sakta hai
    - Apne efforts pe focus karo, sirf results pe nahi
    - Feedback ko positively lo
    """)

elif menu == "Reflection":
    st.header("✍️ Aaj kya seekha?")
    reflection = st.text_area("Aaj aapne kya seekha? Yahan likhein...")
    if st.button("💾 Save Karo"):
        if reflection.strip() != "":
            st.success("Shabash! Apni learning likhna ek growth ka nishan hai. 🎉")
        else:
            st.error("Please kuch likhein pehle!")

elif menu == "Motivation":
    st.header("🔥 Aaj ka Motivation")
    st.info("“Ghaltiyan is baat ka saboot hain ke aap koshish kar rahe hain.” – Carol Dweck")
    st.info("“Mein jitna mehnat karoon, utna behtar ban sakta hoon.”")
    st.success("Aap mein potential hai – har din behtar banne ki koshish karein! 💖")

