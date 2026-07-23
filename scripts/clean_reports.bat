@echo off
setlocal

echo.
echo ============================================================
echo              Cleaning Previous Execution
echo ============================================================
echo.

cd /d "%~dp0.."

if exist artifacts (
    echo [INFO] Removing artifacts folder...
    rmdir /s /q artifacts
)

mkdir artifacts

mkdir artifacts\allure-results

echo.
echo [SUCCESS] Previous execution cleaned.

endlocal

exit /b 0