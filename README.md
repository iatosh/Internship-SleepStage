# 東京農工大学 田中聡久研究室インターン 
機械学習による睡眠ステージの推定

## 行ったこと

1. MNE-Python公式ドキュメントに記載されている手法で推定
2. 公式ドキュメントの手法をベースに、脳波の周波数バンドを調整して推定
3. YASA(自動で睡眠ステージの特定ができるPythonパッケージ)を用いて、EEGデータのみで推定
4. YASAを用いて、EEG、EOG、EMGの3つのデータで推定

## 結論

- EEGデータ1つのみの学習で、ランダムフォレストを用いて平均約60％以上の正解率を出すことができる
- EEGデータによって適する脳波の周波数バンドは異なる
- yasaを用いてEEG、EOG、EMGの3チャンネルで予測する方法の正解率の平均値が最も高い

## ipynbファイルへのリンク
[公式ドキュメントの手法](./get_hypnogram/Document.ipynb) (ヒプノグラムの表示)  
[公式ドキュメントの手法](./get_accuracy/Accuracy_document.ipynb) (複数データの正解率)  

[周波数バンド変更](./get_hypnogram/Document_Changed.ipynb) (ヒプノグラムの表示)  
[周波数バンド変更](./get_accuracy/Accuracy_document_changed.ipynb) (複数データの正解率)  

[YASA 1Channel](./get_hypnogram/YASA_1Ch.ipynb) (ヒプノグラムの表示)  
[YASA 1Channel](./get_accuracy/Accuracy_yasa_3Ch.ipynb) (複数データの正解率)  

[YASA 3Channel](./get_hypnogram/YASA_3Ch.ipynb) (ヒプノグラムの表示)  
[YASA 3Channel](./get_accuracy/Accuracy_yasa_3Ch.ipynb) (複数データの正解率)  
