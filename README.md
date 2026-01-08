# Python_Programming_final_13
## 功能
- IC感應只有名單內的IC卡才可以感應成功
- IC感應後會將感應身份與感應時間通過Line傳送
- LCD顯示日期時間與刷卡是否成功
- 磁簧感應模組，當門開啟超過十秒，蜂鳴器會叫並同時在Line傳訊息提示
- 可以透過在Line傳訊息得到一組限時一分鐘的臨時通行QR code，掃描後可以開門
- 可以透過在Line傳信息，讓樹莓派發送系統紀錄最近十次的門磁感應、QR code、開啟門超過10秒的紀錄
## 安裝方式
- ```bash
- git clone https://github.com/Yojhu/Python_program_final_13.git
- cd Python_program_final_13
- pip install -r requirements.txt
## 執行如何
