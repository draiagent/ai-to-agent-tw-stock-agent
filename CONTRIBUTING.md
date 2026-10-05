# 貢獻規範

修訂前先確認本 Repo 為 VAC 與教材，程式變更請到 ai-stock-skill 提案。說明修改原因、影響步驟與證據，保留原作者與素材聲明。

不得提交金鑰、客戶持倉、帳戶資訊或未確認可公開的行情原件。驗收須區分使用者回報、本輪實測與模擬測試。

任何發布檔案改動後，先審查差異，再執行 `python scripts/checksums.py build` 及 `python scripts/checksums.py verify`，重新封裝 ZIP；不要手改單一 hash 掩蓋問題。
