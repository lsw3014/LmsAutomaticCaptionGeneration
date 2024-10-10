# pyaudio test
import pyaudio

# pyaudio 객체 생성
p = pyaudio.PyAudio()

def select_microphone(index):
   # 기기 정보 불러오기
   device_info = p.get_device_info_by_index(index)
   
   # 입력 장치인지 확인
   if device_info.get('maxInputChannels') > 0:
      print(f"Selected Microphone: {device_info.get('name')}")
   else:
      print(f"No microphone at index {index}")

# 인덱스로 특정 입력 장치 선택
select_microphone(1)
