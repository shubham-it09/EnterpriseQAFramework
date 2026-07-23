@echo off
setlocal

:: ------------------------------------------------------------
:: Validate Input
:: ------------------------------------------------------------

if "%~1"=="" goto usage

echo.
echo ============================================================
echo        Enterprise QA Framework Pipeline
echo ============================================================
echo.

:: ------------------------------------------------------------
:: Clean Previous Execution
:: ------------------------------------------------------------

call "%~dp0clean_reports.bat"

:: ------------------------------------------------------------
:: Initialize Pipeline Exit Code
:: ------------------------------------------------------------

set PIPELINE_EXIT_CODE=0

:: ------------------------------------------------------------
:: Execute Requested Suite
:: ------------------------------------------------------------

if /I "%~1"=="ui" goto ui
if /I "%~1"=="api" goto api
if /I "%~1"=="all" goto all

goto invalid


:ui

echo.
echo [INFO] Running UI Test Suite...

call "%~dp0run_tests.bat" tests

set PIPELINE_EXIT_CODE=%ERRORLEVEL%

goto report


:api

echo.
echo [INFO] Running API Test Suite...

call "%~dp0run_tests.bat" api/tests

set PIPELINE_EXIT_CODE=%ERRORLEVEL%

goto report


:all

echo.
echo [INFO] Running Complete Test Suite...

call "%~dp0run_tests.bat" tests

if errorlevel 1 set PIPELINE_EXIT_CODE=1

call "%~dp0run_tests.bat" api/tests

if errorlevel 1 set PIPELINE_EXIT_CODE=1

goto report


:report

echo.
echo ============================================================
echo             Finalizing Execution
echo ============================================================
echo.

:: Skip opening report in Jenkins
if /I "%~2"=="jenkins" (

    echo [INFO] Jenkins Execution Detected.
    echo [INFO] Skipping Allure UI.

) else (

    echo [INFO] Local Execution Detected.
    call "%~dp0open_allure.bat"

)

echo.
echo ============================================================
echo             Pipeline Execution Completed
echo ============================================================

exit /b %PIPELINE_EXIT_CODE%




:usage

echo.
echo Usage:
echo.
echo     run_framework.bat ui
echo     run_framework.bat api
echo     run_framework.bat all
echo.

exit /b 1


:invalid

echo.
echo Invalid execution type.
echo.
echo Valid options:
echo.
echo     ui
echo     api
echo     all
echo.

exit /b 1