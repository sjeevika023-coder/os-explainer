# Operating Systems Concepts Explainer Pack

**Academic Project Topic :OS Explainer**  
**Candidate:** Jeevika S  

---

## 📌 Project Overview
The **Operating Systems Concepts Explainer Pack** is an interactive, vibrant, and professional web platform built to demonstrate and visualize fundamental Operating Systems algorithms and theoretical concepts.

It bridges theoretical textbook computer science with interactive simulations, step-by-step mathematical execution traces, and visual graph animations.

---

## ✨ Features & Modules

### 1. ⚡ CPU Scheduling Simulator & Visualizer
- **Supported Algorithms:**
  - First-Come, First-Served (FCFS)
  - Shortest Job First (SJF - Non-preemptive)
  - Shortest Remaining Time First (SRTF - Preemptive)
  - Round Robin (RR) with configurable time quantum
  - Priority Scheduling (Preemptive & Non-preemptive)
- **Features:** Dynamic process addition/deletion, interactive Gantt chart, metrics table (CT, TAT, WT, RT), Average TAT, Average WT, CPU Utilization %, and Throughput calculation.

### 2. 🛡️ Deadlock Avoidance (Banker's Algorithm)
- Multi-resource safety algorithm (Resources A, B, C).
- Interactive Allocation Matrix, Max Claim Matrix, and dynamically calculated Need Matrix.
- Safe execution sequence finder with animated badges.
- Step-by-step verification trace for every process evaluation.
- Live Resource-Request evaluation tester.

### 3. 📑 Virtual Memory & Page Replacement Visualizer
- **Supported Algorithms:**
  - First-In, First-Out (FIFO)
  - Least Recently Used (LRU)
  - Belady's Optimal (OPT)
- **Features:** Configurable frames (3 to 5), step-by-step frame matrix tracking, Hit vs Miss tags, Hit/Fault ratios, and Belady's Anomaly comparative benchmark.

### 4. 💽 Disk Arm Scheduling Simulator
- **Supported Algorithms:**
  - SCAN (Elevator Algorithm)
  - C-SCAN (Circular SCAN)
  - LOOK & C-LOOK
  - SSTF (Shortest Seek Time First)
  - FCFS
- **Features:** Canvas 2D seek trajectory plotting with neon glow lines, step traversal log, total cylinder head movement, and average seek length.

### 5. 🔄 Process Synchronization & Concurrency Sandbox
- **Producer-Consumer Problem:** Bounded circular buffer with binary Mutex and counting Semaphores (`empty`, `full`).
- **Dining Philosophers Problem:** Circular table with 5 philosophers and 5 forks, demonstrating state transitions (Thinking, Hungry, Eating), deadlock scenarios (Circular Wait), and solutions.
- Live concurrency event log console.

### 6. 🏛️ Core Concepts Hub
- User Mode vs Kernel Mode & Traps/System Calls
- Process Control Block (PCB) structure & Lifecycle
- Coffman's 4 Deadlock Conditions
- Paging, Page Tables, & TLB Address Translation
- Thrashing & Locality Principle
- Unix Inode & File System Structures

### 7. 🎯 Interactive OS Knowledge Quiz & Cheatsheet
- 10 high-yield questions with instant explanations and score tracker.
- Certificate of Completion generator.
- Quick reference formulas and cheat sheet.

---

## 🚀 How to Run the Application

### Option A: Quick Launch (Recommended)
Double-click `run_server.bat` in the project directory. It will open `http://127.0.0.1:5000` in your web browser and launch the Python Flask server.

### Option B: Command Line (PowerShell)
```powershell
cd C:\Users\sjeev\.gemini\antigravity\scratch\jeevika_os_explainer
.\.venv\Scripts\python.exe app.py
```
Then navigate to `http://127.0.0.1:5000` or `http://localhost:5000`.

---

## 🌐 REST API Endpoints
- `POST /api/cpu-scheduling` - Calculate CPU schedule and Gantt chart
- `POST /api/bankers-algorithm` - Evaluate system safety state
- `POST /api/bankers-request` - Test individual resource allocation request
- `POST /api/page-replacement` - Compute page replacement frame matrix
- `POST /api/disk-scheduling` - Calculate disk seek trajectory
- `GET /api/quiz` - Fetch OS quiz questions and explanations
- `GET /api/cheatsheet` - Fetch OS formulas and summary topics
- `GET /api/health` - Health check status
