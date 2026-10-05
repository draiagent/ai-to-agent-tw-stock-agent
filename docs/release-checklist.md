# 發布檢查與 README 雜湊修正

雜湊只證明檔案位元組與紀錄是否一致，不證明測試成功或資料真實。

原 ai-stock-skill 的修正流程：取得地端修正檔及測試 commit → 比對 README 差異 → 確認變更合理且無遺漏 → 在該 Repo 對全部交付檔重建雜湊 → 驗證 → 重新封裝並再驗證。原失敗紀錄應保留，另記修正後結果。

本教材 Repo 使用：

```bash
python scripts/checksums.py build
python scripts/checksums.py verify
```

清單涵蓋全部交付檔（排除清單自己、.git、__pycache__）。新增、刪除、改動都會被檢出。請在所有文件定稿後建清單，不可在通過後又修改 README。

發布前核對：版本、圖片可讀、相對連結、完整署名、授權範圍、未驗證項目及 GitHub 目標。封裝後解壓到新目錄，執行同一 verify 命令。
