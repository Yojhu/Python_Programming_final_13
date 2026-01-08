# Python_Programming_final_13
## 功能
- IC感應只有名單內的IC卡才可以感應成功
- IC感應後會將感應身份與感應時間通過Line傳送
- LCD顯示日期時間與刷卡是否成功
- 磁簧感應模組，當門開啟超過十秒，蜂鳴器會叫並同時在Line傳訊息提示
- 可以透過在Line傳訊息得到一組限時一分鐘的臨時通行QR code，掃描後可以開門
- 可以透過在Line傳信息，讓樹莓派發送系統紀錄最近十次的門磁感應、QR code、開啟門超過10秒的紀錄
- youtube介紹影片連結:https://youtu.be/JU0dbNAvn0c
## 安裝方式
- ```bash
  git clone https://github.com/Yojhu/Python_Program_final_13.git
  cd Python_program_final_13
  pip install -r requirements.txt
## 如何執行
- 在line_env檔案夾中的QR.py的第134行 pi_ip =""中空改為當前樹莓派主機區域網路IP
- 在line_env檔案夾中的.env的 LINE_CHANNEL_ACCESS_TOKEN \ LINE_CHANNEL_SECRET \ LINE_USER_ID 改成自己的
- 使用ngrok服務
- 執行test.py
- 在樹莓派主機執行
- sudo snap install ngrok
- ngrok config add-authtoken abc (abc為agrok網站上的authtoken)
- ngrok http 5000
