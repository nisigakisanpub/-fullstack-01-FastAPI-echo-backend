pip install fastapi uvicorn

uvicorn main:app --reload

�v���Z�X�m�F�iWindows�j
Get-Process | Where-Object { $_.ProcessName -like "uvicorn*" }
�X���b�h�m�F�iWindows�j
(Get-Process -Name "uvicorn").THreads.Count

