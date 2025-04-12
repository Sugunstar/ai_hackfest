from pydub import AudioSegment
import os

# Set your folder path
folder_path = "C:/Users/pc/MUSDB18/MUSDB18-7/test" 

# Loop through the files
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".mp4"):  # Only process .mp4 files
        file_path = os.path.join(folder_path, filename)
        print(f"🎬 Processing video: {filename}")

        try:
            # Convert video file to audio using pydub
            audio = AudioSegment.from_file(file_path, format="mp4")
            audio_path = file_path.replace(".mp4", ".wav")
            audio.export(audio_path, format="wav")
            print(f"✅ Audio extracted and saved as {audio_path}")

            # Load the extracted audio with librosa
            import librosa
            audio_data, sr = librosa.load(audio_path, sr=22050)

            # Process the audio (e.g., Mel Spectrogram)
            mel_spectrogram = librosa.feature.melspectrogram(y=audio_data, sr=sr)
            log_mel = librosa.power_to_db(mel_spectrogram, ref=np.max)

            # Display the spectrogram
            import matplotlib.pyplot as plt
            plt.figure(figsize=(10, 4))
            librosa.display.specshow(log_mel, sr=sr, x_axis='time', y_axis='mel')
            plt.colorbar(format='%+2.0f dB')
            plt.title(f"Mel Spectrogram - {filename}")
            plt.tight_layout()
            plt.show()

        except Exception as e:
            print(f"❌ Failed to process {filename}: {e}")
