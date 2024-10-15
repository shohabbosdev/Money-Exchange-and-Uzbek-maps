import streamlit as st
import requests
st.title("💸 Valyuta ayriboshlash")
manzil = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"

response = requests.post(manzil)
data = {}
st.write(f"📅 Sana: <code>{response.json()[0]['Date']}-yil</code> <hr/>",unsafe_allow_html=True)
miqdor = st.number_input("So'm miqdoridagi qiymat kiriting", min_value=0, max_value=300_000_000, step=1)
# hisoblash = st.write_stream(miqdor)

def getValue():
    try:
        for i in range(4):
            nomlanishi = response.json()[i]['CcyNm_UZ']
            dollar = float(response.json()[i]['Rate'])
            symbols = response.json()[i]['Ccy']

            data[f"💵{nomlanishi}"] = {
                "Joriy kurs": f"{dollar:.2f} so'm",
                f'💰10': f"{10*dollar:.2f} so'm",
                f'💰15': f"{15*dollar:.2f} so'm",
                f'💰200': f"{200*dollar:.2f} so'm",
                f"{miqdor} so'm": f"{miqdor/dollar:.4f} {symbols}"
            }
            # st.write(f"""
            #         📛 Nomlanishi: <span style='color:red; text-decoration: underline;'>{nomlanishi}</span><br />
            #         💵 Kurs narxi: <code>{dollar} so'm<br />
            #         1️⃣0️⃣ {nomlanishi} = {10*dollar:.2f} so'm bo'ladi <br />
            #         1️⃣5️⃣ {nomlanishi} = {15*dollar:.2f} so'm bo'ladi <br />
            #         2️⃣0️⃣0️⃣ {nomlanishi} = {200*dollar:.2f} so'm bo'ladi
            #         </code><hr />
            #         """,unsafe_allow_html=True)
        return data
    except Exception as e:
        st.error(f"Xatolik: {e}")
st.table(getValue())