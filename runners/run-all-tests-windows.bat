@echo off

cd ".."
pytest "%CD%\tests" "--html=report.html" "--self-contained-html" "-v" "-m" "blockchain"