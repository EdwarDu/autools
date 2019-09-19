# NKT

## AOTF (Fianium_AOTF.py)
To communicate with AOTF device via AotfLibrary.dll (Windows Only).
Legacy AOTFLibrary (.dll, 32bit) is not possible to be directly loaded in 64bit Python environment.

So __msl-loadlib__ is used (Aotf32.py and Aotf64.py) to load the dll in a separated process.
This may cause problems if application is not cleanly exited.
__WARNING__: not fully tested.

## SC400 (FianiumSC400Man.py)
__WARNING__: not tested.
supports SC400 communication via RS232

## A203 (NKTMan_A203.py)
__WARNING__: not tested.

## Fianium (NKTMan_Fianium.py)
__WARNING__: not tested.