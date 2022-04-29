#include "atcore.h"
#include <iostream>
#include <wchar.h>

using namespace std;

FeatureCallback cb = NULL;

int AT_EXP_CONV AT_InitialiseLibrary(){
    cout << __FUNCTION__ << " called " << endl;
    return AT_SUCCESS;
}
int AT_EXP_CONV AT_FinaliseLibrary(){
    cout << __FUNCTION__ << " called " << endl;
    return AT_SUCCESS;
}

int AT_EXP_CONV AT_Open(int CameraIndex, AT_H *Hndl){
    cout << __FUNCTION__ << " called " << CameraIndex << endl;
    *Hndl = 0xAABB;
    return AT_SUCCESS;
}
int AT_EXP_CONV AT_OpenDevice(const AT_WC* Device, AT_H *Hndl){
    cout << __FUNCTION__ << " called " << Device << endl;
    *Hndl = 0xAABB;
    return AT_SUCCESS;
}

int AT_EXP_CONV AT_Close(AT_H Hndl){
    cout << __FUNCTION__ << " called " << Hndl << " " << endl;
    return AT_SUCCESS;
}

int AT_EXP_CONV AT_RegisterFeatureCallback(AT_H Hndl, const AT_WC* Feature, FeatureCallback EvCallback, void* Context){
	cout << __FUNCTION__ << " called " ; wcout << Feature ; cout << " " << endl;
    cb = EvCallback;
    return AT_SUCCESS;
}
int AT_EXP_CONV AT_UnregisterFeatureCallback(AT_H Hndl, const AT_WC* Feature, FeatureCallback EvCallback, void* Context){
	cout << __FUNCTION__ << " called " ; wcout << Feature ; cout << " " << endl;
    cb = NULL;
    return AT_SUCCESS;
}

int AT_EXP_CONV AT_IsImplemented(AT_H Hndl, const AT_WC* Feature, AT_BOOL* Implemented){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << endl;
    *Implemented = rand() % 2;
    cout << *Implemented << endl;
    return AT_SUCCESS;
}
int AT_EXP_CONV AT_IsReadable(AT_H Hndl, const AT_WC* Feature, AT_BOOL* Readable){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << endl;
    *Readable = rand() % 2;
    cout << *Readable << endl;
    return AT_SUCCESS;
}
int AT_EXP_CONV AT_IsWritable(AT_H Hndl, const AT_WC* Feature, AT_BOOL* Writable){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << endl;
    *Writable = rand() % 2;
    cout << *Writable << endl;
	return AT_SUCCESS;
}
int AT_EXP_CONV AT_IsReadOnly(AT_H Hndl, const AT_WC* Feature, AT_BOOL* ReadOnly){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << endl;
    *ReadOnly = rand() % 2;
    cout << *ReadOnly << endl;
	return AT_SUCCESS;
}

int AT_EXP_CONV AT_SetInt(AT_H Hndl, const AT_WC* Feature, AT_64 Value){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << Value << endl;
	return AT_SUCCESS;
}
int AT_EXP_CONV AT_GetInt(AT_H Hndl, const AT_WC* Feature, AT_64* Value){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << endl;
	if (wcscmp(Feature, L"DeviceCount") == 0)
	    *Value = 1;
	else
        *Value = rand();
    cout << *Value << endl;
	return AT_SUCCESS;
}
int AT_EXP_CONV AT_GetIntMax(AT_H Hndl, const AT_WC* Feature, AT_64* MaxValue){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << endl;
    *MaxValue = rand();
    cout << *MaxValue << endl;
	return AT_SUCCESS;
}
int AT_EXP_CONV AT_GetIntMin(AT_H Hndl, const AT_WC* Feature, AT_64* MinValue){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << endl;
    *MinValue = rand();
    cout << *MinValue << endl;
	return AT_SUCCESS;
}

int AT_EXP_CONV AT_SetFloat(AT_H Hndl, const AT_WC* Feature, double Value){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << Value << endl;
	return AT_SUCCESS;
}
int AT_EXP_CONV AT_GetFloat(AT_H Hndl, const AT_WC* Feature, double* Value){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << endl;
    *Value = rand() / 100.0f;
    cout << *Value << endl;
	return AT_SUCCESS;
}
int AT_EXP_CONV AT_GetFloatMax(AT_H Hndl, const AT_WC* Feature, double* MaxValue){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << endl;
    *MaxValue = rand() / 100.0f;
    cout << *MaxValue << endl;
	return AT_SUCCESS;
}
int AT_EXP_CONV AT_GetFloatMin(AT_H Hndl, const AT_WC* Feature, double* MinValue){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << endl;
    *MinValue = rand() / 100.0f;
    cout << *MinValue << endl;
	return AT_SUCCESS;
}

int AT_EXP_CONV AT_SetBool(AT_H Hndl, const AT_WC* Feature, AT_BOOL Value){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << Value << endl;
	return AT_SUCCESS;
}
int AT_EXP_CONV AT_GetBool(AT_H Hndl, const AT_WC* Feature, AT_BOOL* Value){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << endl;
    *Value = rand() % 2;
    cout << *Value << endl;
	return AT_SUCCESS;
}

int AT_EXP_CONV AT_SetEnumIndex(AT_H Hndl, const AT_WC* Feature, int Value){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << Value << endl;
	return AT_SUCCESS;
}
int AT_EXP_CONV AT_SetEnumString(AT_H Hndl, const AT_WC* Feature, const AT_WC* String){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature << " " << String << endl;
	return AT_SUCCESS;
}
int AT_EXP_CONV AT_GetEnumIndex(AT_H Hndl, const AT_WC* Feature, int* Value){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << endl;
    *Value = rand() % 5;
    cout << *Value << endl;
	return AT_SUCCESS;
}
int AT_EXP_CONV AT_GetEnumCount(AT_H Hndl,const  AT_WC* Feature, int* Count){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << endl;
    *Count = 5;
    cout << *Count << endl;
	return AT_SUCCESS;
}
int AT_EXP_CONV AT_IsEnumIndexAvailable(AT_H Hndl, const AT_WC* Feature, int Index, AT_BOOL* Available){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << endl;
    *Available = rand() % 2;
    cout << *Available << endl;
	return AT_SUCCESS;
}
int AT_EXP_CONV AT_IsEnumIndexImplemented(AT_H Hndl, const AT_WC* Feature, int Index, AT_BOOL* Implemented){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << endl;
    *Implemented = rand() % 2;
    cout << *Implemented << endl;
	return AT_SUCCESS;
}
int AT_EXP_CONV AT_GetEnumStringByIndex(AT_H Hndl, const AT_WC* Feature, int Index, AT_WC* String, int StringLength){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << Index << endl;
    swprintf(String, StringLength, L"%ls-%ls:%d", Feature, L"Option", Index);
    cout << String << endl;
	return AT_SUCCESS;
}

int AT_EXP_CONV AT_Command(AT_H Hndl, const AT_WC* Feature){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << endl;
	return AT_SUCCESS;
}

int AT_EXP_CONV AT_SetString(AT_H Hndl, const AT_WC* Feature, const AT_WC* String){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature << " " << String << endl;
    cb(-1, Feature, NULL);
	return AT_SUCCESS;
}
int AT_EXP_CONV AT_GetString(AT_H Hndl, const AT_WC* Feature, AT_WC* String, int StringLength){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << endl;
    swprintf(String, StringLength, L"%ls-%ls:%d", Feature, L"Value", rand());
    cout << String << endl;
	return AT_SUCCESS;
}
int AT_EXP_CONV AT_GetStringMaxLength(AT_H Hndl, const AT_WC* Feature, int* MaxStringLength){
	cout << __FUNCTION__ << " called " << Hndl << " " ; wcout << Feature ; cout << " " << endl;
    *MaxStringLength = rand();
    cout << *MaxStringLength << endl;
	return AT_SUCCESS;
}

AT_U8* buffer_ptr = NULL;
int buffer_ptr_size = 0;

int AT_EXP_CONV AT_QueueBuffer(AT_H Hndl, AT_U8* Ptr, int PtrSize){
	cout << __FUNCTION__ << " called " << Hndl << " " << hex << (void*) Ptr << " S:" << dec << PtrSize << endl;
    buffer_ptr = Ptr;
    buffer_ptr_size = PtrSize;
	return AT_SUCCESS;
}
int AT_EXP_CONV AT_WaitBuffer(AT_H Hndl, AT_U8** Ptr, int* PtrSize, unsigned int Timeout){
	cout << __FUNCTION__ << " called " << Hndl << " " << Timeout << endl;
    cout << hex << (void *) buffer_ptr << dec << " " << buffer_ptr_size << endl;
    *Ptr = buffer_ptr;

    for (int i = 0; i < buffer_ptr_size; i ++){
        buffer_ptr[i] = 'A' + i % 26;
    }

    *PtrSize = buffer_ptr_size;
    cout << hex << (void *) *Ptr << dec << " " << *PtrSize << endl;
	return AT_SUCCESS;
}
int AT_EXP_CONV AT_Flush(AT_H Hndl){
	cout << __FUNCTION__ << " called " << Hndl << " " << endl;
	return AT_SUCCESS;
}
