# 🎮 Magic & Knights: Medieval Combats

## Game Overview｜遊戲介紹
A 2D fighting game where two players engage in a one-on-one battle using different characters.  
Players must utilize precise controls and strategic thinking to defeat their opponent.

本遊戲為一款 **雙人對戰格鬥遊戲**，玩家可選擇不同角色進行 1v1 戰鬥，直到其中一方被擊敗。  
遊戲強調 **操作技巧與策略運用**，玩家需透過精準控制與戰術來取得勝利。

## System Design｜系統設計
The game consists of two main phases: **Character Selection** and **Battle**.  
Players first review instructions and character abilities, then choose their characters and enter combat.

遊戲主要分為兩大部分：**選角階段**與**對戰階段**。  
玩家先於開始畫面閱讀操作說明與角色能力，接著選擇角色並進入戰鬥。  

# Game Screens｜遊戲畫面

## 1. Start Screen｜開始畫面

<img width="997" height="625" alt="Start Screen" src="https://github.com/user-attachments/assets/5253c3e1-39e6-400e-ad64-6a37be6c341d" />


## 2. Character Selection｜選角畫面

<div align="center">
  <img src="https://github.com/user-attachments/assets/fb17c082-2a9e-4ce9-a70d-c42b999a59c2" width="45%">
  <img src="https://github.com/user-attachments/assets/dd357f83-c228-45ab-85b8-dc87bf91f4e3" width="45%">
</div>


> Each character has different attribute values, which are visualized using a radar chart displayed on the right side of the screen. The character selection progress is shown at the top-left corner.  
> 各角色有不同能力數值，雷達圖顯示於畫面右方。選角進度則顯示於畫面左上方。


## 3. Battle Scene｜對戰畫面

### Gameplay Mechanics｜操作與戰鬥系統

- **Movement｜移動**
  - Forward / Backward / Jump  
  - 前進／後退／跳躍（含重力效果）

- **Combat｜攻擊系統**
  - Basic Attack（普攻）  
    - No requirement  
    - Builds mana  
    - 無條件施放，並累積魔力（被攻擊者累積較多）

  - Ultimate Skill（大絕）  
    - Requires full mana  
    - High damage  
    - 需魔力累積滿才可施放，傷害較高

<div align="center">
  <img src="https://github.com/user-attachments/assets/617d8fc8-aa09-4d69-be6e-ca5222eab80f" width="45%">
  <img src="https://github.com/user-attachments/assets/617d8fc8-aa09-4d69-be6e-ca5222eab80f" width="45%">
</div>


> The health bar is displayed at the top of the screen. When the mana bar is fully charged, it turns light blue. After using the ultimate skill, it resets and begins accumulating again.  
> 血條顯示於畫面上方。魔力累積完成顯示淺藍，使用大絕後歸零重計。


## 4. End Screen｜結束畫面

<div align="center">
  <img src="(https://github.com/user-attachments/assets/7960dfb3-79f0-4c0c-8ed7-11989f6a2afd)" width="45%">
  <img src="(https://github.com/user-attachments/assets/c95de713-39a9-4658-b1a3-f09eab153799)" width="45%">
</div>

  
> At the end of each match, players are prompted to choose whether to play again, and the win record is tracked and carried over to the next round.  
> 結束畫面詢問再戰意願，並累積勝負。勝負累計至下局。


## Documentation｜說明文件
-  Please refer to the project manual for detailed design  
-  詳見專案說明手冊
