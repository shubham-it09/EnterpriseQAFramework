@echo off
setlocal

echo.
echo ============================================================
echo               Generating Allure Report
echo ============================================================
echo.

cd /d "%~dp0.."

allure generate artifacts\allure-results --clean -o artifacts\allure-report

if errorlevel 1 (

    echo.
    echo [ERROR] Failed to generate Allure Report.

    exit /b 1
)

echo.
echo [SUCCESS] Allure Report Generated.

endlocal

exit /b 0