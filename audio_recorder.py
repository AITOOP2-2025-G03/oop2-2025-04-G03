# audio_recorder.py
import ffmpeg

class AudioRecorder:
    """FFmpegで音声を録音してWAV保存する超シンプルなクラス。"""
    def __init__(self, backend='avfoundation', input_spec=':0', samplerate=16000, channels=1):
        self.backend = backend        # mac: 'avfoundation', Win: 'dshow', Linux: 'pulse'/'alsa'
        self.input_spec = input_spec  # 例) mac ':0' / Win 'audio=マイク名' / Linux 'default'
        self.samplerate = samplerate
        self.channels = channels

    def record(self, filename='python-audio-output.wav', duration=10, overwrite=True):
        """duration秒録音してfilenameに保存。"""
        try:
            print(f"{duration}秒間、マイクからの録音を開始します...")
            (
                ffmpeg
                .input(self.input_spec, format=self.backend, t=duration)
                .output(filename, acodec='pcm_s16le', ar=self.samplerate, ac=self.channels)
                .run(overwrite_output=overwrite)
            )
            print(f"録音が完了しました。{filename} に保存されました。")
        except ffmpeg.Error as e:
            print(f"エラーが発生しました: {e.stderr.decode(errors='ignore')}")
        except Exception as e:
            print(f"予期せぬエラー: {e}")
            
if __name__ == "__main__":
    # macの例（:0）。必要に応じて backend / input_spec を変えるだけ。
    AudioRecorder(backend='avfoundation', input_spec=':0').record()