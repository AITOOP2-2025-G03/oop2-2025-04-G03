# ファイル名: audio_recorder.py
"""
audio_recorder.py

10秒間音声を録音し、WAVファイルとして保存するためのモジュール。
他のプログラムから簡単に利用できるように設計されています。

使用例:
    from audio_recorder import AudioRecorder
    recorder = AudioRecorder()
    recorder.record_audio("recordings/sample.wav")

依存ライブラリ:
    - sounddevice
    - scipy
"""

import os
import sounddevice as sd
from scipy.io.wavfile import write

class AudioRecorder:
    """音声を録音し、指定したファイルに保存するクラス。"""

    def __init__(self, duration: int = 10, samplerate: int = 44100):
        """
        AudioRecorderの初期化。

        Args:
            duration (int): 録音時間（秒）. デフォルトは10秒.
            samplerate (int): サンプリングレート（Hz）. デフォルトは44100Hz.
        """
        self.duration = duration
        self.samplerate = samplerate

    def record_audio(self, filename: str = "recordings/record.wav") -> None:
        """
        音声を録音し、指定したパスにWAVファイルとして保存する。

        Args:
            filename (str): 保存先ファイルパス.
        """
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        print(f"🎙 録音を開始します（{self.duration}秒間）...")

        # 録音処理
        audio_data = sd.rec(int(self.duration * self.samplerate),
                            samplerate=self.samplerate,
                            channels=1, dtype='int16')
        sd.wait()

        # 保存処理
        write(filename, self.samplerate, audio_data)
        print(f"✅ 録音完了: {filename}")
