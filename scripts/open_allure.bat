@echo off
setlocal

echo.
echo ============================================================
echo                Opening Allure Report
echo ============================================================
echo.

cd /d "%~dp0.."

allure serve artifacts\allure-results




endlocal


exit /b 0