# oop2-2025-04-G03
OOP2 第4回 演習

## 目的

10秒の音声を録音し、Whisper（MLX 版）で文字起こしして、上書きしないで保存する最小パイプラインをチーム開発で実装・共有する。

* * *

## リポジトリ構成

```
oop2-2025-04-GXX/
├─ README.md
```


* * *

## 実行に必要なもの

### 必須ツール

* **Python** 3.10 以上推奨
    
* **FFmpeg**（実行ファイルが PATH にあること）
    
    * macOS: `brew install ffmpeg`
        

### 必須Pythonパッケージ

* `ffmpeg-python`（録音に使用）
    
* `pydub`（音声の読み込み・変換）
    
* `numpy`
    
* `mlx-whisper`（Apple Silicon で軽快に動く Whipser 実装）
    

`requirements.txt`
* * *

## セットアップ（初回のみ）

```bash
# リポジトリ取得
git clone https://github.com/<ORG>/oop2-2025-04-GXX.git
cd oop2-2025-04-GXX

# 仮想環境（任意）
python -m venv .venv
# mac/Linux
source .venv/bin/activate
# Windows
# .venv\Scripts\activate

# 依存インストール
pip install -r requirements.txt
```

FFmpeg が入っているか確認：

```bash
ffmpeg -version
```

* * *

## 実行手順

### 10秒録音だけ試す




## 出力例（保存形式）

