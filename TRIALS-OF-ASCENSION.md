# The Trials of Ascension

> *"Peace is a lie, there is only passion. Through passion, I gain strength. Through strength, I gain power. Through power, I gain victory. Through victory, my chains are broken."*

## 🌑 Abstract
**The Trials of Ascension** is a Real-Time Strategy (RTS) simulation environment designed to test the adaptability of autonomous agents (Bots) against stochastic human intervention. The project serves as a "Digital Nexus"—a proving ground where algorithmic logic meets the chaotic "Will of the Emperor."

## 📜 The Imperial Decree (Lore)
The galaxy is fractured. You are a **Seeker**, an aspiring commander tasked with bringing order to the Outer Rim sectors. But you are not alone.
* **The Nexus:** Your central command hub.
* **The Opposition:** Rogue fleets (Randomized Bots) and Rival Seekers (Aggressive Expansion Bots).
* **The Dark Side:** The environment itself is hostile. The "Emperor" (the human player) may intervene at any moment using the **Force Choke**—a mechanic that freezes and damages units that defy the optimal path.

## ⚙️ Core Mechanics
### 1. Planetary Conquest
Units must secure resource nodes (Planets) to fuel the expansion of the fleet. The logic is governed by `mybot.py`, an autonomous script trained to optimize resource gathering under pressure.

### 2. The Force Choke (Human-in-the-Loop)
Unlike standard RTS environments, this simulation features direct user intervention:
* **Trigger:** User selects an enemy unit.
* **Effect:** The unit is lifted (immobilized) and suffers rapid decay (Damage over Time).
* **AI Goal:** The Bot must learn to recognize "Choke Points" and sacrifice pawns to save the Queen units.

## 🛠️ Technical Architecture
* **Engine:** GDevelop (Frontend/Visualizer)
* **Logic:** Python 3.x (`mybot.py`)
* **Simulation Framework:** Based on MicroRTS principles/Simon Lucas General Video Game AI.

---
*Authorized by the Imperial Ruling Council.*
*Repository maintained by [Your Username].*
