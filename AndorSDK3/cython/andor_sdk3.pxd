cdef extern from "atcore.h":
    ctypedef int AT_H
    ctypedef int AT_BOOL
    ctypedef long long AT_64
    ctypedef unsigned char AT_U8
    ctypedef Py_UNICODE AT_WC

    int AT_INFINITE
    int AT_CALLBACK_SUCCESS
    int AT_TRUE
    int AT_FALSE
    int AT_SUCCESS
    int AT_ERR_NOTINITIALISED
    int AT_ERR_NOTIMPLEMENTED
    int AT_ERR_READONLY
    int AT_ERR_NOTREADABLE
    int AT_ERR_NOTWRITABLE
    int AT_ERR_OUTOFRANGE
    int AT_ERR_INDEXNOTAVAILABLE
    int AT_ERR_INDEXNOTIMPLEMENTED
    int AT_ERR_EXCEEDEDMAXSTRINGLENGTH
    int AT_ERR_CONNECTION
    int AT_ERR_NODATA
    int AT_ERR_INVALIDHANDLE
    int AT_ERR_TIMEDOUT
    int AT_ERR_BUFFERFULL
    int AT_ERR_INVALIDSIZE
    int AT_ERR_INVALIDALIGNMENT
    int AT_ERR_COMM
    int AT_ERR_STRINGNOTAVAILABLE
    int AT_ERR_STRINGNOTIMPLEMENTED
    int AT_ERR_NULL_FEATURE
    int AT_ERR_NULL_HANDLE
    int AT_ERR_NULL_IMPLEMENTED_VAR
    int AT_ERR_NULL_READABLE_VAR
    int AT_ERR_NULL_READONLY_VAR
    int AT_ERR_NULL_WRITABLE_VAR
    int AT_ERR_NULL_MINVALUE
    int AT_ERR_NULL_MAXVALUE
    int AT_ERR_NULL_VALUE
    int AT_ERR_NULL_STRING
    int AT_ERR_NULL_COUNT_VAR
    int AT_ERR_NULL_ISAVAILABLE_VAR
    int AT_ERR_NULL_MAXSTRINGLENGTH
    int AT_ERR_NULL_EVCALLBACK
    int AT_ERR_NULL_QUEUE_PTR
    int AT_ERR_NULL_WAIT_PTR
    int AT_ERR_NULL_PTRSIZE
    int AT_ERR_NOMEMORY
    int AT_ERR_DEVICEINUSE
    int AT_ERR_DEVICENOTFOUND
    int AT_ERR_HARDWARE_OVERFLOW
    int AT_HANDLE_UNINITIALISED
    int AT_HANDLE_SYSTEM
    
    int AT_InitialiseLibrary()
    int AT_FinaliseLibrary()
    int AT_Open(int CameraIndex, AT_H *Hndl)
    int AT_OpenDevice(const AT_WC* Device, AT_H *Hndl)
    int AT_Close(AT_H Hndl)

    ctypedef int (*FeatureCallback)(AT_H Hndl, const AT_WC* Feature, void* Context)
    int AT_RegisterFeatureCallback(AT_H Hndl, const AT_WC* Feature, FeatureCallback EvCallback, void* Context)
    int AT_UnregisterFeatureCallback(AT_H Hndl, const AT_WC* Feature, FeatureCallback EvCallback, void* Context)

    int AT_IsImplemented(AT_H Hndl, const AT_WC* Feature, AT_BOOL* Implemented)
    int AT_IsReadable(AT_H Hndl, const AT_WC* Feature, AT_BOOL* Readable)
    int AT_IsWritable(AT_H Hndl, const AT_WC* Feature, AT_BOOL* Writable)
    int AT_IsReadOnly(AT_H Hndl, const AT_WC* Feature, AT_BOOL* ReadOnly)

    int AT_SetInt(AT_H Hndl, const AT_WC* Feature, AT_64 Value)
    int AT_GetInt(AT_H Hndl, const AT_WC* Feature, AT_64* Value)
    int AT_GetIntMax(AT_H Hndl, const AT_WC* Feature, AT_64* MaxValue)
    int AT_GetIntMin(AT_H Hndl, const AT_WC* Feature, AT_64* MinValue)

    int AT_SetFloat(AT_H Hndl, const AT_WC* Feature, double Value)
    int AT_GetFloat(AT_H Hndl, const AT_WC* Feature, double* Value)
    int AT_GetFloatMax(AT_H Hndl, const AT_WC* Feature, double* MaxValue)
    int AT_GetFloatMin(AT_H Hndl, const AT_WC* Feature, double* MinValue)

    int AT_SetBool(AT_H Hndl, const AT_WC* Feature, AT_BOOL Value)
    int AT_GetBool(AT_H Hndl, const AT_WC* Feature, AT_BOOL* Value)

    int AT_SetEnumIndex(AT_H Hndl, const AT_WC* Feature, int Value)
    int AT_SetEnumString(AT_H Hndl, const AT_WC* Feature, const AT_WC* String)
    int AT_GetEnumIndex(AT_H Hndl, const AT_WC* Feature, int* Value)
    int AT_GetEnumCount(AT_H Hndl,const  AT_WC* Feature, int* Count)
    int AT_IsEnumIndexAvailable(AT_H Hndl, const AT_WC* Feature, int Index, AT_BOOL* Available)
    int AT_IsEnumIndexImplemented(AT_H Hndl, const AT_WC* Feature, int Index, AT_BOOL* Implemented)
    int AT_GetEnumStringByIndex(AT_H Hndl, const AT_WC* Feature, int Index, AT_WC* String, int StringLength)

    int AT_Command(AT_H Hndl, const AT_WC* Feature)

    int AT_SetString(AT_H Hndl, const AT_WC* Feature, const AT_WC* String)
    int AT_GetString(AT_H Hndl, const AT_WC* Feature, AT_WC* String, int StringLength)
    int AT_GetStringMaxLength(AT_H Hndl, const AT_WC* Feature, int* MaxStringLength)

    int AT_QueueBuffer(AT_H Hndl, AT_U8* Ptr, int PtrSize)
    int AT_WaitBuffer(AT_H Hndl, AT_U8** Ptr, int* PtrSize, unsigned int Timeout)
    int AT_Flush(AT_H Hndl)
