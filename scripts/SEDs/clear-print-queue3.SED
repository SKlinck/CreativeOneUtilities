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
InstallPrompt=Click "OK" to restart your print services.
DisplayLicense=
FinishMessage=Thank you for waiting! Please try printing again. 
TargetName=C:\Users\swkli\OneDrive\Desktop\C1ScriptsFixes\scripts\clear-print-queue3.exe
FriendlyName=Restart Print Services
AppLaunched=cmd /c clear-print-queue.bat
PostInstallCmd=<None>
AdminQuietInstCmd=
UserQuietInstCmd=
FILE0="clear-print-queue.bat"
[SourceFiles]
SourceFiles0=C:\Users\swkli\OneDrive\Desktop\C1ScriptsFixes\scripts\
[SourceFiles0]
%FILE0%=
