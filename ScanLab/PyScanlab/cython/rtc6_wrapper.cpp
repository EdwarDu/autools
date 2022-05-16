#include "RTC6impl.hpp"
inline UINT _init_rtc6_dll (int __attribute__((unused)) cardno ) {
 return init_rtc6_dll ();
}
inline void _free_rtc6_dll (int __attribute__((unused)) cardno ) {
 return free_rtc6_dll ();
}
inline void _set_rtc4_mode (int __attribute__((unused)) cardno ) {
 return set_rtc4_mode ();
}
inline void _set_rtc5_mode (int __attribute__((unused)) cardno ) {
 return set_rtc5_mode ();
}
inline void _set_rtc6_mode (int __attribute__((unused)) cardno ) {
 return set_rtc6_mode ();
}
inline UINT _get_rtc_mode (int __attribute__((unused)) cardno ) {
 return get_rtc_mode ();
}
inline UINT _get_error (int cardno ) {
  if (cardno == -1) { return get_error();}
  else { return n_get_error (static_cast<UINT>(cardno));}
}
inline UINT _get_last_error (int cardno ) {
  if (cardno == -1) { return get_last_error();}
  else { return n_get_last_error (static_cast<UINT>(cardno));}
}
inline void _reset_error (int cardno ,const UINT Code) {
  if (cardno == -1) { return reset_error(Code);}
  else { return n_reset_error (static_cast<UINT>(cardno),Code);}
}
inline UINT _set_verify (int cardno ,const UINT Verify) {
  if (cardno == -1) { return set_verify(Verify);}
  else { return n_set_verify (static_cast<UINT>(cardno),Verify);}
}
inline UINT _verify_checksum (int __attribute__((unused)) cardno ,const char* Name) {
 return verify_checksum (Name);
}
inline UINT _eth_count_cards (int __attribute__((unused)) cardno ) {
 return eth_count_cards ();
}
inline UINT _eth_found_cards (int __attribute__((unused)) cardno ) {
 return eth_found_cards ();
}
inline UINT _eth_max_card (int __attribute__((unused)) cardno ) {
 return eth_max_card ();
}
inline long _eth_remove_card (int __attribute__((unused)) cardno ,const UINT CardNo) {
 return eth_remove_card (CardNo);
}
inline void _eth_get_card_info (int __attribute__((unused)) cardno ,const UINT CardNo, const ULONG_PTR Ptr) {
 return eth_get_card_info (CardNo,Ptr);
}
inline void _eth_get_card_info_search (int __attribute__((unused)) cardno ,const UINT SearchNo, const ULONG_PTR Ptr) {
 return eth_get_card_info_search (SearchNo,Ptr);
}
inline void _eth_set_search_cards_timeout (int __attribute__((unused)) cardno ,const UINT TimeOut) {
 return eth_set_search_cards_timeout (TimeOut);
}
inline UINT _eth_search_cards (int __attribute__((unused)) cardno ,const UINT Ip, const UINT NetMask) {
 return eth_search_cards (Ip,NetMask);
}
inline UINT _eth_search_cards_range (int __attribute__((unused)) cardno ,const UINT StartIp, const UINT EndIp) {
 return eth_search_cards_range (StartIp,EndIp);
}
inline long _eth_assign_card_ip (int __attribute__((unused)) cardno ,const UINT Ip, const UINT CardNo) {
 return eth_assign_card_ip (Ip,CardNo);
}
inline long _eth_assign_card (int __attribute__((unused)) cardno ,const UINT SearchNo, const UINT CardNo) {
 return eth_assign_card (SearchNo,CardNo);
}
inline UINT _eth_convert_string_to_ip (int __attribute__((unused)) cardno ,const char* IpString) {
 return eth_convert_string_to_ip (IpString);
}
inline void _eth_convert_ip_to_string (int __attribute__((unused)) cardno ,const UINT Ip, const ULONG_PTR IpString) {
 return eth_convert_ip_to_string (Ip,IpString);
}
inline UINT _eth_get_ip (int __attribute__((unused)) cardno ,const UINT CardNo) {
 return eth_get_ip (CardNo);
}
inline UINT _eth_get_ip_search (int __attribute__((unused)) cardno ,const UINT SearchNo) {
 return eth_get_ip_search (SearchNo);
}
inline UINT _eth_get_serial_search (int __attribute__((unused)) cardno ,const UINT SearchNo) {
 return eth_get_serial_search (SearchNo);
}
inline UINT _eth_get_last_error (int cardno ) {
  if (cardno == -1) { return eth_get_last_error();}
  else { return n_eth_get_last_error (static_cast<UINT>(cardno));}
}
inline UINT _eth_get_error (int cardno ) {
  if (cardno == -1) { return eth_get_error();}
  else { return n_eth_get_error (static_cast<UINT>(cardno));}
}
inline UINT _eth_error_dump (int cardno ,const ULONG_PTR Dump) {
  if (cardno == -1) { return eth_error_dump(Dump);}
  else { return n_eth_error_dump (static_cast<UINT>(cardno),Dump);}
}
inline UINT _eth_set_static_ip (int cardno ,const UINT Ip, const UINT NetMask, const UINT Gateway) {
  if (cardno == -1) { return eth_set_static_ip(Ip,NetMask,Gateway);}
  else { return n_eth_set_static_ip (static_cast<UINT>(cardno),Ip,NetMask,Gateway);}
}
inline UINT _eth_get_static_ip (int cardno ,UINT& Ip, UINT& NetMask, UINT& Gateway) {
  if (cardno == -1) { return eth_get_static_ip(Ip,NetMask,Gateway);}
  else { return n_eth_get_static_ip (static_cast<UINT>(cardno),Ip,NetMask,Gateway);}
}
inline UINT _eth_set_port_numbers (int cardno ,const UINT UDPsearch, const UINT UDPexcl, const UINT TCP) {
  if (cardno == -1) { return eth_set_port_numbers(UDPsearch,UDPexcl,TCP);}
  else { return n_eth_set_port_numbers (static_cast<UINT>(cardno),UDPsearch,UDPexcl,TCP);}
}
inline UINT _eth_get_port_numbers (int cardno ,UINT& UDPsearch, UINT& UDPexcl, UINT& TCP) {
  if (cardno == -1) { return eth_get_port_numbers(UDPsearch,UDPexcl,TCP);}
  else { return n_eth_get_port_numbers (static_cast<UINT>(cardno),UDPsearch,UDPexcl,TCP);}
}
inline void _eth_set_com_timeouts (int cardno ,const UINT AcquireTimeout, const UINT AcquireMaxRetries, const UINT SendRecvTimeout, const UINT SendRecvMaxRetries, const UINT KeepAlive, const UINT KeepInterval) {
  if (cardno == -1) { return eth_set_com_timeouts(AcquireTimeout,AcquireMaxRetries,SendRecvTimeout,SendRecvMaxRetries,KeepAlive,KeepInterval);}
  else { return n_eth_set_com_timeouts (static_cast<UINT>(cardno),AcquireTimeout,AcquireMaxRetries,SendRecvTimeout,SendRecvMaxRetries,KeepAlive,KeepInterval);}
}
inline void _eth_get_com_timeouts (int cardno ,UINT& AcquireTimeout, UINT& AcquireMaxRetries, UINT& SendRecvTimeout, UINT& SendRecvMaxRetries, UINT& KeepAlive, UINT& KeepInterval) {
  if (cardno == -1) { return eth_get_com_timeouts(AcquireTimeout,AcquireMaxRetries,SendRecvTimeout,SendRecvMaxRetries,KeepAlive,KeepInterval);}
  else { return n_eth_get_com_timeouts (static_cast<UINT>(cardno),AcquireTimeout,AcquireMaxRetries,SendRecvTimeout,SendRecvMaxRetries,KeepAlive,KeepInterval);}
}
inline UINT _eth_check_connection (int cardno ) {
  if (cardno == -1) { return eth_check_connection();}
  else { return n_eth_check_connection (static_cast<UINT>(cardno));}
}
inline void _set_eth_boot_control (int cardno ,const UINT Ctrl) {
  if (cardno == -1) { return set_eth_boot_control(Ctrl);}
  else { return n_set_eth_boot_control (static_cast<UINT>(cardno),Ctrl);}
}
inline void _eth_boot_timeout (int cardno ,const UINT Timeout) {
  if (cardno == -1) { return eth_boot_timeout(Timeout);}
  else { return n_eth_boot_timeout (static_cast<UINT>(cardno),Timeout);}
}
inline void _eth_boot_dcmd (int cardno ) {
  if (cardno == -1) { return eth_boot_dcmd();}
  else { return n_eth_boot_dcmd (static_cast<UINT>(cardno));}
}
inline UINT _store_program (int cardno ,const UINT Mode) {
  if (cardno == -1) { return store_program(Mode);}
  else { return n_store_program (static_cast<UINT>(cardno),Mode);}
}
inline UINT _read_image_eth (int cardno ,const char* Name) {
  if (cardno == -1) { return read_image_eth(Name);}
  else { return n_read_image_eth (static_cast<UINT>(cardno),Name);}
}
inline UINT _write_image_eth (int cardno ,const char* Name) {
  if (cardno == -1) { return write_image_eth(Name);}
  else { return n_write_image_eth (static_cast<UINT>(cardno),Name);}
}
inline UINT _read_abc_from_file (int __attribute__((unused)) cardno ,const char* Name, double& A, double& B, double& C) {
 return read_abc_from_file (Name,A,B,C);
}
inline UINT _write_abc_to_file (int __attribute__((unused)) cardno ,const char* Name, const double A, const double B, const double C) {
 return write_abc_to_file (Name,A,B,C);
}
inline UINT _create_dat_file (int cardno ,const long Flag) {
  if (cardno == -1) { return create_dat_file(Flag);}
  else { return n_create_dat_file (static_cast<UINT>(cardno),Flag);}
}
inline UINT _transform (int __attribute__((unused)) cardno ,long& Sig1, long& Sig2, const ULONG_PTR Ptr, const UINT Code) {
 return transform (Sig1,Sig2,Ptr,Code);
}
inline UINT _rtc6_count_cards (int __attribute__((unused)) cardno ) {
 return rtc6_count_cards ();
}
inline UINT _acquire_rtc (int __attribute__((unused)) cardno ,const UINT CardNo) {
 return acquire_rtc (CardNo);
}
inline UINT _release_rtc (int __attribute__((unused)) cardno ,const UINT CardNo) {
 return release_rtc (CardNo);
}
inline UINT _select_rtc (int __attribute__((unused)) cardno ,const UINT CardNo) {
 return select_rtc (CardNo);
}
inline UINT _get_dll_version (int __attribute__((unused)) cardno ) {
 return get_dll_version ();
}
inline UINT _get_card_type (int cardno ) {
  if (cardno == -1) { return get_card_type();}
  else { return n_get_card_type (static_cast<UINT>(cardno));}
}
inline UINT _get_serial_number (int cardno ) {
  if (cardno == -1) { return get_serial_number();}
  else { return n_get_serial_number (static_cast<UINT>(cardno));}
}
inline UINT _get_hex_version (int cardno ) {
  if (cardno == -1) { return get_hex_version();}
  else { return n_get_hex_version (static_cast<UINT>(cardno));}
}
inline UINT _get_rtc_version (int cardno ) {
  if (cardno == -1) { return get_rtc_version();}
  else { return n_get_rtc_version (static_cast<UINT>(cardno));}
}
inline UINT _get_bios_version (int cardno ) {
  if (cardno == -1) { return get_bios_version();}
  else { return n_get_bios_version (static_cast<UINT>(cardno));}
}
inline UINT _load_program_file (int cardno ,const char* Path) {
  if (cardno == -1) { return load_program_file(Path);}
  else { return n_load_program_file (static_cast<UINT>(cardno),Path);}
}
inline void _sync_slaves (int cardno ) {
  if (cardno == -1) { return sync_slaves();}
  else { return n_sync_slaves (static_cast<UINT>(cardno));}
}
inline UINT _get_sync_status (int cardno ) {
  if (cardno == -1) { return get_sync_status();}
  else { return n_get_sync_status (static_cast<UINT>(cardno));}
}
inline void _master_slave_config (int cardno ,const UINT Flags) {
  if (cardno == -1) { return master_slave_config(Flags);}
  else { return n_master_slave_config (static_cast<UINT>(cardno),Flags);}
}
inline UINT _load_correction_file (int cardno ,const char* Name, const UINT No, const UINT Dim) {
  if (cardno == -1) { return load_correction_file(Name,No,Dim);}
  else { return n_load_correction_file (static_cast<UINT>(cardno),Name,No,Dim);}
}
inline UINT _load_zoom_correction_file (int cardno ,const char* Name, const UINT No) {
  if (cardno == -1) { return load_zoom_correction_file(Name,No);}
  else { return n_load_zoom_correction_file (static_cast<UINT>(cardno),Name,No);}
}
inline UINT _load_oct_table_no (int cardno ,const double A, const double B, const UINT No) {
  if (cardno == -1) { return load_oct_table_no(A,B,No);}
  else { return n_load_oct_table_no (static_cast<UINT>(cardno),A,B,No);}
}
inline UINT _load_z_table_no (int cardno ,const double A, const double B, const double C, const UINT No) {
  if (cardno == -1) { return load_z_table_no(A,B,C,No);}
  else { return n_load_z_table_no (static_cast<UINT>(cardno),A,B,C,No);}
}
inline UINT _load_z_table (int cardno ,const double A, const double B, const double C) {
  if (cardno == -1) { return load_z_table(A,B,C);}
  else { return n_load_z_table (static_cast<UINT>(cardno),A,B,C);}
}
inline void _select_cor_table (int cardno ,const UINT HeadA, const UINT HeadB) {
  if (cardno == -1) { return select_cor_table(HeadA,HeadB);}
  else { return n_select_cor_table (static_cast<UINT>(cardno),HeadA,HeadB);}
}
inline UINT _set_dsp_mode (int cardno ,const UINT Mode) {
  if (cardno == -1) { return set_dsp_mode(Mode);}
  else { return n_set_dsp_mode (static_cast<UINT>(cardno),Mode);}
}
inline long _load_stretch_table (int cardno ,const char* Name, const long No, const UINT TableNo) {
  if (cardno == -1) { return load_stretch_table(Name,No,TableNo);}
  else { return n_load_stretch_table (static_cast<UINT>(cardno),Name,No,TableNo);}
}
inline void _number_of_correction_tables (int cardno ,const UINT Number) {
  if (cardno == -1) { return number_of_correction_tables(Number);}
  else { return n_number_of_correction_tables (static_cast<UINT>(cardno),Number);}
}
inline double _get_head_para (int cardno ,const UINT HeadNo, const UINT ParaNo) {
  if (cardno == -1) { return get_head_para(HeadNo,ParaNo);}
  else { return n_get_head_para (static_cast<UINT>(cardno),HeadNo,ParaNo);}
}
inline double _get_table_para (int cardno ,const UINT TableNo, const UINT ParaNo) {
  if (cardno == -1) { return get_table_para(TableNo,ParaNo);}
  else { return n_get_table_para (static_cast<UINT>(cardno),TableNo,ParaNo);}
}
inline void _config_list (int cardno ,const UINT Mem1, const UINT Mem2) {
  if (cardno == -1) { return config_list(Mem1,Mem2);}
  else { return n_config_list (static_cast<UINT>(cardno),Mem1,Mem2);}
}
inline void _get_config_list (int cardno ) {
  if (cardno == -1) { return get_config_list();}
  else { return n_get_config_list (static_cast<UINT>(cardno));}
}
inline UINT _save_disk (int cardno ,const char* Name, const UINT Mode) {
  if (cardno == -1) { return save_disk(Name,Mode);}
  else { return n_save_disk (static_cast<UINT>(cardno),Name,Mode);}
}
inline UINT _load_disk (int cardno ,const char* Name, const UINT Mode) {
  if (cardno == -1) { return load_disk(Name,Mode);}
  else { return n_load_disk (static_cast<UINT>(cardno),Name,Mode);}
}
inline UINT _get_list_space (int cardno ) {
  if (cardno == -1) { return get_list_space();}
  else { return n_get_list_space (static_cast<UINT>(cardno));}
}
inline void _set_start_list_pos (int cardno ,const UINT ListNo, const UINT Pos) {
  if (cardno == -1) { return set_start_list_pos(ListNo,Pos);}
  else { return n_set_start_list_pos (static_cast<UINT>(cardno),ListNo,Pos);}
}
inline void _set_start_list (int cardno ,const UINT ListNo) {
  if (cardno == -1) { return set_start_list(ListNo);}
  else { return n_set_start_list (static_cast<UINT>(cardno),ListNo);}
}
inline void _set_start_list_1 (int cardno ) {
  if (cardno == -1) { return set_start_list_1();}
  else { return n_set_start_list_1 (static_cast<UINT>(cardno));}
}
inline void _set_start_list_2 (int cardno ) {
  if (cardno == -1) { return set_start_list_2();}
  else { return n_set_start_list_2 (static_cast<UINT>(cardno));}
}
inline void _set_input_pointer (int cardno ,const UINT Pos) {
  if (cardno == -1) { return set_input_pointer(Pos);}
  else { return n_set_input_pointer (static_cast<UINT>(cardno),Pos);}
}
inline UINT _load_list (int cardno ,const UINT ListNo, const UINT Pos) {
  if (cardno == -1) { return load_list(ListNo,Pos);}
  else { return n_load_list (static_cast<UINT>(cardno),ListNo,Pos);}
}
inline void _load_sub (int cardno ,const UINT Index) {
  if (cardno == -1) { return load_sub(Index);}
  else { return n_load_sub (static_cast<UINT>(cardno),Index);}
}
inline void _load_char (int cardno ,const UINT Char) {
  if (cardno == -1) { return load_char(Char);}
  else { return n_load_char (static_cast<UINT>(cardno),Char);}
}
inline void _load_text_table (int cardno ,const UINT Index) {
  if (cardno == -1) { return load_text_table(Index);}
  else { return n_load_text_table (static_cast<UINT>(cardno),Index);}
}
inline void _get_list_pointer (int cardno ,UINT& ListNo, UINT& Pos) {
  if (cardno == -1) { return get_list_pointer(ListNo,Pos);}
  else { return n_get_list_pointer (static_cast<UINT>(cardno),ListNo,Pos);}
}
inline UINT _get_input_pointer (int cardno ) {
  if (cardno == -1) { return get_input_pointer();}
  else { return n_get_input_pointer (static_cast<UINT>(cardno));}
}
inline void _execute_list_pos (int cardno ,const UINT ListNo, const UINT Pos) {
  if (cardno == -1) { return execute_list_pos(ListNo,Pos);}
  else { return n_execute_list_pos (static_cast<UINT>(cardno),ListNo,Pos);}
}
inline void _execute_at_pointer (int cardno ,const UINT Pos) {
  if (cardno == -1) { return execute_at_pointer(Pos);}
  else { return n_execute_at_pointer (static_cast<UINT>(cardno),Pos);}
}
inline void _execute_list (int cardno ,const UINT ListNo) {
  if (cardno == -1) { return execute_list(ListNo);}
  else { return n_execute_list (static_cast<UINT>(cardno),ListNo);}
}
inline void _execute_list_1 (int cardno ) {
  if (cardno == -1) { return execute_list_1();}
  else { return n_execute_list_1 (static_cast<UINT>(cardno));}
}
inline void _execute_list_2 (int cardno ) {
  if (cardno == -1) { return execute_list_2();}
  else { return n_execute_list_2 (static_cast<UINT>(cardno));}
}
inline UINT _list_jump_rel_ctrl (int cardno ,const long Pos) {
  if (cardno == -1) { return list_jump_rel_ctrl(Pos);}
  else { return n_list_jump_rel_ctrl (static_cast<UINT>(cardno),Pos);}
}
inline void _get_out_pointer (int cardno ,UINT& ListNo, UINT& Pos) {
  if (cardno == -1) { return get_out_pointer(ListNo,Pos);}
  else { return n_get_out_pointer (static_cast<UINT>(cardno),ListNo,Pos);}
}
inline void _auto_change_pos (int cardno ,const UINT Pos) {
  if (cardno == -1) { return auto_change_pos(Pos);}
  else { return n_auto_change_pos (static_cast<UINT>(cardno),Pos);}
}
inline void _start_loop (int cardno ) {
  if (cardno == -1) { return start_loop();}
  else { return n_start_loop (static_cast<UINT>(cardno));}
}
inline void _quit_loop (int cardno ) {
  if (cardno == -1) { return quit_loop();}
  else { return n_quit_loop (static_cast<UINT>(cardno));}
}
inline void _pause_list (int cardno ) {
  if (cardno == -1) { return pause_list();}
  else { return n_pause_list (static_cast<UINT>(cardno));}
}
inline void _restart_list (int cardno ) {
  if (cardno == -1) { return restart_list();}
  else { return n_restart_list (static_cast<UINT>(cardno));}
}
inline void _release_wait (int cardno ) {
  if (cardno == -1) { return release_wait();}
  else { return n_release_wait (static_cast<UINT>(cardno));}
}
inline void _stop_execution (int cardno ) {
  if (cardno == -1) { return stop_execution();}
  else { return n_stop_execution (static_cast<UINT>(cardno));}
}
inline void _set_pause_list_cond (int cardno ,const UINT Mask1, const UINT Mask0) {
  if (cardno == -1) { return set_pause_list_cond(Mask1,Mask0);}
  else { return n_set_pause_list_cond (static_cast<UINT>(cardno),Mask1,Mask0);}
}
inline void _set_pause_list_not_cond (int cardno ,const UINT Mask1, const UINT Mask0) {
  if (cardno == -1) { return set_pause_list_not_cond(Mask1,Mask0);}
  else { return n_set_pause_list_not_cond (static_cast<UINT>(cardno),Mask1,Mask0);}
}
inline void _auto_change (int cardno ) {
  if (cardno == -1) { return auto_change();}
  else { return n_auto_change (static_cast<UINT>(cardno));}
}
inline void _stop_list (int cardno ) {
  if (cardno == -1) { return stop_list();}
  else { return n_stop_list (static_cast<UINT>(cardno));}
}
inline UINT _get_wait_status (int cardno ) {
  if (cardno == -1) { return get_wait_status();}
  else { return n_get_wait_status (static_cast<UINT>(cardno));}
}
inline UINT _read_status (int cardno ) {
  if (cardno == -1) { return read_status();}
  else { return n_read_status (static_cast<UINT>(cardno));}
}
inline void _get_status (int cardno ,UINT& Status, UINT& Pos) {
  if (cardno == -1) { return get_status(Status,Pos);}
  else { return n_get_status (static_cast<UINT>(cardno),Status,Pos);}
}
inline void _set_extstartpos (int cardno ,const UINT Pos) {
  if (cardno == -1) { return set_extstartpos(Pos);}
  else { return n_set_extstartpos (static_cast<UINT>(cardno),Pos);}
}
inline void _set_max_counts (int cardno ,const UINT Counts) {
  if (cardno == -1) { return set_max_counts(Counts);}
  else { return n_set_max_counts (static_cast<UINT>(cardno),Counts);}
}
inline void _set_control_mode (int cardno ,const UINT Mode) {
  if (cardno == -1) { return set_control_mode(Mode);}
  else { return n_set_control_mode (static_cast<UINT>(cardno),Mode);}
}
inline void _simulate_ext_stop (int cardno ) {
  if (cardno == -1) { return simulate_ext_stop();}
  else { return n_simulate_ext_stop (static_cast<UINT>(cardno));}
}
inline void _simulate_ext_start_ctrl (int cardno ) {
  if (cardno == -1) { return simulate_ext_start_ctrl();}
  else { return n_simulate_ext_start_ctrl (static_cast<UINT>(cardno));}
}
inline void _store_timestamp_counter (int cardno ) {
  if (cardno == -1) { return store_timestamp_counter();}
  else { return n_store_timestamp_counter (static_cast<UINT>(cardno));}
}
inline UINT _get_counts (int cardno ) {
  if (cardno == -1) { return get_counts();}
  else { return n_get_counts (static_cast<UINT>(cardno));}
}
inline UINT _get_startstop_info (int cardno ) {
  if (cardno == -1) { return get_startstop_info();}
  else { return n_get_startstop_info (static_cast<UINT>(cardno));}
}
inline void _copy_dst_src (int cardno ,const UINT Dst, const UINT Src, const UINT Mode) {
  if (cardno == -1) { return copy_dst_src(Dst,Src,Mode);}
  else { return n_copy_dst_src (static_cast<UINT>(cardno),Dst,Src,Mode);}
}
inline void _set_char_pointer (int cardno ,const UINT Char, const UINT Pos) {
  if (cardno == -1) { return set_char_pointer(Char,Pos);}
  else { return n_set_char_pointer (static_cast<UINT>(cardno),Char,Pos);}
}
inline void _set_sub_pointer (int cardno ,const UINT Index, const UINT Pos) {
  if (cardno == -1) { return set_sub_pointer(Index,Pos);}
  else { return n_set_sub_pointer (static_cast<UINT>(cardno),Index,Pos);}
}
inline void _set_text_table_pointer (int cardno ,const UINT Index, const UINT Pos) {
  if (cardno == -1) { return set_text_table_pointer(Index,Pos);}
  else { return n_set_text_table_pointer (static_cast<UINT>(cardno),Index,Pos);}
}
inline void _set_char_table (int cardno ,const UINT Index, const UINT Pos) {
  if (cardno == -1) { return set_char_table(Index,Pos);}
  else { return n_set_char_table (static_cast<UINT>(cardno),Index,Pos);}
}
inline UINT _get_char_pointer (int cardno ,const UINT Char) {
  if (cardno == -1) { return get_char_pointer(Char);}
  else { return n_get_char_pointer (static_cast<UINT>(cardno),Char);}
}
inline UINT _get_sub_pointer (int cardno ,const UINT Index) {
  if (cardno == -1) { return get_sub_pointer(Index);}
  else { return n_get_sub_pointer (static_cast<UINT>(cardno),Index);}
}
inline UINT _get_text_table_pointer (int cardno ,const UINT Index) {
  if (cardno == -1) { return get_text_table_pointer(Index);}
  else { return n_get_text_table_pointer (static_cast<UINT>(cardno),Index);}
}
inline void _time_update (int cardno ) {
  if (cardno == -1) { return time_update();}
  else { return n_time_update (static_cast<UINT>(cardno));}
}
inline void _time_control_eth (int cardno ,const double PPM) {
  if (cardno == -1) { return time_control_eth(PPM);}
  else { return n_time_control_eth (static_cast<UINT>(cardno),PPM);}
}
inline void _set_serial_step (int cardno ,const UINT No, const UINT Step) {
  if (cardno == -1) { return set_serial_step(No,Step);}
  else { return n_set_serial_step (static_cast<UINT>(cardno),No,Step);}
}
inline void _select_serial_set (int cardno ,const UINT No) {
  if (cardno == -1) { return select_serial_set(No);}
  else { return n_select_serial_set (static_cast<UINT>(cardno),No);}
}
inline void _set_serial (int cardno ,const UINT No) {
  if (cardno == -1) { return set_serial(No);}
  else { return n_set_serial (static_cast<UINT>(cardno),No);}
}
inline double _get_serial (int cardno ) {
  if (cardno == -1) { return get_serial();}
  else { return n_get_serial (static_cast<UINT>(cardno));}
}
inline double _get_list_serial (int cardno ,UINT& SetNo) {
  if (cardno == -1) { return get_list_serial(SetNo);}
  else { return n_get_list_serial (static_cast<UINT>(cardno),SetNo);}
}
inline void _write_io_port_mask (int cardno ,const UINT Value, const UINT Mask) {
  if (cardno == -1) { return write_io_port_mask(Value,Mask);}
  else { return n_write_io_port_mask (static_cast<UINT>(cardno),Value,Mask);}
}
inline void _write_8bit_port (int cardno ,const UINT Value) {
  if (cardno == -1) { return write_8bit_port(Value);}
  else { return n_write_8bit_port (static_cast<UINT>(cardno),Value);}
}
inline UINT _read_io_port (int cardno ) {
  if (cardno == -1) { return read_io_port();}
  else { return n_read_io_port (static_cast<UINT>(cardno));}
}
inline UINT _read_io_port_buffer (int cardno ,const UINT Index, UINT& Value, long& XPos, long& YPos, UINT& Time) {
  if (cardno == -1) { return read_io_port_buffer(Index,Value,XPos,YPos,Time);}
  else { return n_read_io_port_buffer (static_cast<UINT>(cardno),Index,Value,XPos,YPos,Time);}
}
inline UINT _get_io_status (int cardno ) {
  if (cardno == -1) { return get_io_status();}
  else { return n_get_io_status (static_cast<UINT>(cardno));}
}
inline UINT _read_analog_in (int cardno ) {
  if (cardno == -1) { return read_analog_in();}
  else { return n_read_analog_in (static_cast<UINT>(cardno));}
}
inline void _write_da_x (int cardno ,const UINT x, const UINT Value) {
  if (cardno == -1) { return write_da_x(x,Value);}
  else { return n_write_da_x (static_cast<UINT>(cardno),x,Value);}
}
inline void _set_laser_off_default (int cardno ,const UINT AnalogOut1, const UINT AnalogOut2, const UINT DigitalOut) {
  if (cardno == -1) { return set_laser_off_default(AnalogOut1,AnalogOut2,DigitalOut);}
  else { return n_set_laser_off_default (static_cast<UINT>(cardno),AnalogOut1,AnalogOut2,DigitalOut);}
}
inline void _set_port_default (int cardno ,const UINT Port, const UINT Value) {
  if (cardno == -1) { return set_port_default(Port,Value);}
  else { return n_set_port_default (static_cast<UINT>(cardno),Port,Value);}
}
inline void _write_io_port (int cardno ,const UINT Value) {
  if (cardno == -1) { return write_io_port(Value);}
  else { return n_write_io_port (static_cast<UINT>(cardno),Value);}
}
inline void _write_da_1 (int cardno ,const UINT Value) {
  if (cardno == -1) { return write_da_1(Value);}
  else { return n_write_da_1 (static_cast<UINT>(cardno),Value);}
}
inline void _write_da_2 (int cardno ,const UINT Value) {
  if (cardno == -1) { return write_da_2(Value);}
  else { return n_write_da_2 (static_cast<UINT>(cardno),Value);}
}
inline void _disable_laser (int cardno ) {
  if (cardno == -1) { return disable_laser();}
  else { return n_disable_laser (static_cast<UINT>(cardno));}
}
inline void _enable_laser (int cardno ) {
  if (cardno == -1) { return enable_laser();}
  else { return n_enable_laser (static_cast<UINT>(cardno));}
}
inline void _laser_signal_on (int cardno ) {
  if (cardno == -1) { return laser_signal_on();}
  else { return n_laser_signal_on (static_cast<UINT>(cardno));}
}
inline void _laser_signal_off (int cardno ) {
  if (cardno == -1) { return laser_signal_off();}
  else { return n_laser_signal_off (static_cast<UINT>(cardno));}
}
inline void _set_standby (int cardno ,const UINT HalfPeriod, const UINT PulseLength) {
  if (cardno == -1) { return set_standby(HalfPeriod,PulseLength);}
  else { return n_set_standby (static_cast<UINT>(cardno),HalfPeriod,PulseLength);}
}
inline void _set_laser_pulses_ctrl (int cardno ,const UINT HalfPeriod, const UINT PulseLength) {
  if (cardno == -1) { return set_laser_pulses_ctrl(HalfPeriod,PulseLength);}
  else { return n_set_laser_pulses_ctrl (static_cast<UINT>(cardno),HalfPeriod,PulseLength);}
}
inline void _set_firstpulse_killer (int cardno ,const UINT Length) {
  if (cardno == -1) { return set_firstpulse_killer(Length);}
  else { return n_set_firstpulse_killer (static_cast<UINT>(cardno),Length);}
}
inline void _set_qswitch_delay (int cardno ,const UINT Delay) {
  if (cardno == -1) { return set_qswitch_delay(Delay);}
  else { return n_set_qswitch_delay (static_cast<UINT>(cardno),Delay);}
}
inline void _set_laser_mode (int cardno ,const UINT Mode) {
  if (cardno == -1) { return set_laser_mode(Mode);}
  else { return n_set_laser_mode (static_cast<UINT>(cardno),Mode);}
}
inline void _set_laser_control (int cardno ,const UINT Ctrl) {
  if (cardno == -1) { return set_laser_control(Ctrl);}
  else { return n_set_laser_control (static_cast<UINT>(cardno),Ctrl);}
}
inline void _set_laser_pin_out (int cardno ,const UINT Pins) {
  if (cardno == -1) { return set_laser_pin_out(Pins);}
  else { return n_set_laser_pin_out (static_cast<UINT>(cardno),Pins);}
}
inline UINT _get_laser_pin_in (int cardno ) {
  if (cardno == -1) { return get_laser_pin_in();}
  else { return n_get_laser_pin_in (static_cast<UINT>(cardno));}
}
inline void _set_softstart_level (int cardno ,const UINT Index, const UINT Level) {
  if (cardno == -1) { return set_softstart_level(Index,Level);}
  else { return n_set_softstart_level (static_cast<UINT>(cardno),Index,Level);}
}
inline void _set_softstart_mode (int cardno ,const UINT Mode, const UINT Number, const UINT Delay) {
  if (cardno == -1) { return set_softstart_mode(Mode,Number,Delay);}
  else { return n_set_softstart_mode (static_cast<UINT>(cardno),Mode,Number,Delay);}
}
inline UINT _set_auto_laser_control (int cardno ,const UINT Ctrl, const UINT Value, const UINT Mode, const UINT MinValue, const UINT MaxValue) {
  if (cardno == -1) { return set_auto_laser_control(Ctrl,Value,Mode,MinValue,MaxValue);}
  else { return n_set_auto_laser_control (static_cast<UINT>(cardno),Ctrl,Value,Mode,MinValue,MaxValue);}
}
inline UINT _set_auto_laser_params (int cardno ,const UINT Ctrl, const UINT Value, const UINT MinValue, const UINT MaxValue) {
  if (cardno == -1) { return set_auto_laser_params(Ctrl,Value,MinValue,MaxValue);}
  else { return n_set_auto_laser_params (static_cast<UINT>(cardno),Ctrl,Value,MinValue,MaxValue);}
}
inline long _load_auto_laser_control (int cardno ,const char* Name, const UINT No) {
  if (cardno == -1) { return load_auto_laser_control(Name,No);}
  else { return n_load_auto_laser_control (static_cast<UINT>(cardno),Name,No);}
}
inline long _load_position_control (int cardno ,const char* Name, const UINT No) {
  if (cardno == -1) { return load_position_control(Name,No);}
  else { return n_load_position_control (static_cast<UINT>(cardno),Name,No);}
}
inline void _set_default_pixel (int cardno ,const UINT PulseLength) {
  if (cardno == -1) { return set_default_pixel(PulseLength);}
  else { return n_set_default_pixel (static_cast<UINT>(cardno),PulseLength);}
}
inline void _get_standby (int cardno ,UINT& HalfPeriod, UINT& PulseLength) {
  if (cardno == -1) { return get_standby(HalfPeriod,PulseLength);}
  else { return n_get_standby (static_cast<UINT>(cardno),HalfPeriod,PulseLength);}
}
inline void _set_pulse_picking (int cardno ,const UINT No) {
  if (cardno == -1) { return set_pulse_picking(No);}
  else { return n_set_pulse_picking (static_cast<UINT>(cardno),No);}
}
inline void _set_pulse_picking_length (int cardno ,const UINT Length) {
  if (cardno == -1) { return set_pulse_picking_length(Length);}
  else { return n_set_pulse_picking_length (static_cast<UINT>(cardno),Length);}
}
inline void _config_laser_signals (int cardno ,const UINT Config) {
  if (cardno == -1) { return config_laser_signals(Config);}
  else { return n_config_laser_signals (static_cast<UINT>(cardno),Config);}
}
inline void _set_laser_power (int cardno ,const UINT Port, const UINT Value) {
  if (cardno == -1) { return set_laser_power(Port,Value);}
  else { return n_set_laser_power (static_cast<UINT>(cardno),Port,Value);}
}
inline void _set_port_default_list (int cardno ,const UINT Port, const UINT Value) {
  if (cardno == -1) { return set_port_default_list(Port,Value);}
  else { return n_set_port_default_list (static_cast<UINT>(cardno),Port,Value);}
}
inline void _spot_distance_ctrl (int cardno ,const double Dist) {
  if (cardno == -1) { return spot_distance_ctrl(Dist);}
  else { return n_spot_distance_ctrl (static_cast<UINT>(cardno),Dist);}
}
inline void _set_ext_start_delay (int cardno ,const long Delay, const UINT EncoderNo) {
  if (cardno == -1) { return set_ext_start_delay(Delay,EncoderNo);}
  else { return n_set_ext_start_delay (static_cast<UINT>(cardno),Delay,EncoderNo);}
}
inline void _set_rot_center (int cardno ,const long X, const long Y) {
  if (cardno == -1) { return set_rot_center(X,Y);}
  else { return n_set_rot_center (static_cast<UINT>(cardno),X,Y);}
}
inline void _simulate_encoder (int cardno ,const UINT EncoderNo) {
  if (cardno == -1) { return simulate_encoder(EncoderNo);}
  else { return n_simulate_encoder (static_cast<UINT>(cardno),EncoderNo);}
}
inline UINT _get_marking_info (int cardno ) {
  if (cardno == -1) { return get_marking_info();}
  else { return n_get_marking_info (static_cast<UINT>(cardno));}
}
inline void _set_encoder_speed_ctrl (int cardno ,const UINT EncoderNo, const double Speed, const double Smooth) {
  if (cardno == -1) { return set_encoder_speed_ctrl(EncoderNo,Speed,Smooth);}
  else { return n_set_encoder_speed_ctrl (static_cast<UINT>(cardno),EncoderNo,Speed,Smooth);}
}
inline void _set_mcbsp_x (int cardno ,const double ScaleX) {
  if (cardno == -1) { return set_mcbsp_x(ScaleX);}
  else { return n_set_mcbsp_x (static_cast<UINT>(cardno),ScaleX);}
}
inline void _set_mcbsp_y (int cardno ,const double ScaleY) {
  if (cardno == -1) { return set_mcbsp_y(ScaleY);}
  else { return n_set_mcbsp_y (static_cast<UINT>(cardno),ScaleY);}
}
inline void _set_mcbsp_rot (int cardno ,const double Resolution) {
  if (cardno == -1) { return set_mcbsp_rot(Resolution);}
  else { return n_set_mcbsp_rot (static_cast<UINT>(cardno),Resolution);}
}
inline void _set_mcbsp_matrix (int cardno ) {
  if (cardno == -1) { return set_mcbsp_matrix();}
  else { return n_set_mcbsp_matrix (static_cast<UINT>(cardno));}
}
inline void _set_mcbsp_global_x (int cardno ,const double ScaleX) {
  if (cardno == -1) { return set_mcbsp_global_x(ScaleX);}
  else { return n_set_mcbsp_global_x (static_cast<UINT>(cardno),ScaleX);}
}
inline void _set_mcbsp_global_y (int cardno ,const double ScaleY) {
  if (cardno == -1) { return set_mcbsp_global_y(ScaleY);}
  else { return n_set_mcbsp_global_y (static_cast<UINT>(cardno),ScaleY);}
}
inline void _set_mcbsp_global_rot (int cardno ,const double Resolution) {
  if (cardno == -1) { return set_mcbsp_global_rot(Resolution);}
  else { return n_set_mcbsp_global_rot (static_cast<UINT>(cardno),Resolution);}
}
inline void _set_mcbsp_global_matrix (int cardno ) {
  if (cardno == -1) { return set_mcbsp_global_matrix();}
  else { return n_set_mcbsp_global_matrix (static_cast<UINT>(cardno));}
}
inline void _set_mcbsp_in (int cardno ,const UINT Mode, const double Scale) {
  if (cardno == -1) { return set_mcbsp_in(Mode,Scale);}
  else { return n_set_mcbsp_in (static_cast<UINT>(cardno),Mode,Scale);}
}
inline void _set_multi_mcbsp_in (int cardno ,const UINT Ctrl, const UINT P, const UINT Mode) {
  if (cardno == -1) { return set_multi_mcbsp_in(Ctrl,P,Mode);}
  else { return n_set_multi_mcbsp_in (static_cast<UINT>(cardno),Ctrl,P,Mode);}
}
inline void _set_fly_tracking_error (int cardno ,const UINT TrackingErrorX, const UINT TrackingErrorY) {
  if (cardno == -1) { return set_fly_tracking_error(TrackingErrorX,TrackingErrorY);}
  else { return n_set_fly_tracking_error (static_cast<UINT>(cardno),TrackingErrorX,TrackingErrorY);}
}
inline long _load_fly_2d_table (int cardno ,const char* Name, const UINT No) {
  if (cardno == -1) { return load_fly_2d_table(Name,No);}
  else { return n_load_fly_2d_table (static_cast<UINT>(cardno),Name,No);}
}
inline void _init_fly_2d (int cardno ,const long OffsetX, const long OffsetY, const UINT No) {
  if (cardno == -1) { return init_fly_2d(OffsetX,OffsetY,No);}
  else { return n_init_fly_2d (static_cast<UINT>(cardno),OffsetX,OffsetY,No);}
}
inline void _get_fly_2d_offset (int cardno ,long& OffsetX, long& OffsetY) {
  if (cardno == -1) { return get_fly_2d_offset(OffsetX,OffsetY);}
  else { return n_get_fly_2d_offset (static_cast<UINT>(cardno),OffsetX,OffsetY);}
}
inline void _get_encoder (int cardno ,long& Encoder0, long& Encoder1) {
  if (cardno == -1) { return get_encoder(Encoder0,Encoder1);}
  else { return n_get_encoder (static_cast<UINT>(cardno),Encoder0,Encoder1);}
}
inline void _read_encoder (int cardno ,long& Encoder0_1, long& Encoder1_1, long& Encoder0_2, long& Encoder1_2) {
  if (cardno == -1) { return read_encoder(Encoder0_1,Encoder1_1,Encoder0_2,Encoder1_2);}
  else { return n_read_encoder (static_cast<UINT>(cardno),Encoder0_1,Encoder1_1,Encoder0_2,Encoder1_2);}
}
inline long _get_mcbsp (int cardno ) {
  if (cardno == -1) { return get_mcbsp();}
  else { return n_get_mcbsp (static_cast<UINT>(cardno));}
}
inline long _read_mcbsp (int cardno ,const UINT No) {
  if (cardno == -1) { return read_mcbsp(No);}
  else { return n_read_mcbsp (static_cast<UINT>(cardno),No);}
}
inline long _read_multi_mcbsp (int cardno ,const UINT No) {
  if (cardno == -1) { return read_multi_mcbsp(No);}
  else { return n_read_multi_mcbsp (static_cast<UINT>(cardno),No);}
}
inline double _get_time (int cardno ) {
  if (cardno == -1) { return get_time();}
  else { return n_get_time (static_cast<UINT>(cardno));}
}
inline double _get_lap_time (int cardno ) {
  if (cardno == -1) { return get_lap_time();}
  else { return n_get_lap_time (static_cast<UINT>(cardno));}
}
inline void _measurement_status (int cardno ,UINT& Busy, UINT& Pos) {
  if (cardno == -1) { return measurement_status(Busy,Pos);}
  else { return n_measurement_status (static_cast<UINT>(cardno),Busy,Pos);}
}
inline void _get_waveform_offset (int cardno ,const UINT Channel, const UINT Offset, const UINT Number, const ULONG_PTR Ptr) {
  if (cardno == -1) { return get_waveform_offset(Channel,Offset,Number,Ptr);}
  else { return n_get_waveform_offset (static_cast<UINT>(cardno),Channel,Offset,Number,Ptr);}
}
inline void _get_waveform (int cardno ,const UINT Channel, const UINT Number, const ULONG_PTR Ptr) {
  if (cardno == -1) { return get_waveform(Channel,Number,Ptr);}
  else { return n_get_waveform (static_cast<UINT>(cardno),Channel,Number,Ptr);}
}
inline void _bounce_supp (int cardno ,const UINT Length) {
  if (cardno == -1) { return bounce_supp(Length);}
  else { return n_bounce_supp (static_cast<UINT>(cardno),Length);}
}
inline void _home_position_4 (int cardno ,const long X0Home, const long X1Home, const long X2Home, const long X3Home) {
  if (cardno == -1) { return home_position_4(X0Home,X1Home,X2Home,X3Home);}
  else { return n_home_position_4 (static_cast<UINT>(cardno),X0Home,X1Home,X2Home,X3Home);}
}
inline void _get_home_position_4 (int cardno ,long& X0Home, long& X1Home, long& X2Home, long& X3Home) {
  if (cardno == -1) { return get_home_position_4(X0Home,X1Home,X2Home,X3Home);}
  else { return n_get_home_position_4 (static_cast<UINT>(cardno),X0Home,X1Home,X2Home,X3Home);}
}
inline void _set_home_4_return_time (int cardno ,const UINT Time) {
  if (cardno == -1) { return set_home_4_return_time(Time);}
  else { return n_set_home_4_return_time (static_cast<UINT>(cardno),Time);}
}
inline UINT _get_home_4_return_time (int cardno ) {
  if (cardno == -1) { return get_home_4_return_time();}
  else { return n_get_home_4_return_time (static_cast<UINT>(cardno));}
}
inline void _home_position_xyz (int cardno ,const long XHome, const long YHome, const long ZHome) {
  if (cardno == -1) { return home_position_xyz(XHome,YHome,ZHome);}
  else { return n_home_position_xyz (static_cast<UINT>(cardno),XHome,YHome,ZHome);}
}
inline void _home_position (int cardno ,const long XHome, const long YHome) {
  if (cardno == -1) { return home_position(XHome,YHome);}
  else { return n_home_position (static_cast<UINT>(cardno),XHome,YHome);}
}
inline UINT _uart_config (int cardno ,const UINT BaudRate) {
  if (cardno == -1) { return uart_config(BaudRate);}
  else { return n_uart_config (static_cast<UINT>(cardno),BaudRate);}
}
inline void _rs232_config (int cardno ,const UINT BaudRate) {
  if (cardno == -1) { return rs232_config(BaudRate);}
  else { return n_rs232_config (static_cast<UINT>(cardno),BaudRate);}
}
inline void _rs232_write_data (int cardno ,const UINT Data) {
  if (cardno == -1) { return rs232_write_data(Data);}
  else { return n_rs232_write_data (static_cast<UINT>(cardno),Data);}
}
inline void _rs232_write_text (int cardno ,const char* pData) {
  if (cardno == -1) { return rs232_write_text(pData);}
  else { return n_rs232_write_text (static_cast<UINT>(cardno),pData);}
}
inline UINT _rs232_read_data (int cardno ) {
  if (cardno == -1) { return rs232_read_data();}
  else { return n_rs232_read_data (static_cast<UINT>(cardno));}
}
inline UINT _set_mcbsp_freq (int cardno ,const UINT Freq) {
  if (cardno == -1) { return set_mcbsp_freq(Freq);}
  else { return n_set_mcbsp_freq (static_cast<UINT>(cardno),Freq);}
}
inline void _mcbsp_init (int cardno ,const UINT XDelay, const UINT RDelay) {
  if (cardno == -1) { return mcbsp_init(XDelay,RDelay);}
  else { return n_mcbsp_init (static_cast<UINT>(cardno),XDelay,RDelay);}
}
inline void _mcbsp_init_spi (int cardno ,const UINT ClockLevel, const UINT ClockDelay) {
  if (cardno == -1) { return mcbsp_init_spi(ClockLevel,ClockDelay);}
  else { return n_mcbsp_init_spi (static_cast<UINT>(cardno),ClockLevel,ClockDelay);}
}
inline UINT _get_overrun (int cardno ) {
  if (cardno == -1) { return get_overrun();}
  else { return n_get_overrun (static_cast<UINT>(cardno));}
}
inline UINT _get_master_slave (int cardno ) {
  if (cardno == -1) { return get_master_slave();}
  else { return n_get_master_slave (static_cast<UINT>(cardno));}
}
inline void _get_transform (int cardno ,const UINT Number, const ULONG_PTR Ptr1, const ULONG_PTR Ptr2, const ULONG_PTR Ptr, const UINT Code) {
  if (cardno == -1) { return get_transform(Number,Ptr1,Ptr2,Ptr,Code);}
  else { return n_get_transform (static_cast<UINT>(cardno),Number,Ptr1,Ptr2,Ptr,Code);}
}
inline void _stop_trigger (int cardno ) {
  if (cardno == -1) { return stop_trigger();}
  else { return n_stop_trigger (static_cast<UINT>(cardno));}
}
inline void _move_to (int cardno ,const UINT Pos) {
  if (cardno == -1) { return move_to(Pos);}
  else { return n_move_to (static_cast<UINT>(cardno),Pos);}
}
inline void _set_enduring_wobbel (int cardno ,const UINT CenterX, const UINT CenterY, const UINT CenterZ, const UINT LimitHi, const UINT LimitLo, const double ScaleX, const double ScaleY, const double ScaleZ) {
  if (cardno == -1) { return set_enduring_wobbel(CenterX,CenterY,CenterZ,LimitHi,LimitLo,ScaleX,ScaleY,ScaleZ);}
  else { return n_set_enduring_wobbel (static_cast<UINT>(cardno),CenterX,CenterY,CenterZ,LimitHi,LimitLo,ScaleX,ScaleY,ScaleZ);}
}
inline void _set_enduring_wobbel_2 (int cardno ,const UINT CenterX, const UINT CenterY, const UINT CenterZ, const UINT LimitHi, const UINT LimitLo, const double ScaleX, const double ScaleY, const double ScaleZ) {
  if (cardno == -1) { return set_enduring_wobbel_2(CenterX,CenterY,CenterZ,LimitHi,LimitLo,ScaleX,ScaleY,ScaleZ);}
  else { return n_set_enduring_wobbel_2 (static_cast<UINT>(cardno),CenterX,CenterY,CenterZ,LimitHi,LimitLo,ScaleX,ScaleY,ScaleZ);}
}
inline void _set_free_variable (int cardno ,const UINT VarNo, const UINT Value) {
  if (cardno == -1) { return set_free_variable(VarNo,Value);}
  else { return n_set_free_variable (static_cast<UINT>(cardno),VarNo,Value);}
}
inline UINT _get_free_variable (int cardno ,const UINT VarNo) {
  if (cardno == -1) { return get_free_variable(VarNo);}
  else { return n_get_free_variable (static_cast<UINT>(cardno),VarNo);}
}
inline void _set_mcbsp_out_ptr (int cardno ,const UINT Number, const ULONG_PTR SignalPtr) {
  if (cardno == -1) { return set_mcbsp_out_ptr(Number,SignalPtr);}
  else { return n_set_mcbsp_out_ptr (static_cast<UINT>(cardno),Number,SignalPtr);}
}
inline void _periodic_toggle (int cardno ,const UINT Port, const UINT Mask, const UINT P1, const UINT P2, const UINT Count, const UINT Start) {
  if (cardno == -1) { return periodic_toggle(Port,Mask,P1,P2,Count,Start);}
  else { return n_periodic_toggle (static_cast<UINT>(cardno),Port,Mask,P1,P2,Count,Start);}
}
inline void _multi_axis_config (int cardno ,const UINT Cfg, const ULONG_PTR Ptr) {
  if (cardno == -1) { return multi_axis_config(Cfg,Ptr);}
  else { return n_multi_axis_config (static_cast<UINT>(cardno),Cfg,Ptr);}
}
inline void _quad_axis_init (int cardno ,const UINT Idle, const double X1, const double Y1) {
  if (cardno == -1) { return quad_axis_init(Idle,X1,Y1);}
  else { return n_quad_axis_init (static_cast<UINT>(cardno),Idle,X1,Y1);}
}
inline UINT _quad_axis_get_status (int cardno ) {
  if (cardno == -1) { return quad_axis_get_status();}
  else { return n_quad_axis_get_status (static_cast<UINT>(cardno));}
}
inline void _quad_axis_get_values (int cardno ,double& X1, double& Y1, UINT& Flags0, UINT& Flags1) {
  if (cardno == -1) { return quad_axis_get_values(X1,Y1,Flags0,Flags1);}
  else { return n_quad_axis_get_values (static_cast<UINT>(cardno),X1,Y1,Flags0,Flags1);}
}
inline void _set_defocus (int cardno ,const long Shift) {
  if (cardno == -1) { return set_defocus(Shift);}
  else { return n_set_defocus (static_cast<UINT>(cardno),Shift);}
}
inline void _set_defocus_offset (int cardno ,const long Shift) {
  if (cardno == -1) { return set_defocus_offset(Shift);}
  else { return n_set_defocus_offset (static_cast<UINT>(cardno),Shift);}
}
inline void _goto_xyz (int cardno ,const long X, const long Y, const long Z) {
  if (cardno == -1) { return goto_xyz(X,Y,Z);}
  else { return n_goto_xyz (static_cast<UINT>(cardno),X,Y,Z);}
}
inline void _goto_xy (int cardno ,const long X, const long Y) {
  if (cardno == -1) { return goto_xy(X,Y);}
  else { return n_goto_xy (static_cast<UINT>(cardno),X,Y);}
}
inline void _set_zoom (int cardno ,const UINT Zoom) {
  if (cardno == -1) { return set_zoom(Zoom);}
  else { return n_set_zoom (static_cast<UINT>(cardno),Zoom);}
}
inline long _get_z_distance (int cardno ,const long X, const long Y, const long Z) {
  if (cardno == -1) { return get_z_distance(X,Y,Z);}
  else { return n_get_z_distance (static_cast<UINT>(cardno),X,Y,Z);}
}
inline void _set_offset_xyz (int cardno ,const UINT HeadNo, const long XOffset, const long YOffset, const long ZOffset, const UINT at_once) {
  if (cardno == -1) { return set_offset_xyz(HeadNo,XOffset,YOffset,ZOffset,at_once);}
  else { return n_set_offset_xyz (static_cast<UINT>(cardno),HeadNo,XOffset,YOffset,ZOffset,at_once);}
}
inline void _set_offset (int cardno ,const UINT HeadNo, const long XOffset, const long YOffset, const UINT at_once) {
  if (cardno == -1) { return set_offset(HeadNo,XOffset,YOffset,at_once);}
  else { return n_set_offset (static_cast<UINT>(cardno),HeadNo,XOffset,YOffset,at_once);}
}
inline void _set_matrix (int cardno ,const UINT HeadNo, const double M11, const double M12, const double M21, const double M22, const UINT at_once) {
  if (cardno == -1) { return set_matrix(HeadNo,M11,M12,M21,M22,at_once);}
  else { return n_set_matrix (static_cast<UINT>(cardno),HeadNo,M11,M12,M21,M22,at_once);}
}
inline void _set_angle (int cardno ,const UINT HeadNo, const double Angle, const UINT at_once) {
  if (cardno == -1) { return set_angle(HeadNo,Angle,at_once);}
  else { return n_set_angle (static_cast<UINT>(cardno),HeadNo,Angle,at_once);}
}
inline void _set_scale (int cardno ,const UINT HeadNo, const double Scale, const UINT at_once) {
  if (cardno == -1) { return set_scale(HeadNo,Scale,at_once);}
  else { return n_set_scale (static_cast<UINT>(cardno),HeadNo,Scale,at_once);}
}
inline void _apply_mcbsp (int cardno ,const UINT HeadNo, const UINT at_once) {
  if (cardno == -1) { return apply_mcbsp(HeadNo,at_once);}
  else { return n_apply_mcbsp (static_cast<UINT>(cardno),HeadNo,at_once);}
}
inline UINT _upload_transform (int cardno ,const UINT HeadNo, const ULONG_PTR Ptr) {
  if (cardno == -1) { return upload_transform(HeadNo,Ptr);}
  else { return n_upload_transform (static_cast<UINT>(cardno),HeadNo,Ptr);}
}
inline void _set_delay_mode (int cardno ,const UINT VarPoly, const UINT DirectMove3D, const UINT EdgeLevel, const UINT MinJumpDelay, const UINT JumpLengthLimit) {
  if (cardno == -1) { return set_delay_mode(VarPoly,DirectMove3D,EdgeLevel,MinJumpDelay,JumpLengthLimit);}
  else { return n_set_delay_mode (static_cast<UINT>(cardno),VarPoly,DirectMove3D,EdgeLevel,MinJumpDelay,JumpLengthLimit);}
}
inline void _set_jump_speed_ctrl (int cardno ,const double Speed) {
  if (cardno == -1) { return set_jump_speed_ctrl(Speed);}
  else { return n_set_jump_speed_ctrl (static_cast<UINT>(cardno),Speed);}
}
inline void _set_mark_speed_ctrl (int cardno ,const double Speed) {
  if (cardno == -1) { return set_mark_speed_ctrl(Speed);}
  else { return n_set_mark_speed_ctrl (static_cast<UINT>(cardno),Speed);}
}
inline void _set_sky_writing_para (int cardno ,const double Timelag, const long LaserOnShift, const UINT Nprev, const UINT Npost) {
  if (cardno == -1) { return set_sky_writing_para(Timelag,LaserOnShift,Nprev,Npost);}
  else { return n_set_sky_writing_para (static_cast<UINT>(cardno),Timelag,LaserOnShift,Nprev,Npost);}
}
inline void _set_sky_writing_limit (int cardno ,const double CosAngle) {
  if (cardno == -1) { return set_sky_writing_limit(CosAngle);}
  else { return n_set_sky_writing_limit (static_cast<UINT>(cardno),CosAngle);}
}
inline void _set_sky_writing_mode (int cardno ,const UINT Mode) {
  if (cardno == -1) { return set_sky_writing_mode(Mode);}
  else { return n_set_sky_writing_mode (static_cast<UINT>(cardno),Mode);}
}
inline long _load_varpolydelay (int cardno ,const char* Name, const UINT No) {
  if (cardno == -1) { return load_varpolydelay(Name,No);}
  else { return n_load_varpolydelay (static_cast<UINT>(cardno),Name,No);}
}
inline void _set_hi (int cardno ,const UINT HeadNo, const double GalvoGainX, const double GalvoGainY, const long GalvoOffsetX, const long GalvoOffsetY) {
  if (cardno == -1) { return set_hi(HeadNo,GalvoGainX,GalvoGainY,GalvoOffsetX,GalvoOffsetY);}
  else { return n_set_hi (static_cast<UINT>(cardno),HeadNo,GalvoGainX,GalvoGainY,GalvoOffsetX,GalvoOffsetY);}
}
inline void _get_hi_pos (int cardno ,const UINT HeadNo, long& X1, long& X2, long& Y1, long& Y2) {
  if (cardno == -1) { return get_hi_pos(HeadNo,X1,X2,Y1,Y2);}
  else { return n_get_hi_pos (static_cast<UINT>(cardno),HeadNo,X1,X2,Y1,Y2);}
}
inline UINT _auto_cal (int cardno ,const UINT HeadNo, const UINT Command) {
  if (cardno == -1) { return auto_cal(HeadNo,Command);}
  else { return n_auto_cal (static_cast<UINT>(cardno),HeadNo,Command);}
}
inline UINT _get_auto_cal (int cardno ,const UINT HeadNo) {
  if (cardno == -1) { return get_auto_cal(HeadNo);}
  else { return n_get_auto_cal (static_cast<UINT>(cardno),HeadNo);}
}
inline UINT _write_hi_pos (int cardno ,const UINT HeadNo, const long X1, const long X2, const long Y1, const long Y2) {
  if (cardno == -1) { return write_hi_pos(HeadNo,X1,X2,Y1,Y2);}
  else { return n_write_hi_pos (static_cast<UINT>(cardno),HeadNo,X1,X2,Y1,Y2);}
}
inline void _set_timelag_compensation (int cardno ,const UINT HeadNo, const UINT TimeLagXY, const UINT TimeLagZ) {
  if (cardno == -1) { return set_timelag_compensation(HeadNo,TimeLagXY,TimeLagZ);}
  else { return n_set_timelag_compensation (static_cast<UINT>(cardno),HeadNo,TimeLagXY,TimeLagZ);}
}
inline void _set_sky_writing (int cardno ,const double Timelag, const long LaserOnShift) {
  if (cardno == -1) { return set_sky_writing(Timelag,LaserOnShift);}
  else { return n_set_sky_writing (static_cast<UINT>(cardno),Timelag,LaserOnShift);}
}
inline void _get_hi_data (int cardno ,long& X1, long& X2, long& Y1, long& Y2) {
  if (cardno == -1) { return get_hi_data(X1,X2,Y1,Y2);}
  else { return n_get_hi_data (static_cast<UINT>(cardno),X1,X2,Y1,Y2);}
}
inline void _send_user_data (int cardno ,const UINT Head, const UINT Axis, const long Data0, const long Data1, const long Data2, const long Data3, const long Data4) {
  if (cardno == -1) { return send_user_data(Head,Axis,Data0,Data1,Data2,Data3,Data4);}
  else { return n_send_user_data (static_cast<UINT>(cardno),Head,Axis,Data0,Data1,Data2,Data3,Data4);}
}
inline long _read_user_data (int cardno ,const UINT Head, const UINT Axis, long& Data0, long& Data1, long& Data2, long& Data3, long& Data4) {
  if (cardno == -1) { return read_user_data(Head,Axis,Data0,Data1,Data2,Data3,Data4);}
  else { return n_read_user_data (static_cast<UINT>(cardno),Head,Axis,Data0,Data1,Data2,Data3,Data4);}
}
inline void _control_command (int cardno ,const UINT Head, const UINT Axis, const UINT Data) {
  if (cardno == -1) { return control_command(Head,Axis,Data);}
  else { return n_control_command (static_cast<UINT>(cardno),Head,Axis,Data);}
}
inline long _get_value (int cardno ,const UINT Signal) {
  if (cardno == -1) { return get_value(Signal);}
  else { return n_get_value (static_cast<UINT>(cardno),Signal);}
}
inline void _get_values (int cardno ,const ULONG_PTR SignalPtr, const ULONG_PTR ResultPtr) {
  if (cardno == -1) { return get_values(SignalPtr,ResultPtr);}
  else { return n_get_values (static_cast<UINT>(cardno),SignalPtr,ResultPtr);}
}
inline void _get_galvo_controls (int cardno ,const ULONG_PTR SignalPtr, const ULONG_PTR ResultPtr) {
  if (cardno == -1) { return get_galvo_controls(SignalPtr,ResultPtr);}
  else { return n_get_galvo_controls (static_cast<UINT>(cardno),SignalPtr,ResultPtr);}
}
inline UINT _get_head_status (int cardno ,const UINT Head) {
  if (cardno == -1) { return get_head_status(Head);}
  else { return n_get_head_status (static_cast<UINT>(cardno),Head);}
}
inline long _set_jump_mode (int cardno ,const long Flag, const UINT Length, const long VA1, const long VA2, const long VB1, const long VB2, const long JA1, const long JA2, const long JB1, const long JB2) {
  if (cardno == -1) { return set_jump_mode(Flag,Length,VA1,VA2,VB1,VB2,JA1,JA2,JB1,JB2);}
  else { return n_set_jump_mode (static_cast<UINT>(cardno),Flag,Length,VA1,VA2,VB1,VB2,JA1,JA2,JB1,JB2);}
}
inline long _load_jump_table_offset (int cardno ,const char* Name, const UINT No, const UINT PosAck, const long Offset, const UINT MinDelay, const UINT MaxDelay, const UINT ListPos) {
  if (cardno == -1) { return load_jump_table_offset(Name,No,PosAck,Offset,MinDelay,MaxDelay,ListPos);}
  else { return n_load_jump_table_offset (static_cast<UINT>(cardno),Name,No,PosAck,Offset,MinDelay,MaxDelay,ListPos);}
}
inline UINT _get_jump_table (int cardno ,const ULONG_PTR Ptr) {
  if (cardno == -1) { return get_jump_table(Ptr);}
  else { return n_get_jump_table (static_cast<UINT>(cardno),Ptr);}
}
inline UINT _set_jump_table (int cardno ,const ULONG_PTR Ptr) {
  if (cardno == -1) { return set_jump_table(Ptr);}
  else { return n_set_jump_table (static_cast<UINT>(cardno),Ptr);}
}
inline long _load_jump_table (int cardno ,const char* Name, const UINT No, const UINT PosAck, const UINT MinDelay, const UINT MaxDelay, const UINT ListPos) {
  if (cardno == -1) { return load_jump_table(Name,No,PosAck,MinDelay,MaxDelay,ListPos);}
  else { return n_load_jump_table (static_cast<UINT>(cardno),Name,No,PosAck,MinDelay,MaxDelay,ListPos);}
}
inline UINT _get_scanahead_params (int cardno ,const UINT HeadNo, UINT& PreViewTime, UINT& Vmax, double& Amax) {
  if (cardno == -1) { return get_scanahead_params(HeadNo,PreViewTime,Vmax,Amax);}
  else { return n_get_scanahead_params (static_cast<UINT>(cardno),HeadNo,PreViewTime,Vmax,Amax);}
}
inline long _activate_scanahead_autodelays (int cardno ,const long Mode) {
  if (cardno == -1) { return activate_scanahead_autodelays(Mode);}
  else { return n_activate_scanahead_autodelays (static_cast<UINT>(cardno),Mode);}
}
inline void _set_scanahead_laser_shifts (int cardno ,const long dLasOn, const long dLasOff) {
  if (cardno == -1) { return set_scanahead_laser_shifts(dLasOn,dLasOff);}
  else { return n_set_scanahead_laser_shifts (static_cast<UINT>(cardno),dLasOn,dLasOff);}
}
inline void _set_scanahead_line_params (int cardno ,const UINT CornerScale, const UINT EndScale, const UINT AccScale) {
  if (cardno == -1) { return set_scanahead_line_params(CornerScale,EndScale,AccScale);}
  else { return n_set_scanahead_line_params (static_cast<UINT>(cardno),CornerScale,EndScale,AccScale);}
}
inline void _set_scanahead_line_params_ex (int cardno ,const UINT CornerScale, const UINT EndScale, const UINT AccScale, const UINT JumpScale) {
  if (cardno == -1) { return set_scanahead_line_params_ex(CornerScale,EndScale,AccScale,JumpScale);}
  else { return n_set_scanahead_line_params_ex (static_cast<UINT>(cardno),CornerScale,EndScale,AccScale,JumpScale);}
}
inline UINT _set_scanahead_params (int cardno ,const UINT Mode, const UINT HeadNo, const UINT TableNo, const UINT PreViewTime, const UINT Vmax, const double Amax) {
  if (cardno == -1) { return set_scanahead_params(Mode,HeadNo,TableNo,PreViewTime,Vmax,Amax);}
  else { return n_set_scanahead_params (static_cast<UINT>(cardno),Mode,HeadNo,TableNo,PreViewTime,Vmax,Amax);}
}
inline void _set_scanahead_speed_control (int cardno ,const UINT Mode) {
  if (cardno == -1) { return set_scanahead_speed_control(Mode);}
  else { return n_set_scanahead_speed_control (static_cast<UINT>(cardno),Mode);}
}
inline void _stepper_init (int cardno ,const UINT No, const UINT Period, const long Dir, const long Pos, const UINT Tol, const UINT Enable, const UINT WaitTime) {
  if (cardno == -1) { return stepper_init(No,Period,Dir,Pos,Tol,Enable,WaitTime);}
  else { return n_stepper_init (static_cast<UINT>(cardno),No,Period,Dir,Pos,Tol,Enable,WaitTime);}
}
inline void _stepper_enable (int cardno ,const long Enable1, const long Enable2) {
  if (cardno == -1) { return stepper_enable(Enable1,Enable2);}
  else { return n_stepper_enable (static_cast<UINT>(cardno),Enable1,Enable2);}
}
inline void _stepper_disable_switch (int cardno ,const long Disable1, const long Disable2) {
  if (cardno == -1) { return stepper_disable_switch(Disable1,Disable2);}
  else { return n_stepper_disable_switch (static_cast<UINT>(cardno),Disable1,Disable2);}
}
inline void _stepper_control (int cardno ,const long Period1, const long Period2) {
  if (cardno == -1) { return stepper_control(Period1,Period2);}
  else { return n_stepper_control (static_cast<UINT>(cardno),Period1,Period2);}
}
inline void _stepper_abs_no (int cardno ,const UINT No, const long Pos, const UINT WaitTime) {
  if (cardno == -1) { return stepper_abs_no(No,Pos,WaitTime);}
  else { return n_stepper_abs_no (static_cast<UINT>(cardno),No,Pos,WaitTime);}
}
inline void _stepper_rel_no (int cardno ,const UINT No, const long dPos, const UINT WaitTime) {
  if (cardno == -1) { return stepper_rel_no(No,dPos,WaitTime);}
  else { return n_stepper_rel_no (static_cast<UINT>(cardno),No,dPos,WaitTime);}
}
inline void _stepper_abs (int cardno ,const long Pos1, const long Pos2, const UINT WaitTime) {
  if (cardno == -1) { return stepper_abs(Pos1,Pos2,WaitTime);}
  else { return n_stepper_abs (static_cast<UINT>(cardno),Pos1,Pos2,WaitTime);}
}
inline void _stepper_rel (int cardno ,const long dPos1, const long dPos2, const UINT WaitTime) {
  if (cardno == -1) { return stepper_rel(dPos1,dPos2,WaitTime);}
  else { return n_stepper_rel (static_cast<UINT>(cardno),dPos1,dPos2,WaitTime);}
}
inline void _get_stepper_status (int cardno ,UINT& Status1, long& Pos1, UINT& Status2, long& Pos2) {
  if (cardno == -1) { return get_stepper_status(Status1,Pos1,Status2,Pos2);}
  else { return n_get_stepper_status (static_cast<UINT>(cardno),Status1,Pos1,Status2,Pos2);}
}
inline void _select_cor_table_list (int cardno ,const UINT HeadA, const UINT HeadB) {
  if (cardno == -1) { return select_cor_table_list(HeadA,HeadB);}
  else { return n_select_cor_table_list (static_cast<UINT>(cardno),HeadA,HeadB);}
}
inline void _list_nop (int cardno ) {
  if (cardno == -1) { return list_nop();}
  else { return n_list_nop (static_cast<UINT>(cardno));}
}
inline void _list_continue (int cardno ) {
  if (cardno == -1) { return list_continue();}
  else { return n_list_continue (static_cast<UINT>(cardno));}
}
inline void _list_next (int cardno ) {
  if (cardno == -1) { return list_next();}
  else { return n_list_next (static_cast<UINT>(cardno));}
}
inline void _long_delay (int cardno ,const UINT Delay) {
  if (cardno == -1) { return long_delay(Delay);}
  else { return n_long_delay (static_cast<UINT>(cardno),Delay);}
}
inline void _set_end_of_list (int cardno ) {
  if (cardno == -1) { return set_end_of_list();}
  else { return n_set_end_of_list (static_cast<UINT>(cardno));}
}
inline void _set_wait (int cardno ,const UINT WaitWord) {
  if (cardno == -1) { return set_wait(WaitWord);}
  else { return n_set_wait (static_cast<UINT>(cardno),WaitWord);}
}
inline void _list_jump_pos (int cardno ,const UINT Pos) {
  if (cardno == -1) { return list_jump_pos(Pos);}
  else { return n_list_jump_pos (static_cast<UINT>(cardno),Pos);}
}
inline void _list_jump_rel (int cardno ,const long Pos) {
  if (cardno == -1) { return list_jump_rel(Pos);}
  else { return n_list_jump_rel (static_cast<UINT>(cardno),Pos);}
}
inline void _list_repeat (int cardno ) {
  if (cardno == -1) { return list_repeat();}
  else { return n_list_repeat (static_cast<UINT>(cardno));}
}
inline void _list_until (int cardno ,const UINT Number) {
  if (cardno == -1) { return list_until(Number);}
  else { return n_list_until (static_cast<UINT>(cardno),Number);}
}
inline void _range_checking (int cardno ,const UINT HeadNo, const UINT Mode, const UINT Data) {
  if (cardno == -1) { return range_checking(HeadNo,Mode,Data);}
  else { return n_range_checking (static_cast<UINT>(cardno),HeadNo,Mode,Data);}
}
inline void _store_timestamp_counter_list (int cardno ) {
  if (cardno == -1) { return store_timestamp_counter_list();}
  else { return n_store_timestamp_counter_list (static_cast<UINT>(cardno));}
}
inline void _wait_for_timestamp_counter (int cardno ,const UINT TimeStampCounter) {
  if (cardno == -1) { return wait_for_timestamp_counter(TimeStampCounter);}
  else { return n_wait_for_timestamp_counter (static_cast<UINT>(cardno),TimeStampCounter);}
}
inline void _set_list_jump (int cardno ,const UINT Pos) {
  if (cardno == -1) { return set_list_jump(Pos);}
  else { return n_set_list_jump (static_cast<UINT>(cardno),Pos);}
}
inline void _set_extstartpos_list (int cardno ,const UINT Pos) {
  if (cardno == -1) { return set_extstartpos_list(Pos);}
  else { return n_set_extstartpos_list (static_cast<UINT>(cardno),Pos);}
}
inline void _set_control_mode_list (int cardno ,const UINT Mode) {
  if (cardno == -1) { return set_control_mode_list(Mode);}
  else { return n_set_control_mode_list (static_cast<UINT>(cardno),Mode);}
}
inline void _simulate_ext_start (int cardno ,const long Delay, const UINT EncoderNo) {
  if (cardno == -1) { return simulate_ext_start(Delay,EncoderNo);}
  else { return n_simulate_ext_start (static_cast<UINT>(cardno),Delay,EncoderNo);}
}
inline void _list_return (int cardno ) {
  if (cardno == -1) { return list_return();}
  else { return n_list_return (static_cast<UINT>(cardno));}
}
inline void _list_call_repeat (int cardno ,const UINT Pos, const UINT Number) {
  if (cardno == -1) { return list_call_repeat(Pos,Number);}
  else { return n_list_call_repeat (static_cast<UINT>(cardno),Pos,Number);}
}
inline void _list_call_abs_repeat (int cardno ,const UINT Pos, const UINT Number) {
  if (cardno == -1) { return list_call_abs_repeat(Pos,Number);}
  else { return n_list_call_abs_repeat (static_cast<UINT>(cardno),Pos,Number);}
}
inline void _list_call (int cardno ,const UINT Pos) {
  if (cardno == -1) { return list_call(Pos);}
  else { return n_list_call (static_cast<UINT>(cardno),Pos);}
}
inline void _list_call_abs (int cardno ,const UINT Pos) {
  if (cardno == -1) { return list_call_abs(Pos);}
  else { return n_list_call_abs (static_cast<UINT>(cardno),Pos);}
}
inline void _sub_call_repeat (int cardno ,const UINT Index, const UINT Number) {
  if (cardno == -1) { return sub_call_repeat(Index,Number);}
  else { return n_sub_call_repeat (static_cast<UINT>(cardno),Index,Number);}
}
inline void _sub_call_abs_repeat (int cardno ,const UINT Index, const UINT Number) {
  if (cardno == -1) { return sub_call_abs_repeat(Index,Number);}
  else { return n_sub_call_abs_repeat (static_cast<UINT>(cardno),Index,Number);}
}
inline void _sub_call (int cardno ,const UINT Index) {
  if (cardno == -1) { return sub_call(Index);}
  else { return n_sub_call (static_cast<UINT>(cardno),Index);}
}
inline void _sub_call_abs (int cardno ,const UINT Index) {
  if (cardno == -1) { return sub_call_abs(Index);}
  else { return n_sub_call_abs (static_cast<UINT>(cardno),Index);}
}
inline void _list_call_cond (int cardno ,const UINT Mask1, const UINT Mask0, const UINT Pos) {
  if (cardno == -1) { return list_call_cond(Mask1,Mask0,Pos);}
  else { return n_list_call_cond (static_cast<UINT>(cardno),Mask1,Mask0,Pos);}
}
inline void _list_call_abs_cond (int cardno ,const UINT Mask1, const UINT Mask0, const UINT Pos) {
  if (cardno == -1) { return list_call_abs_cond(Mask1,Mask0,Pos);}
  else { return n_list_call_abs_cond (static_cast<UINT>(cardno),Mask1,Mask0,Pos);}
}
inline void _sub_call_cond (int cardno ,const UINT Mask1, const UINT Mask0, const UINT Index) {
  if (cardno == -1) { return sub_call_cond(Mask1,Mask0,Index);}
  else { return n_sub_call_cond (static_cast<UINT>(cardno),Mask1,Mask0,Index);}
}
inline void _sub_call_abs_cond (int cardno ,const UINT Mask1, const UINT Mask0, const UINT Index) {
  if (cardno == -1) { return sub_call_abs_cond(Mask1,Mask0,Index);}
  else { return n_sub_call_abs_cond (static_cast<UINT>(cardno),Mask1,Mask0,Index);}
}
inline void _list_jump_pos_cond (int cardno ,const UINT Mask1, const UINT Mask0, const UINT Pos) {
  if (cardno == -1) { return list_jump_pos_cond(Mask1,Mask0,Pos);}
  else { return n_list_jump_pos_cond (static_cast<UINT>(cardno),Mask1,Mask0,Pos);}
}
inline void _list_jump_rel_cond (int cardno ,const UINT Mask1, const UINT Mask0, const long Pos) {
  if (cardno == -1) { return list_jump_rel_cond(Mask1,Mask0,Pos);}
  else { return n_list_jump_rel_cond (static_cast<UINT>(cardno),Mask1,Mask0,Pos);}
}
inline void _if_cond (int cardno ,const UINT Mask1, const UINT Mask0) {
  if (cardno == -1) { return if_cond(Mask1,Mask0);}
  else { return n_if_cond (static_cast<UINT>(cardno),Mask1,Mask0);}
}
inline void _if_not_cond (int cardno ,const UINT Mask1, const UINT Mask0) {
  if (cardno == -1) { return if_not_cond(Mask1,Mask0);}
  else { return n_if_not_cond (static_cast<UINT>(cardno),Mask1,Mask0);}
}
inline void _if_pin_cond (int cardno ,const UINT Mask1, const UINT Mask0) {
  if (cardno == -1) { return if_pin_cond(Mask1,Mask0);}
  else { return n_if_pin_cond (static_cast<UINT>(cardno),Mask1,Mask0);}
}
inline void _if_not_pin_cond (int cardno ,const UINT Mask1, const UINT Mask0) {
  if (cardno == -1) { return if_not_pin_cond(Mask1,Mask0);}
  else { return n_if_not_pin_cond (static_cast<UINT>(cardno),Mask1,Mask0);}
}
inline void _switch_ioport (int cardno ,const UINT MaskBits, const UINT ShiftBits) {
  if (cardno == -1) { return switch_ioport(MaskBits,ShiftBits);}
  else { return n_switch_ioport (static_cast<UINT>(cardno),MaskBits,ShiftBits);}
}
inline void _list_jump_cond (int cardno ,const UINT Mask1, const UINT Mask0, const UINT Pos) {
  if (cardno == -1) { return list_jump_cond(Mask1,Mask0,Pos);}
  else { return n_list_jump_cond (static_cast<UINT>(cardno),Mask1,Mask0,Pos);}
}
inline void _select_char_set (int cardno ,const UINT No) {
  if (cardno == -1) { return select_char_set(No);}
  else { return n_select_char_set (static_cast<UINT>(cardno),No);}
}
inline void _mark_text (int cardno ,const char* Text) {
  if (cardno == -1) { return mark_text(Text);}
  else { return n_mark_text (static_cast<UINT>(cardno),Text);}
}
inline void _mark_text_abs (int cardno ,const char* Text) {
  if (cardno == -1) { return mark_text_abs(Text);}
  else { return n_mark_text_abs (static_cast<UINT>(cardno),Text);}
}
inline void _mark_char (int cardno ,const UINT Char) {
  if (cardno == -1) { return mark_char(Char);}
  else { return n_mark_char (static_cast<UINT>(cardno),Char);}
}
inline void _mark_char_abs (int cardno ,const UINT Char) {
  if (cardno == -1) { return mark_char_abs(Char);}
  else { return n_mark_char_abs (static_cast<UINT>(cardno),Char);}
}
inline void _mark_serial (int cardno ,const UINT Mode, const UINT Digits) {
  if (cardno == -1) { return mark_serial(Mode,Digits);}
  else { return n_mark_serial (static_cast<UINT>(cardno),Mode,Digits);}
}
inline void _mark_serial_abs (int cardno ,const UINT Mode, const UINT Digits) {
  if (cardno == -1) { return mark_serial_abs(Mode,Digits);}
  else { return n_mark_serial_abs (static_cast<UINT>(cardno),Mode,Digits);}
}
inline void _mark_date (int cardno ,const UINT Part, const UINT Mode) {
  if (cardno == -1) { return mark_date(Part,Mode);}
  else { return n_mark_date (static_cast<UINT>(cardno),Part,Mode);}
}
inline void _mark_date_abs (int cardno ,const UINT Part, const UINT Mode) {
  if (cardno == -1) { return mark_date_abs(Part,Mode);}
  else { return n_mark_date_abs (static_cast<UINT>(cardno),Part,Mode);}
}
inline void _mark_time (int cardno ,const UINT Part, const UINT Mode) {
  if (cardno == -1) { return mark_time(Part,Mode);}
  else { return n_mark_time (static_cast<UINT>(cardno),Part,Mode);}
}
inline void _mark_time_abs (int cardno ,const UINT Part, const UINT Mode) {
  if (cardno == -1) { return mark_time_abs(Part,Mode);}
  else { return n_mark_time_abs (static_cast<UINT>(cardno),Part,Mode);}
}
inline void _time_fix_f_off (int cardno ,const UINT FirstDay, const UINT Offset) {
  if (cardno == -1) { return time_fix_f_off(FirstDay,Offset);}
  else { return n_time_fix_f_off (static_cast<UINT>(cardno),FirstDay,Offset);}
}
inline void _select_serial_set_list (int cardno ,const UINT No) {
  if (cardno == -1) { return select_serial_set_list(No);}
  else { return n_select_serial_set_list (static_cast<UINT>(cardno),No);}
}
inline void _set_serial_step_list (int cardno ,const UINT No, const UINT Step) {
  if (cardno == -1) { return set_serial_step_list(No,Step);}
  else { return n_set_serial_step_list (static_cast<UINT>(cardno),No,Step);}
}
inline void _time_fix_f (int cardno ,const UINT FirstDay) {
  if (cardno == -1) { return time_fix_f(FirstDay);}
  else { return n_time_fix_f (static_cast<UINT>(cardno),FirstDay);}
}
inline void _time_fix (int cardno ) {
  if (cardno == -1) { return time_fix();}
  else { return n_time_fix (static_cast<UINT>(cardno));}
}
inline void _clear_io_cond_list (int cardno ,const UINT Mask1, const UINT Mask0, const UINT MaskClear) {
  if (cardno == -1) { return clear_io_cond_list(Mask1,Mask0,MaskClear);}
  else { return n_clear_io_cond_list (static_cast<UINT>(cardno),Mask1,Mask0,MaskClear);}
}
inline void _set_io_cond_list (int cardno ,const UINT Mask1, const UINT Mask0, const UINT MaskSet) {
  if (cardno == -1) { return set_io_cond_list(Mask1,Mask0,MaskSet);}
  else { return n_set_io_cond_list (static_cast<UINT>(cardno),Mask1,Mask0,MaskSet);}
}
inline void _write_io_port_mask_list (int cardno ,const UINT Value, const UINT Mask) {
  if (cardno == -1) { return write_io_port_mask_list(Value,Mask);}
  else { return n_write_io_port_mask_list (static_cast<UINT>(cardno),Value,Mask);}
}
inline void _write_8bit_port_list (int cardno ,const UINT Value) {
  if (cardno == -1) { return write_8bit_port_list(Value);}
  else { return n_write_8bit_port_list (static_cast<UINT>(cardno),Value);}
}
inline void _read_io_port_list (int cardno ) {
  if (cardno == -1) { return read_io_port_list();}
  else { return n_read_io_port_list (static_cast<UINT>(cardno));}
}
inline void _write_da_x_list (int cardno ,const UINT x, const UINT Value) {
  if (cardno == -1) { return write_da_x_list(x,Value);}
  else { return n_write_da_x_list (static_cast<UINT>(cardno),x,Value);}
}
inline void _write_io_port_list (int cardno ,const UINT Value) {
  if (cardno == -1) { return write_io_port_list(Value);}
  else { return n_write_io_port_list (static_cast<UINT>(cardno),Value);}
}
inline void _write_da_1_list (int cardno ,const UINT Value) {
  if (cardno == -1) { return write_da_1_list(Value);}
  else { return n_write_da_1_list (static_cast<UINT>(cardno),Value);}
}
inline void _write_da_2_list (int cardno ,const UINT Value) {
  if (cardno == -1) { return write_da_2_list(Value);}
  else { return n_write_da_2_list (static_cast<UINT>(cardno),Value);}
}
inline void _laser_signal_on_list (int cardno ) {
  if (cardno == -1) { return laser_signal_on_list();}
  else { return n_laser_signal_on_list (static_cast<UINT>(cardno));}
}
inline void _laser_signal_off_list (int cardno ) {
  if (cardno == -1) { return laser_signal_off_list();}
  else { return n_laser_signal_off_list (static_cast<UINT>(cardno));}
}
inline void _para_laser_on_pulses_list (int cardno ,const UINT Period, const UINT Pulses, const UINT P) {
  if (cardno == -1) { return para_laser_on_pulses_list(Period,Pulses,P);}
  else { return n_para_laser_on_pulses_list (static_cast<UINT>(cardno),Period,Pulses,P);}
}
inline void _laser_on_pulses_list (int cardno ,const UINT Period, const UINT Pulses) {
  if (cardno == -1) { return laser_on_pulses_list(Period,Pulses);}
  else { return n_laser_on_pulses_list (static_cast<UINT>(cardno),Period,Pulses);}
}
inline void _laser_on_list (int cardno ,const UINT Period) {
  if (cardno == -1) { return laser_on_list(Period);}
  else { return n_laser_on_list (static_cast<UINT>(cardno),Period);}
}
inline void _set_laser_delays (int cardno ,const long LaserOnDelay, const UINT LaserOffDelay) {
  if (cardno == -1) { return set_laser_delays(LaserOnDelay,LaserOffDelay);}
  else { return n_set_laser_delays (static_cast<UINT>(cardno),LaserOnDelay,LaserOffDelay);}
}
inline void _set_standby_list (int cardno ,const UINT HalfPeriod, const UINT PulseLength) {
  if (cardno == -1) { return set_standby_list(HalfPeriod,PulseLength);}
  else { return n_set_standby_list (static_cast<UINT>(cardno),HalfPeriod,PulseLength);}
}
inline void _set_laser_pulses (int cardno ,const UINT HalfPeriod, const UINT PulseLength) {
  if (cardno == -1) { return set_laser_pulses(HalfPeriod,PulseLength);}
  else { return n_set_laser_pulses (static_cast<UINT>(cardno),HalfPeriod,PulseLength);}
}
inline void _set_firstpulse_killer_list (int cardno ,const UINT Length) {
  if (cardno == -1) { return set_firstpulse_killer_list(Length);}
  else { return n_set_firstpulse_killer_list (static_cast<UINT>(cardno),Length);}
}
inline void _set_qswitch_delay_list (int cardno ,const UINT Delay) {
  if (cardno == -1) { return set_qswitch_delay_list(Delay);}
  else { return n_set_qswitch_delay_list (static_cast<UINT>(cardno),Delay);}
}
inline void _set_laser_pin_out_list (int cardno ,const UINT Pins) {
  if (cardno == -1) { return set_laser_pin_out_list(Pins);}
  else { return n_set_laser_pin_out_list (static_cast<UINT>(cardno),Pins);}
}
inline void _set_vector_control (int cardno ,const UINT Ctrl, const UINT Value) {
  if (cardno == -1) { return set_vector_control(Ctrl,Value);}
  else { return n_set_vector_control (static_cast<UINT>(cardno),Ctrl,Value);}
}
inline void _set_default_pixel_list (int cardno ,const UINT PulseLength) {
  if (cardno == -1) { return set_default_pixel_list(PulseLength);}
  else { return n_set_default_pixel_list (static_cast<UINT>(cardno),PulseLength);}
}
inline void _set_auto_laser_params_list (int cardno ,const UINT Ctrl, const UINT Value, const UINT MinValue, const UINT MaxValue) {
  if (cardno == -1) { return set_auto_laser_params_list(Ctrl,Value,MinValue,MaxValue);}
  else { return n_set_auto_laser_params_list (static_cast<UINT>(cardno),Ctrl,Value,MinValue,MaxValue);}
}
inline void _set_pulse_picking_list (int cardno ,const UINT No) {
  if (cardno == -1) { return set_pulse_picking_list(No);}
  else { return n_set_pulse_picking_list (static_cast<UINT>(cardno),No);}
}
inline void _set_softstart_level_list (int cardno ,const UINT Index, const UINT Level1, const UINT Level2, const UINT Level3) {
  if (cardno == -1) { return set_softstart_level_list(Index,Level1,Level2,Level3);}
  else { return n_set_softstart_level_list (static_cast<UINT>(cardno),Index,Level1,Level2,Level3);}
}
inline void _set_softstart_mode_list (int cardno ,const UINT Mode, const UINT Number, const UINT Delay) {
  if (cardno == -1) { return set_softstart_mode_list(Mode,Number,Delay);}
  else { return n_set_softstart_mode_list (static_cast<UINT>(cardno),Mode,Number,Delay);}
}
inline void _config_laser_signals_list (int cardno ,const UINT Config) {
  if (cardno == -1) { return config_laser_signals_list(Config);}
  else { return n_config_laser_signals_list (static_cast<UINT>(cardno),Config);}
}
inline void _spot_distance (int cardno ,const double Dist) {
  if (cardno == -1) { return spot_distance(Dist);}
  else { return n_spot_distance (static_cast<UINT>(cardno),Dist);}
}
inline void _set_laser_timing (int cardno ,const UINT HalfPeriod, const UINT PulseLength1, const UINT PulseLength2, const UINT TimeBase) {
  if (cardno == -1) { return set_laser_timing(HalfPeriod,PulseLength1,PulseLength2,TimeBase);}
  else { return n_set_laser_timing (static_cast<UINT>(cardno),HalfPeriod,PulseLength1,PulseLength2,TimeBase);}
}
inline void _fly_return_z (int cardno ,const long X, const long Y, const long Z) {
  if (cardno == -1) { return fly_return_z(X,Y,Z);}
  else { return n_fly_return_z (static_cast<UINT>(cardno),X,Y,Z);}
}
inline void _fly_return (int cardno ,const long X, const long Y) {
  if (cardno == -1) { return fly_return(X,Y);}
  else { return n_fly_return (static_cast<UINT>(cardno),X,Y);}
}
inline void _set_rot_center_list (int cardno ,const long X, const long Y) {
  if (cardno == -1) { return set_rot_center_list(X,Y);}
  else { return n_set_rot_center_list (static_cast<UINT>(cardno),X,Y);}
}
inline void _set_ext_start_delay_list (int cardno ,const long Delay, const UINT EncoderNo) {
  if (cardno == -1) { return set_ext_start_delay_list(Delay,EncoderNo);}
  else { return n_set_ext_start_delay_list (static_cast<UINT>(cardno),Delay,EncoderNo);}
}
inline void _set_fly_x (int cardno ,const double ScaleX) {
  if (cardno == -1) { return set_fly_x(ScaleX);}
  else { return n_set_fly_x (static_cast<UINT>(cardno),ScaleX);}
}
inline void _set_fly_y (int cardno ,const double ScaleY) {
  if (cardno == -1) { return set_fly_y(ScaleY);}
  else { return n_set_fly_y (static_cast<UINT>(cardno),ScaleY);}
}
inline void _set_fly_z (int cardno ,const double ScaleZ, const UINT EncoderNo) {
  if (cardno == -1) { return set_fly_z(ScaleZ,EncoderNo);}
  else { return n_set_fly_z (static_cast<UINT>(cardno),ScaleZ,EncoderNo);}
}
inline void _set_fly_rot (int cardno ,const double Resolution) {
  if (cardno == -1) { return set_fly_rot(Resolution);}
  else { return n_set_fly_rot (static_cast<UINT>(cardno),Resolution);}
}
inline void _set_fly_2d (int cardno ,const double ScaleX, const double ScaleY) {
  if (cardno == -1) { return set_fly_2d(ScaleX,ScaleY);}
  else { return n_set_fly_2d (static_cast<UINT>(cardno),ScaleX,ScaleY);}
}
inline void _set_fly_x_pos (int cardno ,const double ScaleX) {
  if (cardno == -1) { return set_fly_x_pos(ScaleX);}
  else { return n_set_fly_x_pos (static_cast<UINT>(cardno),ScaleX);}
}
inline void _set_fly_y_pos (int cardno ,const double ScaleY) {
  if (cardno == -1) { return set_fly_y_pos(ScaleY);}
  else { return n_set_fly_y_pos (static_cast<UINT>(cardno),ScaleY);}
}
inline void _set_fly_rot_pos (int cardno ,const double Resolution) {
  if (cardno == -1) { return set_fly_rot_pos(Resolution);}
  else { return n_set_fly_rot_pos (static_cast<UINT>(cardno),Resolution);}
}
inline void _set_fly_limits (int cardno ,const long Xmin, const long Xmax, const long Ymin, const long Ymax) {
  if (cardno == -1) { return set_fly_limits(Xmin,Xmax,Ymin,Ymax);}
  else { return n_set_fly_limits (static_cast<UINT>(cardno),Xmin,Xmax,Ymin,Ymax);}
}
inline void _set_fly_limits_z (int cardno ,const long Zmin, const long Zmax) {
  if (cardno == -1) { return set_fly_limits_z(Zmin,Zmax);}
  else { return n_set_fly_limits_z (static_cast<UINT>(cardno),Zmin,Zmax);}
}
inline void _if_fly_x_overflow (int cardno ,const long Mode) {
  if (cardno == -1) { return if_fly_x_overflow(Mode);}
  else { return n_if_fly_x_overflow (static_cast<UINT>(cardno),Mode);}
}
inline void _if_fly_y_overflow (int cardno ,const long Mode) {
  if (cardno == -1) { return if_fly_y_overflow(Mode);}
  else { return n_if_fly_y_overflow (static_cast<UINT>(cardno),Mode);}
}
inline void _if_fly_z_overflow (int cardno ,const long Mode) {
  if (cardno == -1) { return if_fly_z_overflow(Mode);}
  else { return n_if_fly_z_overflow (static_cast<UINT>(cardno),Mode);}
}
inline void _if_not_fly_x_overflow (int cardno ,const long Mode) {
  if (cardno == -1) { return if_not_fly_x_overflow(Mode);}
  else { return n_if_not_fly_x_overflow (static_cast<UINT>(cardno),Mode);}
}
inline void _if_not_fly_y_overflow (int cardno ,const long Mode) {
  if (cardno == -1) { return if_not_fly_y_overflow(Mode);}
  else { return n_if_not_fly_y_overflow (static_cast<UINT>(cardno),Mode);}
}
inline void _if_not_fly_z_overflow (int cardno ,const long Mode) {
  if (cardno == -1) { return if_not_fly_z_overflow(Mode);}
  else { return n_if_not_fly_z_overflow (static_cast<UINT>(cardno),Mode);}
}
inline void _clear_fly_overflow (int cardno ,const UINT Mode) {
  if (cardno == -1) { return clear_fly_overflow(Mode);}
  else { return n_clear_fly_overflow (static_cast<UINT>(cardno),Mode);}
}
inline void _set_mcbsp_x_list (int cardno ,const double ScaleX) {
  if (cardno == -1) { return set_mcbsp_x_list(ScaleX);}
  else { return n_set_mcbsp_x_list (static_cast<UINT>(cardno),ScaleX);}
}
inline void _set_mcbsp_y_list (int cardno ,const double ScaleY) {
  if (cardno == -1) { return set_mcbsp_y_list(ScaleY);}
  else { return n_set_mcbsp_y_list (static_cast<UINT>(cardno),ScaleY);}
}
inline void _set_mcbsp_rot_list (int cardno ,const double Resolution) {
  if (cardno == -1) { return set_mcbsp_rot_list(Resolution);}
  else { return n_set_mcbsp_rot_list (static_cast<UINT>(cardno),Resolution);}
}
inline void _set_mcbsp_matrix_list (int cardno ) {
  if (cardno == -1) { return set_mcbsp_matrix_list();}
  else { return n_set_mcbsp_matrix_list (static_cast<UINT>(cardno));}
}
inline void _set_mcbsp_global_x_list (int cardno ,const double ScaleX) {
  if (cardno == -1) { return set_mcbsp_global_x_list(ScaleX);}
  else { return n_set_mcbsp_global_x_list (static_cast<UINT>(cardno),ScaleX);}
}
inline void _set_mcbsp_global_y_list (int cardno ,const double ScaleY) {
  if (cardno == -1) { return set_mcbsp_global_y_list(ScaleY);}
  else { return n_set_mcbsp_global_y_list (static_cast<UINT>(cardno),ScaleY);}
}
inline void _set_mcbsp_global_rot_list (int cardno ,const double Resolution) {
  if (cardno == -1) { return set_mcbsp_global_rot_list(Resolution);}
  else { return n_set_mcbsp_global_rot_list (static_cast<UINT>(cardno),Resolution);}
}
inline void _set_mcbsp_global_matrix_list (int cardno ) {
  if (cardno == -1) { return set_mcbsp_global_matrix_list();}
  else { return n_set_mcbsp_global_matrix_list (static_cast<UINT>(cardno));}
}
inline void _set_mcbsp_in_list (int cardno ,const UINT Mode, const double Scale) {
  if (cardno == -1) { return set_mcbsp_in_list(Mode,Scale);}
  else { return n_set_mcbsp_in_list (static_cast<UINT>(cardno),Mode,Scale);}
}
inline void _set_multi_mcbsp_in_list (int cardno ,const UINT Ctrl, const UINT P, const UINT Mode) {
  if (cardno == -1) { return set_multi_mcbsp_in_list(Ctrl,P,Mode);}
  else { return n_set_multi_mcbsp_in_list (static_cast<UINT>(cardno),Ctrl,P,Mode);}
}
inline void _wait_for_encoder_mode (int cardno ,const long Value, const UINT EncoderNo, const long Mode) {
  if (cardno == -1) { return wait_for_encoder_mode(Value,EncoderNo,Mode);}
  else { return n_wait_for_encoder_mode (static_cast<UINT>(cardno),Value,EncoderNo,Mode);}
}
inline void _wait_for_mcbsp (int cardno ,const UINT Axis, const long Value, const long Mode) {
  if (cardno == -1) { return wait_for_mcbsp(Axis,Value,Mode);}
  else { return n_wait_for_mcbsp (static_cast<UINT>(cardno),Axis,Value,Mode);}
}
inline void _set_encoder_speed (int cardno ,const UINT EncoderNo, const double Speed, const double Smooth) {
  if (cardno == -1) { return set_encoder_speed(EncoderNo,Speed,Smooth);}
  else { return n_set_encoder_speed (static_cast<UINT>(cardno),EncoderNo,Speed,Smooth);}
}
inline void _get_mcbsp_list (int cardno ) {
  if (cardno == -1) { return get_mcbsp_list();}
  else { return n_get_mcbsp_list (static_cast<UINT>(cardno));}
}
inline void _store_encoder (int cardno ,const UINT Pos) {
  if (cardno == -1) { return store_encoder(Pos);}
  else { return n_store_encoder (static_cast<UINT>(cardno),Pos);}
}
inline void _wait_for_encoder_in_range_mode (int cardno ,const long EncXmin, const long EncXmax, const long EncYmin, const long EncYmax, const UINT Mode) {
  if (cardno == -1) { return wait_for_encoder_in_range_mode(EncXmin,EncXmax,EncYmin,EncYmax,Mode);}
  else { return n_wait_for_encoder_in_range_mode (static_cast<UINT>(cardno),EncXmin,EncXmax,EncYmin,EncYmax,Mode);}
}
inline void _wait_for_encoder_in_range (int cardno ,const long EncXmin, const long EncXmax, const long EncYmin, const long EncYmax) {
  if (cardno == -1) { return wait_for_encoder_in_range(EncXmin,EncXmax,EncYmin,EncYmax);}
  else { return n_wait_for_encoder_in_range (static_cast<UINT>(cardno),EncXmin,EncXmax,EncYmin,EncYmax);}
}
inline void _activate_fly_xy (int cardno ,const double ScaleX, const double ScaleY) {
  if (cardno == -1) { return activate_fly_xy(ScaleX,ScaleY);}
  else { return n_activate_fly_xy (static_cast<UINT>(cardno),ScaleX,ScaleY);}
}
inline void _activate_fly_2d (int cardno ,const double ScaleX, const double ScaleY) {
  if (cardno == -1) { return activate_fly_2d(ScaleX,ScaleY);}
  else { return n_activate_fly_2d (static_cast<UINT>(cardno),ScaleX,ScaleY);}
}
inline void _activate_fly_xy_encoder (int cardno ,const double ScaleX, const double ScaleY, const long EncX, const long EncY) {
  if (cardno == -1) { return activate_fly_xy_encoder(ScaleX,ScaleY,EncX,EncY);}
  else { return n_activate_fly_xy_encoder (static_cast<UINT>(cardno),ScaleX,ScaleY,EncX,EncY);}
}
inline void _activate_fly_2d_encoder (int cardno ,const double ScaleX, const double ScaleY, const long EncX, const long EncY) {
  if (cardno == -1) { return activate_fly_2d_encoder(ScaleX,ScaleY,EncX,EncY);}
  else { return n_activate_fly_2d_encoder (static_cast<UINT>(cardno),ScaleX,ScaleY,EncX,EncY);}
}
inline void _if_not_activated (int cardno ) {
  if (cardno == -1) { return if_not_activated();}
  else { return n_if_not_activated (static_cast<UINT>(cardno));}
}
inline void _park_position (int cardno ,const UINT Mode, const long X, const long Y) {
  if (cardno == -1) { return park_position(Mode,X,Y);}
  else { return n_park_position (static_cast<UINT>(cardno),Mode,X,Y);}
}
inline void _park_return (int cardno ,const UINT Mode, const long X, const long Y) {
  if (cardno == -1) { return park_return(Mode,X,Y);}
  else { return n_park_return (static_cast<UINT>(cardno),Mode,X,Y);}
}
inline void _fly_prediction (int cardno ,UINT PredictionX, UINT PredictionY) {
  if (cardno == -1) { return fly_prediction(PredictionX,PredictionY);}
  else { return n_fly_prediction (static_cast<UINT>(cardno),PredictionX,PredictionY);}
}
inline void _set_fly_1_axis (int cardno ,const UINT Axis, const UINT Mode, const double Scale) {
  if (cardno == -1) { return set_fly_1_axis(Axis,Mode,Scale);}
  else { return n_set_fly_1_axis (static_cast<UINT>(cardno),Axis,Mode,Scale);}
}
inline void _fly_return_1_axis (int cardno ,const UINT Axis, const long RetPos) {
  if (cardno == -1) { return fly_return_1_axis(Axis,RetPos);}
  else { return n_fly_return_1_axis (static_cast<UINT>(cardno),Axis,RetPos);}
}
inline void _wait_for_1_axis (int cardno ,const long Value, const UINT EncoderMode, const long WaitMode, const UINT LaserMode) {
  if (cardno == -1) { return wait_for_1_axis(Value,EncoderMode,WaitMode,LaserMode);}
  else { return n_wait_for_1_axis (static_cast<UINT>(cardno),Value,EncoderMode,WaitMode,LaserMode);}
}
inline void _activate_fly_1_axis (int cardno ,const UINT Axis, const UINT Mode, const double Scale, const long Offset) {
  if (cardno == -1) { return activate_fly_1_axis(Axis,Mode,Scale,Offset);}
  else { return n_activate_fly_1_axis (static_cast<UINT>(cardno),Axis,Mode,Scale,Offset);}
}
inline void _park_position_1_axis (int cardno ,const UINT Mode, const UINT Axis, const long ParkPos) {
  if (cardno == -1) { return park_position_1_axis(Mode,Axis,ParkPos);}
  else { return n_park_position_1_axis (static_cast<UINT>(cardno),Mode,Axis,ParkPos);}
}
inline void _park_return_1_axis (int cardno ,const UINT Mode, const UINT Axis, const long RetPos) {
  if (cardno == -1) { return park_return_1_axis(Mode,Axis,RetPos);}
  else { return n_park_return_1_axis (static_cast<UINT>(cardno),Mode,Axis,RetPos);}
}
inline void _set_fly_2_axes (int cardno ,const UINT Axis1, const UINT Mode1, const double Scale1, const UINT Axis2, const UINT Mode2, const double Scale2) {
  if (cardno == -1) { return set_fly_2_axes(Axis1,Mode1,Scale1,Axis2,Mode2,Scale2);}
  else { return n_set_fly_2_axes (static_cast<UINT>(cardno),Axis1,Mode1,Scale1,Axis2,Mode2,Scale2);}
}
inline void _fly_return_2_axes (int cardno ,const UINT Axis1, const long RetPos1, const UINT Axis2, const long RetPos2) {
  if (cardno == -1) { return fly_return_2_axes(Axis1,RetPos1,Axis2,RetPos2);}
  else { return n_fly_return_2_axes (static_cast<UINT>(cardno),Axis1,RetPos1,Axis2,RetPos2);}
}
inline void _wait_for_2_axes (int cardno ,const UINT EncoderModeX, const long MinValueX, const long MaxValueX, const UINT EncoderModeY, const long MinValueY, const long MaxValueY, const long WaitMode, const UINT LaserMode) {
  if (cardno == -1) { return wait_for_2_axes(EncoderModeX,MinValueX,MaxValueX,EncoderModeY,MinValueY,MaxValueY,WaitMode,LaserMode);}
  else { return n_wait_for_2_axes (static_cast<UINT>(cardno),EncoderModeX,MinValueX,MaxValueX,EncoderModeY,MinValueY,MaxValueY,WaitMode,LaserMode);}
}
inline void _activate_fly_2_axes (int cardno ,const UINT ModeX, const double ScaleX, const long OffsetX, const UINT ModeY, const double ScaleY, const long OffsetY) {
  if (cardno == -1) { return activate_fly_2_axes(ModeX,ScaleX,OffsetX,ModeY,ScaleY,OffsetY);}
  else { return n_activate_fly_2_axes (static_cast<UINT>(cardno),ModeX,ScaleX,OffsetX,ModeY,ScaleY,OffsetY);}
}
inline void _park_position_2_axes (int cardno ,const UINT Mode, const long ParkPosX, const long ParkPosY) {
  if (cardno == -1) { return park_position_2_axes(Mode,ParkPosX,ParkPosY);}
  else { return n_park_position_2_axes (static_cast<UINT>(cardno),Mode,ParkPosX,ParkPosY);}
}
inline void _park_return_2_axes (int cardno ,const UINT Mode, const long RetPosX, const long RetPosY) {
  if (cardno == -1) { return park_return_2_axes(Mode,RetPosX,RetPosY);}
  else { return n_park_return_2_axes (static_cast<UINT>(cardno),Mode,RetPosX,RetPosY);}
}
inline void _set_fly_3_axes (int cardno ,const UINT ModeX, const double ScaleX, const UINT ModeY, const double ScaleY, const UINT ModeZ, const double ScaleZ) {
  if (cardno == -1) { return set_fly_3_axes(ModeX,ScaleX,ModeY,ScaleY,ModeZ,ScaleZ);}
  else { return n_set_fly_3_axes (static_cast<UINT>(cardno),ModeX,ScaleX,ModeY,ScaleY,ModeZ,ScaleZ);}
}
inline void _fly_return_3_axes (int cardno ,const long RetPosX, const long RetPosY, const long RetPosZ) {
  if (cardno == -1) { return fly_return_3_axes(RetPosX,RetPosY,RetPosZ);}
  else { return n_fly_return_3_axes (static_cast<UINT>(cardno),RetPosX,RetPosY,RetPosZ);}
}
inline void _wait_for_encoder (int cardno ,const long Value, const UINT EncoderNo) {
  if (cardno == -1) { return wait_for_encoder(Value,EncoderNo);}
  else { return n_wait_for_encoder (static_cast<UINT>(cardno),Value,EncoderNo);}
}
inline void _save_and_restart_timer (int cardno ) {
  if (cardno == -1) { return save_and_restart_timer();}
  else { return n_save_and_restart_timer (static_cast<UINT>(cardno));}
}
inline void _set_wobbel_mode_phase (int cardno ,const UINT Transversal, const UINT Longitudinal, const double Freq, const long Mode, const double Phase) {
  if (cardno == -1) { return set_wobbel_mode_phase(Transversal,Longitudinal,Freq,Mode,Phase);}
  else { return n_set_wobbel_mode_phase (static_cast<UINT>(cardno),Transversal,Longitudinal,Freq,Mode,Phase);}
}
inline void _set_wobbel_mode (int cardno ,const UINT Transversal, const UINT Longitudinal, const double Freq, const long Mode) {
  if (cardno == -1) { return set_wobbel_mode(Transversal,Longitudinal,Freq,Mode);}
  else { return n_set_wobbel_mode (static_cast<UINT>(cardno),Transversal,Longitudinal,Freq,Mode);}
}
inline void _set_wobbel (int cardno ,const UINT Transversal, const UINT Longitudinal, const double Freq) {
  if (cardno == -1) { return set_wobbel(Transversal,Longitudinal,Freq);}
  else { return n_set_wobbel (static_cast<UINT>(cardno),Transversal,Longitudinal,Freq);}
}
inline void _set_wobbel_direction (int cardno ,const long dX, const long dY) {
  if (cardno == -1) { return set_wobbel_direction(dX,dY);}
  else { return n_set_wobbel_direction (static_cast<UINT>(cardno),dX,dY);}
}
inline void _set_wobbel_control (int cardno ,const UINT Ctrl, const UINT Value, const UINT MinValue, const UINT MaxValue) {
  if (cardno == -1) { return set_wobbel_control(Ctrl,Value,MinValue,MaxValue);}
  else { return n_set_wobbel_control (static_cast<UINT>(cardno),Ctrl,Value,MinValue,MaxValue);}
}
inline void _set_wobbel_vector (int cardno ,const double dTrans, const double dLong, const UINT Period, const double dPower) {
  if (cardno == -1) { return set_wobbel_vector(dTrans,dLong,Period,dPower);}
  else { return n_set_wobbel_vector (static_cast<UINT>(cardno),dTrans,dLong,Period,dPower);}
}
inline void _set_wobbel_offset (int cardno ,const long OffsetTrans, const long OffsetLong) {
  if (cardno == -1) { return set_wobbel_offset(OffsetTrans,OffsetLong);}
  else { return n_set_wobbel_offset (static_cast<UINT>(cardno),OffsetTrans,OffsetLong);}
}
inline void _set_trigger (int cardno ,const UINT Period, const UINT Signal1, const UINT Signal2) {
  if (cardno == -1) { return set_trigger(Period,Signal1,Signal2);}
  else { return n_set_trigger (static_cast<UINT>(cardno),Period,Signal1,Signal2);}
}
inline void _set_trigger4 (int cardno ,const UINT Period, const UINT Signal1, const UINT Signal2, const UINT Signal3, const UINT Signal4) {
  if (cardno == -1) { return set_trigger4(Period,Signal1,Signal2,Signal3,Signal4);}
  else { return n_set_trigger4 (static_cast<UINT>(cardno),Period,Signal1,Signal2,Signal3,Signal4);}
}
inline void _set_pixel_line_3d (int cardno ,const UINT Channel, const UINT HalfPeriod, const double dX, const double dY, const double dZ) {
  if (cardno == -1) { return set_pixel_line_3d(Channel,HalfPeriod,dX,dY,dZ);}
  else { return n_set_pixel_line_3d (static_cast<UINT>(cardno),Channel,HalfPeriod,dX,dY,dZ);}
}
inline void _set_pixel_line (int cardno ,const UINT Channel, const UINT HalfPeriod, const double dX, const double dY) {
  if (cardno == -1) { return set_pixel_line(Channel,HalfPeriod,dX,dY);}
  else { return n_set_pixel_line (static_cast<UINT>(cardno),Channel,HalfPeriod,dX,dY);}
}
inline void _set_n_pixel (int cardno ,const UINT PortOutValue1, const UINT PortOutValue2, const UINT Number) {
  if (cardno == -1) { return set_n_pixel(PortOutValue1,PortOutValue2,Number);}
  else { return n_set_n_pixel (static_cast<UINT>(cardno),PortOutValue1,PortOutValue2,Number);}
}
inline void _set_pixel (int cardno ,const UINT PortOutValue1, const UINT PortOutValue2) {
  if (cardno == -1) { return set_pixel(PortOutValue1,PortOutValue2);}
  else { return n_set_pixel (static_cast<UINT>(cardno),PortOutValue1,PortOutValue2);}
}
inline void _rs232_write_text_list (int cardno ,const char* pData) {
  if (cardno == -1) { return rs232_write_text_list(pData);}
  else { return n_rs232_write_text_list (static_cast<UINT>(cardno),pData);}
}
inline void _set_mcbsp_out (int cardno ,const UINT Signal1, const UINT Signal2) {
  if (cardno == -1) { return set_mcbsp_out(Signal1,Signal2);}
  else { return n_set_mcbsp_out (static_cast<UINT>(cardno),Signal1,Signal2);}
}
inline void _camming (int cardno ,const UINT FirstPos, const UINT NPos, const UINT No, const UINT Ctrl, const double Scale, const UINT Code) {
  if (cardno == -1) { return camming(FirstPos,NPos,No,Ctrl,Scale,Code);}
  else { return n_camming (static_cast<UINT>(cardno),FirstPos,NPos,No,Ctrl,Scale,Code);}
}
inline void _periodic_toggle_list (int cardno ,const UINT Port, const UINT Mask, const UINT P1, const UINT P2, const UINT Count, const UINT Start) {
  if (cardno == -1) { return periodic_toggle_list(Port,Mask,P1,P2,Count,Start);}
  else { return n_periodic_toggle_list (static_cast<UINT>(cardno),Port,Mask,P1,P2,Count,Start);}
}
inline void _micro_vector_abs_3d (int cardno ,const long X, const long Y, const long Z, const long LasOn, const long LasOff) {
  if (cardno == -1) { return micro_vector_abs_3d(X,Y,Z,LasOn,LasOff);}
  else { return n_micro_vector_abs_3d (static_cast<UINT>(cardno),X,Y,Z,LasOn,LasOff);}
}
inline void _micro_vector_rel_3d (int cardno ,const long dX, const long dY, const long dZ, const long LasOn, const long LasOff) {
  if (cardno == -1) { return micro_vector_rel_3d(dX,dY,dZ,LasOn,LasOff);}
  else { return n_micro_vector_rel_3d (static_cast<UINT>(cardno),dX,dY,dZ,LasOn,LasOff);}
}
inline void _micro_vector_abs (int cardno ,const long X, const long Y, const long LasOn, const long LasOff) {
  if (cardno == -1) { return micro_vector_abs(X,Y,LasOn,LasOff);}
  else { return n_micro_vector_abs (static_cast<UINT>(cardno),X,Y,LasOn,LasOff);}
}
inline void _micro_vector_rel (int cardno ,const long dX, const long dY, const long LasOn, const long LasOff) {
  if (cardno == -1) { return micro_vector_rel(dX,dY,LasOn,LasOff);}
  else { return n_micro_vector_rel (static_cast<UINT>(cardno),dX,dY,LasOn,LasOff);}
}
inline void _micro_vector_quad_axis_v_2 (int cardno ,const long X0, const long Y0, const long X1, const long Y1, const long LasOn, const long LasOff, const UINT Power, const UINT Port, const UINT Flags, const double Velocity) {
  if (cardno == -1) { return micro_vector_quad_axis_v_2(X0,Y0,X1,Y1,LasOn,LasOff,Power,Port,Flags,Velocity);}
  else { return n_micro_vector_quad_axis_v_2 (static_cast<UINT>(cardno),X0,Y0,X1,Y1,LasOn,LasOff,Power,Port,Flags,Velocity);}
}
inline void _micro_vector_quad_axis_v (int cardno ,const long X0, const long Y0, const double X1, const double Y1, const long LasOn, const long LasOff, const UINT Power, const UINT Port, const UINT Flags, const double Velocity) {
  if (cardno == -1) { return micro_vector_quad_axis_v(X0,Y0,X1,Y1,LasOn,LasOff,Power,Port,Flags,Velocity);}
  else { return n_micro_vector_quad_axis_v (static_cast<UINT>(cardno),X0,Y0,X1,Y1,LasOn,LasOff,Power,Port,Flags,Velocity);}
}
inline void _micro_vector_quad_axis (int cardno ,const long X0, const long Y0, const double X1, const double Y1, const long LasOn, const long LasOff, const UINT Power, const UINT Port, const UINT Flags) {
  if (cardno == -1) { return micro_vector_quad_axis(X0,Y0,X1,Y1,LasOn,LasOff,Power,Port,Flags);}
  else { return n_micro_vector_quad_axis (static_cast<UINT>(cardno),X0,Y0,X1,Y1,LasOn,LasOff,Power,Port,Flags);}
}
inline void _micro_vector_set_position (int cardno ,const long X0, const long X1, const long X2, const long X3, const long LasOn, const long LasOff) {
  if (cardno == -1) { return micro_vector_set_position(X0,X1,X2,X3,LasOn,LasOff);}
  else { return n_micro_vector_set_position (static_cast<UINT>(cardno),X0,X1,X2,X3,LasOn,LasOff);}
}
inline void _multi_axis_flags (int cardno ,const UINT Flags) {
  if (cardno == -1) { return multi_axis_flags(Flags);}
  else { return n_multi_axis_flags (static_cast<UINT>(cardno),Flags);}
}
inline void _set_free_variable_list (int cardno ,const UINT VarNo, const UINT Value) {
  if (cardno == -1) { return set_free_variable_list(VarNo,Value);}
  else { return n_set_free_variable_list (static_cast<UINT>(cardno),VarNo,Value);}
}
inline void _jump_abs_drill_2 (int cardno ,const long X, const long Y, const UINT DrillTime, const long XOff, const long YOff) {
  if (cardno == -1) { return jump_abs_drill_2(X,Y,DrillTime,XOff,YOff);}
  else { return n_jump_abs_drill_2 (static_cast<UINT>(cardno),X,Y,DrillTime,XOff,YOff);}
}
inline void _jump_rel_drill_2 (int cardno ,const long dX, const long dY, const UINT DrillTime, const long XOff, const long YOff) {
  if (cardno == -1) { return jump_rel_drill_2(dX,dY,DrillTime,XOff,YOff);}
  else { return n_jump_rel_drill_2 (static_cast<UINT>(cardno),dX,dY,DrillTime,XOff,YOff);}
}
inline void _jump_abs_drill (int cardno ,const long X, const long Y, const UINT DrillTime) {
  if (cardno == -1) { return jump_abs_drill(X,Y,DrillTime);}
  else { return n_jump_abs_drill (static_cast<UINT>(cardno),X,Y,DrillTime);}
}
inline void _jump_rel_drill (int cardno ,const long dX, const long dY, const UINT DrillTime) {
  if (cardno == -1) { return jump_rel_drill(dX,dY,DrillTime);}
  else { return n_jump_rel_drill (static_cast<UINT>(cardno),dX,dY,DrillTime);}
}
inline void _timed_mark_abs_3d (int cardno ,const long X, const long Y, const long Z, const double T) {
  if (cardno == -1) { return timed_mark_abs_3d(X,Y,Z,T);}
  else { return n_timed_mark_abs_3d (static_cast<UINT>(cardno),X,Y,Z,T);}
}
inline void _timed_mark_rel_3d (int cardno ,const long dX, const long dY, const long dZ, const double T) {
  if (cardno == -1) { return timed_mark_rel_3d(dX,dY,dZ,T);}
  else { return n_timed_mark_rel_3d (static_cast<UINT>(cardno),dX,dY,dZ,T);}
}
inline void _timed_mark_abs (int cardno ,const long X, const long Y, const double T) {
  if (cardno == -1) { return timed_mark_abs(X,Y,T);}
  else { return n_timed_mark_abs (static_cast<UINT>(cardno),X,Y,T);}
}
inline void _timed_mark_rel (int cardno ,const long dX, const long dY, const double T) {
  if (cardno == -1) { return timed_mark_rel(dX,dY,T);}
  else { return n_timed_mark_rel (static_cast<UINT>(cardno),dX,dY,T);}
}
inline void _mark_abs_3d (int cardno ,const long X, const long Y, const long Z) {
  if (cardno == -1) { return mark_abs_3d(X,Y,Z);}
  else { return n_mark_abs_3d (static_cast<UINT>(cardno),X,Y,Z);}
}
inline void _mark_rel_3d (int cardno ,const long dX, const long dY, const long dZ) {
  if (cardno == -1) { return mark_rel_3d(dX,dY,dZ);}
  else { return n_mark_rel_3d (static_cast<UINT>(cardno),dX,dY,dZ);}
}
inline void _mark_abs (int cardno ,const long X, const long Y) {
  if (cardno == -1) { return mark_abs(X,Y);}
  else { return n_mark_abs (static_cast<UINT>(cardno),X,Y);}
}
inline void _mark_rel (int cardno ,const long dX, const long dY) {
  if (cardno == -1) { return mark_rel(dX,dY);}
  else { return n_mark_rel (static_cast<UINT>(cardno),dX,dY);}
}
inline void _timed_jump_abs_3d (int cardno ,const long X, const long Y, const long Z, const double T) {
  if (cardno == -1) { return timed_jump_abs_3d(X,Y,Z,T);}
  else { return n_timed_jump_abs_3d (static_cast<UINT>(cardno),X,Y,Z,T);}
}
inline void _timed_jump_rel_3d (int cardno ,const long dX, const long dY, const long dZ, const double T) {
  if (cardno == -1) { return timed_jump_rel_3d(dX,dY,dZ,T);}
  else { return n_timed_jump_rel_3d (static_cast<UINT>(cardno),dX,dY,dZ,T);}
}
inline void _timed_jump_abs (int cardno ,const long X, const long Y, const double T) {
  if (cardno == -1) { return timed_jump_abs(X,Y,T);}
  else { return n_timed_jump_abs (static_cast<UINT>(cardno),X,Y,T);}
}
inline void _timed_jump_rel (int cardno ,const long dX, const long dY, const double T) {
  if (cardno == -1) { return timed_jump_rel(dX,dY,T);}
  else { return n_timed_jump_rel (static_cast<UINT>(cardno),dX,dY,T);}
}
inline void _jump_abs_3d (int cardno ,const long X, const long Y, const long Z) {
  if (cardno == -1) { return jump_abs_3d(X,Y,Z);}
  else { return n_jump_abs_3d (static_cast<UINT>(cardno),X,Y,Z);}
}
inline void _jump_rel_3d (int cardno ,const long dX, const long dY, const long dZ) {
  if (cardno == -1) { return jump_rel_3d(dX,dY,dZ);}
  else { return n_jump_rel_3d (static_cast<UINT>(cardno),dX,dY,dZ);}
}
inline void _jump_abs (int cardno ,const long X, const long Y) {
  if (cardno == -1) { return jump_abs(X,Y);}
  else { return n_jump_abs (static_cast<UINT>(cardno),X,Y);}
}
inline void _jump_rel (int cardno ,const long dX, const long dY) {
  if (cardno == -1) { return jump_rel(dX,dY);}
  else { return n_jump_rel (static_cast<UINT>(cardno),dX,dY);}
}
inline void _para_mark_abs_3d (int cardno ,const long X, const long Y, const long Z, const UINT P) {
  if (cardno == -1) { return para_mark_abs_3d(X,Y,Z,P);}
  else { return n_para_mark_abs_3d (static_cast<UINT>(cardno),X,Y,Z,P);}
}
inline void _para_mark_rel_3d (int cardno ,const long dX, const long dY, const long dZ, const UINT P) {
  if (cardno == -1) { return para_mark_rel_3d(dX,dY,dZ,P);}
  else { return n_para_mark_rel_3d (static_cast<UINT>(cardno),dX,dY,dZ,P);}
}
inline void _para_mark_abs (int cardno ,const long X, const long Y, const UINT P) {
  if (cardno == -1) { return para_mark_abs(X,Y,P);}
  else { return n_para_mark_abs (static_cast<UINT>(cardno),X,Y,P);}
}
inline void _para_mark_rel (int cardno ,const long dX, const long dY, const UINT P) {
  if (cardno == -1) { return para_mark_rel(dX,dY,P);}
  else { return n_para_mark_rel (static_cast<UINT>(cardno),dX,dY,P);}
}
inline void _para_jump_abs_3d (int cardno ,const long X, const long Y, const long Z, const UINT P) {
  if (cardno == -1) { return para_jump_abs_3d(X,Y,Z,P);}
  else { return n_para_jump_abs_3d (static_cast<UINT>(cardno),X,Y,Z,P);}
}
inline void _para_jump_rel_3d (int cardno ,const long dX, const long dY, const long dZ, const UINT P) {
  if (cardno == -1) { return para_jump_rel_3d(dX,dY,dZ,P);}
  else { return n_para_jump_rel_3d (static_cast<UINT>(cardno),dX,dY,dZ,P);}
}
inline void _para_jump_abs (int cardno ,const long X, const long Y, const UINT P) {
  if (cardno == -1) { return para_jump_abs(X,Y,P);}
  else { return n_para_jump_abs (static_cast<UINT>(cardno),X,Y,P);}
}
inline void _para_jump_rel (int cardno ,const long dX, const long dY, const UINT P) {
  if (cardno == -1) { return para_jump_rel(dX,dY,P);}
  else { return n_para_jump_rel (static_cast<UINT>(cardno),dX,dY,P);}
}
inline void _timed_para_mark_abs_3d (int cardno ,const long X, const long Y, const long Z, const UINT P, const double T) {
  if (cardno == -1) { return timed_para_mark_abs_3d(X,Y,Z,P,T);}
  else { return n_timed_para_mark_abs_3d (static_cast<UINT>(cardno),X,Y,Z,P,T);}
}
inline void _timed_para_mark_rel_3d (int cardno ,const long dX, const long dY, const long dZ, const UINT P, const double T) {
  if (cardno == -1) { return timed_para_mark_rel_3d(dX,dY,dZ,P,T);}
  else { return n_timed_para_mark_rel_3d (static_cast<UINT>(cardno),dX,dY,dZ,P,T);}
}
inline void _timed_para_jump_abs_3d (int cardno ,const long X, const long Y, const long Z, const UINT P, const double T) {
  if (cardno == -1) { return timed_para_jump_abs_3d(X,Y,Z,P,T);}
  else { return n_timed_para_jump_abs_3d (static_cast<UINT>(cardno),X,Y,Z,P,T);}
}
inline void _timed_para_jump_rel_3d (int cardno ,const long dX, const long dY, const long dZ, const UINT P, const double T) {
  if (cardno == -1) { return timed_para_jump_rel_3d(dX,dY,dZ,P,T);}
  else { return n_timed_para_jump_rel_3d (static_cast<UINT>(cardno),dX,dY,dZ,P,T);}
}
inline void _timed_para_mark_abs (int cardno ,const long X, const long Y, const UINT P, const double T) {
  if (cardno == -1) { return timed_para_mark_abs(X,Y,P,T);}
  else { return n_timed_para_mark_abs (static_cast<UINT>(cardno),X,Y,P,T);}
}
inline void _timed_para_mark_rel (int cardno ,const long dX, const long dY, const UINT P, const double T) {
  if (cardno == -1) { return timed_para_mark_rel(dX,dY,P,T);}
  else { return n_timed_para_mark_rel (static_cast<UINT>(cardno),dX,dY,P,T);}
}
inline void _timed_para_jump_abs (int cardno ,const long X, const long Y, const UINT P, const double T) {
  if (cardno == -1) { return timed_para_jump_abs(X,Y,P,T);}
  else { return n_timed_para_jump_abs (static_cast<UINT>(cardno),X,Y,P,T);}
}
inline void _timed_para_jump_rel (int cardno ,const long dX, const long dY, const UINT P, const double T) {
  if (cardno == -1) { return timed_para_jump_rel(dX,dY,P,T);}
  else { return n_timed_para_jump_rel (static_cast<UINT>(cardno),dX,dY,P,T);}
}
inline void _set_defocus_list (int cardno ,const long Shift) {
  if (cardno == -1) { return set_defocus_list(Shift);}
  else { return n_set_defocus_list (static_cast<UINT>(cardno),Shift);}
}
inline void _set_defocus_offset_list (int cardno ,const long Shift) {
  if (cardno == -1) { return set_defocus_offset_list(Shift);}
  else { return n_set_defocus_offset_list (static_cast<UINT>(cardno),Shift);}
}
inline void _set_zoom_list (int cardno ,const UINT Zoom) {
  if (cardno == -1) { return set_zoom_list(Zoom);}
  else { return n_set_zoom_list (static_cast<UINT>(cardno),Zoom);}
}
inline void _timed_arc_abs (int cardno ,const long X, const long Y, const double Angle, const double T) {
  if (cardno == -1) { return timed_arc_abs(X,Y,Angle,T);}
  else { return n_timed_arc_abs (static_cast<UINT>(cardno),X,Y,Angle,T);}
}
inline void _timed_arc_rel (int cardno ,const long dX, const long dY, const double Angle, const double T) {
  if (cardno == -1) { return timed_arc_rel(dX,dY,Angle,T);}
  else { return n_timed_arc_rel (static_cast<UINT>(cardno),dX,dY,Angle,T);}
}
inline void _arc_abs_3d (int cardno ,const long X, const long Y, const long Z, const double Angle) {
  if (cardno == -1) { return arc_abs_3d(X,Y,Z,Angle);}
  else { return n_arc_abs_3d (static_cast<UINT>(cardno),X,Y,Z,Angle);}
}
inline void _arc_rel_3d (int cardno ,const long dX, const long dY, const long dZ, const double Angle) {
  if (cardno == -1) { return arc_rel_3d(dX,dY,dZ,Angle);}
  else { return n_arc_rel_3d (static_cast<UINT>(cardno),dX,dY,dZ,Angle);}
}
inline void _arc_abs (int cardno ,const long X, const long Y, const double Angle) {
  if (cardno == -1) { return arc_abs(X,Y,Angle);}
  else { return n_arc_abs (static_cast<UINT>(cardno),X,Y,Angle);}
}
inline void _arc_rel (int cardno ,const long dX, const long dY, const double Angle) {
  if (cardno == -1) { return arc_rel(dX,dY,Angle);}
  else { return n_arc_rel (static_cast<UINT>(cardno),dX,dY,Angle);}
}
inline void _set_ellipse (int cardno ,const UINT A, const UINT B, const double Phi0, const double Phi) {
  if (cardno == -1) { return set_ellipse(A,B,Phi0,Phi);}
  else { return n_set_ellipse (static_cast<UINT>(cardno),A,B,Phi0,Phi);}
}
inline void _mark_ellipse_abs (int cardno ,const long X, const long Y, const double Alpha) {
  if (cardno == -1) { return mark_ellipse_abs(X,Y,Alpha);}
  else { return n_mark_ellipse_abs (static_cast<UINT>(cardno),X,Y,Alpha);}
}
inline void _mark_ellipse_rel (int cardno ,const long dX, const long dY, const double Alpha) {
  if (cardno == -1) { return mark_ellipse_rel(dX,dY,Alpha);}
  else { return n_mark_ellipse_rel (static_cast<UINT>(cardno),dX,dY,Alpha);}
}
inline void _set_offset_xyz_list (int cardno ,const UINT HeadNo, const long XOffset, const long YOffset, const long ZOffset, const UINT at_once) {
  if (cardno == -1) { return set_offset_xyz_list(HeadNo,XOffset,YOffset,ZOffset,at_once);}
  else { return n_set_offset_xyz_list (static_cast<UINT>(cardno),HeadNo,XOffset,YOffset,ZOffset,at_once);}
}
inline void _set_offset_list (int cardno ,const UINT HeadNo, const long XOffset, const long YOffset, const UINT at_once) {
  if (cardno == -1) { return set_offset_list(HeadNo,XOffset,YOffset,at_once);}
  else { return n_set_offset_list (static_cast<UINT>(cardno),HeadNo,XOffset,YOffset,at_once);}
}
inline void _set_matrix_list (int cardno ,const UINT HeadNo, const UINT Ind1, const UINT Ind2, const double Mij, const UINT at_once) {
  if (cardno == -1) { return set_matrix_list(HeadNo,Ind1,Ind2,Mij,at_once);}
  else { return n_set_matrix_list (static_cast<UINT>(cardno),HeadNo,Ind1,Ind2,Mij,at_once);}
}
inline void _set_angle_list (int cardno ,const UINT HeadNo, const double Angle, const UINT at_once) {
  if (cardno == -1) { return set_angle_list(HeadNo,Angle,at_once);}
  else { return n_set_angle_list (static_cast<UINT>(cardno),HeadNo,Angle,at_once);}
}
inline void _set_scale_list (int cardno ,const UINT HeadNo, const double Scale, const UINT at_once) {
  if (cardno == -1) { return set_scale_list(HeadNo,Scale,at_once);}
  else { return n_set_scale_list (static_cast<UINT>(cardno),HeadNo,Scale,at_once);}
}
inline void _apply_mcbsp_list (int cardno ,const UINT HeadNo, const UINT at_once) {
  if (cardno == -1) { return apply_mcbsp_list(HeadNo,at_once);}
  else { return n_apply_mcbsp_list (static_cast<UINT>(cardno),HeadNo,at_once);}
}
inline void _set_mark_speed (int cardno ,const double Speed) {
  if (cardno == -1) { return set_mark_speed(Speed);}
  else { return n_set_mark_speed (static_cast<UINT>(cardno),Speed);}
}
inline void _set_jump_speed (int cardno ,const double Speed) {
  if (cardno == -1) { return set_jump_speed(Speed);}
  else { return n_set_jump_speed (static_cast<UINT>(cardno),Speed);}
}
inline void _set_sky_writing_para_list (int cardno ,const double Timelag, const long LaserOnShift, const UINT Nprev, const UINT Npost) {
  if (cardno == -1) { return set_sky_writing_para_list(Timelag,LaserOnShift,Nprev,Npost);}
  else { return n_set_sky_writing_para_list (static_cast<UINT>(cardno),Timelag,LaserOnShift,Nprev,Npost);}
}
inline void _set_sky_writing_list (int cardno ,const double Timelag, const long LaserOnShift) {
  if (cardno == -1) { return set_sky_writing_list(Timelag,LaserOnShift);}
  else { return n_set_sky_writing_list (static_cast<UINT>(cardno),Timelag,LaserOnShift);}
}
inline void _set_sky_writing_limit_list (int cardno ,const double CosAngle) {
  if (cardno == -1) { return set_sky_writing_limit_list(CosAngle);}
  else { return n_set_sky_writing_limit_list (static_cast<UINT>(cardno),CosAngle);}
}
inline void _set_sky_writing_mode_list (int cardno ,const UINT Mode) {
  if (cardno == -1) { return set_sky_writing_mode_list(Mode);}
  else { return n_set_sky_writing_mode_list (static_cast<UINT>(cardno),Mode);}
}
inline void _set_scanner_delays (int cardno ,const UINT Jump, const UINT Mark, const UINT Polygon) {
  if (cardno == -1) { return set_scanner_delays(Jump,Mark,Polygon);}
  else { return n_set_scanner_delays (static_cast<UINT>(cardno),Jump,Mark,Polygon);}
}
inline void _set_jump_mode_list (int cardno ,const long Flag) {
  if (cardno == -1) { return set_jump_mode_list(Flag);}
  else { return n_set_jump_mode_list (static_cast<UINT>(cardno),Flag);}
}
inline void _enduring_wobbel (int cardno ) {
  if (cardno == -1) { return enduring_wobbel();}
  else { return n_enduring_wobbel (static_cast<UINT>(cardno));}
}
inline void _set_delay_mode_list (int cardno ,const UINT VarPoly, const UINT DirectMove3D, const UINT EdgeLevel, const UINT MinJumpDelay, const UINT JumpLengthLimit) {
  if (cardno == -1) { return set_delay_mode_list(VarPoly,DirectMove3D,EdgeLevel,MinJumpDelay,JumpLengthLimit);}
  else { return n_set_delay_mode_list (static_cast<UINT>(cardno),VarPoly,DirectMove3D,EdgeLevel,MinJumpDelay,JumpLengthLimit);}
}
inline void _activate_scanahead_autodelays_list (int cardno ,const long Mode) {
  if (cardno == -1) { return activate_scanahead_autodelays_list(Mode);}
  else { return n_activate_scanahead_autodelays_list (static_cast<UINT>(cardno),Mode);}
}
inline void _set_scanahead_laser_shifts_list (int cardno ,const long dLasOn, const long dLasOff) {
  if (cardno == -1) { return set_scanahead_laser_shifts_list(dLasOn,dLasOff);}
  else { return n_set_scanahead_laser_shifts_list (static_cast<UINT>(cardno),dLasOn,dLasOff);}
}
inline void _set_scanahead_line_params_list (int cardno ,const UINT CornerScale, const UINT EndScale, const UINT AccScale) {
  if (cardno == -1) { return set_scanahead_line_params_list(CornerScale,EndScale,AccScale);}
  else { return n_set_scanahead_line_params_list (static_cast<UINT>(cardno),CornerScale,EndScale,AccScale);}
}
inline void _set_scanahead_line_params_ex_list (int cardno ,const UINT CornerScale, const UINT EndScale, const UINT AccScale, const UINT JumpScale) {
  if (cardno == -1) { return set_scanahead_line_params_ex_list(CornerScale,EndScale,AccScale,JumpScale);}
  else { return n_set_scanahead_line_params_ex_list (static_cast<UINT>(cardno),CornerScale,EndScale,AccScale,JumpScale);}
}
inline void _stepper_enable_list (int cardno ,const long Enable1, const long Enable2) {
  if (cardno == -1) { return stepper_enable_list(Enable1,Enable2);}
  else { return n_stepper_enable_list (static_cast<UINT>(cardno),Enable1,Enable2);}
}
inline void _stepper_control_list (int cardno ,const long Period1, const long Period2) {
  if (cardno == -1) { return stepper_control_list(Period1,Period2);}
  else { return n_stepper_control_list (static_cast<UINT>(cardno),Period1,Period2);}
}
inline void _stepper_abs_no_list (int cardno ,const UINT No, const long Pos) {
  if (cardno == -1) { return stepper_abs_no_list(No,Pos);}
  else { return n_stepper_abs_no_list (static_cast<UINT>(cardno),No,Pos);}
}
inline void _stepper_rel_no_list (int cardno ,const UINT No, const long dPos) {
  if (cardno == -1) { return stepper_rel_no_list(No,dPos);}
  else { return n_stepper_rel_no_list (static_cast<UINT>(cardno),No,dPos);}
}
inline void _stepper_abs_list (int cardno ,const long Pos1, const long Pos2) {
  if (cardno == -1) { return stepper_abs_list(Pos1,Pos2);}
  else { return n_stepper_abs_list (static_cast<UINT>(cardno),Pos1,Pos2);}
}
inline void _stepper_rel_list (int cardno ,const long dPos1, const long dPos2) {
  if (cardno == -1) { return stepper_rel_list(dPos1,dPos2);}
  else { return n_stepper_rel_list (static_cast<UINT>(cardno),dPos1,dPos2);}
}
inline void _stepper_wait (int cardno ,const UINT No) {
  if (cardno == -1) { return stepper_wait(No);}
  else { return n_stepper_wait (static_cast<UINT>(cardno),No);}
}
