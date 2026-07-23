@echo off
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

) else (

    echo [INFO] Virtual Environment already exists.

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

echo.
echo [INFO] Checking Python Dependencies...

pip show pytest >nul 2>&1

if errorlevel 1 (

    echo [INFO] Installing Dependencies...

    pip install -r requirements.txt

) else (

    echo [SUCCESS] Dependencies already installed.

)

echo.

:: ------------------------------------------------------------
:: Install Playwright Browsers
:: ------------------------------------------------------------

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

    echo.
    echo [INFO] Installing Playwright Browsers...

    playwright install

) else (

    echo.
    echo [SUCCESS] Playwright Browsers already installed.

)

if errorlevel 1 (
    echo.
    echo [ERROR] Playwright browser installation failed.
    exit /b 1
)

echo [SUCCESS] Playwright Browsers Installed.

if errorlevel 1 (
    echo.
    echo [ERROR] Playwright browser installation failed.
    exit /b 1
)

echo [SUCCESS] Playwright Browsers Installed.

echo.

:: ------------------------------------------------------------
:: Verify Installation
:: ------------------------------------------------------------

echo [INFO] Verifying Installation...

pytest --version

playwright --version

echo.

echo ============================================================
echo      Environment Setup Completed Successfully
echo ============================================================

endlocal

exit /b 0