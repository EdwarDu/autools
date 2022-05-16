#include "RTC6impl.hpp"
#include <iostream>
using namespace std;
RTC6_API UINT __stdcall init_rtc6_dll(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API void __stdcall free_rtc6_dll(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall set_rtc4_mode(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall set_rtc5_mode(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall set_rtc6_mode(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API UINT __stdcall get_rtc_mode(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall n_get_error(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API UINT __stdcall n_get_last_error(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API void __stdcall n_reset_error(const UINT CardNo, const UINT Code){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Code = " << Code << endl;
  return;
}

RTC6_API UINT __stdcall n_set_verify(const UINT CardNo, const UINT Verify){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Verify = " << Verify << endl;
  return 0;
}

RTC6_API UINT __stdcall get_error(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall get_last_error(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API void __stdcall reset_error(const UINT Code){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Code = " << Code << endl;
  return;
}

RTC6_API UINT __stdcall set_verify(const UINT Verify){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Verify = " << Verify << endl;
  return 0;
}

RTC6_API UINT __stdcall verify_checksum(const char* Name){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Name = " << Name << endl;
  return 0;
}

RTC6_API UINT __stdcall eth_count_cards(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall eth_found_cards(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall eth_max_card(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API long __stdcall eth_remove_card(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0L;
}

RTC6_API void __stdcall eth_get_card_info(const UINT CardNo, const ULONG_PTR Ptr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Ptr = " << Ptr << endl;
  return;
}

RTC6_API void __stdcall eth_get_card_info_search(const UINT SearchNo, const ULONG_PTR Ptr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " SearchNo = " << SearchNo << " Ptr = " << Ptr << endl;
  return;
}

RTC6_API void __stdcall eth_set_search_cards_timeout(const UINT TimeOut){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " TimeOut = " << TimeOut << endl;
  return;
}

RTC6_API UINT __stdcall eth_search_cards(const UINT Ip, const UINT NetMask){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Ip = " << Ip << " NetMask = " << NetMask << endl;
  return 0;
}

RTC6_API UINT __stdcall eth_search_cards_range(const UINT StartIp, const UINT EndIp){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " StartIp = " << StartIp << " EndIp = " << EndIp << endl;
  return 0;
}

RTC6_API long __stdcall eth_assign_card_ip(const UINT Ip, const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Ip = " << Ip << " CardNo = " << CardNo << endl;
  return 0L;
}

RTC6_API long __stdcall eth_assign_card(const UINT SearchNo, const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " SearchNo = " << SearchNo << " CardNo = " << CardNo << endl;
  return 0L;
}

RTC6_API UINT __stdcall eth_convert_string_to_ip(const char* IpString){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " IpString = " << IpString << endl;
  return 0;
}

RTC6_API void __stdcall eth_convert_ip_to_string(const UINT Ip, const ULONG_PTR IpString){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Ip = " << Ip << " IpString = " << IpString << endl;
  return;
}

RTC6_API UINT __stdcall eth_get_ip(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API UINT __stdcall eth_get_ip_search(const UINT SearchNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " SearchNo = " << SearchNo << endl;
  return 0;
}

RTC6_API UINT __stdcall eth_get_serial_search(const UINT SearchNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " SearchNo = " << SearchNo << endl;
  return 0;
}

RTC6_API UINT __stdcall n_eth_get_last_error(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API UINT __stdcall n_eth_get_error(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API UINT __stdcall n_eth_error_dump(const UINT CardNo, const ULONG_PTR Dump){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Dump = " << Dump << endl;
  return 0;
}

RTC6_API UINT __stdcall n_eth_set_static_ip(const UINT CardNo, const UINT Ip, const UINT NetMask, const UINT Gateway){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Ip = " << Ip << " NetMask = " << NetMask << " Gateway = " << Gateway << endl;
  return 0;
}

RTC6_API UINT __stdcall n_eth_get_static_ip(const UINT CardNo, UINT& Ip, UINT& NetMask, UINT& Gateway){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Ip = " << Ip << " NetMask = " << NetMask << " Gateway = " << Gateway << endl;
  return 0;
}

RTC6_API UINT __stdcall n_eth_set_port_numbers(const UINT CardNo, const UINT UDPsearch, const UINT UDPexcl, const UINT TCP){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " UDPsearch = " << UDPsearch << " UDPexcl = " << UDPexcl << " TCP = " << TCP << endl;
  return 0;
}

RTC6_API UINT __stdcall n_eth_get_port_numbers(const UINT CardNo, UINT& UDPsearch, UINT& UDPexcl, UINT& TCP){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " UDPsearch = " << UDPsearch << " UDPexcl = " << UDPexcl << " TCP = " << TCP << endl;
  return 0;
}

RTC6_API void __stdcall n_eth_set_com_timeouts(const UINT CardNo, const UINT AcquireTimeout, const UINT AcquireMaxRetries, const UINT SendRecvTimeout, const UINT SendRecvMaxRetries, const UINT KeepAlive, const UINT KeepInterval){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " AcquireTimeout = " << AcquireTimeout << " AcquireMaxRetries = " << AcquireMaxRetries << " SendRecvTimeout = " << SendRecvTimeout << " SendRecvMaxRetries = " << SendRecvMaxRetries << " KeepAlive = " << KeepAlive << " KeepInterval = " << KeepInterval << endl;
  return;
}

RTC6_API void __stdcall n_eth_get_com_timeouts(const UINT CardNo, UINT& AcquireTimeout, UINT& AcquireMaxRetries, UINT& SendRecvTimeout, UINT& SendRecvMaxRetries, UINT& KeepAlive, UINT& KeepInterval){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " AcquireTimeout = " << AcquireTimeout << " AcquireMaxRetries = " << AcquireMaxRetries << " SendRecvTimeout = " << SendRecvTimeout << " SendRecvMaxRetries = " << SendRecvMaxRetries << " KeepAlive = " << KeepAlive << " KeepInterval = " << KeepInterval << endl;
  return;
}

RTC6_API UINT __stdcall n_eth_check_connection(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API void __stdcall n_set_eth_boot_control(const UINT CardNo, const UINT Ctrl){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Ctrl = " << Ctrl << endl;
  return;
}

RTC6_API void __stdcall n_eth_boot_timeout(const UINT CardNo, const UINT Timeout){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Timeout = " << Timeout << endl;
  return;
}

RTC6_API void __stdcall n_eth_boot_dcmd(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API UINT __stdcall n_store_program(const UINT CardNo, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << endl;
  return 0;
}

RTC6_API UINT __stdcall n_read_image_eth(const UINT CardNo, const char* Name){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Name = " << Name << endl;
  return 0;
}

RTC6_API UINT __stdcall n_write_image_eth(const UINT CardNo, const char* Name){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Name = " << Name << endl;
  return 0;
}

RTC6_API UINT __stdcall eth_get_last_error(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall eth_get_error(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall eth_error_dump(const ULONG_PTR Dump){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Dump = " << Dump << endl;
  return 0;
}

RTC6_API UINT __stdcall eth_set_static_ip(const UINT Ip, const UINT NetMask, const UINT Gateway){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Ip = " << Ip << " NetMask = " << NetMask << " Gateway = " << Gateway << endl;
  return 0;
}

RTC6_API UINT __stdcall eth_get_static_ip(UINT& Ip, UINT& NetMask, UINT& Gateway){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Ip = " << Ip << " NetMask = " << NetMask << " Gateway = " << Gateway << endl;
  return 0;
}

RTC6_API UINT __stdcall eth_set_port_numbers(const UINT UDPsearch, const UINT UDPexcl, const UINT TCP){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " UDPsearch = " << UDPsearch << " UDPexcl = " << UDPexcl << " TCP = " << TCP << endl;
  return 0;
}

RTC6_API UINT __stdcall eth_get_port_numbers(UINT& UDPsearch, UINT& UDPexcl, UINT& TCP){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " UDPsearch = " << UDPsearch << " UDPexcl = " << UDPexcl << " TCP = " << TCP << endl;
  return 0;
}

RTC6_API void __stdcall eth_set_com_timeouts(const UINT AcquireTimeout, const UINT AcquireMaxRetries, const UINT SendRecvTimeout, const UINT SendRecvMaxRetries, const UINT KeepAlive, const UINT KeepInterval){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " AcquireTimeout = " << AcquireTimeout << " AcquireMaxRetries = " << AcquireMaxRetries << " SendRecvTimeout = " << SendRecvTimeout << " SendRecvMaxRetries = " << SendRecvMaxRetries << " KeepAlive = " << KeepAlive << " KeepInterval = " << KeepInterval << endl;
  return;
}

RTC6_API void __stdcall eth_get_com_timeouts(UINT& AcquireTimeout, UINT& AcquireMaxRetries, UINT& SendRecvTimeout, UINT& SendRecvMaxRetries, UINT& KeepAlive, UINT& KeepInterval){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " AcquireTimeout = " << AcquireTimeout << " AcquireMaxRetries = " << AcquireMaxRetries << " SendRecvTimeout = " << SendRecvTimeout << " SendRecvMaxRetries = " << SendRecvMaxRetries << " KeepAlive = " << KeepAlive << " KeepInterval = " << KeepInterval << endl;
  return;
}

RTC6_API UINT __stdcall eth_check_connection(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API void __stdcall set_eth_boot_control(const UINT Ctrl){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Ctrl = " << Ctrl << endl;
  return;
}

RTC6_API void __stdcall eth_boot_timeout(const UINT Timeout){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Timeout = " << Timeout << endl;
  return;
}

RTC6_API void __stdcall eth_boot_dcmd(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API UINT __stdcall store_program(const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << endl;
  return 0;
}

RTC6_API UINT __stdcall read_image_eth(const char* Name){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Name = " << Name << endl;
  return 0;
}

RTC6_API UINT __stdcall write_image_eth(const char* Name){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Name = " << Name << endl;
  return 0;
}

RTC6_API UINT __stdcall read_abc_from_file(const char* Name, double& A, double& B, double& C){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Name = " << Name << " A = " << A << " B = " << B << " C = " << C << endl;
  return 0;
}

RTC6_API UINT __stdcall write_abc_to_file(const char* Name, const double A, const double B, const double C){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Name = " << Name << " A = " << A << " B = " << B << " C = " << C << endl;
  return 0;
}

RTC6_API UINT __stdcall n_create_dat_file(const UINT CardNo, const long Flag){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Flag = " << Flag << endl;
  return 0;
}

RTC6_API UINT __stdcall create_dat_file(const long Flag){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Flag = " << Flag << endl;
  return 0;
}

RTC6_API UINT __stdcall transform(long& Sig1, long& Sig2, const ULONG_PTR Ptr, const UINT Code){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Sig1 = " << Sig1 << " Sig2 = " << Sig2 << " Ptr = " << Ptr << " Code = " << Code << endl;
  return 0;
}

RTC6_API UINT __stdcall rtc6_count_cards(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall acquire_rtc(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API UINT __stdcall release_rtc(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API UINT __stdcall select_rtc(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API UINT __stdcall get_dll_version(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall n_get_card_type(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API UINT __stdcall n_get_serial_number(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API UINT __stdcall n_get_hex_version(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API UINT __stdcall n_get_rtc_version(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API UINT __stdcall n_get_bios_version(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API UINT __stdcall get_card_type(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall get_serial_number(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall get_hex_version(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall get_rtc_version(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall get_bios_version(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall n_load_program_file(const UINT CardNo, const char* Path){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Path = " << Path << endl;
  return 0;
}

RTC6_API void __stdcall n_sync_slaves(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API UINT __stdcall n_get_sync_status(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API void __stdcall n_master_slave_config(const UINT CardNo, const UINT Flags){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Flags = " << Flags << endl;
  return;
}

RTC6_API UINT __stdcall n_load_correction_file(const UINT CardNo, const char* Name, const UINT No, const UINT Dim){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Name = " << Name << " No = " << No << " Dim = " << Dim << endl;
  return 0;
}

RTC6_API UINT __stdcall n_load_zoom_correction_file(const UINT CardNo, const char* Name, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Name = " << Name << " No = " << No << endl;
  return 0;
}

RTC6_API UINT __stdcall n_load_oct_table_no(const UINT CardNo, const double A, const double B, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " A = " << A << " B = " << B << " No = " << No << endl;
  return 0;
}

RTC6_API UINT __stdcall n_load_z_table_no(const UINT CardNo, const double A, const double B, const double C, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " A = " << A << " B = " << B << " C = " << C << " No = " << No << endl;
  return 0;
}

RTC6_API UINT __stdcall n_load_z_table(const UINT CardNo, const double A, const double B, const double C){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " A = " << A << " B = " << B << " C = " << C << endl;
  return 0;
}

RTC6_API void __stdcall n_select_cor_table(const UINT CardNo, const UINT HeadA, const UINT HeadB){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadA = " << HeadA << " HeadB = " << HeadB << endl;
  return;
}

RTC6_API UINT __stdcall n_set_dsp_mode(const UINT CardNo, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << endl;
  return 0;
}

RTC6_API long __stdcall n_load_stretch_table(const UINT CardNo, const char* Name, const long No, const UINT TableNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Name = " << Name << " No = " << No << " TableNo = " << TableNo << endl;
  return 0L;
}

RTC6_API void __stdcall n_number_of_correction_tables(const UINT CardNo, const UINT Number){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Number = " << Number << endl;
  return;
}

RTC6_API double __stdcall n_get_head_para(const UINT CardNo, const UINT HeadNo, const UINT ParaNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " ParaNo = " << ParaNo << endl;
  return 0.0;
}

RTC6_API double __stdcall n_get_table_para(const UINT CardNo, const UINT TableNo, const UINT ParaNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " TableNo = " << TableNo << " ParaNo = " << ParaNo << endl;
  return 0.0;
}

RTC6_API UINT __stdcall load_program_file(const char* Path){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Path = " << Path << endl;
  return 0;
}

RTC6_API void __stdcall sync_slaves(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API UINT __stdcall get_sync_status(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API void __stdcall master_slave_config(const UINT Flags){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Flags = " << Flags << endl;
  return;
}

RTC6_API UINT __stdcall load_correction_file(const char* Name, const UINT No, const UINT Dim){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Name = " << Name << " No = " << No << " Dim = " << Dim << endl;
  return 0;
}

RTC6_API UINT __stdcall load_zoom_correction_file(const char* Name, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Name = " << Name << " No = " << No << endl;
  return 0;
}

RTC6_API UINT __stdcall load_oct_table_no(const double A, const double B, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " A = " << A << " B = " << B << " No = " << No << endl;
  return 0;
}

RTC6_API UINT __stdcall load_z_table_no(const double A, const double B, const double C, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " A = " << A << " B = " << B << " C = " << C << " No = " << No << endl;
  return 0;
}

RTC6_API UINT __stdcall load_z_table(const double A, const double B, const double C){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " A = " << A << " B = " << B << " C = " << C << endl;
  return 0;
}

RTC6_API void __stdcall select_cor_table(const UINT HeadA, const UINT HeadB){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadA = " << HeadA << " HeadB = " << HeadB << endl;
  return;
}

RTC6_API UINT __stdcall set_dsp_mode(const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << endl;
  return 0;
}

RTC6_API long __stdcall load_stretch_table(const char* Name, const long No, const UINT TableNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Name = " << Name << " No = " << No << " TableNo = " << TableNo << endl;
  return 0L;
}

RTC6_API void __stdcall number_of_correction_tables(const UINT Number){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Number = " << Number << endl;
  return;
}

RTC6_API double __stdcall get_head_para(const UINT HeadNo, const UINT ParaNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " ParaNo = " << ParaNo << endl;
  return 0.0;
}

RTC6_API double __stdcall get_table_para(const UINT TableNo, const UINT ParaNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " TableNo = " << TableNo << " ParaNo = " << ParaNo << endl;
  return 0.0;
}

RTC6_API void __stdcall n_config_list(const UINT CardNo, const UINT Mem1, const UINT Mem2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mem1 = " << Mem1 << " Mem2 = " << Mem2 << endl;
  return;
}

RTC6_API void __stdcall n_get_config_list(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API UINT __stdcall n_save_disk(const UINT CardNo, const char* Name, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Name = " << Name << " Mode = " << Mode << endl;
  return 0;
}

RTC6_API UINT __stdcall n_load_disk(const UINT CardNo, const char* Name, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Name = " << Name << " Mode = " << Mode << endl;
  return 0;
}

RTC6_API UINT __stdcall n_get_list_space(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API void __stdcall config_list(const UINT Mem1, const UINT Mem2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mem1 = " << Mem1 << " Mem2 = " << Mem2 << endl;
  return;
}

RTC6_API void __stdcall get_config_list(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API UINT __stdcall save_disk(const char* Name, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Name = " << Name << " Mode = " << Mode << endl;
  return 0;
}

RTC6_API UINT __stdcall load_disk(const char* Name, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Name = " << Name << " Mode = " << Mode << endl;
  return 0;
}

RTC6_API UINT __stdcall get_list_space(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API void __stdcall n_set_start_list_pos(const UINT CardNo, const UINT ListNo, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ListNo = " << ListNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_set_start_list(const UINT CardNo, const UINT ListNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ListNo = " << ListNo << endl;
  return;
}

RTC6_API void __stdcall n_set_start_list_1(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_set_start_list_2(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_set_input_pointer(const UINT CardNo, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API UINT __stdcall n_load_list(const UINT CardNo, const UINT ListNo, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ListNo = " << ListNo << " Pos = " << Pos << endl;
  return 0;
}

RTC6_API void __stdcall n_load_sub(const UINT CardNo, const UINT Index){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Index = " << Index << endl;
  return;
}

RTC6_API void __stdcall n_load_char(const UINT CardNo, const UINT Char){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Char = " << Char << endl;
  return;
}

RTC6_API void __stdcall n_load_text_table(const UINT CardNo, const UINT Index){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Index = " << Index << endl;
  return;
}

RTC6_API void __stdcall n_get_list_pointer(const UINT CardNo, UINT& ListNo, UINT& Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ListNo = " << ListNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API UINT __stdcall n_get_input_pointer(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API void __stdcall set_start_list_pos(const UINT ListNo, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ListNo = " << ListNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall set_start_list(const UINT ListNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ListNo = " << ListNo << endl;
  return;
}

RTC6_API void __stdcall set_start_list_1(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall set_start_list_2(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall set_input_pointer(const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pos = " << Pos << endl;
  return;
}

RTC6_API UINT __stdcall load_list(const UINT ListNo, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ListNo = " << ListNo << " Pos = " << Pos << endl;
  return 0;
}

RTC6_API void __stdcall load_sub(const UINT Index){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Index = " << Index << endl;
  return;
}

RTC6_API void __stdcall load_char(const UINT Char){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Char = " << Char << endl;
  return;
}

RTC6_API void __stdcall load_text_table(const UINT Index){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Index = " << Index << endl;
  return;
}

RTC6_API void __stdcall get_list_pointer(UINT& ListNo, UINT& Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ListNo = " << ListNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API UINT __stdcall get_input_pointer(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API void __stdcall n_execute_list_pos(const UINT CardNo, const UINT ListNo, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ListNo = " << ListNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_execute_at_pointer(const UINT CardNo, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_execute_list(const UINT CardNo, const UINT ListNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ListNo = " << ListNo << endl;
  return;
}

RTC6_API void __stdcall n_execute_list_1(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_execute_list_2(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API UINT __stdcall n_list_jump_rel_ctrl(const UINT CardNo, const long Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pos = " << Pos << endl;
  return 0;
}

RTC6_API void __stdcall n_get_out_pointer(const UINT CardNo, UINT& ListNo, UINT& Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ListNo = " << ListNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall execute_list_pos(const UINT ListNo, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ListNo = " << ListNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall execute_at_pointer(const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall execute_list(const UINT ListNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ListNo = " << ListNo << endl;
  return;
}

RTC6_API void __stdcall execute_list_1(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall execute_list_2(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API UINT __stdcall list_jump_rel_ctrl(const long Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pos = " << Pos << endl;
  return 0;
}

RTC6_API void __stdcall get_out_pointer(UINT& ListNo, UINT& Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ListNo = " << ListNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_auto_change_pos(const UINT CardNo, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_start_loop(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_quit_loop(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_pause_list(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_restart_list(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_release_wait(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_stop_execution(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_set_pause_list_cond(const UINT CardNo, const UINT Mask1, const UINT Mask0){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << endl;
  return;
}

RTC6_API void __stdcall n_set_pause_list_not_cond(const UINT CardNo, const UINT Mask1, const UINT Mask0){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << endl;
  return;
}

RTC6_API void __stdcall n_auto_change(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_stop_list(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API UINT __stdcall n_get_wait_status(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API UINT __stdcall n_read_status(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API void __stdcall n_get_status(const UINT CardNo, UINT& Status, UINT& Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Status = " << Status << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall auto_change_pos(const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall start_loop(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall quit_loop(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall pause_list(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall restart_list(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall release_wait(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall stop_execution(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall set_pause_list_cond(const UINT Mask1, const UINT Mask0){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << endl;
  return;
}

RTC6_API void __stdcall set_pause_list_not_cond(const UINT Mask1, const UINT Mask0){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << endl;
  return;
}

RTC6_API void __stdcall auto_change(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall stop_list(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API UINT __stdcall get_wait_status(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall read_status(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API void __stdcall get_status(UINT& Status, UINT& Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Status = " << Status << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_set_extstartpos(const UINT CardNo, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_set_max_counts(const UINT CardNo, const UINT Counts){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Counts = " << Counts << endl;
  return;
}

RTC6_API void __stdcall n_set_control_mode(const UINT CardNo, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_simulate_ext_stop(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_simulate_ext_start_ctrl(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_store_timestamp_counter(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API UINT __stdcall n_get_counts(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API UINT __stdcall n_get_startstop_info(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API void __stdcall set_extstartpos(const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall set_max_counts(const UINT Counts){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Counts = " << Counts << endl;
  return;
}

RTC6_API void __stdcall set_control_mode(const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall simulate_ext_stop(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall simulate_ext_start_ctrl(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall store_timestamp_counter(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API UINT __stdcall get_counts(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall get_startstop_info(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API void __stdcall n_copy_dst_src(const UINT CardNo, const UINT Dst, const UINT Src, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Dst = " << Dst << " Src = " << Src << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_set_char_pointer(const UINT CardNo, const UINT Char, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Char = " << Char << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_set_sub_pointer(const UINT CardNo, const UINT Index, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Index = " << Index << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_set_text_table_pointer(const UINT CardNo, const UINT Index, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Index = " << Index << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_set_char_table(const UINT CardNo, const UINT Index, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Index = " << Index << " Pos = " << Pos << endl;
  return;
}

RTC6_API UINT __stdcall n_get_char_pointer(const UINT CardNo, const UINT Char){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Char = " << Char << endl;
  return 0;
}

RTC6_API UINT __stdcall n_get_sub_pointer(const UINT CardNo, const UINT Index){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Index = " << Index << endl;
  return 0;
}

RTC6_API UINT __stdcall n_get_text_table_pointer(const UINT CardNo, const UINT Index){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Index = " << Index << endl;
  return 0;
}

RTC6_API void __stdcall copy_dst_src(const UINT Dst, const UINT Src, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Dst = " << Dst << " Src = " << Src << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall set_char_pointer(const UINT Char, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Char = " << Char << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall set_sub_pointer(const UINT Index, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Index = " << Index << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall set_text_table_pointer(const UINT Index, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Index = " << Index << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall set_char_table(const UINT Index, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Index = " << Index << " Pos = " << Pos << endl;
  return;
}

RTC6_API UINT __stdcall get_char_pointer(const UINT Char){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Char = " << Char << endl;
  return 0;
}

RTC6_API UINT __stdcall get_sub_pointer(const UINT Index){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Index = " << Index << endl;
  return 0;
}

RTC6_API UINT __stdcall get_text_table_pointer(const UINT Index){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Index = " << Index << endl;
  return 0;
}

RTC6_API void __stdcall n_time_update(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_time_control_eth(const UINT CardNo, const double PPM){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " PPM = " << PPM << endl;
  return;
}

RTC6_API void __stdcall n_set_serial_step(const UINT CardNo, const UINT No, const UINT Step){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " No = " << No << " Step = " << Step << endl;
  return;
}

RTC6_API void __stdcall n_select_serial_set(const UINT CardNo, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " No = " << No << endl;
  return;
}

RTC6_API void __stdcall n_set_serial(const UINT CardNo, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " No = " << No << endl;
  return;
}

RTC6_API double __stdcall n_get_serial(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0.0;
}

RTC6_API double __stdcall n_get_list_serial(const UINT CardNo, UINT& SetNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " SetNo = " << SetNo << endl;
  return 0.0;
}

RTC6_API void __stdcall time_update(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall time_control_eth(const double PPM){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " PPM = " << PPM << endl;
  return;
}

RTC6_API void __stdcall set_serial_step(const UINT No, const UINT Step){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " No = " << No << " Step = " << Step << endl;
  return;
}

RTC6_API void __stdcall select_serial_set(const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " No = " << No << endl;
  return;
}

RTC6_API void __stdcall set_serial(const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " No = " << No << endl;
  return;
}

RTC6_API double __stdcall get_serial(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0.0;
}

RTC6_API double __stdcall get_list_serial(UINT& SetNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " SetNo = " << SetNo << endl;
  return 0.0;
}

RTC6_API void __stdcall n_write_io_port_mask(const UINT CardNo, const UINT Value, const UINT Mask){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Value = " << Value << " Mask = " << Mask << endl;
  return;
}

RTC6_API void __stdcall n_write_8bit_port(const UINT CardNo, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Value = " << Value << endl;
  return;
}

RTC6_API UINT __stdcall n_read_io_port(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API UINT __stdcall n_read_io_port_buffer(const UINT CardNo, const UINT Index, UINT& Value, long& XPos, long& YPos, UINT& Time){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Index = " << Index << " Value = " << Value << " XPos = " << XPos << " YPos = " << YPos << " Time = " << Time << endl;
  return 0;
}

RTC6_API UINT __stdcall n_get_io_status(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API UINT __stdcall n_read_analog_in(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API void __stdcall n_write_da_x(const UINT CardNo, const UINT x, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " x = " << x << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall n_set_laser_off_default(const UINT CardNo, const UINT AnalogOut1, const UINT AnalogOut2, const UINT DigitalOut){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " AnalogOut1 = " << AnalogOut1 << " AnalogOut2 = " << AnalogOut2 << " DigitalOut = " << DigitalOut << endl;
  return;
}

RTC6_API void __stdcall n_set_port_default(const UINT CardNo, const UINT Port, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Port = " << Port << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall n_write_io_port(const UINT CardNo, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall n_write_da_1(const UINT CardNo, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall n_write_da_2(const UINT CardNo, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall write_io_port_mask(const UINT Value, const UINT Mask){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Value = " << Value << " Mask = " << Mask << endl;
  return;
}

RTC6_API void __stdcall write_8bit_port(const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Value = " << Value << endl;
  return;
}

RTC6_API UINT __stdcall read_io_port(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall read_io_port_buffer(const UINT Index, UINT& Value, long& XPos, long& YPos, UINT& Time){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Index = " << Index << " Value = " << Value << " XPos = " << XPos << " YPos = " << YPos << " Time = " << Time << endl;
  return 0;
}

RTC6_API UINT __stdcall get_io_status(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall read_analog_in(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API void __stdcall write_da_x(const UINT x, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " x = " << x << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall set_laser_off_default(const UINT AnalogOut1, const UINT AnalogOut2, const UINT DigitalOut){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " AnalogOut1 = " << AnalogOut1 << " AnalogOut2 = " << AnalogOut2 << " DigitalOut = " << DigitalOut << endl;
  return;
}

RTC6_API void __stdcall set_port_default(const UINT Port, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Port = " << Port << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall write_io_port(const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall write_da_1(const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall write_da_2(const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall n_disable_laser(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_enable_laser(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_laser_signal_on(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_laser_signal_off(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_set_standby(const UINT CardNo, const UINT HalfPeriod, const UINT PulseLength){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HalfPeriod = " << HalfPeriod << " PulseLength = " << PulseLength << endl;
  return;
}

RTC6_API void __stdcall n_set_laser_pulses_ctrl(const UINT CardNo, const UINT HalfPeriod, const UINT PulseLength){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HalfPeriod = " << HalfPeriod << " PulseLength = " << PulseLength << endl;
  return;
}

RTC6_API void __stdcall n_set_firstpulse_killer(const UINT CardNo, const UINT Length){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Length = " << Length << endl;
  return;
}

RTC6_API void __stdcall n_set_qswitch_delay(const UINT CardNo, const UINT Delay){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Delay = " << Delay << endl;
  return;
}

RTC6_API void __stdcall n_set_laser_mode(const UINT CardNo, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_set_laser_control(const UINT CardNo, const UINT Ctrl){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Ctrl = " << Ctrl << endl;
  return;
}

RTC6_API void __stdcall n_set_laser_pin_out(const UINT CardNo, const UINT Pins){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pins = " << Pins << endl;
  return;
}

RTC6_API UINT __stdcall n_get_laser_pin_in(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API void __stdcall n_set_softstart_level(const UINT CardNo, const UINT Index, const UINT Level){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Index = " << Index << " Level = " << Level << endl;
  return;
}

RTC6_API void __stdcall n_set_softstart_mode(const UINT CardNo, const UINT Mode, const UINT Number, const UINT Delay){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << " Number = " << Number << " Delay = " << Delay << endl;
  return;
}

RTC6_API UINT __stdcall n_set_auto_laser_control(const UINT CardNo, const UINT Ctrl, const UINT Value, const UINT Mode, const UINT MinValue, const UINT MaxValue){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Ctrl = " << Ctrl << " Value = " << Value << " Mode = " << Mode << " MinValue = " << MinValue << " MaxValue = " << MaxValue << endl;
  return 0;
}

RTC6_API UINT __stdcall n_set_auto_laser_params(const UINT CardNo, const UINT Ctrl, const UINT Value, const UINT MinValue, const UINT MaxValue){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Ctrl = " << Ctrl << " Value = " << Value << " MinValue = " << MinValue << " MaxValue = " << MaxValue << endl;
  return 0;
}

RTC6_API long __stdcall n_load_auto_laser_control(const UINT CardNo, const char* Name, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Name = " << Name << " No = " << No << endl;
  return 0L;
}

RTC6_API long __stdcall n_load_position_control(const UINT CardNo, const char* Name, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Name = " << Name << " No = " << No << endl;
  return 0L;
}

RTC6_API void __stdcall n_set_default_pixel(const UINT CardNo, const UINT PulseLength){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " PulseLength = " << PulseLength << endl;
  return;
}

RTC6_API void __stdcall n_get_standby(const UINT CardNo, UINT& HalfPeriod, UINT& PulseLength){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HalfPeriod = " << HalfPeriod << " PulseLength = " << PulseLength << endl;
  return;
}

RTC6_API void __stdcall n_set_pulse_picking(const UINT CardNo, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " No = " << No << endl;
  return;
}

RTC6_API void __stdcall n_set_pulse_picking_length(const UINT CardNo, const UINT Length){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Length = " << Length << endl;
  return;
}

RTC6_API void __stdcall n_config_laser_signals(const UINT CardNo, const UINT Config){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Config = " << Config << endl;
  return;
}

RTC6_API void __stdcall n_set_laser_power(const UINT CardNo, const UINT Port, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Port = " << Port << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall n_set_port_default_list(const UINT CardNo, const UINT Port, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Port = " << Port << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall n_spot_distance_ctrl(const UINT CardNo, const double Dist){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Dist = " << Dist << endl;
  return;
}

RTC6_API void __stdcall disable_laser(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall enable_laser(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall laser_signal_on(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall laser_signal_off(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall set_standby(const UINT HalfPeriod, const UINT PulseLength){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HalfPeriod = " << HalfPeriod << " PulseLength = " << PulseLength << endl;
  return;
}

RTC6_API void __stdcall set_laser_pulses_ctrl(const UINT HalfPeriod, const UINT PulseLength){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HalfPeriod = " << HalfPeriod << " PulseLength = " << PulseLength << endl;
  return;
}

RTC6_API void __stdcall set_firstpulse_killer(const UINT Length){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Length = " << Length << endl;
  return;
}

RTC6_API void __stdcall set_qswitch_delay(const UINT Delay){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Delay = " << Delay << endl;
  return;
}

RTC6_API void __stdcall set_laser_mode(const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall set_laser_control(const UINT Ctrl){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Ctrl = " << Ctrl << endl;
  return;
}

RTC6_API void __stdcall set_laser_pin_out(const UINT Pins){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pins = " << Pins << endl;
  return;
}

RTC6_API UINT __stdcall get_laser_pin_in(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API void __stdcall set_softstart_level(const UINT Index, const UINT Level){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Index = " << Index << " Level = " << Level << endl;
  return;
}

RTC6_API void __stdcall set_softstart_mode(const UINT Mode, const UINT Number, const UINT Delay){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << " Number = " << Number << " Delay = " << Delay << endl;
  return;
}

RTC6_API UINT __stdcall set_auto_laser_control(const UINT Ctrl, const UINT Value, const UINT Mode, const UINT MinValue, const UINT MaxValue){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Ctrl = " << Ctrl << " Value = " << Value << " Mode = " << Mode << " MinValue = " << MinValue << " MaxValue = " << MaxValue << endl;
  return 0;
}

RTC6_API UINT __stdcall set_auto_laser_params(const UINT Ctrl, const UINT Value, const UINT MinValue, const UINT MaxValue){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Ctrl = " << Ctrl << " Value = " << Value << " MinValue = " << MinValue << " MaxValue = " << MaxValue << endl;
  return 0;
}

RTC6_API long __stdcall load_auto_laser_control(const char* Name, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Name = " << Name << " No = " << No << endl;
  return 0L;
}

RTC6_API long __stdcall load_position_control(const char* Name, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Name = " << Name << " No = " << No << endl;
  return 0L;
}

RTC6_API void __stdcall set_default_pixel(const UINT PulseLength){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " PulseLength = " << PulseLength << endl;
  return;
}

RTC6_API void __stdcall get_standby(UINT& HalfPeriod, UINT& PulseLength){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HalfPeriod = " << HalfPeriod << " PulseLength = " << PulseLength << endl;
  return;
}

RTC6_API void __stdcall set_pulse_picking(const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " No = " << No << endl;
  return;
}

RTC6_API void __stdcall set_pulse_picking_length(const UINT Length){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Length = " << Length << endl;
  return;
}

RTC6_API void __stdcall config_laser_signals(const UINT Config){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Config = " << Config << endl;
  return;
}

RTC6_API void __stdcall set_laser_power(const UINT Port, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Port = " << Port << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall set_port_default_list(const UINT Port, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Port = " << Port << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall spot_distance_ctrl(const double Dist){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Dist = " << Dist << endl;
  return;
}

RTC6_API void __stdcall n_set_ext_start_delay(const UINT CardNo, const long Delay, const UINT EncoderNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Delay = " << Delay << " EncoderNo = " << EncoderNo << endl;
  return;
}

RTC6_API void __stdcall n_set_rot_center(const UINT CardNo, const long X, const long Y){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << endl;
  return;
}

RTC6_API void __stdcall n_simulate_encoder(const UINT CardNo, const UINT EncoderNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " EncoderNo = " << EncoderNo << endl;
  return;
}

RTC6_API UINT __stdcall n_get_marking_info(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API void __stdcall n_set_encoder_speed_ctrl(const UINT CardNo, const UINT EncoderNo, const double Speed, const double Smooth){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " EncoderNo = " << EncoderNo << " Speed = " << Speed << " Smooth = " << Smooth << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_x(const UINT CardNo, const double ScaleX){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ScaleX = " << ScaleX << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_y(const UINT CardNo, const double ScaleY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ScaleY = " << ScaleY << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_rot(const UINT CardNo, const double Resolution){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Resolution = " << Resolution << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_matrix(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_global_x(const UINT CardNo, const double ScaleX){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ScaleX = " << ScaleX << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_global_y(const UINT CardNo, const double ScaleY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ScaleY = " << ScaleY << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_global_rot(const UINT CardNo, const double Resolution){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Resolution = " << Resolution << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_global_matrix(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_in(const UINT CardNo, const UINT Mode, const double Scale){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << " Scale = " << Scale << endl;
  return;
}

RTC6_API void __stdcall n_set_multi_mcbsp_in(const UINT CardNo, const UINT Ctrl, const UINT P, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Ctrl = " << Ctrl << " P = " << P << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_set_fly_tracking_error(const UINT CardNo, const UINT TrackingErrorX, const UINT TrackingErrorY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " TrackingErrorX = " << TrackingErrorX << " TrackingErrorY = " << TrackingErrorY << endl;
  return;
}

RTC6_API long __stdcall n_load_fly_2d_table(const UINT CardNo, const char* Name, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Name = " << Name << " No = " << No << endl;
  return 0L;
}

RTC6_API void __stdcall n_init_fly_2d(const UINT CardNo, const long OffsetX, const long OffsetY, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " OffsetX = " << OffsetX << " OffsetY = " << OffsetY << " No = " << No << endl;
  return;
}

RTC6_API void __stdcall n_get_fly_2d_offset(const UINT CardNo, long& OffsetX, long& OffsetY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " OffsetX = " << OffsetX << " OffsetY = " << OffsetY << endl;
  return;
}

RTC6_API void __stdcall n_get_encoder(const UINT CardNo, long& Encoder0, long& Encoder1){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Encoder0 = " << Encoder0 << " Encoder1 = " << Encoder1 << endl;
  return;
}

RTC6_API void __stdcall n_read_encoder(const UINT CardNo, long& Encoder0_1, long& Encoder1_1, long& Encoder0_2, long& Encoder1_2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Encoder0_1 = " << Encoder0_1 << " Encoder1_1 = " << Encoder1_1 << " Encoder0_2 = " << Encoder0_2 << " Encoder1_2 = " << Encoder1_2 << endl;
  return;
}

RTC6_API long __stdcall n_get_mcbsp(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0L;
}

RTC6_API long __stdcall n_read_mcbsp(const UINT CardNo, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " No = " << No << endl;
  return 0L;
}

RTC6_API long __stdcall n_read_multi_mcbsp(const UINT CardNo, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " No = " << No << endl;
  return 0L;
}

RTC6_API void __stdcall set_ext_start_delay(const long Delay, const UINT EncoderNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Delay = " << Delay << " EncoderNo = " << EncoderNo << endl;
  return;
}

RTC6_API void __stdcall set_rot_center(const long X, const long Y){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << endl;
  return;
}

RTC6_API void __stdcall simulate_encoder(const UINT EncoderNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " EncoderNo = " << EncoderNo << endl;
  return;
}

RTC6_API UINT __stdcall get_marking_info(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API void __stdcall set_encoder_speed_ctrl(const UINT EncoderNo, const double Speed, const double Smooth){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " EncoderNo = " << EncoderNo << " Speed = " << Speed << " Smooth = " << Smooth << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_x(const double ScaleX){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ScaleX = " << ScaleX << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_y(const double ScaleY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ScaleY = " << ScaleY << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_rot(const double Resolution){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Resolution = " << Resolution << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_matrix(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_global_x(const double ScaleX){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ScaleX = " << ScaleX << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_global_y(const double ScaleY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ScaleY = " << ScaleY << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_global_rot(const double Resolution){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Resolution = " << Resolution << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_global_matrix(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_in(const UINT Mode, const double Scale){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << " Scale = " << Scale << endl;
  return;
}

RTC6_API void __stdcall set_multi_mcbsp_in(const UINT Ctrl, const UINT P, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Ctrl = " << Ctrl << " P = " << P << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall set_fly_tracking_error(const UINT TrackingErrorX, const UINT TrackingErrorY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " TrackingErrorX = " << TrackingErrorX << " TrackingErrorY = " << TrackingErrorY << endl;
  return;
}

RTC6_API long __stdcall load_fly_2d_table(const char* Name, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Name = " << Name << " No = " << No << endl;
  return 0L;
}

RTC6_API void __stdcall init_fly_2d(const long OffsetX, const long OffsetY, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " OffsetX = " << OffsetX << " OffsetY = " << OffsetY << " No = " << No << endl;
  return;
}

RTC6_API void __stdcall get_fly_2d_offset(long& OffsetX, long& OffsetY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " OffsetX = " << OffsetX << " OffsetY = " << OffsetY << endl;
  return;
}

RTC6_API void __stdcall get_encoder(long& Encoder0, long& Encoder1){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Encoder0 = " << Encoder0 << " Encoder1 = " << Encoder1 << endl;
  return;
}

RTC6_API void __stdcall read_encoder(long& Encoder0_1, long& Encoder1_1, long& Encoder0_2, long& Encoder1_2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Encoder0_1 = " << Encoder0_1 << " Encoder1_1 = " << Encoder1_1 << " Encoder0_2 = " << Encoder0_2 << " Encoder1_2 = " << Encoder1_2 << endl;
  return;
}

RTC6_API long __stdcall get_mcbsp(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0L;
}

RTC6_API long __stdcall read_mcbsp(const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " No = " << No << endl;
  return 0L;
}

RTC6_API long __stdcall read_multi_mcbsp(const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " No = " << No << endl;
  return 0L;
}

RTC6_API double __stdcall n_get_time(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0.0;
}

RTC6_API double __stdcall n_get_lap_time(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0.0;
}

RTC6_API void __stdcall n_measurement_status(const UINT CardNo, UINT& Busy, UINT& Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Busy = " << Busy << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_get_waveform_offset(const UINT CardNo, const UINT Channel, const UINT Offset, const UINT Number, const ULONG_PTR Ptr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Channel = " << Channel << " Offset = " << Offset << " Number = " << Number << " Ptr = " << Ptr << endl;
  return;
}

RTC6_API void __stdcall n_get_waveform(const UINT CardNo, const UINT Channel, const UINT Number, const ULONG_PTR Ptr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Channel = " << Channel << " Number = " << Number << " Ptr = " << Ptr << endl;
  return;
}

RTC6_API void __stdcall n_bounce_supp(const UINT CardNo, const UINT Length){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Length = " << Length << endl;
  return;
}

RTC6_API void __stdcall n_home_position_4(const UINT CardNo, const long X0Home, const long X1Home, const long X2Home, const long X3Home){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X0Home = " << X0Home << " X1Home = " << X1Home << " X2Home = " << X2Home << " X3Home = " << X3Home << endl;
  return;
}

RTC6_API void __stdcall n_get_home_position_4(const UINT CardNo, long& X0Home, long& X1Home, long& X2Home, long& X3Home){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X0Home = " << X0Home << " X1Home = " << X1Home << " X2Home = " << X2Home << " X3Home = " << X3Home << endl;
  return;
}

RTC6_API void __stdcall n_set_home_4_return_time(const UINT CardNo, const UINT Time){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Time = " << Time << endl;
  return;
}

RTC6_API UINT __stdcall n_get_home_4_return_time(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API void __stdcall n_home_position_xyz(const UINT CardNo, const long XHome, const long YHome, const long ZHome){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " XHome = " << XHome << " YHome = " << YHome << " ZHome = " << ZHome << endl;
  return;
}

RTC6_API void __stdcall n_home_position(const UINT CardNo, const long XHome, const long YHome){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " XHome = " << XHome << " YHome = " << YHome << endl;
  return;
}

RTC6_API UINT __stdcall n_uart_config(const UINT CardNo, const UINT BaudRate){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " BaudRate = " << BaudRate << endl;
  return 0;
}

RTC6_API void __stdcall n_rs232_config(const UINT CardNo, const UINT BaudRate){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " BaudRate = " << BaudRate << endl;
  return;
}

RTC6_API void __stdcall n_rs232_write_data(const UINT CardNo, const UINT Data){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Data = " << Data << endl;
  return;
}

RTC6_API void __stdcall n_rs232_write_text(const UINT CardNo, const char* pData){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " pData = " << pData << endl;
  return;
}

RTC6_API UINT __stdcall n_rs232_read_data(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API UINT __stdcall n_set_mcbsp_freq(const UINT CardNo, const UINT Freq){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Freq = " << Freq << endl;
  return 0;
}

RTC6_API void __stdcall n_mcbsp_init(const UINT CardNo, const UINT XDelay, const UINT RDelay){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " XDelay = " << XDelay << " RDelay = " << RDelay << endl;
  return;
}

RTC6_API void __stdcall n_mcbsp_init_spi(const UINT CardNo, const UINT ClockLevel, const UINT ClockDelay){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ClockLevel = " << ClockLevel << " ClockDelay = " << ClockDelay << endl;
  return;
}

RTC6_API UINT __stdcall n_get_overrun(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API UINT __stdcall n_get_master_slave(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API void __stdcall n_get_transform(const UINT CardNo, const UINT Number, const ULONG_PTR Ptr1, const ULONG_PTR Ptr2, const ULONG_PTR Ptr, const UINT Code){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Number = " << Number << " Ptr1 = " << Ptr1 << " Ptr2 = " << Ptr2 << " Ptr = " << Ptr << " Code = " << Code << endl;
  return;
}

RTC6_API void __stdcall n_stop_trigger(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_move_to(const UINT CardNo, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_set_enduring_wobbel(const UINT CardNo, const UINT CenterX, const UINT CenterY, const UINT CenterZ, const UINT LimitHi, const UINT LimitLo, const double ScaleX, const double ScaleY, const double ScaleZ){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " CenterX = " << CenterX << " CenterY = " << CenterY << " CenterZ = " << CenterZ << " LimitHi = " << LimitHi << " LimitLo = " << LimitLo << " ScaleX = " << ScaleX << " ScaleY = " << ScaleY << " ScaleZ = " << ScaleZ << endl;
  return;
}

RTC6_API void __stdcall n_set_enduring_wobbel_2(const UINT CardNo, const UINT CenterX, const UINT CenterY, const UINT CenterZ, const UINT LimitHi, const UINT LimitLo, const double ScaleX, const double ScaleY, const double ScaleZ){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " CenterX = " << CenterX << " CenterY = " << CenterY << " CenterZ = " << CenterZ << " LimitHi = " << LimitHi << " LimitLo = " << LimitLo << " ScaleX = " << ScaleX << " ScaleY = " << ScaleY << " ScaleZ = " << ScaleZ << endl;
  return;
}

RTC6_API void __stdcall n_set_free_variable(const UINT CardNo, const UINT VarNo, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " VarNo = " << VarNo << " Value = " << Value << endl;
  return;
}

RTC6_API UINT __stdcall n_get_free_variable(const UINT CardNo, const UINT VarNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " VarNo = " << VarNo << endl;
  return 0;
}

RTC6_API void __stdcall n_set_mcbsp_out_ptr(const UINT CardNo, const UINT Number, const ULONG_PTR SignalPtr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Number = " << Number << " SignalPtr = " << SignalPtr << endl;
  return;
}

RTC6_API void __stdcall n_periodic_toggle(const UINT CardNo, const UINT Port, const UINT Mask, const UINT P1, const UINT P2, const UINT Count, const UINT Start){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Port = " << Port << " Mask = " << Mask << " P1 = " << P1 << " P2 = " << P2 << " Count = " << Count << " Start = " << Start << endl;
  return;
}

RTC6_API void __stdcall n_multi_axis_config(const UINT CardNo, const UINT Cfg, const ULONG_PTR Ptr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Cfg = " << Cfg << " Ptr = " << Ptr << endl;
  return;
}

RTC6_API void __stdcall n_quad_axis_init(const UINT CardNo, const UINT Idle, const double X1, const double Y1){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Idle = " << Idle << " X1 = " << X1 << " Y1 = " << Y1 << endl;
  return;
}

RTC6_API UINT __stdcall n_quad_axis_get_status(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return 0;
}

RTC6_API void __stdcall n_quad_axis_get_values(const UINT CardNo, double& X1, double& Y1, UINT& Flags0, UINT& Flags1){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X1 = " << X1 << " Y1 = " << Y1 << " Flags0 = " << Flags0 << " Flags1 = " << Flags1 << endl;
  return;
}

RTC6_API double __stdcall get_time(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0.0;
}

RTC6_API double __stdcall get_lap_time(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0.0;
}

RTC6_API void __stdcall measurement_status(UINT& Busy, UINT& Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Busy = " << Busy << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall get_waveform_offset(const UINT Channel, const UINT Offset, const UINT Number, const ULONG_PTR Ptr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Channel = " << Channel << " Offset = " << Offset << " Number = " << Number << " Ptr = " << Ptr << endl;
  return;
}

RTC6_API void __stdcall get_waveform(const UINT Channel, const UINT Number, const ULONG_PTR Ptr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Channel = " << Channel << " Number = " << Number << " Ptr = " << Ptr << endl;
  return;
}

RTC6_API void __stdcall bounce_supp(const UINT Length){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Length = " << Length << endl;
  return;
}

RTC6_API void __stdcall home_position_4(const long X0Home, const long X1Home, const long X2Home, const long X3Home){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X0Home = " << X0Home << " X1Home = " << X1Home << " X2Home = " << X2Home << " X3Home = " << X3Home << endl;
  return;
}

RTC6_API void __stdcall get_home_position_4(long& X0Home, long& X1Home, long& X2Home, long& X3Home){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X0Home = " << X0Home << " X1Home = " << X1Home << " X2Home = " << X2Home << " X3Home = " << X3Home << endl;
  return;
}

RTC6_API void __stdcall set_home_4_return_time(const UINT Time){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Time = " << Time << endl;
  return;
}

RTC6_API UINT __stdcall get_home_4_return_time(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API void __stdcall home_position_xyz(const long XHome, const long YHome, const long ZHome){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " XHome = " << XHome << " YHome = " << YHome << " ZHome = " << ZHome << endl;
  return;
}

RTC6_API void __stdcall home_position(const long XHome, const long YHome){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " XHome = " << XHome << " YHome = " << YHome << endl;
  return;
}

RTC6_API UINT __stdcall uart_config(const UINT BaudRate){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " BaudRate = " << BaudRate << endl;
  return 0;
}

RTC6_API void __stdcall rs232_config(const UINT BaudRate){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " BaudRate = " << BaudRate << endl;
  return;
}

RTC6_API void __stdcall rs232_write_data(const UINT Data){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Data = " << Data << endl;
  return;
}

RTC6_API void __stdcall rs232_write_text(const char* pData){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " pData = " << pData << endl;
  return;
}

RTC6_API UINT __stdcall rs232_read_data(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall set_mcbsp_freq(const UINT Freq){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Freq = " << Freq << endl;
  return 0;
}

RTC6_API void __stdcall mcbsp_init(const UINT XDelay, const UINT RDelay){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " XDelay = " << XDelay << " RDelay = " << RDelay << endl;
  return;
}

RTC6_API void __stdcall mcbsp_init_spi(const UINT ClockLevel, const UINT ClockDelay){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ClockLevel = " << ClockLevel << " ClockDelay = " << ClockDelay << endl;
  return;
}

RTC6_API UINT __stdcall get_overrun(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API UINT __stdcall get_master_slave(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API void __stdcall get_transform(const UINT Number, const ULONG_PTR Ptr1, const ULONG_PTR Ptr2, const ULONG_PTR Ptr, const UINT Code){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Number = " << Number << " Ptr1 = " << Ptr1 << " Ptr2 = " << Ptr2 << " Ptr = " << Ptr << " Code = " << Code << endl;
  return;
}

RTC6_API void __stdcall stop_trigger(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall move_to(const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall set_enduring_wobbel(const UINT CenterX, const UINT CenterY, const UINT CenterZ, const UINT LimitHi, const UINT LimitLo, const double ScaleX, const double ScaleY, const double ScaleZ){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CenterX = " << CenterX << " CenterY = " << CenterY << " CenterZ = " << CenterZ << " LimitHi = " << LimitHi << " LimitLo = " << LimitLo << " ScaleX = " << ScaleX << " ScaleY = " << ScaleY << " ScaleZ = " << ScaleZ << endl;
  return;
}

RTC6_API void __stdcall set_enduring_wobbel_2(const UINT CenterX, const UINT CenterY, const UINT CenterZ, const UINT LimitHi, const UINT LimitLo, const double ScaleX, const double ScaleY, const double ScaleZ){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CenterX = " << CenterX << " CenterY = " << CenterY << " CenterZ = " << CenterZ << " LimitHi = " << LimitHi << " LimitLo = " << LimitLo << " ScaleX = " << ScaleX << " ScaleY = " << ScaleY << " ScaleZ = " << ScaleZ << endl;
  return;
}

RTC6_API void __stdcall set_free_variable(const UINT VarNo, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " VarNo = " << VarNo << " Value = " << Value << endl;
  return;
}

RTC6_API UINT __stdcall get_free_variable(const UINT VarNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " VarNo = " << VarNo << endl;
  return 0;
}

RTC6_API void __stdcall set_mcbsp_out_ptr(const UINT Number, const ULONG_PTR SignalPtr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Number = " << Number << " SignalPtr = " << SignalPtr << endl;
  return;
}

RTC6_API void __stdcall periodic_toggle(const UINT Port, const UINT Mask, const UINT P1, const UINT P2, const UINT Count, const UINT Start){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Port = " << Port << " Mask = " << Mask << " P1 = " << P1 << " P2 = " << P2 << " Count = " << Count << " Start = " << Start << endl;
  return;
}

RTC6_API void __stdcall multi_axis_config(const UINT Cfg, const ULONG_PTR Ptr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Cfg = " << Cfg << " Ptr = " << Ptr << endl;
  return;
}

RTC6_API void __stdcall quad_axis_init(const UINT Idle, const double X1, const double Y1){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Idle = " << Idle << " X1 = " << X1 << " Y1 = " << Y1 << endl;
  return;
}

RTC6_API UINT __stdcall quad_axis_get_status(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return 0;
}

RTC6_API void __stdcall quad_axis_get_values(double& X1, double& Y1, UINT& Flags0, UINT& Flags1){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X1 = " << X1 << " Y1 = " << Y1 << " Flags0 = " << Flags0 << " Flags1 = " << Flags1 << endl;
  return;
}

RTC6_API void __stdcall n_set_defocus(const UINT CardNo, const long Shift){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Shift = " << Shift << endl;
  return;
}

RTC6_API void __stdcall n_set_defocus_offset(const UINT CardNo, const long Shift){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Shift = " << Shift << endl;
  return;
}

RTC6_API void __stdcall n_goto_xyz(const UINT CardNo, const long X, const long Y, const long Z){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " Z = " << Z << endl;
  return;
}

RTC6_API void __stdcall n_set_zoom(const UINT CardNo, const UINT Zoom){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Zoom = " << Zoom << endl;
  return;
}

RTC6_API void __stdcall n_goto_xy(const UINT CardNo, const long X, const long Y){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << endl;
  return;
}

RTC6_API long __stdcall n_get_z_distance(const UINT CardNo, const long X, const long Y, const long Z){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " Z = " << Z << endl;
  return 0L;
}

RTC6_API void __stdcall set_defocus(const long Shift){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Shift = " << Shift << endl;
  return;
}

RTC6_API void __stdcall set_defocus_offset(const long Shift){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Shift = " << Shift << endl;
  return;
}

RTC6_API void __stdcall goto_xyz(const long X, const long Y, const long Z){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " Z = " << Z << endl;
  return;
}

RTC6_API void __stdcall goto_xy(const long X, const long Y){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << endl;
  return;
}

RTC6_API void __stdcall set_zoom(const UINT Zoom){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Zoom = " << Zoom << endl;
  return;
}

RTC6_API long __stdcall get_z_distance(const long X, const long Y, const long Z){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " Z = " << Z << endl;
  return 0L;
}

RTC6_API void __stdcall n_set_offset_xyz(const UINT CardNo, const UINT HeadNo, const long XOffset, const long YOffset, const long ZOffset, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " XOffset = " << XOffset << " YOffset = " << YOffset << " ZOffset = " << ZOffset << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall n_set_offset(const UINT CardNo, const UINT HeadNo, const long XOffset, const long YOffset, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " XOffset = " << XOffset << " YOffset = " << YOffset << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall n_set_matrix(const UINT CardNo, const UINT HeadNo, const double M11, const double M12, const double M21, const double M22, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " M11 = " << M11 << " M12 = " << M12 << " M21 = " << M21 << " M22 = " << M22 << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall n_set_angle(const UINT CardNo, const UINT HeadNo, const double Angle, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " Angle = " << Angle << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall n_set_scale(const UINT CardNo, const UINT HeadNo, const double Scale, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " Scale = " << Scale << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall n_apply_mcbsp(const UINT CardNo, const UINT HeadNo, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " at_once = " << at_once << endl;
  return;
}

RTC6_API UINT __stdcall n_upload_transform(const UINT CardNo, const UINT HeadNo, const ULONG_PTR Ptr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " Ptr = " << Ptr << endl;
  return 0;
}

RTC6_API void __stdcall set_offset_xyz(const UINT HeadNo, const long XOffset, const long YOffset, const long ZOffset, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " XOffset = " << XOffset << " YOffset = " << YOffset << " ZOffset = " << ZOffset << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall set_offset(const UINT HeadNo, const long XOffset, const long YOffset, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " XOffset = " << XOffset << " YOffset = " << YOffset << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall set_matrix(const UINT HeadNo, const double M11, const double M12, const double M21, const double M22, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " M11 = " << M11 << " M12 = " << M12 << " M21 = " << M21 << " M22 = " << M22 << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall set_angle(const UINT HeadNo, const double Angle, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " Angle = " << Angle << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall set_scale(const UINT HeadNo, const double Scale, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " Scale = " << Scale << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall apply_mcbsp(const UINT HeadNo, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " at_once = " << at_once << endl;
  return;
}

RTC6_API UINT __stdcall upload_transform(const UINT HeadNo, const ULONG_PTR Ptr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " Ptr = " << Ptr << endl;
  return 0;
}

RTC6_API void __stdcall n_set_delay_mode(const UINT CardNo, const UINT VarPoly, const UINT DirectMove3D, const UINT EdgeLevel, const UINT MinJumpDelay, const UINT JumpLengthLimit){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " VarPoly = " << VarPoly << " DirectMove3D = " << DirectMove3D << " EdgeLevel = " << EdgeLevel << " MinJumpDelay = " << MinJumpDelay << " JumpLengthLimit = " << JumpLengthLimit << endl;
  return;
}

RTC6_API void __stdcall n_set_jump_speed_ctrl(const UINT CardNo, const double Speed){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Speed = " << Speed << endl;
  return;
}

RTC6_API void __stdcall n_set_mark_speed_ctrl(const UINT CardNo, const double Speed){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Speed = " << Speed << endl;
  return;
}

RTC6_API void __stdcall n_set_sky_writing_para(const UINT CardNo, const double Timelag, const long LaserOnShift, const UINT Nprev, const UINT Npost){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Timelag = " << Timelag << " LaserOnShift = " << LaserOnShift << " Nprev = " << Nprev << " Npost = " << Npost << endl;
  return;
}

RTC6_API void __stdcall n_set_sky_writing_limit(const UINT CardNo, const double CosAngle){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " CosAngle = " << CosAngle << endl;
  return;
}

RTC6_API void __stdcall n_set_sky_writing_mode(const UINT CardNo, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << endl;
  return;
}

RTC6_API long __stdcall n_load_varpolydelay(const UINT CardNo, const char* Name, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Name = " << Name << " No = " << No << endl;
  return 0L;
}

RTC6_API void __stdcall n_set_hi(const UINT CardNo, const UINT HeadNo, const double GalvoGainX, const double GalvoGainY, const long GalvoOffsetX, const long GalvoOffsetY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " GalvoGainX = " << GalvoGainX << " GalvoGainY = " << GalvoGainY << " GalvoOffsetX = " << GalvoOffsetX << " GalvoOffsetY = " << GalvoOffsetY << endl;
  return;
}

RTC6_API void __stdcall n_get_hi_pos(const UINT CardNo, const UINT HeadNo, long& X1, long& X2, long& Y1, long& Y2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " X1 = " << X1 << " X2 = " << X2 << " Y1 = " << Y1 << " Y2 = " << Y2 << endl;
  return;
}

RTC6_API UINT __stdcall n_auto_cal(const UINT CardNo, const UINT HeadNo, const UINT Command){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " Command = " << Command << endl;
  return 0;
}

RTC6_API UINT __stdcall n_get_auto_cal(const UINT CardNo, const UINT HeadNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << endl;
  return 0;
}

RTC6_API UINT __stdcall n_write_hi_pos(const UINT CardNo, const UINT HeadNo, const long X1, const long X2, const long Y1, const long Y2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " X1 = " << X1 << " X2 = " << X2 << " Y1 = " << Y1 << " Y2 = " << Y2 << endl;
  return 0;
}

RTC6_API void __stdcall n_set_timelag_compensation(const UINT CardNo, const UINT HeadNo, const UINT TimeLagXY, const UINT TimeLagZ){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " TimeLagXY = " << TimeLagXY << " TimeLagZ = " << TimeLagZ << endl;
  return;
}

RTC6_API void __stdcall n_set_sky_writing(const UINT CardNo, const double Timelag, const long LaserOnShift){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Timelag = " << Timelag << " LaserOnShift = " << LaserOnShift << endl;
  return;
}

RTC6_API void __stdcall n_get_hi_data(const UINT CardNo, long& X1, long& X2, long& Y1, long& Y2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X1 = " << X1 << " X2 = " << X2 << " Y1 = " << Y1 << " Y2 = " << Y2 << endl;
  return;
}

RTC6_API void __stdcall set_delay_mode(const UINT VarPoly, const UINT DirectMove3D, const UINT EdgeLevel, const UINT MinJumpDelay, const UINT JumpLengthLimit){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " VarPoly = " << VarPoly << " DirectMove3D = " << DirectMove3D << " EdgeLevel = " << EdgeLevel << " MinJumpDelay = " << MinJumpDelay << " JumpLengthLimit = " << JumpLengthLimit << endl;
  return;
}

RTC6_API void __stdcall set_jump_speed_ctrl(const double Speed){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Speed = " << Speed << endl;
  return;
}

RTC6_API void __stdcall set_mark_speed_ctrl(const double Speed){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Speed = " << Speed << endl;
  return;
}

RTC6_API void __stdcall set_sky_writing_para(const double Timelag, const long LaserOnShift, const UINT Nprev, const UINT Npost){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Timelag = " << Timelag << " LaserOnShift = " << LaserOnShift << " Nprev = " << Nprev << " Npost = " << Npost << endl;
  return;
}

RTC6_API void __stdcall set_sky_writing_limit(const double CosAngle){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CosAngle = " << CosAngle << endl;
  return;
}

RTC6_API void __stdcall set_sky_writing_mode(const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << endl;
  return;
}

RTC6_API long __stdcall load_varpolydelay(const char* Name, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Name = " << Name << " No = " << No << endl;
  return 0L;
}

RTC6_API void __stdcall set_hi(const UINT HeadNo, const double GalvoGainX, const double GalvoGainY, const long GalvoOffsetX, const long GalvoOffsetY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " GalvoGainX = " << GalvoGainX << " GalvoGainY = " << GalvoGainY << " GalvoOffsetX = " << GalvoOffsetX << " GalvoOffsetY = " << GalvoOffsetY << endl;
  return;
}

RTC6_API void __stdcall get_hi_pos(const UINT HeadNo, long& X1, long& X2, long& Y1, long& Y2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " X1 = " << X1 << " X2 = " << X2 << " Y1 = " << Y1 << " Y2 = " << Y2 << endl;
  return;
}

RTC6_API UINT __stdcall auto_cal(const UINT HeadNo, const UINT Command){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " Command = " << Command << endl;
  return 0;
}

RTC6_API UINT __stdcall get_auto_cal(const UINT HeadNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << endl;
  return 0;
}

RTC6_API UINT __stdcall write_hi_pos(const UINT HeadNo, const long X1, const long X2, const long Y1, const long Y2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " X1 = " << X1 << " X2 = " << X2 << " Y1 = " << Y1 << " Y2 = " << Y2 << endl;
  return 0;
}

RTC6_API void __stdcall set_timelag_compensation(const UINT HeadNo, const UINT TimeLagXY, const UINT TimeLagZ){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " TimeLagXY = " << TimeLagXY << " TimeLagZ = " << TimeLagZ << endl;
  return;
}

RTC6_API void __stdcall set_sky_writing(const double Timelag, const long LaserOnShift){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Timelag = " << Timelag << " LaserOnShift = " << LaserOnShift << endl;
  return;
}

RTC6_API void __stdcall get_hi_data(long& X1, long& X2, long& Y1, long& Y2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X1 = " << X1 << " X2 = " << X2 << " Y1 = " << Y1 << " Y2 = " << Y2 << endl;
  return;
}

RTC6_API void __stdcall n_send_user_data(const UINT CardNo, const UINT Head, const UINT Axis, const long Data0, const long Data1, const long Data2, const long Data3, const long Data4){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Head = " << Head << " Axis = " << Axis << " Data0 = " << Data0 << " Data1 = " << Data1 << " Data2 = " << Data2 << " Data3 = " << Data3 << " Data4 = " << Data4 << endl;
  return;
}

RTC6_API long __stdcall n_read_user_data(const UINT CardNo, const UINT Head, const UINT Axis, long& Data0, long& Data1, long& Data2, long& Data3, long& Data4){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Head = " << Head << " Axis = " << Axis << " Data0 = " << Data0 << " Data1 = " << Data1 << " Data2 = " << Data2 << " Data3 = " << Data3 << " Data4 = " << Data4 << endl;
  return 0L;
}

RTC6_API void __stdcall n_control_command(const UINT CardNo, const UINT Head, const UINT Axis, const UINT Data){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Head = " << Head << " Axis = " << Axis << " Data = " << Data << endl;
  return;
}

RTC6_API long __stdcall n_get_value(const UINT CardNo, const UINT Signal){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Signal = " << Signal << endl;
  return 0L;
}

RTC6_API void __stdcall n_get_values(const UINT CardNo, const ULONG_PTR SignalPtr, const ULONG_PTR ResultPtr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " SignalPtr = " << SignalPtr << " ResultPtr = " << ResultPtr << endl;
  return;
}

RTC6_API void __stdcall n_get_galvo_controls(const UINT CardNo, const ULONG_PTR SignalPtr, const ULONG_PTR ResultPtr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " SignalPtr = " << SignalPtr << " ResultPtr = " << ResultPtr << endl;
  return;
}

RTC6_API UINT __stdcall n_get_head_status(const UINT CardNo, const UINT Head){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Head = " << Head << endl;
  return 0;
}

RTC6_API long __stdcall n_set_jump_mode(const UINT CardNo, const long Flag, const UINT Length, const long VA1, const long VA2, const long VB1, const long VB2, const long JA1, const long JA2, const long JB1, const long JB2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Flag = " << Flag << " Length = " << Length << " VA1 = " << VA1 << " VA2 = " << VA2 << " VB1 = " << VB1 << " VB2 = " << VB2 << " JA1 = " << JA1 << " JA2 = " << JA2 << " JB1 = " << JB1 << " JB2 = " << JB2 << endl;
  return 0L;
}

RTC6_API long __stdcall n_load_jump_table_offset(const UINT CardNo, const char* Name, const UINT No, const UINT PosAck, const long Offset, const UINT MinDelay, const UINT MaxDelay, const UINT ListPos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Name = " << Name << " No = " << No << " PosAck = " << PosAck << " Offset = " << Offset << " MinDelay = " << MinDelay << " MaxDelay = " << MaxDelay << " ListPos = " << ListPos << endl;
  return 0L;
}

RTC6_API UINT __stdcall n_get_jump_table(const UINT CardNo, const ULONG_PTR Ptr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Ptr = " << Ptr << endl;
  return 0;
}

RTC6_API UINT __stdcall n_set_jump_table(const UINT CardNo, const ULONG_PTR Ptr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Ptr = " << Ptr << endl;
  return 0;
}

RTC6_API long __stdcall n_load_jump_table(const UINT CardNo, const char* Name, const UINT No, const UINT PosAck, const UINT MinDelay, const UINT MaxDelay, const UINT ListPos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Name = " << Name << " No = " << No << " PosAck = " << PosAck << " MinDelay = " << MinDelay << " MaxDelay = " << MaxDelay << " ListPos = " << ListPos << endl;
  return 0L;
}

RTC6_API void __stdcall send_user_data(const UINT Head, const UINT Axis, const long Data0, const long Data1, const long Data2, const long Data3, const long Data4){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Head = " << Head << " Axis = " << Axis << " Data0 = " << Data0 << " Data1 = " << Data1 << " Data2 = " << Data2 << " Data3 = " << Data3 << " Data4 = " << Data4 << endl;
  return;
}

RTC6_API long __stdcall read_user_data(const UINT Head, const UINT Axis, long& Data0, long& Data1, long& Data2, long& Data3, long& Data4){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Head = " << Head << " Axis = " << Axis << " Data0 = " << Data0 << " Data1 = " << Data1 << " Data2 = " << Data2 << " Data3 = " << Data3 << " Data4 = " << Data4 << endl;
  return 0L;
}

RTC6_API void __stdcall control_command(const UINT Head, const UINT Axis, const UINT Data){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Head = " << Head << " Axis = " << Axis << " Data = " << Data << endl;
  return;
}

RTC6_API long __stdcall get_value(const UINT Signal){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Signal = " << Signal << endl;
  return 0L;
}

RTC6_API void __stdcall get_values(const ULONG_PTR SignalPtr, const ULONG_PTR ResultPtr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " SignalPtr = " << SignalPtr << " ResultPtr = " << ResultPtr << endl;
  return;
}

RTC6_API void __stdcall get_galvo_controls(const ULONG_PTR SignalPtr, const ULONG_PTR ResultPtr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " SignalPtr = " << SignalPtr << " ResultPtr = " << ResultPtr << endl;
  return;
}

RTC6_API UINT __stdcall get_head_status(const UINT Head){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Head = " << Head << endl;
  return 0;
}

RTC6_API long __stdcall set_jump_mode(const long Flag, const UINT Length, const long VA1, const long VA2, const long VB1, const long VB2, const long JA1, const long JA2, const long JB1, const long JB2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Flag = " << Flag << " Length = " << Length << " VA1 = " << VA1 << " VA2 = " << VA2 << " VB1 = " << VB1 << " VB2 = " << VB2 << " JA1 = " << JA1 << " JA2 = " << JA2 << " JB1 = " << JB1 << " JB2 = " << JB2 << endl;
  return 0L;
}

RTC6_API long __stdcall load_jump_table_offset(const char* Name, const UINT No, const UINT PosAck, const long Offset, const UINT MinDelay, const UINT MaxDelay, const UINT ListPos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Name = " << Name << " No = " << No << " PosAck = " << PosAck << " Offset = " << Offset << " MinDelay = " << MinDelay << " MaxDelay = " << MaxDelay << " ListPos = " << ListPos << endl;
  return 0L;
}

RTC6_API UINT __stdcall get_jump_table(const ULONG_PTR Ptr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Ptr = " << Ptr << endl;
  return 0;
}

RTC6_API UINT __stdcall set_jump_table(const ULONG_PTR Ptr){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Ptr = " << Ptr << endl;
  return 0;
}

RTC6_API long __stdcall load_jump_table(const char* Name, const UINT No, const UINT PosAck, const UINT MinDelay, const UINT MaxDelay, const UINT ListPos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Name = " << Name << " No = " << No << " PosAck = " << PosAck << " MinDelay = " << MinDelay << " MaxDelay = " << MaxDelay << " ListPos = " << ListPos << endl;
  return 0L;
}

RTC6_API UINT __stdcall n_get_scanahead_params(const UINT CardNo, const UINT HeadNo, UINT& PreViewTime, UINT& Vmax, double& Amax){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " PreViewTime = " << PreViewTime << " Vmax = " << Vmax << " Amax = " << Amax << endl;
  return 0;
}

RTC6_API long __stdcall n_activate_scanahead_autodelays(const UINT CardNo, const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << endl;
  return 0L;
}

RTC6_API void __stdcall n_set_scanahead_laser_shifts(const UINT CardNo, const long dLasOn, const long dLasOff){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dLasOn = " << dLasOn << " dLasOff = " << dLasOff << endl;
  return;
}

RTC6_API void __stdcall n_set_scanahead_line_params(const UINT CardNo, const UINT CornerScale, const UINT EndScale, const UINT AccScale){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " CornerScale = " << CornerScale << " EndScale = " << EndScale << " AccScale = " << AccScale << endl;
  return;
}

RTC6_API void __stdcall n_set_scanahead_line_params_ex(const UINT CardNo, const UINT CornerScale, const UINT EndScale, const UINT AccScale, const UINT JumpScale){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " CornerScale = " << CornerScale << " EndScale = " << EndScale << " AccScale = " << AccScale << " JumpScale = " << JumpScale << endl;
  return;
}

RTC6_API UINT __stdcall n_set_scanahead_params(const UINT CardNo, const UINT Mode, const UINT HeadNo, const UINT TableNo, const UINT PreViewTime, const UINT Vmax, const double Amax){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << " HeadNo = " << HeadNo << " TableNo = " << TableNo << " PreViewTime = " << PreViewTime << " Vmax = " << Vmax << " Amax = " << Amax << endl;
  return 0;
}

RTC6_API void __stdcall n_set_scanahead_speed_control(const UINT CardNo, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << endl;
  return;
}

RTC6_API UINT __stdcall get_scanahead_params(const UINT HeadNo, UINT& PreViewTime, UINT& Vmax, double& Amax){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " PreViewTime = " << PreViewTime << " Vmax = " << Vmax << " Amax = " << Amax << endl;
  return 0;
}

RTC6_API long __stdcall activate_scanahead_autodelays(const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << endl;
  return 0L;
}

RTC6_API void __stdcall set_scanahead_laser_shifts(const long dLasOn, const long dLasOff){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dLasOn = " << dLasOn << " dLasOff = " << dLasOff << endl;
  return;
}

RTC6_API void __stdcall set_scanahead_line_params(const UINT CornerScale, const UINT EndScale, const UINT AccScale){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CornerScale = " << CornerScale << " EndScale = " << EndScale << " AccScale = " << AccScale << endl;
  return;
}

RTC6_API void __stdcall set_scanahead_line_params_ex(const UINT CornerScale, const UINT EndScale, const UINT AccScale, const UINT JumpScale){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CornerScale = " << CornerScale << " EndScale = " << EndScale << " AccScale = " << AccScale << " JumpScale = " << JumpScale << endl;
  return;
}

RTC6_API UINT __stdcall set_scanahead_params(const UINT Mode, const UINT HeadNo, const UINT TableNo, const UINT PreViewTime, const UINT Vmax, const double Amax){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << " HeadNo = " << HeadNo << " TableNo = " << TableNo << " PreViewTime = " << PreViewTime << " Vmax = " << Vmax << " Amax = " << Amax << endl;
  return 0;
}

RTC6_API void __stdcall set_scanahead_speed_control(const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_stepper_init(const UINT CardNo, const UINT No, const UINT Period, const long Dir, const long Pos, const UINT Tol, const UINT Enable, const UINT WaitTime){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " No = " << No << " Period = " << Period << " Dir = " << Dir << " Pos = " << Pos << " Tol = " << Tol << " Enable = " << Enable << " WaitTime = " << WaitTime << endl;
  return;
}

RTC6_API void __stdcall n_stepper_enable(const UINT CardNo, const long Enable1, const long Enable2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Enable1 = " << Enable1 << " Enable2 = " << Enable2 << endl;
  return;
}

RTC6_API void __stdcall n_stepper_disable_switch(const UINT CardNo, const long Disable1, const long Disable2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Disable1 = " << Disable1 << " Disable2 = " << Disable2 << endl;
  return;
}

RTC6_API void __stdcall n_stepper_control(const UINT CardNo, const long Period1, const long Period2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Period1 = " << Period1 << " Period2 = " << Period2 << endl;
  return;
}

RTC6_API void __stdcall n_stepper_abs_no(const UINT CardNo, const UINT No, const long Pos, const UINT WaitTime){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " No = " << No << " Pos = " << Pos << " WaitTime = " << WaitTime << endl;
  return;
}

RTC6_API void __stdcall n_stepper_rel_no(const UINT CardNo, const UINT No, const long dPos, const UINT WaitTime){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " No = " << No << " dPos = " << dPos << " WaitTime = " << WaitTime << endl;
  return;
}

RTC6_API void __stdcall n_stepper_abs(const UINT CardNo, const long Pos1, const long Pos2, const UINT WaitTime){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pos1 = " << Pos1 << " Pos2 = " << Pos2 << " WaitTime = " << WaitTime << endl;
  return;
}

RTC6_API void __stdcall n_stepper_rel(const UINT CardNo, const long dPos1, const long dPos2, const UINT WaitTime){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dPos1 = " << dPos1 << " dPos2 = " << dPos2 << " WaitTime = " << WaitTime << endl;
  return;
}

RTC6_API void __stdcall n_get_stepper_status(const UINT CardNo, UINT& Status1, long& Pos1, UINT& Status2, long& Pos2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Status1 = " << Status1 << " Pos1 = " << Pos1 << " Status2 = " << Status2 << " Pos2 = " << Pos2 << endl;
  return;
}

RTC6_API void __stdcall stepper_init(const UINT No, const UINT Period, const long Dir, const long Pos, const UINT Tol, const UINT Enable, const UINT WaitTime){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " No = " << No << " Period = " << Period << " Dir = " << Dir << " Pos = " << Pos << " Tol = " << Tol << " Enable = " << Enable << " WaitTime = " << WaitTime << endl;
  return;
}

RTC6_API void __stdcall stepper_enable(const long Enable1, const long Enable2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Enable1 = " << Enable1 << " Enable2 = " << Enable2 << endl;
  return;
}

RTC6_API void __stdcall stepper_disable_switch(const long Disable1, const long Disable2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Disable1 = " << Disable1 << " Disable2 = " << Disable2 << endl;
  return;
}

RTC6_API void __stdcall stepper_control(const long Period1, const long Period2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Period1 = " << Period1 << " Period2 = " << Period2 << endl;
  return;
}

RTC6_API void __stdcall stepper_abs_no(const UINT No, const long Pos, const UINT WaitTime){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " No = " << No << " Pos = " << Pos << " WaitTime = " << WaitTime << endl;
  return;
}

RTC6_API void __stdcall stepper_rel_no(const UINT No, const long dPos, const UINT WaitTime){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " No = " << No << " dPos = " << dPos << " WaitTime = " << WaitTime << endl;
  return;
}

RTC6_API void __stdcall stepper_abs(const long Pos1, const long Pos2, const UINT WaitTime){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pos1 = " << Pos1 << " Pos2 = " << Pos2 << " WaitTime = " << WaitTime << endl;
  return;
}

RTC6_API void __stdcall stepper_rel(const long dPos1, const long dPos2, const UINT WaitTime){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dPos1 = " << dPos1 << " dPos2 = " << dPos2 << " WaitTime = " << WaitTime << endl;
  return;
}

RTC6_API void __stdcall get_stepper_status(UINT& Status1, long& Pos1, UINT& Status2, long& Pos2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Status1 = " << Status1 << " Pos1 = " << Pos1 << " Status2 = " << Status2 << " Pos2 = " << Pos2 << endl;
  return;
}

RTC6_API void __stdcall n_select_cor_table_list(const UINT CardNo, const UINT HeadA, const UINT HeadB){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadA = " << HeadA << " HeadB = " << HeadB << endl;
  return;
}

RTC6_API void __stdcall select_cor_table_list(const UINT HeadA, const UINT HeadB){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadA = " << HeadA << " HeadB = " << HeadB << endl;
  return;
}

RTC6_API void __stdcall n_list_nop(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_list_continue(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_list_next(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_long_delay(const UINT CardNo, const UINT Delay){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Delay = " << Delay << endl;
  return;
}

RTC6_API void __stdcall n_set_end_of_list(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_set_wait(const UINT CardNo, const UINT WaitWord){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " WaitWord = " << WaitWord << endl;
  return;
}

RTC6_API void __stdcall n_list_jump_pos(const UINT CardNo, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_list_jump_rel(const UINT CardNo, const long Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_list_repeat(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_list_until(const UINT CardNo, const UINT Number){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Number = " << Number << endl;
  return;
}

RTC6_API void __stdcall n_range_checking(const UINT CardNo, const UINT HeadNo, const UINT Mode, const UINT Data){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " Mode = " << Mode << " Data = " << Data << endl;
  return;
}

RTC6_API void __stdcall n_store_timestamp_counter_list(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_wait_for_timestamp_counter(const UINT CardNo, const UINT TimeStampCounter){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " TimeStampCounter = " << TimeStampCounter << endl;
  return;
}

RTC6_API void __stdcall n_set_list_jump(const UINT CardNo, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall list_nop(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall list_continue(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall list_next(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall long_delay(const UINT Delay){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Delay = " << Delay << endl;
  return;
}

RTC6_API void __stdcall set_end_of_list(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall set_wait(const UINT WaitWord){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " WaitWord = " << WaitWord << endl;
  return;
}

RTC6_API void __stdcall list_jump_pos(const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall list_jump_rel(const long Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall list_repeat(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall list_until(const UINT Number){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Number = " << Number << endl;
  return;
}

RTC6_API void __stdcall range_checking(const UINT HeadNo, const UINT Mode, const UINT Data){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " Mode = " << Mode << " Data = " << Data << endl;
  return;
}

RTC6_API void __stdcall store_timestamp_counter_list(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall wait_for_timestamp_counter(const UINT TimeStampCounter){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " TimeStampCounter = " << TimeStampCounter << endl;
  return;
}

RTC6_API void __stdcall set_list_jump(const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_set_extstartpos_list(const UINT CardNo, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_set_control_mode_list(const UINT CardNo, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_simulate_ext_start(const UINT CardNo, const long Delay, const UINT EncoderNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Delay = " << Delay << " EncoderNo = " << EncoderNo << endl;
  return;
}

RTC6_API void __stdcall set_extstartpos_list(const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall set_control_mode_list(const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall simulate_ext_start(const long Delay, const UINT EncoderNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Delay = " << Delay << " EncoderNo = " << EncoderNo << endl;
  return;
}

RTC6_API void __stdcall n_list_return(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_list_call_repeat(const UINT CardNo, const UINT Pos, const UINT Number){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pos = " << Pos << " Number = " << Number << endl;
  return;
}

RTC6_API void __stdcall n_list_call_abs_repeat(const UINT CardNo, const UINT Pos, const UINT Number){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pos = " << Pos << " Number = " << Number << endl;
  return;
}

RTC6_API void __stdcall n_list_call(const UINT CardNo, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_list_call_abs(const UINT CardNo, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_sub_call_repeat(const UINT CardNo, const UINT Index, const UINT Number){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Index = " << Index << " Number = " << Number << endl;
  return;
}

RTC6_API void __stdcall n_sub_call_abs_repeat(const UINT CardNo, const UINT Index, const UINT Number){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Index = " << Index << " Number = " << Number << endl;
  return;
}

RTC6_API void __stdcall n_sub_call(const UINT CardNo, const UINT Index){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Index = " << Index << endl;
  return;
}

RTC6_API void __stdcall n_sub_call_abs(const UINT CardNo, const UINT Index){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Index = " << Index << endl;
  return;
}

RTC6_API void __stdcall list_return(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall list_call_repeat(const UINT Pos, const UINT Number){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pos = " << Pos << " Number = " << Number << endl;
  return;
}

RTC6_API void __stdcall list_call_abs_repeat(const UINT Pos, const UINT Number){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pos = " << Pos << " Number = " << Number << endl;
  return;
}

RTC6_API void __stdcall list_call(const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall list_call_abs(const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall sub_call_repeat(const UINT Index, const UINT Number){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Index = " << Index << " Number = " << Number << endl;
  return;
}

RTC6_API void __stdcall sub_call_abs_repeat(const UINT Index, const UINT Number){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Index = " << Index << " Number = " << Number << endl;
  return;
}

RTC6_API void __stdcall sub_call(const UINT Index){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Index = " << Index << endl;
  return;
}

RTC6_API void __stdcall sub_call_abs(const UINT Index){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Index = " << Index << endl;
  return;
}

RTC6_API void __stdcall n_list_call_cond(const UINT CardNo, const UINT Mask1, const UINT Mask0, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_list_call_abs_cond(const UINT CardNo, const UINT Mask1, const UINT Mask0, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_sub_call_cond(const UINT CardNo, const UINT Mask1, const UINT Mask0, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_sub_call_abs_cond(const UINT CardNo, const UINT Mask1, const UINT Mask0, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_list_jump_pos_cond(const UINT CardNo, const UINT Mask1, const UINT Mask0, const UINT Index){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << " Index = " << Index << endl;
  return;
}

RTC6_API void __stdcall n_list_jump_rel_cond(const UINT CardNo, const UINT Mask1, const UINT Mask0, const long Index){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << " Index = " << Index << endl;
  return;
}

RTC6_API void __stdcall n_if_cond(const UINT CardNo, const UINT Mask1, const UINT Mask0){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << endl;
  return;
}

RTC6_API void __stdcall n_if_not_cond(const UINT CardNo, const UINT Mask1, const UINT Mask0){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << endl;
  return;
}

RTC6_API void __stdcall n_if_pin_cond(const UINT CardNo, const UINT Mask1, const UINT Mask0){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << endl;
  return;
}

RTC6_API void __stdcall n_if_not_pin_cond(const UINT CardNo, const UINT Mask1, const UINT Mask0){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << endl;
  return;
}

RTC6_API void __stdcall n_switch_ioport(const UINT CardNo, const UINT MaskBits, const UINT ShiftBits){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " MaskBits = " << MaskBits << " ShiftBits = " << ShiftBits << endl;
  return;
}

RTC6_API void __stdcall n_list_jump_cond(const UINT CardNo, const UINT Mask1, const UINT Mask0, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall list_call_cond(const UINT Mask1, const UINT Mask0, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall list_call_abs_cond(const UINT Mask1, const UINT Mask0, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall sub_call_cond(const UINT Mask1, const UINT Mask0, const UINT Index){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << " Index = " << Index << endl;
  return;
}

RTC6_API void __stdcall sub_call_abs_cond(const UINT Mask1, const UINT Mask0, const UINT Index){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << " Index = " << Index << endl;
  return;
}

RTC6_API void __stdcall list_jump_pos_cond(const UINT Mask1, const UINT Mask0, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall list_jump_rel_cond(const UINT Mask1, const UINT Mask0, const long Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall if_cond(const UINT Mask1, const UINT Mask0){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << endl;
  return;
}

RTC6_API void __stdcall if_not_cond(const UINT Mask1, const UINT Mask0){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << endl;
  return;
}

RTC6_API void __stdcall if_pin_cond(const UINT Mask1, const UINT Mask0){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << endl;
  return;
}

RTC6_API void __stdcall if_not_pin_cond(const UINT Mask1, const UINT Mask0){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << endl;
  return;
}

RTC6_API void __stdcall switch_ioport(const UINT MaskBits, const UINT ShiftBits){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " MaskBits = " << MaskBits << " ShiftBits = " << ShiftBits << endl;
  return;
}

RTC6_API void __stdcall list_jump_cond(const UINT Mask1, const UINT Mask0, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_select_char_set(const UINT CardNo, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " No = " << No << endl;
  return;
}

RTC6_API void __stdcall n_mark_text(const UINT CardNo, const char* Text){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Text = " << Text << endl;
  return;
}

RTC6_API void __stdcall n_mark_text_abs(const UINT CardNo, const char* Text){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Text = " << Text << endl;
  return;
}

RTC6_API void __stdcall n_mark_char(const UINT CardNo, const UINT Char){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Char = " << Char << endl;
  return;
}

RTC6_API void __stdcall n_mark_char_abs(const UINT CardNo, const UINT Char){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Char = " << Char << endl;
  return;
}

RTC6_API void __stdcall select_char_set(const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " No = " << No << endl;
  return;
}

RTC6_API void __stdcall mark_text(const char* Text){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Text = " << Text << endl;
  return;
}

RTC6_API void __stdcall mark_text_abs(const char* Text){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Text = " << Text << endl;
  return;
}

RTC6_API void __stdcall mark_char(const UINT Char){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Char = " << Char << endl;
  return;
}

RTC6_API void __stdcall mark_char_abs(const UINT Char){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Char = " << Char << endl;
  return;
}

RTC6_API void __stdcall n_mark_serial(const UINT CardNo, const UINT Mode, const UINT Digits){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << " Digits = " << Digits << endl;
  return;
}

RTC6_API void __stdcall n_mark_serial_abs(const UINT CardNo, const UINT Mode, const UINT Digits){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << " Digits = " << Digits << endl;
  return;
}

RTC6_API void __stdcall n_mark_date(const UINT CardNo, const UINT Part, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Part = " << Part << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_mark_date_abs(const UINT CardNo, const UINT Part, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Part = " << Part << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_mark_time(const UINT CardNo, const UINT Part, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Part = " << Part << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_mark_time_abs(const UINT CardNo, const UINT Part, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Part = " << Part << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_select_serial_set_list(const UINT CardNo, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " No = " << No << endl;
  return;
}

RTC6_API void __stdcall n_set_serial_step_list(const UINT CardNo, const UINT No, const UINT Step){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " No = " << No << " Step = " << Step << endl;
  return;
}

RTC6_API void __stdcall n_time_fix_f_off(const UINT CardNo, const UINT FirstDay, const UINT Offset){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " FirstDay = " << FirstDay << " Offset = " << Offset << endl;
  return;
}

RTC6_API void __stdcall n_time_fix_f(const UINT CardNo, const UINT FirstDay){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " FirstDay = " << FirstDay << endl;
  return;
}

RTC6_API void __stdcall n_time_fix(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall mark_serial(const UINT Mode, const UINT Digits){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << " Digits = " << Digits << endl;
  return;
}

RTC6_API void __stdcall mark_serial_abs(const UINT Mode, const UINT Digits){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << " Digits = " << Digits << endl;
  return;
}

RTC6_API void __stdcall mark_date(const UINT Part, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Part = " << Part << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall mark_date_abs(const UINT Part, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Part = " << Part << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall mark_time(const UINT Part, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Part = " << Part << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall mark_time_abs(const UINT Part, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Part = " << Part << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall time_fix_f_off(const UINT FirstDay, const UINT Offset){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " FirstDay = " << FirstDay << " Offset = " << Offset << endl;
  return;
}

RTC6_API void __stdcall select_serial_set_list(const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " No = " << No << endl;
  return;
}

RTC6_API void __stdcall set_serial_step_list(const UINT No, const UINT Step){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " No = " << No << " Step = " << Step << endl;
  return;
}

RTC6_API void __stdcall time_fix_f(const UINT FirstDay){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " FirstDay = " << FirstDay << endl;
  return;
}

RTC6_API void __stdcall time_fix(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall n_clear_io_cond_list(const UINT CardNo, const UINT Mask1, const UINT Mask0, const UINT Mask){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << " Mask = " << Mask << endl;
  return;
}

RTC6_API void __stdcall n_set_io_cond_list(const UINT CardNo, const UINT Mask1, const UINT Mask0, const UINT Mask){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << " Mask = " << Mask << endl;
  return;
}

RTC6_API void __stdcall n_write_io_port_mask_list(const UINT CardNo, const UINT Value, const UINT Mask){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Value = " << Value << " Mask = " << Mask << endl;
  return;
}

RTC6_API void __stdcall n_write_8bit_port_list(const UINT CardNo, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall n_read_io_port_list(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_write_da_x_list(const UINT CardNo, const UINT x, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " x = " << x << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall n_write_io_port_list(const UINT CardNo, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall n_write_da_1_list(const UINT CardNo, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall n_write_da_2_list(const UINT CardNo, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall clear_io_cond_list(const UINT Mask1, const UINT Mask0, const UINT MaskClear){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << " MaskClear = " << MaskClear << endl;
  return;
}

RTC6_API void __stdcall set_io_cond_list(const UINT Mask1, const UINT Mask0, const UINT MaskSet){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mask1 = " << Mask1 << " Mask0 = " << Mask0 << " MaskSet = " << MaskSet << endl;
  return;
}

RTC6_API void __stdcall write_io_port_mask_list(const UINT Value, const UINT Mask){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Value = " << Value << " Mask = " << Mask << endl;
  return;
}

RTC6_API void __stdcall write_8bit_port_list(const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall read_io_port_list(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall write_da_x_list(const UINT x, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " x = " << x << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall write_io_port_list(const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall write_da_1_list(const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall write_da_2_list(const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall n_laser_signal_on_list(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_laser_signal_off_list(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_para_laser_on_pulses_list(const UINT CardNo, const UINT Period, const UINT Pulses, const UINT P){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Period = " << Period << " Pulses = " << Pulses << " P = " << P << endl;
  return;
}

RTC6_API void __stdcall n_laser_on_pulses_list(const UINT CardNo, const UINT Period, const UINT Pulses){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Period = " << Period << " Pulses = " << Pulses << endl;
  return;
}

RTC6_API void __stdcall n_laser_on_list(const UINT CardNo, const UINT Period){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Period = " << Period << endl;
  return;
}

RTC6_API void __stdcall n_set_laser_delays(const UINT CardNo, const long LaserOnDelay, const UINT LaserOffDelay){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " LaserOnDelay = " << LaserOnDelay << " LaserOffDelay = " << LaserOffDelay << endl;
  return;
}

RTC6_API void __stdcall n_set_standby_list(const UINT CardNo, const UINT HalfPeriod, const UINT PulseLength){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HalfPeriod = " << HalfPeriod << " PulseLength = " << PulseLength << endl;
  return;
}

RTC6_API void __stdcall n_set_laser_pulses(const UINT CardNo, const UINT HalfPeriod, const UINT PulseLength){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HalfPeriod = " << HalfPeriod << " PulseLength = " << PulseLength << endl;
  return;
}

RTC6_API void __stdcall n_set_firstpulse_killer_list(const UINT CardNo, const UINT Length){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Length = " << Length << endl;
  return;
}

RTC6_API void __stdcall n_set_qswitch_delay_list(const UINT CardNo, const UINT Delay){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Delay = " << Delay << endl;
  return;
}

RTC6_API void __stdcall n_set_laser_pin_out_list(const UINT CardNo, const UINT Pins){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pins = " << Pins << endl;
  return;
}

RTC6_API void __stdcall n_set_vector_control(const UINT CardNo, const UINT Ctrl, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Ctrl = " << Ctrl << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall n_set_default_pixel_list(const UINT CardNo, const UINT PulseLength){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " PulseLength = " << PulseLength << endl;
  return;
}

RTC6_API void __stdcall n_set_auto_laser_params_list(const UINT CardNo, const UINT Ctrl, const UINT Value, const UINT MinValue, const UINT MaxValue){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Ctrl = " << Ctrl << " Value = " << Value << " MinValue = " << MinValue << " MaxValue = " << MaxValue << endl;
  return;
}

RTC6_API void __stdcall n_set_pulse_picking_list(const UINT CardNo, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " No = " << No << endl;
  return;
}

RTC6_API void __stdcall n_set_softstart_level_list(const UINT CardNo, const UINT Index, const UINT Level1, const UINT Level2, const UINT Level3){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Index = " << Index << " Level1 = " << Level1 << " Level2 = " << Level2 << " Level3 = " << Level3 << endl;
  return;
}

RTC6_API void __stdcall n_set_softstart_mode_list(const UINT CardNo, const UINT Mode, const UINT Number, const UINT Delay){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << " Number = " << Number << " Delay = " << Delay << endl;
  return;
}

RTC6_API void __stdcall n_config_laser_signals_list(const UINT CardNo, const UINT Config){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Config = " << Config << endl;
  return;
}

RTC6_API void __stdcall n_spot_distance(const UINT CardNo, const double Dist){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Dist = " << Dist << endl;
  return;
}

RTC6_API void __stdcall n_set_laser_timing(const UINT CardNo, const UINT HalfPeriod, const UINT PulseLength1, const UINT PulseLength2, const UINT TimeBase){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HalfPeriod = " << HalfPeriod << " PulseLength1 = " << PulseLength1 << " PulseLength2 = " << PulseLength2 << " TimeBase = " << TimeBase << endl;
  return;
}

RTC6_API void __stdcall laser_signal_on_list(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall laser_signal_off_list(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall para_laser_on_pulses_list(const UINT Period, const UINT Pulses, const UINT P){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Period = " << Period << " Pulses = " << Pulses << " P = " << P << endl;
  return;
}

RTC6_API void __stdcall laser_on_pulses_list(const UINT Period, const UINT Pulses){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Period = " << Period << " Pulses = " << Pulses << endl;
  return;
}

RTC6_API void __stdcall laser_on_list(const UINT Period){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Period = " << Period << endl;
  return;
}

RTC6_API void __stdcall set_laser_delays(const long LaserOnDelay, const UINT LaserOffDelay){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " LaserOnDelay = " << LaserOnDelay << " LaserOffDelay = " << LaserOffDelay << endl;
  return;
}

RTC6_API void __stdcall set_standby_list(const UINT HalfPeriod, const UINT PulseLength){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HalfPeriod = " << HalfPeriod << " PulseLength = " << PulseLength << endl;
  return;
}

RTC6_API void __stdcall set_laser_pulses(const UINT HalfPeriod, const UINT PulseLength){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HalfPeriod = " << HalfPeriod << " PulseLength = " << PulseLength << endl;
  return;
}

RTC6_API void __stdcall set_firstpulse_killer_list(const UINT Length){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Length = " << Length << endl;
  return;
}

RTC6_API void __stdcall set_qswitch_delay_list(const UINT Delay){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Delay = " << Delay << endl;
  return;
}

RTC6_API void __stdcall set_laser_pin_out_list(const UINT Pins){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pins = " << Pins << endl;
  return;
}

RTC6_API void __stdcall set_vector_control(const UINT Ctrl, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Ctrl = " << Ctrl << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall set_default_pixel_list(const UINT PulseLength){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " PulseLength = " << PulseLength << endl;
  return;
}

RTC6_API void __stdcall set_auto_laser_params_list(const UINT Ctrl, const UINT Value, const UINT MinValue, const UINT MaxValue){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Ctrl = " << Ctrl << " Value = " << Value << " MinValue = " << MinValue << " MaxValue = " << MaxValue << endl;
  return;
}

RTC6_API void __stdcall set_pulse_picking_list(const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " No = " << No << endl;
  return;
}

RTC6_API void __stdcall set_softstart_level_list(const UINT Index, const UINT Level1, const UINT Level2, const UINT Level3){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Index = " << Index << " Level1 = " << Level1 << " Level2 = " << Level2 << " Level3 = " << Level3 << endl;
  return;
}

RTC6_API void __stdcall set_softstart_mode_list(const UINT Mode, const UINT Number, const UINT Delay){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << " Number = " << Number << " Delay = " << Delay << endl;
  return;
}

RTC6_API void __stdcall config_laser_signals_list(const UINT Config){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Config = " << Config << endl;
  return;
}

RTC6_API void __stdcall spot_distance(const double Dist){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Dist = " << Dist << endl;
  return;
}

RTC6_API void __stdcall set_laser_timing(const UINT HalfPeriod, const UINT PulseLength1, const UINT PulseLength2, const UINT TimeBase){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HalfPeriod = " << HalfPeriod << " PulseLength1 = " << PulseLength1 << " PulseLength2 = " << PulseLength2 << " TimeBase = " << TimeBase << endl;
  return;
}

RTC6_API void __stdcall n_fly_return_z(const UINT CardNo, const long X, const long Y, const long Z){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " Z = " << Z << endl;
  return;
}

RTC6_API void __stdcall n_fly_return(const UINT CardNo, const long X, const long Y){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << endl;
  return;
}

RTC6_API void __stdcall n_set_rot_center_list(const UINT CardNo, const long X, const long Y){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << endl;
  return;
}

RTC6_API void __stdcall n_set_ext_start_delay_list(const UINT CardNo, const long Delay, const UINT EncoderNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Delay = " << Delay << " EncoderNo = " << EncoderNo << endl;
  return;
}

RTC6_API void __stdcall n_set_fly_x(const UINT CardNo, const double ScaleX){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ScaleX = " << ScaleX << endl;
  return;
}

RTC6_API void __stdcall n_set_fly_y(const UINT CardNo, const double ScaleY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ScaleY = " << ScaleY << endl;
  return;
}

RTC6_API void __stdcall n_set_fly_z(const UINT CardNo, const double ScaleZ, const UINT EndoderNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ScaleZ = " << ScaleZ << " EndoderNo = " << EndoderNo << endl;
  return;
}

RTC6_API void __stdcall n_set_fly_rot(const UINT CardNo, const double Resolution){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Resolution = " << Resolution << endl;
  return;
}

RTC6_API void __stdcall n_set_fly_2d(const UINT CardNo, const double ScaleX, const double ScaleY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ScaleX = " << ScaleX << " ScaleY = " << ScaleY << endl;
  return;
}

RTC6_API void __stdcall n_set_fly_x_pos(const UINT CardNo, const double ScaleX){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ScaleX = " << ScaleX << endl;
  return;
}

RTC6_API void __stdcall n_set_fly_y_pos(const UINT CardNo, const double ScaleY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ScaleY = " << ScaleY << endl;
  return;
}

RTC6_API void __stdcall n_set_fly_rot_pos(const UINT CardNo, const double Resolution){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Resolution = " << Resolution << endl;
  return;
}

RTC6_API void __stdcall n_set_fly_limits(const UINT CardNo, const long Xmin, const long Xmax, const long Ymin, const long Ymax){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Xmin = " << Xmin << " Xmax = " << Xmax << " Ymin = " << Ymin << " Ymax = " << Ymax << endl;
  return;
}

RTC6_API void __stdcall n_set_fly_limits_z(const UINT CardNo, const long Zmin, const long Zmax){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Zmin = " << Zmin << " Zmax = " << Zmax << endl;
  return;
}

RTC6_API void __stdcall n_if_fly_x_overflow(const UINT CardNo, const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_if_fly_y_overflow(const UINT CardNo, const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_if_fly_z_overflow(const UINT CardNo, const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_if_not_fly_x_overflow(const UINT CardNo, const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_if_not_fly_y_overflow(const UINT CardNo, const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_if_not_fly_z_overflow(const UINT CardNo, const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_clear_fly_overflow(const UINT CardNo, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_x_list(const UINT CardNo, const double ScaleX){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ScaleX = " << ScaleX << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_y_list(const UINT CardNo, const double ScaleY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ScaleY = " << ScaleY << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_rot_list(const UINT CardNo, const double Resolution){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Resolution = " << Resolution << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_matrix_list(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_global_x_list(const UINT CardNo, const double ScaleX){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ScaleX = " << ScaleX << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_global_y_list(const UINT CardNo, const double ScaleY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ScaleY = " << ScaleY << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_global_rot_list(const UINT CardNo, const double Resolution){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Resolution = " << Resolution << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_global_matrix_list(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_in_list(const UINT CardNo, const UINT Mode, const double Scale){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << " Scale = " << Scale << endl;
  return;
}

RTC6_API void __stdcall n_set_multi_mcbsp_in_list(const UINT CardNo, const UINT Ctrl, const UINT P, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Ctrl = " << Ctrl << " P = " << P << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_wait_for_encoder_mode(const UINT CardNo, const long Value, const UINT EncoderNo, const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Value = " << Value << " EncoderNo = " << EncoderNo << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_wait_for_mcbsp(const UINT CardNo, const UINT Axis, const long Value, const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Axis = " << Axis << " Value = " << Value << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_set_encoder_speed(const UINT CardNo, const UINT EncoderNo, const double Speed, const double Smooth){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " EncoderNo = " << EncoderNo << " Speed = " << Speed << " Smooth = " << Smooth << endl;
  return;
}

RTC6_API void __stdcall n_get_mcbsp_list(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_store_encoder(const UINT CardNo, const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_wait_for_encoder_in_range_mode(const UINT CardNo, const long EncXmin, const long EncXmax, const long EncYmin, const long EncYmax, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " EncXmin = " << EncXmin << " EncXmax = " << EncXmax << " EncYmin = " << EncYmin << " EncYmax = " << EncYmax << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_wait_for_encoder_in_range(const UINT CardNo, const long EncXmin, const long EncXmax, const long EncYmin, const long EncYmax){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " EncXmin = " << EncXmin << " EncXmax = " << EncXmax << " EncYmin = " << EncYmin << " EncYmax = " << EncYmax << endl;
  return;
}

RTC6_API void __stdcall n_activate_fly_xy(const UINT CardNo, const double ScaleX, const double ScaleY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ScaleX = " << ScaleX << " ScaleY = " << ScaleY << endl;
  return;
}

RTC6_API void __stdcall n_activate_fly_2d(const UINT CardNo, const double ScaleX, const double ScaleY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ScaleX = " << ScaleX << " ScaleY = " << ScaleY << endl;
  return;
}

RTC6_API void __stdcall n_activate_fly_xy_encoder(const UINT CardNo, const double ScaleX, const double ScaleY, const long EncX, const long EncY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ScaleX = " << ScaleX << " ScaleY = " << ScaleY << " EncX = " << EncX << " EncY = " << EncY << endl;
  return;
}

RTC6_API void __stdcall n_activate_fly_2d_encoder(const UINT CardNo, const double ScaleX, const double ScaleY, const long EncX, const long EncY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ScaleX = " << ScaleX << " ScaleY = " << ScaleY << " EncX = " << EncX << " EncY = " << EncY << endl;
  return;
}

RTC6_API void __stdcall n_if_not_activated(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_park_position(const UINT CardNo, const UINT Mode, const long X, const long Y){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << " X = " << X << " Y = " << Y << endl;
  return;
}

RTC6_API void __stdcall n_park_return(const UINT CardNo, const UINT Mode, const long X, const long Y){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << " X = " << X << " Y = " << Y << endl;
  return;
}

RTC6_API void __stdcall n_fly_prediction(const UINT CardNo, UINT PredictionX, UINT PredictionY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " PredictionX = " << PredictionX << " PredictionY = " << PredictionY << endl;
  return;
}

RTC6_API void __stdcall n_set_fly_1_axis(const UINT CardNo, const UINT Axis, const UINT Mode, const double Scale){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Axis = " << Axis << " Mode = " << Mode << " Scale = " << Scale << endl;
  return;
}

RTC6_API void __stdcall n_fly_return_1_axis(const UINT CardNo, const UINT Axis, const long RetPos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Axis = " << Axis << " RetPos = " << RetPos << endl;
  return;
}

RTC6_API void __stdcall n_wait_for_1_axis(const UINT CardNo, long Value, const UINT EncoderMode, const long WaitMode, const UINT LaserMode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Value = " << Value << " EncoderMode = " << EncoderMode << " WaitMode = " << WaitMode << " LaserMode = " << LaserMode << endl;
  return;
}

RTC6_API void __stdcall n_activate_fly_1_axis(const UINT CardNo, const UINT Axis, const UINT Mode, const double Scale, const long Offset){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Axis = " << Axis << " Mode = " << Mode << " Scale = " << Scale << " Offset = " << Offset << endl;
  return;
}

RTC6_API void __stdcall n_park_position_1_axis(const UINT CardNo, const UINT Mode, const UINT Axis, const long ParkPos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << " Axis = " << Axis << " ParkPos = " << ParkPos << endl;
  return;
}

RTC6_API void __stdcall n_park_return_1_axis(const UINT CardNo, const UINT Mode, const UINT Axis, const long RetPos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << " Axis = " << Axis << " RetPos = " << RetPos << endl;
  return;
}

RTC6_API void __stdcall n_set_fly_2_axes(const UINT CardNo, const UINT Axis1, const UINT Mode1, const double Scale1, const UINT Axis2, const UINT Mode2, const double Scale2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Axis1 = " << Axis1 << " Mode1 = " << Mode1 << " Scale1 = " << Scale1 << " Axis2 = " << Axis2 << " Mode2 = " << Mode2 << " Scale2 = " << Scale2 << endl;
  return;
}

RTC6_API void __stdcall n_fly_return_2_axes(const UINT CardNo, const UINT Axis1, const long RetPos1, const UINT Axis2, const long RetPos2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Axis1 = " << Axis1 << " RetPos1 = " << RetPos1 << " Axis2 = " << Axis2 << " RetPos2 = " << RetPos2 << endl;
  return;
}

RTC6_API void __stdcall n_wait_for_2_axes(const UINT CardNo, const UINT EncoderModeX, const long MinValueX, const long MaxValueX, const UINT EncoderModeY, const long MinValueY, const long MaxValueY, const long WaitMode, const UINT LaserMode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " EncoderModeX = " << EncoderModeX << " MinValueX = " << MinValueX << " MaxValueX = " << MaxValueX << " EncoderModeY = " << EncoderModeY << " MinValueY = " << MinValueY << " MaxValueY = " << MaxValueY << " WaitMode = " << WaitMode << " LaserMode = " << LaserMode << endl;
  return;
}

RTC6_API void __stdcall n_activate_fly_2_axes(const UINT CardNo, const UINT ModeX, const double ScaleX, const long OffsetX, const UINT ModeY, const double ScaleY, const long OffsetY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ModeX = " << ModeX << " ScaleX = " << ScaleX << " OffsetX = " << OffsetX << " ModeY = " << ModeY << " ScaleY = " << ScaleY << " OffsetY = " << OffsetY << endl;
  return;
}

RTC6_API void __stdcall n_park_position_2_axes(const UINT CardNo, const UINT Mode, const long ParkPosX, const long ParkPosY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << " ParkPosX = " << ParkPosX << " ParkPosY = " << ParkPosY << endl;
  return;
}

RTC6_API void __stdcall n_park_return_2_axes(const UINT CardNo, const UINT Mode, const long RetPosX, const long RetkPosY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << " RetPosX = " << RetPosX << " RetkPosY = " << RetkPosY << endl;
  return;
}

RTC6_API void __stdcall n_set_fly_3_axes(const UINT CardNo, const UINT ModeX, const double ScaleX, const UINT ModeY, const double ScaleY, const UINT ModeZ, const double ScaleZ){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " ModeX = " << ModeX << " ScaleX = " << ScaleX << " ModeY = " << ModeY << " ScaleY = " << ScaleY << " ModeZ = " << ModeZ << " ScaleZ = " << ScaleZ << endl;
  return;
}

RTC6_API void __stdcall n_fly_return_3_axes(const UINT CardNo, const long RetPosX, const long RetPosY, const long RetPosZ){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " RetPosX = " << RetPosX << " RetPosY = " << RetPosY << " RetPosZ = " << RetPosZ << endl;
  return;
}

RTC6_API void __stdcall n_wait_for_encoder(const UINT CardNo, const long Value, const UINT EncoderNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Value = " << Value << " EncoderNo = " << EncoderNo << endl;
  return;
}

RTC6_API void __stdcall fly_return_z(const long X, const long Y, const long Z){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " Z = " << Z << endl;
  return;
}

RTC6_API void __stdcall fly_return(const long X, const long Y){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << endl;
  return;
}

RTC6_API void __stdcall set_rot_center_list(const long X, const long Y){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << endl;
  return;
}

RTC6_API void __stdcall set_ext_start_delay_list(const long Delay, const UINT EncoderNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Delay = " << Delay << " EncoderNo = " << EncoderNo << endl;
  return;
}

RTC6_API void __stdcall set_fly_x(const double ScaleX){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ScaleX = " << ScaleX << endl;
  return;
}

RTC6_API void __stdcall set_fly_y(const double ScaleY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ScaleY = " << ScaleY << endl;
  return;
}

RTC6_API void __stdcall set_fly_z(const double ScaleZ, const UINT EncoderNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ScaleZ = " << ScaleZ << " EncoderNo = " << EncoderNo << endl;
  return;
}

RTC6_API void __stdcall set_fly_rot(const double Resolution){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Resolution = " << Resolution << endl;
  return;
}

RTC6_API void __stdcall set_fly_2d(const double ScaleX, const double ScaleY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ScaleX = " << ScaleX << " ScaleY = " << ScaleY << endl;
  return;
}

RTC6_API void __stdcall set_fly_x_pos(const double ScaleX){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ScaleX = " << ScaleX << endl;
  return;
}

RTC6_API void __stdcall set_fly_y_pos(const double ScaleY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ScaleY = " << ScaleY << endl;
  return;
}

RTC6_API void __stdcall set_fly_rot_pos(const double Resolution){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Resolution = " << Resolution << endl;
  return;
}

RTC6_API void __stdcall set_fly_limits(const long Xmin, const long Xmax, const long Ymin, const long Ymax){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Xmin = " << Xmin << " Xmax = " << Xmax << " Ymin = " << Ymin << " Ymax = " << Ymax << endl;
  return;
}

RTC6_API void __stdcall set_fly_limits_z(const long Zmin, const long Zmax){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Zmin = " << Zmin << " Zmax = " << Zmax << endl;
  return;
}

RTC6_API void __stdcall if_fly_x_overflow(const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall if_fly_y_overflow(const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall if_fly_z_overflow(const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall if_not_fly_x_overflow(const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall if_not_fly_y_overflow(const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall if_not_fly_z_overflow(const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall clear_fly_overflow(const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_x_list(const double ScaleX){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ScaleX = " << ScaleX << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_y_list(const double ScaleY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ScaleY = " << ScaleY << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_rot_list(const double Resolution){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Resolution = " << Resolution << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_matrix_list(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_global_x_list(const double ScaleX){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ScaleX = " << ScaleX << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_global_y_list(const double ScaleY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ScaleY = " << ScaleY << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_global_rot_list(const double Resolution){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Resolution = " << Resolution << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_global_matrix_list(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_in_list(const UINT Mode, const double Scale){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << " Scale = " << Scale << endl;
  return;
}

RTC6_API void __stdcall set_multi_mcbsp_in_list(const UINT Ctrl, const UINT P, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Ctrl = " << Ctrl << " P = " << P << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall wait_for_encoder_mode(const long Value, const UINT EncoderNo, const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Value = " << Value << " EncoderNo = " << EncoderNo << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall wait_for_mcbsp(const UINT Axis, const long Value, const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Axis = " << Axis << " Value = " << Value << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall set_encoder_speed(const UINT EncoderNo, const double Speed, const double Smooth){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " EncoderNo = " << EncoderNo << " Speed = " << Speed << " Smooth = " << Smooth << endl;
  return;
}

RTC6_API void __stdcall get_mcbsp_list(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall store_encoder(const UINT Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall wait_for_encoder_in_range_mode(const long EncXmin, const long EncXmax, const long EncYmin, const long EncYmax, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " EncXmin = " << EncXmin << " EncXmax = " << EncXmax << " EncYmin = " << EncYmin << " EncYmax = " << EncYmax << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall wait_for_encoder_in_range(const long EncXmin, const long EncXmax, const long EncYmin, const long EncYmax){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " EncXmin = " << EncXmin << " EncXmax = " << EncXmax << " EncYmin = " << EncYmin << " EncYmax = " << EncYmax << endl;
  return;
}

RTC6_API void __stdcall activate_fly_xy(const double ScaleX, const double ScaleY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ScaleX = " << ScaleX << " ScaleY = " << ScaleY << endl;
  return;
}

RTC6_API void __stdcall activate_fly_2d(const double ScaleX, const double ScaleY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ScaleX = " << ScaleX << " ScaleY = " << ScaleY << endl;
  return;
}

RTC6_API void __stdcall activate_fly_xy_encoder(const double ScaleX, const double ScaleY, const long EncX, const long EncY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ScaleX = " << ScaleX << " ScaleY = " << ScaleY << " EncX = " << EncX << " EncY = " << EncY << endl;
  return;
}

RTC6_API void __stdcall activate_fly_2d_encoder(const double ScaleX, const double ScaleY, const long EncX, const long EncY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ScaleX = " << ScaleX << " ScaleY = " << ScaleY << " EncX = " << EncX << " EncY = " << EncY << endl;
  return;
}

RTC6_API void __stdcall if_not_activated(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall park_position(const UINT Mode, const long X, const long Y){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << " X = " << X << " Y = " << Y << endl;
  return;
}

RTC6_API void __stdcall park_return(const UINT Mode, const long X, const long Y){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << " X = " << X << " Y = " << Y << endl;
  return;
}

RTC6_API void __stdcall fly_prediction(UINT PredictionX, UINT PredictionY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " PredictionX = " << PredictionX << " PredictionY = " << PredictionY << endl;
  return;
}

RTC6_API void __stdcall set_fly_1_axis(const UINT Axis, const UINT Mode, const double Scale){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Axis = " << Axis << " Mode = " << Mode << " Scale = " << Scale << endl;
  return;
}

RTC6_API void __stdcall fly_return_1_axis(const UINT Axis, const long RetPos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Axis = " << Axis << " RetPos = " << RetPos << endl;
  return;
}

RTC6_API void __stdcall wait_for_1_axis(const long Value, const UINT EncoderMode, const long WaitMode, const UINT LaserMode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Value = " << Value << " EncoderMode = " << EncoderMode << " WaitMode = " << WaitMode << " LaserMode = " << LaserMode << endl;
  return;
}

RTC6_API void __stdcall activate_fly_1_axis(const UINT Axis, const UINT Mode, const double Scale, const long Offset){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Axis = " << Axis << " Mode = " << Mode << " Scale = " << Scale << " Offset = " << Offset << endl;
  return;
}

RTC6_API void __stdcall park_position_1_axis(const UINT Mode, const UINT Axis, const long ParkPos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << " Axis = " << Axis << " ParkPos = " << ParkPos << endl;
  return;
}

RTC6_API void __stdcall park_return_1_axis(const UINT Mode, const UINT Axis, const long RetPos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << " Axis = " << Axis << " RetPos = " << RetPos << endl;
  return;
}

RTC6_API void __stdcall set_fly_2_axes(const UINT Axis1, const UINT Mode1, const double Scale1, const UINT Axis2, const UINT Mode2, const double Scale2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Axis1 = " << Axis1 << " Mode1 = " << Mode1 << " Scale1 = " << Scale1 << " Axis2 = " << Axis2 << " Mode2 = " << Mode2 << " Scale2 = " << Scale2 << endl;
  return;
}

RTC6_API void __stdcall fly_return_2_axes(const UINT Axis1, const long RetPos1, const UINT Axis2, const long RetPos2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Axis1 = " << Axis1 << " RetPos1 = " << RetPos1 << " Axis2 = " << Axis2 << " RetPos2 = " << RetPos2 << endl;
  return;
}

RTC6_API void __stdcall wait_for_2_axes(const UINT EncoderModeX, const long MinValueX, const long MaxValueX, const UINT EncoderModeY, const long MinValueY, const long MaxValueY, const long WaitMode, const UINT LaserMode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " EncoderModeX = " << EncoderModeX << " MinValueX = " << MinValueX << " MaxValueX = " << MaxValueX << " EncoderModeY = " << EncoderModeY << " MinValueY = " << MinValueY << " MaxValueY = " << MaxValueY << " WaitMode = " << WaitMode << " LaserMode = " << LaserMode << endl;
  return;
}

RTC6_API void __stdcall activate_fly_2_axes(const UINT ModeX, const double ScaleX, const long OffsetX, const UINT ModeY, const double ScaleY, const long OffsetY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ModeX = " << ModeX << " ScaleX = " << ScaleX << " OffsetX = " << OffsetX << " ModeY = " << ModeY << " ScaleY = " << ScaleY << " OffsetY = " << OffsetY << endl;
  return;
}

RTC6_API void __stdcall park_position_2_axes(const UINT Mode, const long ParkPosX, const long ParkPosY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << " ParkPosX = " << ParkPosX << " ParkPosY = " << ParkPosY << endl;
  return;
}

RTC6_API void __stdcall park_return_2_axes(const UINT Mode, const long RetPosX, const long RetPosY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << " RetPosX = " << RetPosX << " RetPosY = " << RetPosY << endl;
  return;
}

RTC6_API void __stdcall set_fly_3_axes(const UINT ModeX, const double ScaleX, const UINT ModeY, const double ScaleY, const UINT ModeZ, const double ScaleZ){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " ModeX = " << ModeX << " ScaleX = " << ScaleX << " ModeY = " << ModeY << " ScaleY = " << ScaleY << " ModeZ = " << ModeZ << " ScaleZ = " << ScaleZ << endl;
  return;
}

RTC6_API void __stdcall fly_return_3_axes(const long RetPosX, const long RetPosY, const long RetPosZ){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " RetPosX = " << RetPosX << " RetPosY = " << RetPosY << " RetPosZ = " << RetPosZ << endl;
  return;
}

RTC6_API void __stdcall wait_for_encoder(const long Value, const UINT EncoderNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Value = " << Value << " EncoderNo = " << EncoderNo << endl;
  return;
}

RTC6_API void __stdcall n_save_and_restart_timer(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_set_wobbel_mode_phase(const UINT CardNo, const UINT Transversal, const UINT Longitudinal, const double Freq, const long Mode, const double Phase){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Transversal = " << Transversal << " Longitudinal = " << Longitudinal << " Freq = " << Freq << " Mode = " << Mode << " Phase = " << Phase << endl;
  return;
}

RTC6_API void __stdcall n_set_wobbel_mode(const UINT CardNo, const UINT Transversal, const UINT Longitudinal, const double Freq, const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Transversal = " << Transversal << " Longitudinal = " << Longitudinal << " Freq = " << Freq << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_set_wobbel(const UINT CardNo, const UINT Transversal, const UINT Longitudinal, const double Freq){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Transversal = " << Transversal << " Longitudinal = " << Longitudinal << " Freq = " << Freq << endl;
  return;
}

RTC6_API void __stdcall n_set_wobbel_direction(const UINT CardNo, const long dX, const long dY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << endl;
  return;
}

RTC6_API void __stdcall n_set_wobbel_control(const UINT CardNo, const UINT Ctrl, const UINT Value, const UINT MinValue, const UINT MaxValue){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Ctrl = " << Ctrl << " Value = " << Value << " MinValue = " << MinValue << " MaxValue = " << MaxValue << endl;
  return;
}

RTC6_API void __stdcall n_set_wobbel_vector(const UINT CardNo, const double dTrans, const double dLong, const UINT Period, const double dPower){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dTrans = " << dTrans << " dLong = " << dLong << " Period = " << Period << " dPower = " << dPower << endl;
  return;
}

RTC6_API void __stdcall n_set_wobbel_offset(const UINT CardNo, const long OffsetTrans, const long OffsetLong){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " OffsetTrans = " << OffsetTrans << " OffsetLong = " << OffsetLong << endl;
  return;
}

RTC6_API void __stdcall n_set_trigger(const UINT CardNo, const UINT Period, const UINT Signal1, const UINT Signal2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Period = " << Period << " Signal1 = " << Signal1 << " Signal2 = " << Signal2 << endl;
  return;
}

RTC6_API void __stdcall n_set_trigger4(const UINT CardNo, const UINT Period, const UINT Signal1, const UINT Signal2, const UINT Signal3, const UINT Signal4){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Period = " << Period << " Signal1 = " << Signal1 << " Signal2 = " << Signal2 << " Signal3 = " << Signal3 << " Signal4 = " << Signal4 << endl;
  return;
}

RTC6_API void __stdcall n_set_pixel_line_3d(const UINT CardNo, const UINT Channel, const UINT HalfPeriod, const double dX, const double dY, const double dZ){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Channel = " << Channel << " HalfPeriod = " << HalfPeriod << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << endl;
  return;
}

RTC6_API void __stdcall n_set_pixel_line(const UINT CardNo, const UINT Channel, const UINT HalfPeriod, const double dX, const double dY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Channel = " << Channel << " HalfPeriod = " << HalfPeriod << " dX = " << dX << " dY = " << dY << endl;
  return;
}

RTC6_API void __stdcall n_set_n_pixel(const UINT CardNo, const UINT PortOutValue1, const UINT PortOutValue2, const UINT Number){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " PortOutValue1 = " << PortOutValue1 << " PortOutValue2 = " << PortOutValue2 << " Number = " << Number << endl;
  return;
}

RTC6_API void __stdcall n_set_pixel(const UINT CardNo, const UINT PortOutValue1, const UINT PortOutValue2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " PortOutValue1 = " << PortOutValue1 << " PortOutValue2 = " << PortOutValue2 << endl;
  return;
}

RTC6_API void __stdcall n_rs232_write_text_list(const UINT CardNo, const char* pData){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " pData = " << pData << endl;
  return;
}

RTC6_API void __stdcall n_set_mcbsp_out(const UINT CardNo, const UINT Signal1, const UINT Signal2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Signal1 = " << Signal1 << " Signal2 = " << Signal2 << endl;
  return;
}

RTC6_API void __stdcall n_camming(const UINT CardNo, const UINT FirstPos, const UINT NPos, const UINT No, const UINT Ctrl, const double Scale, const UINT Code){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " FirstPos = " << FirstPos << " NPos = " << NPos << " No = " << No << " Ctrl = " << Ctrl << " Scale = " << Scale << " Code = " << Code << endl;
  return;
}

RTC6_API void __stdcall n_periodic_toggle_list(const UINT CardNo, const UINT Port, const UINT Mask, const UINT P1, const UINT P2, const UINT Count, const UINT Start){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Port = " << Port << " Mask = " << Mask << " P1 = " << P1 << " P2 = " << P2 << " Count = " << Count << " Start = " << Start << endl;
  return;
}

RTC6_API void __stdcall n_micro_vector_abs_3d(const UINT CardNo, const long X, const long Y, const long Z, const long LasOn, const long LasOff){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " Z = " << Z << " LasOn = " << LasOn << " LasOff = " << LasOff << endl;
  return;
}

RTC6_API void __stdcall n_micro_vector_rel_3d(const UINT CardNo, const long dX, const long dY, const long dZ, const long LasOn, const long LasOff){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << " LasOn = " << LasOn << " LasOff = " << LasOff << endl;
  return;
}

RTC6_API void __stdcall n_micro_vector_abs(const UINT CardNo, const long X, const long Y, const long LasOn, const long LasOff){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " LasOn = " << LasOn << " LasOff = " << LasOff << endl;
  return;
}

RTC6_API void __stdcall n_micro_vector_rel(const UINT CardNo, const long dX, const long dY, const long LasOn, const long LasOff){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " LasOn = " << LasOn << " LasOff = " << LasOff << endl;
  return;
}

RTC6_API void __stdcall n_micro_vector_quad_axis_v_2(const UINT CardNo, const long X0, const long Y0, const long X1, const long Y1, const long LasOn, const long LasOff, const UINT Power, const UINT Port, const UINT Flags, const double Velocity){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X0 = " << X0 << " Y0 = " << Y0 << " X1 = " << X1 << " Y1 = " << Y1 << " LasOn = " << LasOn << " LasOff = " << LasOff << " Power = " << Power << " Port = " << Port << " Flags = " << Flags << " Velocity = " << Velocity << endl;
  return;
}

RTC6_API void __stdcall n_micro_vector_quad_axis_v(const UINT CardNo, const long X0, const long Y0, const double X1, const double Y1, const long LasOn, const long LasOff, const UINT Power, const UINT Port, const UINT Flags, const double Velocity){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X0 = " << X0 << " Y0 = " << Y0 << " X1 = " << X1 << " Y1 = " << Y1 << " LasOn = " << LasOn << " LasOff = " << LasOff << " Power = " << Power << " Port = " << Port << " Flags = " << Flags << " Velocity = " << Velocity << endl;
  return;
}

RTC6_API void __stdcall n_micro_vector_quad_axis(const UINT CardNo, const long X0, const long Y0, const double X1, const double Y1, const long LasOn, const long LasOff, const UINT Power, const UINT Port, const UINT Flags){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X0 = " << X0 << " Y0 = " << Y0 << " X1 = " << X1 << " Y1 = " << Y1 << " LasOn = " << LasOn << " LasOff = " << LasOff << " Power = " << Power << " Port = " << Port << " Flags = " << Flags << endl;
  return;
}

RTC6_API void __stdcall n_micro_vector_set_position(const UINT CardNo, const long X0, const long X1, const long X2, const long X3, const long LasOn, const long LasOff){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X0 = " << X0 << " X1 = " << X1 << " X2 = " << X2 << " X3 = " << X3 << " LasOn = " << LasOn << " LasOff = " << LasOff << endl;
  return;
}

RTC6_API void __stdcall n_multi_axis_flags(const UINT CardNo, const UINT Flags){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Flags = " << Flags << endl;
  return;
}

RTC6_API void __stdcall n_set_free_variable_list(const UINT CardNo, const UINT VarNo, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " VarNo = " << VarNo << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall n_jump_abs_drill_2(const UINT CardNo, const long X, const long Y, const UINT DrillTime, const long XOff, const long YOff){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " DrillTime = " << DrillTime << " XOff = " << XOff << " YOff = " << YOff << endl;
  return;
}

RTC6_API void __stdcall n_jump_rel_drill_2(const UINT CardNo, const long dX, const long dY, const UINT DrillTime, const long XOff, const long YOff){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " DrillTime = " << DrillTime << " XOff = " << XOff << " YOff = " << YOff << endl;
  return;
}

RTC6_API void __stdcall n_jump_abs_drill(const UINT CardNo, const long X, const long Y, const UINT DrillTime){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " DrillTime = " << DrillTime << endl;
  return;
}

RTC6_API void __stdcall n_jump_rel_drill(const UINT CardNo, const long dX, const long dY, const UINT DrillTime){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " DrillTime = " << DrillTime << endl;
  return;
}

RTC6_API void __stdcall save_and_restart_timer(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall set_wobbel_mode_phase(const UINT Transversal, const UINT Longitudinal, const double Freq, const long Mode, const double Phase){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Transversal = " << Transversal << " Longitudinal = " << Longitudinal << " Freq = " << Freq << " Mode = " << Mode << " Phase = " << Phase << endl;
  return;
}

RTC6_API void __stdcall set_wobbel_mode(const UINT Transversal, const UINT Longitudinal, const double Freq, const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Transversal = " << Transversal << " Longitudinal = " << Longitudinal << " Freq = " << Freq << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall set_wobbel(const UINT Transversal, const UINT Longitudinal, const double Freq){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Transversal = " << Transversal << " Longitudinal = " << Longitudinal << " Freq = " << Freq << endl;
  return;
}

RTC6_API void __stdcall set_wobbel_direction(const long dX, const long dY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << endl;
  return;
}

RTC6_API void __stdcall set_wobbel_control(const UINT Ctrl, const UINT Value, const UINT MinValue, const UINT MaxValue){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Ctrl = " << Ctrl << " Value = " << Value << " MinValue = " << MinValue << " MaxValue = " << MaxValue << endl;
  return;
}

RTC6_API void __stdcall set_wobbel_vector(const double dTrans, const double dLong, const UINT Period, const double dPower){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dTrans = " << dTrans << " dLong = " << dLong << " Period = " << Period << " dPower = " << dPower << endl;
  return;
}

RTC6_API void __stdcall set_wobbel_offset(const long OffsetTrans, const long OffsetLong){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " OffsetTrans = " << OffsetTrans << " OffsetLong = " << OffsetLong << endl;
  return;
}

RTC6_API void __stdcall set_trigger(const UINT Period, const UINT Signal1, const UINT Signal2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Period = " << Period << " Signal1 = " << Signal1 << " Signal2 = " << Signal2 << endl;
  return;
}

RTC6_API void __stdcall set_trigger4(const UINT Period, const UINT Signal1, const UINT Signal2, const UINT Signal3, const UINT Signal4){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Period = " << Period << " Signal1 = " << Signal1 << " Signal2 = " << Signal2 << " Signal3 = " << Signal3 << " Signal4 = " << Signal4 << endl;
  return;
}

RTC6_API void __stdcall set_pixel_line_3d(const UINT Channel, const UINT HalfPeriod, const double dX, const double dY, const double dZ){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Channel = " << Channel << " HalfPeriod = " << HalfPeriod << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << endl;
  return;
}

RTC6_API void __stdcall set_pixel_line(const UINT Channel, const UINT HalfPeriod, const double dX, const double dY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Channel = " << Channel << " HalfPeriod = " << HalfPeriod << " dX = " << dX << " dY = " << dY << endl;
  return;
}

RTC6_API void __stdcall set_n_pixel(const UINT PortOutValue1, const UINT PortOutValue2, const UINT Number){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " PortOutValue1 = " << PortOutValue1 << " PortOutValue2 = " << PortOutValue2 << " Number = " << Number << endl;
  return;
}

RTC6_API void __stdcall set_pixel(const UINT PortOutValue1, const UINT PortOutValue2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " PortOutValue1 = " << PortOutValue1 << " PortOutValue2 = " << PortOutValue2 << endl;
  return;
}

RTC6_API void __stdcall rs232_write_text_list(const char* pData){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " pData = " << pData << endl;
  return;
}

RTC6_API void __stdcall set_mcbsp_out(const UINT Signal1, const UINT Signal2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Signal1 = " << Signal1 << " Signal2 = " << Signal2 << endl;
  return;
}

RTC6_API void __stdcall camming(const UINT FirstPos, const UINT NPos, const UINT No, const UINT Ctrl, const double Scale, const UINT Code){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " FirstPos = " << FirstPos << " NPos = " << NPos << " No = " << No << " Ctrl = " << Ctrl << " Scale = " << Scale << " Code = " << Code << endl;
  return;
}

RTC6_API void __stdcall periodic_toggle_list(const UINT Port, const UINT Mask, const UINT P1, const UINT P2, const UINT Count, const UINT Start){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Port = " << Port << " Mask = " << Mask << " P1 = " << P1 << " P2 = " << P2 << " Count = " << Count << " Start = " << Start << endl;
  return;
}

RTC6_API void __stdcall micro_vector_abs_3d(const long X, const long Y, const long Z, const long LasOn, const long LasOff){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " Z = " << Z << " LasOn = " << LasOn << " LasOff = " << LasOff << endl;
  return;
}

RTC6_API void __stdcall micro_vector_rel_3d(const long dX, const long dY, const long dZ, const long LasOn, const long LasOff){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << " LasOn = " << LasOn << " LasOff = " << LasOff << endl;
  return;
}

RTC6_API void __stdcall micro_vector_abs(const long X, const long Y, const long LasOn, const long LasOff){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " LasOn = " << LasOn << " LasOff = " << LasOff << endl;
  return;
}

RTC6_API void __stdcall micro_vector_rel(const long dX, const long dY, const long LasOn, const long LasOff){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " LasOn = " << LasOn << " LasOff = " << LasOff << endl;
  return;
}

RTC6_API void __stdcall micro_vector_quad_axis_v_2(const long X0, const long Y0, const long X1, const long Y1, const long LasOn, const long LasOff, const UINT Power, const UINT Port, const UINT Flags, const double Velocity){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X0 = " << X0 << " Y0 = " << Y0 << " X1 = " << X1 << " Y1 = " << Y1 << " LasOn = " << LasOn << " LasOff = " << LasOff << " Power = " << Power << " Port = " << Port << " Flags = " << Flags << " Velocity = " << Velocity << endl;
  return;
}

RTC6_API void __stdcall micro_vector_quad_axis_v(const long X0, const long Y0, const double X1, const double Y1, const long LasOn, const long LasOff, const UINT Power, const UINT Port, const UINT Flags, const double Velocity){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X0 = " << X0 << " Y0 = " << Y0 << " X1 = " << X1 << " Y1 = " << Y1 << " LasOn = " << LasOn << " LasOff = " << LasOff << " Power = " << Power << " Port = " << Port << " Flags = " << Flags << " Velocity = " << Velocity << endl;
  return;
}

RTC6_API void __stdcall micro_vector_quad_axis(const long X0, const long Y0, const double X1, const double Y1, const long LasOn, const long LasOff, const UINT Power, const UINT Port, const UINT Flags){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X0 = " << X0 << " Y0 = " << Y0 << " X1 = " << X1 << " Y1 = " << Y1 << " LasOn = " << LasOn << " LasOff = " << LasOff << " Power = " << Power << " Port = " << Port << " Flags = " << Flags << endl;
  return;
}

RTC6_API void __stdcall micro_vector_set_position(const long X0, const long X1, const long X2, const long X3, const long LasOn, const long LasOff){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X0 = " << X0 << " X1 = " << X1 << " X2 = " << X2 << " X3 = " << X3 << " LasOn = " << LasOn << " LasOff = " << LasOff << endl;
  return;
}

RTC6_API void __stdcall multi_axis_flags(const UINT Flags){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Flags = " << Flags << endl;
  return;
}

RTC6_API void __stdcall set_free_variable_list(const UINT VarNo, const UINT Value){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " VarNo = " << VarNo << " Value = " << Value << endl;
  return;
}

RTC6_API void __stdcall jump_abs_drill_2(const long X, const long Y, const UINT DrillTime, const long XOff, const long YOff){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " DrillTime = " << DrillTime << " XOff = " << XOff << " YOff = " << YOff << endl;
  return;
}

RTC6_API void __stdcall jump_rel_drill_2(const long dX, const long dY, const UINT DrillTime, const long XOff, const long YOff){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " DrillTime = " << DrillTime << " XOff = " << XOff << " YOff = " << YOff << endl;
  return;
}

RTC6_API void __stdcall jump_abs_drill(const long X, const long Y, const UINT DrillTime){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " DrillTime = " << DrillTime << endl;
  return;
}

RTC6_API void __stdcall jump_rel_drill(const long dX, const long dY, const UINT DrillTime){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " DrillTime = " << DrillTime << endl;
  return;
}

RTC6_API void __stdcall n_timed_mark_abs_3d(const UINT CardNo, const long X, const long Y, const long Z, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " Z = " << Z << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall n_timed_mark_rel_3d(const UINT CardNo, const long dX, const long dY, const long dZ, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall n_timed_mark_abs(const UINT CardNo, const long X, const long Y, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall n_timed_mark_rel(const UINT CardNo, const long dX, const long dY, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall timed_mark_abs_3d(const long X, const long Y, const long Z, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " Z = " << Z << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall timed_mark_rel_3d(const long dX, const long dY, const long dZ, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall timed_mark_abs(const long X, const long Y, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall timed_mark_rel(const long dX, const long dY, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall n_mark_abs_3d(const UINT CardNo, const long X, const long Y, const long Z){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " Z = " << Z << endl;
  return;
}

RTC6_API void __stdcall n_mark_rel_3d(const UINT CardNo, const long dX, const long dY, const long dZ){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << endl;
  return;
}

RTC6_API void __stdcall n_mark_abs(const UINT CardNo, const long X, const long Y){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << endl;
  return;
}

RTC6_API void __stdcall n_mark_rel(const UINT CardNo, const long dX, const long dY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << endl;
  return;
}

RTC6_API void __stdcall mark_abs_3d(const long X, const long Y, const long Z){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " Z = " << Z << endl;
  return;
}

RTC6_API void __stdcall mark_rel_3d(const long dX, const long dY, const long dZ){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << endl;
  return;
}

RTC6_API void __stdcall mark_abs(const long X, const long Y){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << endl;
  return;
}

RTC6_API void __stdcall mark_rel(const long dX, const long dY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << endl;
  return;
}

RTC6_API void __stdcall n_timed_jump_abs_3d(const UINT CardNo, const long X, const long Y, const long Z, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " Z = " << Z << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall n_timed_jump_rel_3d(const UINT CardNo, const long dX, const long dY, const long dZ, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall n_timed_jump_abs(const UINT CardNo, const long X, const long Y, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall n_timed_jump_rel(const UINT CardNo, const long dX, const long dY, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall timed_jump_abs_3d(const long X, const long Y, const long Z, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " Z = " << Z << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall timed_jump_rel_3d(const long dX, const long dY, const long dZ, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall timed_jump_abs(const long X, const long Y, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall timed_jump_rel(const long dX, const long dY, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall n_jump_abs_3d(const UINT CardNo, const long X, const long Y, const long Z){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " Z = " << Z << endl;
  return;
}

RTC6_API void __stdcall n_jump_rel_3d(const UINT CardNo, const long dX, const long dY, const long dZ){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << endl;
  return;
}

RTC6_API void __stdcall n_jump_abs(const UINT CardNo, const long X, const long Y){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << endl;
  return;
}

RTC6_API void __stdcall n_jump_rel(const UINT CardNo, const long dX, const long dY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << endl;
  return;
}

RTC6_API void __stdcall jump_abs_3d(const long X, const long Y, const long Z){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " Z = " << Z << endl;
  return;
}

RTC6_API void __stdcall jump_rel_3d(const long dX, const long dY, const long dZ){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << endl;
  return;
}

RTC6_API void __stdcall jump_abs(const long X, const long Y){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << endl;
  return;
}

RTC6_API void __stdcall jump_rel(const long dX, const long dY){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << endl;
  return;
}

RTC6_API void __stdcall n_para_mark_abs_3d(const UINT CardNo, const long X, const long Y, const long Z, const UINT P){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " Z = " << Z << " P = " << P << endl;
  return;
}

RTC6_API void __stdcall n_para_mark_rel_3d(const UINT CardNo, const long dX, const long dY, const long dZ, const UINT P){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << " P = " << P << endl;
  return;
}

RTC6_API void __stdcall n_para_mark_abs(const UINT CardNo, const long X, const long Y, const UINT P){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " P = " << P << endl;
  return;
}

RTC6_API void __stdcall n_para_mark_rel(const UINT CardNo, const long dX, const long dY, const UINT P){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " P = " << P << endl;
  return;
}

RTC6_API void __stdcall para_mark_abs_3d(const long X, const long Y, const long Z, const UINT P){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " Z = " << Z << " P = " << P << endl;
  return;
}

RTC6_API void __stdcall para_mark_rel_3d(const long dX, const long dY, const long dZ, const UINT P){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << " P = " << P << endl;
  return;
}

RTC6_API void __stdcall para_mark_abs(const long X, const long Y, const UINT P){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " P = " << P << endl;
  return;
}

RTC6_API void __stdcall para_mark_rel(const long dX, const long dY, const UINT P){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " P = " << P << endl;
  return;
}

RTC6_API void __stdcall n_para_jump_abs_3d(const UINT CardNo, const long X, const long Y, const long Z, const UINT P){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " Z = " << Z << " P = " << P << endl;
  return;
}

RTC6_API void __stdcall n_para_jump_rel_3d(const UINT CardNo, const long dX, const long dY, const long dZ, const UINT P){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << " P = " << P << endl;
  return;
}

RTC6_API void __stdcall n_para_jump_abs(const UINT CardNo, const long X, const long Y, const UINT P){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " P = " << P << endl;
  return;
}

RTC6_API void __stdcall n_para_jump_rel(const UINT CardNo, const long dX, const long dY, const UINT P){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " P = " << P << endl;
  return;
}

RTC6_API void __stdcall para_jump_abs_3d(const long X, const long Y, const long Z, const UINT P){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " Z = " << Z << " P = " << P << endl;
  return;
}

RTC6_API void __stdcall para_jump_rel_3d(const long dX, const long dY, const long dZ, const UINT P){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << " P = " << P << endl;
  return;
}

RTC6_API void __stdcall para_jump_abs(const long X, const long Y, const UINT P){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " P = " << P << endl;
  return;
}

RTC6_API void __stdcall para_jump_rel(const long dX, const long dY, const UINT P){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " P = " << P << endl;
  return;
}

RTC6_API void __stdcall n_timed_para_mark_abs_3d(const UINT CardNo, const long X, const long Y, const long Z, const UINT P, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " Z = " << Z << " P = " << P << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall n_timed_para_mark_rel_3d(const UINT CardNo, const long dX, const long dY, const long dZ, const UINT P, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << " P = " << P << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall n_timed_para_jump_abs_3d(const UINT CardNo, const long X, const long Y, const long Z, const UINT P, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " Z = " << Z << " P = " << P << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall n_timed_para_jump_rel_3d(const UINT CardNo, const long dX, const long dY, const long dZ, const UINT P, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << " P = " << P << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall n_timed_para_mark_abs(const UINT CardNo, const long X, const long Y, const UINT P, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " P = " << P << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall n_timed_para_mark_rel(const UINT CardNo, const long dX, const long dY, const UINT P, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " P = " << P << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall n_timed_para_jump_abs(const UINT CardNo, const long X, const long Y, const UINT P, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " P = " << P << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall n_timed_para_jump_rel(const UINT CardNo, const long dX, const long dY, const UINT P, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " P = " << P << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall timed_para_mark_abs_3d(const long X, const long Y, const long Z, const UINT P, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " Z = " << Z << " P = " << P << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall timed_para_mark_rel_3d(const long dX, const long dY, const long dZ, const UINT P, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << " P = " << P << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall timed_para_jump_abs_3d(const long X, const long Y, const long Z, const UINT P, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " Z = " << Z << " P = " << P << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall timed_para_jump_rel_3d(const long dX, const long dY, const long dZ, const UINT P, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << " P = " << P << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall timed_para_mark_abs(const long X, const long Y, const UINT P, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " P = " << P << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall timed_para_mark_rel(const long dX, const long dY, const UINT P, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " P = " << P << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall timed_para_jump_abs(const long X, const long Y, const UINT P, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " P = " << P << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall timed_para_jump_rel(const long dX, const long dY, const UINT P, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " P = " << P << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall n_set_defocus_list(const UINT CardNo, const long Shift){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Shift = " << Shift << endl;
  return;
}

RTC6_API void __stdcall n_set_defocus_offset_list(const UINT CardNo, const long Shift){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Shift = " << Shift << endl;
  return;
}

RTC6_API void __stdcall n_set_zoom_list(const UINT CardNo, const UINT Zoom){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Zoom = " << Zoom << endl;
  return;
}

RTC6_API void __stdcall set_defocus_list(const long Shift){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Shift = " << Shift << endl;
  return;
}

RTC6_API void __stdcall set_defocus_offset_list(const long Shift){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Shift = " << Shift << endl;
  return;
}

RTC6_API void __stdcall set_zoom_list(const UINT Zoom){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Zoom = " << Zoom << endl;
  return;
}

RTC6_API void __stdcall n_timed_arc_abs(const UINT CardNo, const long X, const long Y, const double Angle, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " Angle = " << Angle << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall n_timed_arc_rel(const UINT CardNo, const long dX, const long dY, const double Angle, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " Angle = " << Angle << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall timed_arc_abs(const long X, const long Y, const double Angle, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " Angle = " << Angle << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall timed_arc_rel(const long dX, const long dY, const double Angle, const double T){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " Angle = " << Angle << " T = " << T << endl;
  return;
}

RTC6_API void __stdcall n_arc_abs_3d(const UINT CardNo, const long X, const long Y, const long Z, const double Angle){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " Z = " << Z << " Angle = " << Angle << endl;
  return;
}

RTC6_API void __stdcall n_arc_rel_3d(const UINT CardNo, const long dX, const long dY, const long dZ, const double Angle){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << " Angle = " << Angle << endl;
  return;
}

RTC6_API void __stdcall n_arc_abs(const UINT CardNo, const long X, const long Y, const double Angle){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " Angle = " << Angle << endl;
  return;
}

RTC6_API void __stdcall n_arc_rel(const UINT CardNo, const long dX, const long dY, const double Angle){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " Angle = " << Angle << endl;
  return;
}

RTC6_API void __stdcall n_set_ellipse(const UINT CardNo, const UINT A, const UINT B, const double Phi0, const double Phi){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " A = " << A << " B = " << B << " Phi0 = " << Phi0 << " Phi = " << Phi << endl;
  return;
}

RTC6_API void __stdcall n_mark_ellipse_abs(const UINT CardNo, const long X, const long Y, const double Alpha){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " X = " << X << " Y = " << Y << " Alpha = " << Alpha << endl;
  return;
}

RTC6_API void __stdcall n_mark_ellipse_rel(const UINT CardNo, const long dX, const long dY, const double Alpha){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dX = " << dX << " dY = " << dY << " Alpha = " << Alpha << endl;
  return;
}

RTC6_API void __stdcall arc_abs_3d(const long X, const long Y, const long Z, const double Angle){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " Z = " << Z << " Angle = " << Angle << endl;
  return;
}

RTC6_API void __stdcall arc_rel_3d(const long dX, const long dY, const long dZ, const double Angle){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " dZ = " << dZ << " Angle = " << Angle << endl;
  return;
}

RTC6_API void __stdcall arc_abs(const long X, const long Y, const double Angle){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " Angle = " << Angle << endl;
  return;
}

RTC6_API void __stdcall arc_rel(const long dX, const long dY, const double Angle){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " Angle = " << Angle << endl;
  return;
}

RTC6_API void __stdcall set_ellipse(const UINT A, const UINT B, const double Phi0, const double Phi){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " A = " << A << " B = " << B << " Phi0 = " << Phi0 << " Phi = " << Phi << endl;
  return;
}

RTC6_API void __stdcall mark_ellipse_abs(const long X, const long Y, const double Alpha){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " X = " << X << " Y = " << Y << " Alpha = " << Alpha << endl;
  return;
}

RTC6_API void __stdcall mark_ellipse_rel(const long dX, const long dY, const double Alpha){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dX = " << dX << " dY = " << dY << " Alpha = " << Alpha << endl;
  return;
}

RTC6_API void __stdcall n_set_offset_xyz_list(const UINT CardNo, const UINT HeadNo, const long XOffset, const long YOffset, const long ZOffset, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " XOffset = " << XOffset << " YOffset = " << YOffset << " ZOffset = " << ZOffset << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall n_set_offset_list(const UINT CardNo, const UINT HeadNo, const long XOffset, const long YOffset, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " XOffset = " << XOffset << " YOffset = " << YOffset << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall n_set_matrix_list(const UINT CardNo, const UINT HeadNo, const UINT Ind1, const UINT Ind2, const double Mij, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " Ind1 = " << Ind1 << " Ind2 = " << Ind2 << " Mij = " << Mij << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall n_set_angle_list(const UINT CardNo, const UINT HeadNo, const double Angle, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " Angle = " << Angle << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall n_set_scale_list(const UINT CardNo, const UINT HeadNo, const double Scale, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " Scale = " << Scale << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall n_apply_mcbsp_list(const UINT CardNo, const UINT HeadNo, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " HeadNo = " << HeadNo << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall set_offset_xyz_list(const UINT HeadNo, const long XOffset, const long YOffset, const long ZOffset, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " XOffset = " << XOffset << " YOffset = " << YOffset << " ZOffset = " << ZOffset << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall set_offset_list(const UINT HeadNo, const long XOffset, const long YOffset, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " XOffset = " << XOffset << " YOffset = " << YOffset << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall set_matrix_list(const UINT HeadNo, const UINT Ind1, const UINT Ind2, const double Mij, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " Ind1 = " << Ind1 << " Ind2 = " << Ind2 << " Mij = " << Mij << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall set_angle_list(const UINT HeadNo, const double Angle, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " Angle = " << Angle << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall set_scale_list(const UINT HeadNo, const double Scale, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " Scale = " << Scale << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall apply_mcbsp_list(const UINT HeadNo, const UINT at_once){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " HeadNo = " << HeadNo << " at_once = " << at_once << endl;
  return;
}

RTC6_API void __stdcall n_set_mark_speed(const UINT CardNo, const double Speed){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Speed = " << Speed << endl;
  return;
}

RTC6_API void __stdcall n_set_jump_speed(const UINT CardNo, const double Speed){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Speed = " << Speed << endl;
  return;
}

RTC6_API void __stdcall n_set_sky_writing_para_list(const UINT CardNo, const double Timelag, const long LaserOnShift, const UINT Nprev, const UINT Npost){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Timelag = " << Timelag << " LaserOnShift = " << LaserOnShift << " Nprev = " << Nprev << " Npost = " << Npost << endl;
  return;
}

RTC6_API void __stdcall n_set_sky_writing_list(const UINT CardNo, const double Timelag, const long LaserOnShift){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Timelag = " << Timelag << " LaserOnShift = " << LaserOnShift << endl;
  return;
}

RTC6_API void __stdcall n_set_sky_writing_limit_list(const UINT CardNo, const double CosAngle){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " CosAngle = " << CosAngle << endl;
  return;
}

RTC6_API void __stdcall n_set_sky_writing_mode_list(const UINT CardNo, const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_set_scanner_delays(const UINT CardNo, const UINT Jump, const UINT Mark, const UINT Polygon){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Jump = " << Jump << " Mark = " << Mark << " Polygon = " << Polygon << endl;
  return;
}

RTC6_API void __stdcall n_set_jump_mode_list(const UINT CardNo, const long Flag){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Flag = " << Flag << endl;
  return;
}

RTC6_API void __stdcall n_enduring_wobbel(const UINT CardNo){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << endl;
  return;
}

RTC6_API void __stdcall n_set_delay_mode_list(const UINT CardNo, const UINT VarPoly, const UINT DirectMove3D, const UINT EdgeLevel, const UINT MinJumpDelay, const UINT JumpLengthLimit){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " VarPoly = " << VarPoly << " DirectMove3D = " << DirectMove3D << " EdgeLevel = " << EdgeLevel << " MinJumpDelay = " << MinJumpDelay << " JumpLengthLimit = " << JumpLengthLimit << endl;
  return;
}

RTC6_API void __stdcall set_mark_speed(const double Speed){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Speed = " << Speed << endl;
  return;
}

RTC6_API void __stdcall set_jump_speed(const double Speed){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Speed = " << Speed << endl;
  return;
}

RTC6_API void __stdcall set_sky_writing_para_list(const double Timelag, const long LaserOnShift, const UINT Nprev, const UINT Npost){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Timelag = " << Timelag << " LaserOnShift = " << LaserOnShift << " Nprev = " << Nprev << " Npost = " << Npost << endl;
  return;
}

RTC6_API void __stdcall set_sky_writing_list(const double Timelag, const long LaserOnShift){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Timelag = " << Timelag << " LaserOnShift = " << LaserOnShift << endl;
  return;
}

RTC6_API void __stdcall set_sky_writing_limit_list(const double CosAngle){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CosAngle = " << CosAngle << endl;
  return;
}

RTC6_API void __stdcall set_sky_writing_mode_list(const UINT Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall set_scanner_delays(const UINT Jump, const UINT Mark, const UINT Polygon){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Jump = " << Jump << " Mark = " << Mark << " Polygon = " << Polygon << endl;
  return;
}

RTC6_API void __stdcall set_jump_mode_list(const long Flag){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Flag = " << Flag << endl;
  return;
}

RTC6_API void __stdcall enduring_wobbel(void){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << endl;
  return;
}

RTC6_API void __stdcall set_delay_mode_list(const UINT VarPoly, const UINT DirectMove3D, const UINT EdgeLevel, const UINT MinJumpDelay, const UINT JumpLengthLimit){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " VarPoly = " << VarPoly << " DirectMove3D = " << DirectMove3D << " EdgeLevel = " << EdgeLevel << " MinJumpDelay = " << MinJumpDelay << " JumpLengthLimit = " << JumpLengthLimit << endl;
  return;
}

RTC6_API void __stdcall n_activate_scanahead_autodelays_list(const UINT CardNo, const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall n_set_scanahead_laser_shifts_list(const UINT CardNo, const long dLasOn, const long dLasOff){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dLasOn = " << dLasOn << " dLasOff = " << dLasOff << endl;
  return;
}

RTC6_API void __stdcall n_set_scanahead_line_params_list(const UINT CardNo, const UINT CornerScale, const UINT EndScale, const UINT AccScale){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " CornerScale = " << CornerScale << " EndScale = " << EndScale << " AccScale = " << AccScale << endl;
  return;
}

RTC6_API void __stdcall n_set_scanahead_line_params_ex_list(const UINT CardNo, const UINT CornerScale, const UINT EndScale, const UINT AccScale, const UINT JumpScale){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " CornerScale = " << CornerScale << " EndScale = " << EndScale << " AccScale = " << AccScale << " JumpScale = " << JumpScale << endl;
  return;
}

RTC6_API void __stdcall activate_scanahead_autodelays_list(const long Mode){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Mode = " << Mode << endl;
  return;
}

RTC6_API void __stdcall set_scanahead_laser_shifts_list(const long dLasOn, const long dLasOff){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dLasOn = " << dLasOn << " dLasOff = " << dLasOff << endl;
  return;
}

RTC6_API void __stdcall set_scanahead_line_params_list(const UINT CornerScale, const UINT EndScale, const UINT AccScale){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CornerScale = " << CornerScale << " EndScale = " << EndScale << " AccScale = " << AccScale << endl;
  return;
}

RTC6_API void __stdcall set_scanahead_line_params_ex_list(const UINT CornerScale, const UINT EndScale, const UINT AccScale, const UINT JumpScale){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CornerScale = " << CornerScale << " EndScale = " << EndScale << " AccScale = " << AccScale << " JumpScale = " << JumpScale << endl;
  return;
}

RTC6_API void __stdcall n_stepper_enable_list(const UINT CardNo, const long Enable1, const long Enable2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Enable1 = " << Enable1 << " Enable2 = " << Enable2 << endl;
  return;
}

RTC6_API void __stdcall n_stepper_control_list(const UINT CardNo, const long Period1, const long Period2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Period1 = " << Period1 << " Period2 = " << Period2 << endl;
  return;
}

RTC6_API void __stdcall n_stepper_abs_no_list(const UINT CardNo, const UINT No, const long Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " No = " << No << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall n_stepper_rel_no_list(const UINT CardNo, const UINT No, const long dPos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " No = " << No << " dPos = " << dPos << endl;
  return;
}

RTC6_API void __stdcall n_stepper_abs_list(const UINT CardNo, const long Pos1, const long Pos2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " Pos1 = " << Pos1 << " Pos2 = " << Pos2 << endl;
  return;
}

RTC6_API void __stdcall n_stepper_rel_list(const UINT CardNo, const long dPos1, const long dPos2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " dPos1 = " << dPos1 << " dPos2 = " << dPos2 << endl;
  return;
}

RTC6_API void __stdcall n_stepper_wait(const UINT CardNo, const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " CardNo = " << CardNo << " No = " << No << endl;
  return;
}

RTC6_API void __stdcall stepper_enable_list(const long Enable1, const long Enable2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Enable1 = " << Enable1 << " Enable2 = " << Enable2 << endl;
  return;
}

RTC6_API void __stdcall stepper_control_list(const long Period1, const long Period2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Period1 = " << Period1 << " Period2 = " << Period2 << endl;
  return;
}

RTC6_API void __stdcall stepper_abs_no_list(const UINT No, const long Pos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " No = " << No << " Pos = " << Pos << endl;
  return;
}

RTC6_API void __stdcall stepper_rel_no_list(const UINT No, const long dPos){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " No = " << No << " dPos = " << dPos << endl;
  return;
}

RTC6_API void __stdcall stepper_abs_list(const long Pos1, const long Pos2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " Pos1 = " << Pos1 << " Pos2 = " << Pos2 << endl;
  return;
}

RTC6_API void __stdcall stepper_rel_list(const long dPos1, const long dPos2){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " dPos1 = " << dPos1 << " dPos2 = " << dPos2 << endl;
  return;
}

RTC6_API void __stdcall stepper_wait(const UINT No){
  // auto-gen dummy impl of function
  cout << __FUNCTION__ << " called " << " No = " << No << endl;
  return;
}

