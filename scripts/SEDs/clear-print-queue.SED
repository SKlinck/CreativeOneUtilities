[Version]
Class=IEXPRESS
SEDVersion=3
[Options]
PackagePurpose=InstallApp
ShowInstallProgramWindow=2
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
InstallPrompt=Reboot your PCs print services?
DisplayLicense=
FinishMessage=All Done! Please see if you are now able to print.
TargetName=C:\Users\swkli\OneDrive\Desktop\C1ScriptsFixes\scripts\clear-print-queue.exe
FriendlyName=Clear Print Queue
AppLaunched=cmd /c clear-print-queue.bat
PostInstallCmd=<None>
AdminQuietInstCmd=
UserQuietInstCmd=
FILE0="clear-print-queue.bat"
[SourceFiles]
SourceFiles0=C:\Users\swkli\OneDrive\Desktop\C1ScriptsFixes\scripts\
[SourceFiles0]
%FILE0%=
