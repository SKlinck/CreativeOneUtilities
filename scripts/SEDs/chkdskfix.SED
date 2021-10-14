[Version]
Class=IEXPRESS
SEDVersion=3
[Options]
PackagePurpose=InstallApp
ShowInstallProgramWindow=0
HideExtractAnimation=0
UseLongFileName=1
InsideCompressed=0
CAB_FixedSize=0
CAB_ResvCodeSigning=0
RebootMode=N
InstallPrompt=%InstallPrompt%
DisplayLicense=%DisplayLicense%
FinishMessage=%FinishMessage%
TargetName=%TargetName%
FriendlyName=%FriendlyName%
AppLaunched=%AppLaunched%
PostInstallCmd=%PostInstallCmd%
AdminQuietInstCmd=%AdminQuietInstCmd%
UserQuietInstCmd=%UserQuietInstCmd%
SourceFiles=SourceFiles
[Strings]
InstallPrompt=Press "OK" to schedule a scan of your disk that checks for errors and bad data sectors. Afterwards, reboot your system to begin the process. If errors or bad data sectors are found the process will attempt to automatically repair them. On the pop-up screen press "Y" and then "Enter" or "Return" to schedule the process. NOTE: Once the process has been scheduled, restart your computer system to begin. Are you ready to begin?
DisplayLicense=
FinishMessage=Thanks for running our disk check and repair service. If you still have an issue contact IT support.
TargetName=C:\Users\swkli\OneDrive\Desktop\C1ScriptsFixes\scripts\chkdskfix.EXE
FriendlyName=Check & Fix Disk
AppLaunched=cmd /c chkdskfix.bat
PostInstallCmd=<None>
AdminQuietInstCmd=
UserQuietInstCmd=
FILE0="chkdskfix.bat"
[SourceFiles]
SourceFiles0=C:\Users\swkli\OneDrive\Desktop\C1ScriptsFixes\scripts\
[SourceFiles0]
%FILE0%=
