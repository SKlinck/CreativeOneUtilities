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
InstallPrompt=This process wll scan a USB in drive E: and attempt to repair errors and bad sectors. Ready to begin?
DisplayLicense=
FinishMessage=Thanks for using our USB repair tool. If you need further data recovery consider contacting an IT professional. 
TargetName=C:\Users\swkli\OneDrive\Desktop\C1ScriptsFixes\scripts\chkdskusb.EXE
FriendlyName=Check & Fix USB (E:)
AppLaunched=cmd /c chkdskusb.bat
PostInstallCmd=<None>
AdminQuietInstCmd=
UserQuietInstCmd=
FILE0="chkdskusb.bat"
[SourceFiles]
SourceFiles0=C:\Users\swkli\OneDrive\Desktop\C1ScriptsFixes\scripts\
[SourceFiles0]
%FILE0%=
