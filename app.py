import streamlit as st
import pyttsx3

def main():
    st.title("Text-to-Speech App")
    st.subheader("Convert Text to Speech with Custom Options")

    # Text Input
    text = st.text_area("Enter Text to Speak", placeholder="Type something here...")

    # Initialize pyttsx3 engine locally
    engine = pyttsx3.init()

    # Voice Selection
    voices = engine.getProperty('voices')
    voice_options = [voice.name for voice in voices]
    selected_voice = st.selectbox("Select Voice", voice_options)

    # Set the selected voice
    selected_voice_id = [voice.id for voice in voices if voice.name == selected_voice][0]
    engine.setProperty('voice', selected_voice_id)

    # Speech Rate
    rate = engine.getProperty('rate')
    new_rate = st.slider("Speech Rate (words per minute)", min_value=50, max_value=300, value=rate)
    engine.setProperty('rate', new_rate)

    # Volume Control
    volume = engine.getProperty('volume')
    new_volume = st.slider("Volume", min_value=0.0, max_value=1.0, value=volume)
    engine.setProperty('volume', new_volume)

    # Speak Button
    if st.button("Speak"):
        if text.strip():
            engine.say(text)
            engine.runAndWait()
        else:
            st.warning("Please enter text to speak.")

    # Save Audio Button
    if st.button("Save as Audio File"):
        if text.strip():
            filename = st.text_input("Enter Filename (e.g., output.mp3):", "output.mp3")
            if filename:
                engine.save_to_file(text, filename)
                engine.runAndWait()
                engine.stop()
                st.success(f"Audio saved as {filename}")
            else:
                st.warning("Please enter a valid filename.")
        else:
            st.warning("Please enter text to save.")

    st.markdown("---")
    st.markdown("Developed with 💻 and 🎙️ using Streamlit and pyttsx3.")

if __name__ == "__main__":
    main()
