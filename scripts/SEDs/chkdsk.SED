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
InstallPrompt=Press "OK" to scan the disk for errors.
DisplayLicense=
FinishMessage=Thanks for using our disk checker tool. If disk errors were found, your PC may be at risk of data loss.
TargetName=C:\Users\swkli\OneDrive\Desktop\C1ScriptsFixes\scripts\chkdsk.exe
FriendlyName=Check Disk
AppLaunched=cmd /c chkdsk.bat
PostInstallCmd=<None>
AdminQuietInstCmd=
UserQuietInstCmd=
FILE0="chkdsk.bat"
[SourceFiles]
SourceFiles0=C:\Users\swkli\OneDrive\Desktop\C1ScriptsFixes\scripts\
[SourceFiles0]
%FILE0%=
