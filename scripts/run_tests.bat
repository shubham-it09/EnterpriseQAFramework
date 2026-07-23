@echo off
setlocal

:: ------------------------------------------------------------
:: Validate Input
:: ------------------------------------------------------------

if "%~1"=="" (
    echo.
    echo [ERROR] No test path provided.
    echo.
    echo Usage:
    echo     run_tests.bat tests
    echo     run_tests.bat api/tests
    exit /b 1
)

:: ------------------------------------------------------------
:: Project Root
:: ------------------------------------------------------------

:: ------------------------------------------------------------
:: Configure Playwright Browser Location
:: ------------------------------------------------------------

set PLAYWRIGHT_BROWSERS_PATH=%CD%\browsers

echo.
echo [INFO] Playwright Browser Path:
echo %PLAYWRIGHT_BROWSERS_PATH%
echo.

:: ------------------------------------------------------------
:: Activate Virtual Environment
:: ------------------------------------------------------------

echo.
echo [INFO] Activating Virtual Environment...

call .venv\Scripts\activate.bat

if errorlevel 1 (
    echo.
    echo [ERROR] Failed to activate virtual environment.
    exit /b 1
)

echo [SUCCESS] Virtual Environment Activated.
echo.

:: ------------------------------------------------------------
:: Execute Tests
:: ------------------------------------------------------------

echo [INFO] Running Tests...
echo.

pytest %*

:: Save pytest exit code
set TEST_EXIT_CODE=%ERRORLEVEL%

echo.
if %TEST_EXIT_CODE% EQU 0 (
    echo [SUCCESS] Test Execution Completed.
) else (
    echo [WARNING] One or more tests failed.
)

:: Return original pytest exit code
endlocal & exit /b %TEST_EXIT_CODE%