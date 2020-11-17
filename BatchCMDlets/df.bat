@echo off
dir %1 | find "Directory of" 
dir %1 /a:-d-h | find "/"
dir %1 /a:-d-h | find "File(s)"
