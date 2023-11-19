"""
【作成中】
食品の成分表示の画像からエネルギーと三大栄養素を取得する
"""
from PIL import Image
import pytesseract
import re

class Nutrient:
    def __init__(self, name, content):
        self.name = name  # 栄養素の名前
        self.content = content  # 栄養素の含有量

    def __repr__(self):
        return f"Nutrient(name='{self.name}', content={self.content})"

def is_energy(key, value):
    print(f'key: {key}')
    queries = ["エネルギー", "熱量", "エネ", "ルギ", "熱"]
    if any(query in key for query in queries):
        return True, "エネルギー"
    if "kcal" in value.lower():
        return True, "エネルギー"
    return False, key

def is_protein(key):
    if any(substr in key for substr in ["たんぱく質", "タンパク質", "蛋白質"]):
        return True, "たんぱく質"
    if len(re.findall(r"[たんぱくタンパク蛋白]", key)) >= 2:
        return True, "たんぱく質"
    return False, key

def is_fat(key):
    if "脂質" in key or "脂" in key:
        return True, "脂質"
    return False, key

def is_carbohydrates(key):
    if len(re.findall(r"[炭水化物]", key)) >= 2:
        return True, "炭水化物"
    return False, key

def extract_nutrients(file_path):
    # 画像を読み込む
    image = Image.open(file_path)

    # Tesseractを使って画像内のテキストを抽出する
    text = pytesseract.image_to_string(image, lang='jpn')

    return text

def normalize_text(text):
    # スペースと改行を削除
    text = text.replace(" ", "").replace("\n", "")
    print(f'スペースを削除した文字列: {text}')
    pattern = r"(\D+?)(\d+\.?\d*|[①-⑨]+\.?[①-⑨]*)([gkcal]+)|(\D+?)(\d+\.?\d*|[①-⑨]+\.?[①-⑨]*)(?![gkcal])"
    items = re.findall(pattern, text)

     # 辞書を作成
    nutrients = {}
    for item in items:
        if len(item) == 6:  # 単位が存在しないケース
            key, value, unit = item[3], item[4], ''
        else:  # 単位が存在するケース
            key, value, unit = item[0], item[1], item[2]

        key = key.rstrip('/')

        # 特殊文字列を半角数字に変換
        value = re.sub(r"[\①-\⑨]", lambda x: str(ord(x.group(0)) - ord('①') + 1), value)
        value = re.sub(r"[０-９]", lambda x: str(ord(x.group(0)) - ord('０')), value)

        if unit:
            value += unit

        # 各栄養素の判定
        energy_check, new_key = is_energy(key, value)
        if energy_check:
            nutrients[new_key] = value
            continue

        protein_check, new_key = is_protein(key)
        if protein_check:
            nutrients[new_key] = value
            continue

        fat_check, new_key = is_fat(key)
        if fat_check:
            nutrients[new_key] = value
            continue

        carb_check, new_key = is_carbohydrates(key)
        if carb_check:
            nutrients[new_key] = value
            continue
            
    print(f'nutrients:{nutrients}')

    # 不要なレコードの削除
    nutrients = {k: v for k, v in nutrients.items() if k in ["エネルギー", "たんぱく質", "脂質", "炭水化物"]}

    # Nutrientインスタンスの作成
    nutrient_objects = [Nutrient(name=k, content=v) for k, v in nutrients.items()]

    return nutrient_objects

def create_nutrients_list():
    # ファイル名
    file_name = 'test_10.jpg'

    # extract_nutrients 関数を実行して結果を取得
    extracted_text = extract_nutrients(file_name)

    # normalize_text 関数を実行してテキストを正規化
    normalized_nutrients = normalize_text(extracted_text)

    # 結果を表示
    for nutrient in normalized_nutrients:
        print(nutrient)

if __name__ == "__main__":
    print(f'実行開始')
    create_nutrients_list()
    print(f'実行終了')
