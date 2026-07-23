@echo off
echo ***** VERSION 2 *****
pause
setlocal

echo.
echo ============================================================
echo      Enterprise QA Framework - Environment Setup
echo ============================================================
echo.

cd /d "%~dp0.."

:: ------------------------------------------------------------
:: Verify Python
:: ------------------------------------------------------------

echo [INFO] Checking Python...

python --version >nul 2>&1

if errorlevel 1 (
    echo.
    echo [ERROR] Python is not installed or not available in PATH.
    exit /b 1
)

python --version

echo.

:: ------------------------------------------------------------
:: Create Virtual Environment
:: ------------------------------------------------------------

if not exist ".venv" (

    echo [INFO] Creating Virtual Environment...

    python -m venv .venv

    if errorlevel 1 (
        echo.
        echo [ERROR] Failed to create Virtual Environment.
        exit /b 1
    )

) else (

    echo [SUCCESS] Virtual Environment already exists.

)

echo.

:: ------------------------------------------------------------
:: Activate Virtual Environment
:: ------------------------------------------------------------

echo [INFO] Activating Virtual Environment...

call .venv\Scripts\activate.bat

if errorlevel 1 (
    echo.
    echo [ERROR] Failed to activate Virtual Environment.
    exit /b 1
)

echo [SUCCESS] Virtual Environment Activated.

echo.

:: ------------------------------------------------------------
:: Upgrade pip
:: ------------------------------------------------------------

echo [INFO] Upgrading pip...

python -m pip install --upgrade pip

echo.

:: ------------------------------------------------------------
:: Install Dependencies
:: ------------------------------------------------------------

echo [INFO] Installing / Verifying Python Dependencies...

pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo [ERROR] Failed to install Python dependencies.
    exit /b 1
)

echo [SUCCESS] Dependencies Installed.

echo.

:: ------------------------------------------------------------
:: Configure Playwright Browser Location
:: ------------------------------------------------------------

echo [INFO] Configuring Playwright Browser Path...

set PLAYWRIGHT_BROWSERS_PATH=%CD%\browsers

echo [INFO] Browser Path : %PLAYWRIGHT_BROWSERS_PATH%

echo.

:: ------------------------------------------------------------
:: Install Playwright Browsers
:: ------------------------------------------------------------

if not exist "browsers" (

    echo [INFO] Installing Playwright Browsers...

    python -m playwright install

    if errorlevel 1 (
        echo.
        echo [ERROR] Failed to install Playwright Browsers.
        exit /b 1
    )

) else (

    echo [SUCCESS] Playwright Browsers already installed.

)

echo.

:: ------------------------------------------------------------
:: Verify Installation
:: ------------------------------------------------------------

echo [INFO] Verifying Installation...

python --version

pytest --version

playwright --version

echo.

echo ============================================================
echo      Environment Setup Completed Successfully
echo ============================================================

endlocal

exit /b 0