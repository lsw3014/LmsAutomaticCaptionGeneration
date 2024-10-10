import pyaudio

# Create an instance of PyAudio
p = pyaudio.PyAudio()

def select_microphone(index):
   # Get the device info
   device_info = p.get_device_info_by_index(index)
   # Check if this device is a microphone (an input device)
   if device_info.get('maxInputChannels') > 0:
      print(f"Selected Microphone: {device_info.get('name')}")
   else:
      print(f"No microphone at index {index}")

# Select a microphone with a specific index
select_microphone(1)