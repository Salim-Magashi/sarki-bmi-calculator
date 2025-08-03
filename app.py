import streamlit as st

# Page setup
st.set_page_config(page_title="SARKI BMI Calculator", page_icon="🧮", layout="centered")

# Language selection
language = st.selectbox("Choose Language / Zaɓi Yare:", ["English", "Hausa"])

st.title("🧮 SARKI BMI Calculator")

if language == "English":
    st.write("Easily calculate your Body Mass Index (BMI) and understand what your result means.")
    weight = st.number_input("Enter your weight (kg):", min_value=1.0)
    height = st.number_input("Enter your height (m):", min_value=0.1)

    if st.button("Calculate BMI"):
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            st.warning("You are underweight.")
            st.markdown("""
            **Suggestions:**
            - Try to eat more frequently and choose nutrient-rich foods.
            - Include protein-rich snacks like nuts and dairy.
            - Consult a healthcare provider or dietitian for proper evaluation.
            """)
        elif 18.5 <= bmi < 25:
            st.success("You have a normal weight. Keep it up!")
            st.markdown("""
            **Tips to Maintain:**
            - Stay physically active.
            - Eat a balanced diet.
            """)
        elif 25 <= bmi < 30:
            st.warning("You are overweight.")
            st.markdown("""
            **Suggestions:**
            - Reduce intake of high-calorie foods and sugary drinks.
            - Try regular aerobic activities like walking, jogging, or swimming.
            - Consider speaking with a health expert for tailored advice.
            """)
        else:
            st.error("You are obese.")
            st.markdown("""
            **Suggestions:**
            - Adopt a low-calorie, nutritious diet plan.
            - Engage in physical activity for at least 30 minutes most days.
            - Seek support from healthcare professionals.
            """)

        # BMI Reference Table
        st.markdown("""
        ### 📊 BMI Reference Table
        | BMI Range        | Category      |
        |------------------|---------------|
        | Less than 18.5   | Underweight   |
        | 18.5 – 24.9      | Normal        |
        | 25.0 – 29.9      | Overweight    |
        | 30.0 and above   | Obese         |
        """)
else:
    st.write("Sauƙin lissafa Body Mass Index (BMI) ɗinka kuma fahimci sakamakon.")

    weight = st.number_input("Shigar da nauyin ka (kg):", min_value=1.0)
    height = st.number_input("Shigar da tsayin ka (m):", min_value=0.1)

    if st.button("Lissafa BMI"):
        bmi = weight / (height ** 2)
        st.success(f"BMIn ka: {bmi:.2f}")

        if bmi < 18.5:
            st.warning("Kana da ƙarancin nauyi.")
            st.markdown("""
            **Shawarwari:**
            - Yi ƙoƙarin cin abinci mai yawa da kuma wadatuwa.
            - Ka haɗa da abubuwan cin abinci masu furotin kamar kwayoyi da madara.
            - Tuntuɓi likita ko mai ba da shawara kan abinci.
            """)
        elif 18.5 <= bmi < 25:
            st.success("Kana da nauyin da ya dace. Ci gaba da haka!")
            st.markdown("""
            **Shawarwarin Riƙewa:**
            - Ci gaba da motsa jiki.
            - Ci abinci mai daidaito.
            """)
        elif 25 <= bmi < 30:
            st.warning("Kana da nauyi fiye da kima.")
            st.markdown("""
            **Shawarwari:**
            - Rage cin abinci mai yawa da abin sha masu zaki.
            - Yi ayyukan motsa jiki kamar tafiya ko iyo.
            - Tuntuɓi kwararre don shawara ta musamman.
            """)
        else:
            st.error("Kana da nauyi sosai (obese).")
            st.markdown("""
            **Shawarwari:**
            - Fara cin abinci mai ƙananan kalori da wadatuwa.
            - Yi motsa jiki akalla mintuna 30 a kowace rana.
            - Nemi taimako daga ƙwararrun lafiya.
            """)

        # BMI Reference Table in Hausa
        st.markdown("""
        ### 📊 Teburin Ma'aunin BMI
        | Ma'auni (BMI)     | Matsayi           |
        |-------------------|--------------------|
        | Kasa da 18.5      | Ƙarancin nauyi     |
        | 18.5 – 24.9       | Nauyi na al'ada    |
        | 25.0 – 29.9       | Nauyi fiye da kima |
        | Sama da 30.0      | Nauyi sosai (obese)|
        """)

# Footer
st.markdown("© 2025 Nuhu Salim Ali. All rights reserved.")
