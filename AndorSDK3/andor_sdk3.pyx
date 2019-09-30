# distutils: language = c++
cimport andor_sdk3 as andor3
from cpython.mem cimport PyMem_Malloc, PyMem_Free
from cpython.pycapsule cimport PyCapsule_New, PyCapsule_GetPointer
import numpy as np
import logging

_SPLIT_LOG = True

if _SPLIT_LOG:
    andor3_logger = logging.getLogger("andor3")
    andor3_logger.setLevel(logging.DEBUG)
    andor3_fh = logging.FileHandler("andor3.log")
    andor3_formatter = logging.Formatter('%(asctime)s [%(name)s] - %(levelname)s - %(message)s')
    andor3_fh.setFormatter(andor3_formatter)
    andor3_logger.addHandler(andor3_fh)

    andor3_ch = logging.StreamHandler()
    andor3_ch.setFormatter(andor3_formatter)
    andor3_logger.addHandler(andor3_ch)
else:
    andor3_logger = logging.getLogger("autools_setup_main")


feature_callback_table = {}

# feature callback hub to call python callbacks, "with gil" is mandatory
# Warning: 32bit Python build will crash
cdef int feature_cb(andor3.AT_H handle, const andor3.AT_WC* feature, void* context) with gil:
    global feature_callback_table
    andor3_logger.info(f"{feature} notified")
    if handle in feature_callback_table.keys():
        if feature in feature_callback_table[handle].keys():
            for cb in feature_callback_table[handle][feature]:
                cb(feature)

    return andor3.AT_SUCCESS

andor3_errcode_dict = {
    andor3.AT_ERR_NOTINITIALISED : "NOTINITIALISED",
    andor3.AT_ERR_NOTIMPLEMENTED : "NOTIMPLEMENTED",
    andor3.AT_ERR_READONLY : "READONLY",
    andor3.AT_ERR_NOTREADABLE : "NOTREADABLE",
    andor3.AT_ERR_NOTWRITABLE : "NOTWRITABLE",
    andor3.AT_ERR_OUTOFRANGE : "OUTOFRANGE",
    andor3.AT_ERR_INDEXNOTAVAILABLE : "INDEXNOTAVAILABLE",
    andor3.AT_ERR_INDEXNOTIMPLEMENTED : "INDEXNOTIMPLEMENTED",
    andor3.AT_ERR_EXCEEDEDMAXSTRINGLENGTH : "EXCEEDEDMAXSTRINGLENGTH",
    andor3.AT_ERR_CONNECTION : "CONNECTION",
    andor3.AT_ERR_NODATA : "NODATA",
    andor3.AT_ERR_INVALIDHANDLE : "INVALIDHANDLE",
    andor3.AT_ERR_TIMEDOUT : "TIMEDOUT",
    andor3.AT_ERR_BUFFERFULL : "BUFFERFULL",
    andor3.AT_ERR_INVALIDSIZE : "INVALIDSIZE",
    andor3.AT_ERR_INVALIDALIGNMENT : "INVALIDALIGNMENT",
    andor3.AT_ERR_COMM : "COMM",
    andor3.AT_ERR_STRINGNOTAVAILABLE : "STRINGNOTAVAILABLE",
    andor3.AT_ERR_STRINGNOTIMPLEMENTED : "STRINGNOTIMPLEMENTED",
    andor3.AT_ERR_NULL_FEATURE : "NULL_FEATURE",
    andor3.AT_ERR_NULL_HANDLE : "NULL_HANDLE",
    andor3.AT_ERR_NULL_IMPLEMENTED_VAR : "NULL_IMPLEMENTED_VAR",
    andor3.AT_ERR_NULL_READABLE_VAR : "NULL_READABLE_VAR",
    andor3.AT_ERR_NULL_READONLY_VAR : "NULL_READONLY_VAR",
    andor3.AT_ERR_NULL_WRITABLE_VAR : "NULL_WRITABLE_VAR",
    andor3.AT_ERR_NULL_MINVALUE : "NULL_MINVALUE",
    andor3.AT_ERR_NULL_MAXVALUE : "NULL_MAXVALUE",
    andor3.AT_ERR_NULL_VALUE : "NULL_VALUE",
    andor3.AT_ERR_NULL_STRING : "NULL_STRING",
    andor3.AT_ERR_NULL_COUNT_VAR : "NULL_COUNT_VAR",
    andor3.AT_ERR_NULL_ISAVAILABLE_VAR : "NULL_ISAVAILABLE_VAR",
    andor3.AT_ERR_NULL_MAXSTRINGLENGTH : "NULL_MAXSTRINGLENGTH",
    andor3.AT_ERR_NULL_EVCALLBACK : "NULL_EVCALLBACK",
    andor3.AT_ERR_NULL_QUEUE_PTR : "NULL_QUEUE_PTR",
    andor3.AT_ERR_NULL_WAIT_PTR : "NULL_WAIT_PTR",
    andor3.AT_ERR_NULL_PTRSIZE : "NULL_PTRSIZE",
    andor3.AT_ERR_NOMEMORY : "NOMEMORY",
    andor3.AT_ERR_DEVICEINUSE : "DEVICEINUSE",
    andor3.AT_ERR_DEVICENOTFOUND : "DEVICENOTFOUND",
    andor3.AT_ERR_HARDWARE_OVERFLOW : "HARDWARE_OVERFLOW",
}

def error_code_to_str(err_code: int):
    global andor3_errcode_dict
    if err_code in andor3_errcode_dict.keys():
        return andor3_errcode_dict[err_code]
    else:
        return f"__UNKNOWN__{err_code}"


cdef class Andor3Man:
    """
    Cython class for wrapping API calls to Andor3SDK
    [WARNING]: currently only support the Neon CMOS camera, for other camera, please check the feature_map used.
    TODO?: more elegant to use __getattr__ to avoid repeated code
    """

    cdef int _c_dev_id
    cdef andor3.AT_H _c_dev_h
    cdef list _feature_cb_list
    cdef dict _feature_map
    cdef dict _buffer_map
    cdef int _buffer_id

    def __cinit__(self):
        self._c_dev_h = -1
        self._buffer_id = 0
        self._feature_cb_list = []
        self._feature_map = {}
        self._buffer_map = {}
        ret = andor3.AT_InitialiseLibrary()
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to initialise andor3 library, {error_code_to_str(ret)}")
            raise Exception(f"Failed to initialise andor3 library, {error_code_to_str(ret)}")
        else:
            andor3_logger.info(f"Andor3 Library initialized")

    def __del__(self):
        andor3.AT_FinaliseLibrary()

    def load_feature_map(self, feature_map: dict):
        self._feature_map = feature_map

    def get_dev_id(self):
        return self._c_dev_id

    def get_dev_handle(self):
        return self._c_dev_h

    def open_dev(self,  dev_id: int):
        if self._c_dev_h != -1:
            andor3_logger.error(f"Already with an open device ID:{self._c_dev_id} H:{self._c_dev_h}")
            raise Exception(f"Already with an open device ID:{self._c_dev_id} H:{self._c_dev_h}")
        self._c_dev_id = dev_id
        ret = andor3.AT_Open(self._c_dev_id, &self._c_dev_h)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to open dev {self._c_dev_id}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to open dev {self._c_dev_id}, {error_code_to_str(ret)}")

        andor3_logger.info(f"Andor3 device {self._c_dev_id} opened")

    def is_open(self):
        return self._c_dev_h != -1

    def close(self):
        ret = andor3.AT_Close(self._c_dev_h)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to close dev ID:{self._c_dev_id} H:{self._c_dev_h}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to close dev ID:{self._c_dev_id} H:{self._c_dev_h}, {error_code_to_str(ret)}")
        andor3_logger.info(f"Andor3 device ID:{self._c_dev_id} H:{self._c_dev_h} closed")
        self._c_dev_h = -1

    def is_sys_feature(self, feature: str):
        return self._feature_map[feature]['system'] \
            if feature in self._feature_map.keys() and 'system' in self._feature_map[feature].keys() \
            else False

    def register_feature_cb(self, feature, cb):
        global feature_callback_table
        if self._c_dev_h not in feature_callback_table.keys():
            feature_callback_table[self._c_dev_h] = {}

        if feature not in feature_callback_table[self._c_dev_h].keys():
            feature_callback_table[self._c_dev_h][feature] = set()

        feature_callback_table[self._c_dev_h][feature].add(cb)
        andor3_logger.debug(f"Register callback (Python) {cb} for {feature}")

        if feature not in self._feature_cb_list:
            ret = andor3.AT_RegisterFeatureCallback(self._c_dev_h, feature, feature_cb, NULL)
            if ret != andor3.AT_SUCCESS:
                andor3_logger.error(f"Failed to register callback for {feature}, {error_code_to_str(ret)}")
                raise Exception(f"Failed to register callback for {feature}, {error_code_to_str(ret)}")

            andor3_logger.info(f"Register callback (relay) for {feature}")

    def unregister_feature_cb(self, feature, cb):
        global feature_callback_table
        if self._c_dev_h in feature_callback_table.keys():
            if feature in feature_callback_table[self._c_dev_h].keys():
                if cb in feature_callback_table[self._c_dev_h][feature]:
                    feature_callback_table[self._c_dev_h][feature].remove(cb)
                    andor3_logger.debug(f"UnRegister callback (Python) {cb} for {feature}")

                if len(feature_callback_table[self._c_dev_h][feature]) == 0:
                    ret = andor3.AT_UnregisterFeatureCallback(self._c_dev_h, feature, feature_cb, NULL)
                    andor3_logger.info(f"UnRegister callback (relay&Python) for {feature}")
                    del feature_callback_table[self._c_dev_h][feature]

    def clear_feature_cb(self, feature):
        global feature_callback_table
        if self._c_dev_h in feature_callback_table.keys():
            if feature in feature_callback_table[self._c_dev_h].keys():
                ret = andor3.AT_UnregisterFeatureCallback(self._c_dev_h, feature, feature_cb, NULL)
                andor3_logger.info(f"UnRegister callback (relay&Python) for {feature}")
                del feature_callback_table[self._c_dev_h][feature]

    def _is_feature_what(self, feature: str, what: str):
        cdef andor3.AT_BOOL b
        handle = 1 if self.is_sys_feature(feature) else self._c_dev_h
        if what == "implemented":
            ret = andor3.AT_IsImplemented(handle, feature, &b)
        elif what == "readable":
            ret = andor3.AT_IsReadable(handle, feature, &b)
        elif what == "writable":
            ret = andor3.AT_IsWritable(handle, feature, &b)
        elif what == "readonly":
            ret = andor3.AT_IsReadOnly(handle, feature, &b)
        else:
            return False

        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to check {what} for {feature}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to check {what} for {feature}, {error_code_to_str(ret)}")
        andor3_logger.debug(f"{feature} is {'not' if b!=andor3.AT_TRUE else ''} {what}")
        return b == andor3.AT_TRUE

    def is_feature_implemented(self, feature: str):
        return self._is_feature_what(feature, "implemented")

    def is_feature_readable(self, feature: str):
        return self._is_feature_what(feature, "readable")

    def is_feature_writable(self, feature: str):
        return self._is_feature_what(feature, "writable")

    def is_feature_readonly(self, feature: str):
        return self._is_feature_what(feature, "readonly")

    def _get_i_f_feature_what(self, feature: str, is_int: bool, what: str):
        cdef andor3.AT_64 i_value
        cdef double f_value
        handle = 1 if self.is_sys_feature(feature) else self._c_dev_h
        if is_int and what == "max":
            ret = andor3.AT_GetIntMax(handle, feature, &i_value)
        elif is_int and what == "min":
            ret = andor3.AT_GetIntMin(handle, feature, &i_value)
        elif is_int and what == "value":
            ret = andor3.AT_GetInt(handle, feature, &i_value)
        elif not is_int and what == "max":
            ret = andor3.AT_GetFloatMax(handle, feature, &f_value)
        elif not is_int and what == "min":
            ret = andor3.AT_GetFloatMin(handle, feature, &f_value)
        elif not is_int and what == "value":
            ret = andor3.AT_GetFloat(handle, feature, &f_value)
        else:
            ret = andor3.AT_ERR_NODATA  # causing Exception

        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to get({'i' if is_int else 'f'}) {what} "
                                f"for {feature}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to get({'i' if is_int else 'f'}) {what} "
                            f"for {feature}, {error_code_to_str(ret)}")
        andor3_logger.debug(f"{feature}({'i' if is_int else 'f'}) {what} = {i_value if is_int else f_value}")
        return i_value if is_int else f_value

    def get_i_feature_max(self, feature: str):
        return self._get_i_f_feature_what(feature, is_int=True, what="max")

    def get_i_feature_min(self, feature: str):
        return self._get_i_f_feature_what(feature, is_int=True, what="min")

    def get_i_feature(self, feature: str):
        return self._get_i_f_feature_what(feature, is_int=True, what="value")

    def set_i_feature(self, feature: str, feature_value: int):
        cdef andor3.AT_64 i_value = feature_value
        handle = 1 if self.is_sys_feature(feature) else self._c_dev_h
        ret = andor3.AT_SetInt(handle, feature, i_value)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to set(i) for {feature}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to set(i) for {feature}, {error_code_to_str(ret)}")
        andor3_logger.debug(f"{feature}(i) set to {feature_value}")

    def get_f_feature_max(self, feature: str):
        return self._get_i_f_feature_what(feature, is_int=False, what="max")

    def get_f_feature_min(self, feature: str):
        return self._get_i_f_feature_what(feature, is_int=False, what="min")

    def get_f_feature(self, feature: str):
        return self._get_i_f_feature_what(feature, is_int=False, what="value")

    def set_f_feature(self, feature: str, feature_value: float):
        cdef double f_value = feature_value
        handle = 1 if self.is_sys_feature(feature) else self._c_dev_h
        ret = andor3.AT_SetFloat(handle, feature, f_value)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to set(f) for {feature}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to set(f) for {feature}, {error_code_to_str(ret)}")
        andor3_logger.debug(f"{feature}(f) set to {feature_value}")

    def get_b_feature(self, feature: str):
        cdef andor3.AT_BOOL b_value
        handle = 1 if self.is_sys_feature(feature) else self._c_dev_h
        ret = andor3.AT_GetBool(handle, feature, &b_value)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to get(b) for {feature}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to get(b) for {feature}, {error_code_to_str(ret)}")
        andor3_logger.debug(f"{feature}(b) = {b_value}")
        return b_value == andor3.AT_TRUE

    def set_b_feature(self, feature: str, feature_value: bool):
        cdef andor3.AT_BOOL b_value = andor3.AT_TRUE if feature_value else andor3.AT_FALSE
        handle = 1 if self.is_sys_feature(feature) else self._c_dev_h
        ret = andor3.AT_SetBool(handle, feature, b_value)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to set(b) for {feature}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to set(b) for {feature}, {error_code_to_str(ret)}")
        andor3_logger.debug(f"{feature}(b) set to {feature_value}")

    def get_e_feature_count(self, feature: str):
        cdef int i_count
        handle = 1 if self.is_sys_feature(feature) else self._c_dev_h
        ret = andor3.AT_GetEnumCount(handle, feature, &i_count)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to get(e) count for {feature}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to get(e) count for {feature}, {error_code_to_str(ret)}")
        andor3_logger.debug(f"{feature}(e) count = {i_count}")
        return i_count

    def is_e_feature_index_implemented(self, feature: str, index: int):
        cdef andor3.AT_BOOL b
        handle = 1 if self.is_sys_feature(feature) else self._c_dev_h
        ret = andor3.AT_IsEnumIndexImplemented(handle, feature, index, &b)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to check(e) implemented for {feature} "
                                f"index={index}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to check(e) implemented for {feature} "
                            f"index={index}, {error_code_to_str(ret)}")
        andor3_logger.debug(f"{index}@{feature}(e) implemented = {b}")
        return b == andor3.AT_TRUE

    def is_e_feature_index_available(self, feature: str, index: int):
        cdef andor3.AT_BOOL b
        handle = 1 if self.is_sys_feature(feature) else self._c_dev_h
        ret = andor3.AT_IsEnumIndexAvailable(handle, feature, index, &b)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to check(e) available for {feature} "
                                f"index={index}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to check(e) available for {feature} "
                            f"index={index}, {error_code_to_str(ret)}")
        andor3_logger.debug(f"{index}@{feature}(e) available = {b}")
        return b == andor3.AT_TRUE

    def get_e_feature_str_at(self, feature: str, index: int):
        handle = 1 if self.is_sys_feature(feature) else self._c_dev_h
        cdef andor3.AT_WC* str_buf = <andor3.AT_WC*> PyMem_Malloc(1024*sizeof(andor3.AT_WC))
        ret = andor3.AT_GetEnumStringByIndex(handle, feature, index, str_buf, 1024)
        py_str = str_buf[:]
        PyMem_Free(str_buf)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to get(e) string {feature} index={index}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to get(e) string {feature} index={index}, {error_code_to_str(ret)}")
        andor3_logger.debug(f"{index}@{feature}(e) str = {py_str}")
        return py_str

    def get_e_feature_index(self, feature: str):
        cdef int i_value
        handle = 1 if self.is_sys_feature(feature) else self._c_dev_h
        ret = andor3.AT_GetEnumIndex(handle, feature, &i_value)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to get(e) for {feature}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to get(e) for {feature}, {error_code_to_str(ret)}")
        andor3_logger.debug(f"{feature}(e) index = {i_value}")
        return i_value

    def get_e_feature_str(self, feature: str):
        return self.get_e_feature_str_at(feature, self.get_e_feature_index(feature))

    def set_e_feature(self, feature: str, value: int or str):
        handle = 1 if self.is_sys_feature(feature) else self._c_dev_h
        if type(value) is int:
            ret = andor3.AT_SetEnumIndex(handle, feature, value)
        else:  # type(index) is str
            ret = andor3.AT_SetEnumString(handle, feature, value)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to set(e) for {feature}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to set(e) for {feature}, {error_code_to_str(ret)}")
        andor3_logger.debug(f"{feature}(e) (index/str) = {value}")

    def set_e_feature_check(self, feature: str, value: int or str):
        try:
            if type(value) is int:
                if value == self.get_e_feature_index(feature):
                    return value
            self.set_e_feature(feature, value)
            return value
        except Exception as e:
            return self.get_e_feature_index(feature)

    def send_command(self, cmd_feature: str):
        handle = 1 if self.is_sys_feature(cmd_feature) else self._c_dev_h
        ret = andor3.AT_Command(handle, cmd_feature)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to send command {cmd_feature}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to send command {cmd_feature}, {error_code_to_str(ret)}")
        andor3_logger.info(f"Command = {cmd_feature}")

    def get_s_feature(self, feature: str):
        cdef int str_len
        handle = 1 if self.is_sys_feature(feature) else self._c_dev_h
        ret = andor3.AT_GetStringMaxLength(handle, feature, &str_len)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to get max length of {feature}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to get max length of {feature}, {error_code_to_str(ret)}")

        cdef andor3.AT_WC* str_buf = <andor3.AT_WC*> PyMem_Malloc(str_len*sizeof(andor3.AT_WC))
        ret = andor3.AT_GetString(handle, feature, str_buf, str_len)
        py_str = str_buf[:]
        PyMem_Free(str_buf)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to get(s) {feature}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to get(s) {feature}, {error_code_to_str(ret)}")
        andor3_logger.debug(f"{feature}(s) = {py_str}")
        return py_str

    def set_s_feature(self, feature: str, feature_value: str):
        handle = 1 if self.is_sys_feature(feature) else self._c_dev_h
        ret = andor3.AT_SetString(handle, feature, feature_value)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to set(s) {feature}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to set(s) {feature}, {error_code_to_str(ret)}")
        andor3_logger.debug(f"{feature}(s) set to {feature_value}")

    def flush(self):
        ret = andor3.AT_Flush(self._c_dev_h)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to flush, {error_code_to_str(ret)}")
            raise Exception(f"Failed to flush, {error_code_to_str(ret)}")
        andor3_logger.info(f"Flushed")

    def create_buffer(self, buffersize: int):
        cdef long buffer_aligned_size = buffersize + (8 - buffersize % 8)
        cdef andor3.AT_U8* buffer = <andor3.AT_U8*> PyMem_Malloc(buffer_aligned_size)
        if buffer is None:
            andor3_logger.error(f"Failed to allocate memory size = {buffer_aligned_size}")
            raise MemoryError()

        cdef andor3.AT_U8* buffer_aligned = <andor3.AT_U8*> &(buffer[8- (<unsigned long long>buffer)%8])
        self._buffer_map[self._buffer_id] = (PyCapsule_New(<void*>buffer, "buffer", NULL),
                                             PyCapsule_New(<void*>buffer_aligned, "buffer_aligned", NULL),
                                             buffersize)
        self._buffer_id += 1
        andor3_logger.info(f"Buffer id {self._buffer_id-1} created")
        return self._buffer_id-1

    def get_buffer_size(self, buffer_id):
        if buffer_id not in self._buffer_map.keys():
            return 0

        return self._buffer_map[buffer_id][2]

    def free_buffer(self, buffer_id: int):
        if buffer_id not in self._buffer_map.keys():
            return

        cdef andor3.AT_U8* buffer = <andor3.AT_U8*> PyCapsule_GetPointer(self._buffer_map[buffer_id][0], "buffer")
        PyMem_Free(buffer)
        del self._buffer_map[buffer_id]
        andor3_logger.info(f"Buffer id {buffer_id} freed")

    def queue_buffer(self, buffer_id: int):
        if buffer_id not in self._buffer_map.keys():
            andor3_logger.error(f"Invalid buffer id {buffer_id}")
            raise ValueError(f"Invalid buffer id {buffer_id}")

        cdef andor3.AT_U8* buffer_aligned = <andor3.AT_U8*> PyCapsule_GetPointer(
                                                self._buffer_map[buffer_id][1], "buffer_aligned")
        cdef int buffer_size = self._buffer_map[buffer_id][2]

        ret = andor3.AT_QueueBuffer(self._c_dev_h, buffer_aligned, buffer_size)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to queue buffer {buffer_id}:{buffer_size}"
                                f"@>{<unsigned long>buffer_aligned:016X}, {error_code_to_str(ret)}")
            raise Exception(f"Failed to queue buffer {buffer_id}:{buffer_size}"
                            f"@>{<unsigned long>buffer_aligned:016X}, {error_code_to_str(ret)}")
        andor3_logger.info(f"Buffer {buffer_id} queued")

    def wait_buffer(self, timeout_ms: int):
        cdef andor3.AT_U8* buffer_pointer
        cdef int buffer_readout_size
        cdef unsigned int timeout = timeout_ms
        ret = andor3.AT_WaitBuffer(self._c_dev_h, &buffer_pointer, &buffer_readout_size, timeout)
        if ret != andor3.AT_SUCCESS:
            andor3_logger.error(f"Failed to wait buffer, {error_code_to_str(ret)}")
            raise Exception(f"Failed to wait buffer, {error_code_to_str(ret)}")

        for buffer_id in self._buffer_map.keys():
            # print(f'{<unsigned int>PyCapsule_GetPointer(self._buffer_map[buffer_id][1], "buffer_aligned"):016X} '
            #       f'?? {<unsigned int>buffer_pointer:016X}')
            if PyCapsule_GetPointer(self._buffer_map[buffer_id][1], "buffer_aligned") == <void*>buffer_pointer:
                andor3_logger.info(f"Buffer {buffer_id} ready with size {buffer_readout_size}")
                return buffer_id, buffer_readout_size

        andor3_logger.error(f"Failed to find buffer in internal map")
        raise Exception(f"Failed to find buffer in internal map")

    def get_data_from_buffer(self, buffer_id: int, actual_size: int):
        if buffer_id not in self._buffer_map.keys():
            andor3_logger.error(f"Invalid buffer id {buffer_id}")
            raise ValueError(f"Invalid buffer id {buffer_id}")

        cdef andor3.AT_U8* buffer_aligned = <andor3.AT_U8*> PyCapsule_GetPointer(
                                                self._buffer_map[buffer_id][1], "buffer_aligned")
        cdef int buffer_size = self._buffer_map[buffer_id][2]
        if actual_size > buffer_size:
            actual_size = buffer_size

        return buffer_aligned[:actual_size]

    @staticmethod
    def convert_bytes_to_numpy_array(buffer: bytes or bytearray, pixel_encoding: str,
                                     stride: int, width: int,
                                     height: int):
        if pixel_encoding not in ('Mono12', 'Mono12Packed', 'Mono16', 'Mono32'):
            raise ValueError(f"Invalid pixel encoding {pixel_encoding}")

        if len(buffer) < stride * height:
            buffer_fixed = buffer + "\0"*(stride*height - len(buffer))
            andor3_logger.warning(f"Buffer size {len(buffer)} is less than excepted size {stride*height}, padding 0")
        elif len(buffer) > stride * height:
            buffer_fixed = buffer[:stride * height]
            andor3_logger.warning(f"Buffer size {len(buffer)} is larger than excepted size {stride*height}, truncating")
        else:
            buffer_fixed = buffer

        if pixel_encoding == "Mono12" or pixel_encoding == "Mono16":
            pixels_rows = np.frombuffer(buffer_fixed[:2*width], '<u2')
            for i in range(1, height):
                pixels_rows = np.vstack((
                    pixels_rows,
                    np.frombuffer(buffer_fixed[i*stride:i*stride+2*width], '<u2')))
            return pixels_rows
        elif pixel_encoding == "Mono32":
            pixels_rows = np.frombuffer(buffer_fixed[:4*width], '<u4')
            for i in range(1, height):
                pixels_rows = np.vstack((
                    pixels_rows,
                    np.frombuffer(buffer_fixed[i*stride:i*stride+4*width], '<u4')))
            return pixels_rows
        elif pixel_encoding == "Mono12Packed":
            # FIXME: This format is not working
            pixels_rows = None
            for i in range(0, height):
                row_bytes = buffer_fixed[i*stride:i*stride+int(3*width/2)]
                np_row = np.zeros(width, dtype='<u4')
                pixel_col_index = 0
                byte_index = 0
                while pixel_col_index < width:
                    byte0 = buffer[byte_index]
                    byte_index += 1
                    byte1 = buffer[byte_index]
                    byte_index += 1
                    byte2 = buffer[byte_index]
                    byte_index += 1

                    np_row[pixel_col_index] = ((byte1 & 0xF) << 8) + byte0
                    pixel_col_index += 1
                    np_row[pixel_col_index] = (byte2 << 4) + (byte1 >> 4)
                    pixel_col_index += 1

                if i == 0:
                    pixels_rows = np_row
                else:
                    pixels_rows = np.vstack((pixels_rows, np_row))

            return pixels_rows
