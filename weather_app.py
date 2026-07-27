import streamlit as st
import requests

# -----------------------------
# PAGE SETTINGS
# -----------------------------
st.set_page_config(
    page_title="Weather Forecast",
    page_icon="🌤",
    layout="centered"
)

# -----------------------------
# YOUR API KEY
# -----------------------------
API_KEY = "7572b607ae73ba103b6c95c9aa2eb928"

# -----------------------------
# TITLE
# -----------------------------
st.title("🌤 Live Weather Forecast")

st.write("Search the weather of any city.")

city = st.text_input("Enter City Name")

if st.button("Get Weather"):

    if city.strip() == "":
        st.warning("Please enter a city name.")

    else:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        try:

            response = requests.get(url)

            data = response.json()

            # Uncomment this line if you want to see exactly what the API returns
             st.write(data)

            if response.status_code == 200:

                st.success("Weather Loaded Successfully")

                st.subheader(f"📍 {data['name']}, {data['sys']['country']}")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("🌡 Temperature", f"{data['main']['temp']} °C")

                with col2:
                    st.metric("🤗 Feels Like", f"{data['main']['feels_like']} °C")

                col3, col4 = st.columns(2)

                with col3:
                    st.metric("💧 Humidity", f"{data['main']['humidity']} %")

                with col4:
                    st.metric("💨 Wind Speed", f"{data['wind']['speed']} m/s")

                st.info("☁ " + data["weather"][0]["description"].title())

            else:
                st.error(data.get("message", "City not found"))

        except Exception as e:
            st.error(f"Error: {e}")