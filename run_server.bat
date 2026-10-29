@echo off
title Jeevika S - Operating Systems Concepts Explainer Pack
cd /d "%~dp0"
echo ===============================================================
echo   Operating Systems Concepts Explainer Pack
echo   Candidate: Jeevika S  ^|  Topic #13
echo ===============================================================
echo Starting Python Flask Server on http://127.0.0.1:5000 ...
start http://127.0.0.1:5000
".venv\Scripts\python.exe" app.py
pause
