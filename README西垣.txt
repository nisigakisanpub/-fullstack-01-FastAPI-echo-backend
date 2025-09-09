pip install fastapi uvicorn

uvicorn main:app --reload

プロセス確認（Windows）
Get-Process | Where-Object { $_.ProcessName -like "uvicorn*" }
スレッド確認（Windows）
(Get-Process -Name "uvicorn").THreads.Count

