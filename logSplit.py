#!/usr/bin/python3
import os
import csv

location = os.getcwd()

dict = {'refclocks.log':['date', 'time', 'ref_id', 'sequence_num', 'leap_status', 'pps_flag', 'local_clock_error', 'local_clock_corrected', 'assumed_dispersion_of_sample'],
        'measurements.log' : ['date', 'time', 'ip', 'leap_status', 'stratum', 'rfc_5905_1-3', 'rfc_5905_3-5', 'delay_tests', 'local_poll', 'remote_poll', 'score', 'estimated_local_error', 'peer_delay', 'peer_dispersion', 'reference_id', 'ntp_mode', 'transmit_timestamp_source', 'receive_timestamp_source'],
        'statistics.log' : ['date', 'time', 'ip', 'estimated_sd_src', 'estimated_offset_src', 'estimated_sd_offset', 'estimated_rate_of_deviation', 'estimated_error_in_rate', 'ratio', 'number_of_measurements', 'new_starting_index', 'number_of_runs', 'est_or_conf_asym_of network_jitter'],
        'tracking.log' : ['date', 'time', 'ip', 'stratum', 'local_system_frequency', 'error_bounds', 'estimated_local_offset', 'leap_status', 'num_combined_sources', 'estimated_sd_combined_offset', 'remaining_offset_correction_from previous_update', 'total_of_network_path_delays_to_ref_clocks', 'total_dispersion_accumulated', 'maximum estimated_error'],
        'rtc.log' : ['date', 'time', 'measured_offset_between_sys_rtc', 'flag_valid_coefficients', 'offsets_predicted', 'rate_of_deviation', 'num_measurements', 'number_runs_regression', 'measurement_interval'],
        'tempcomp.log' : ['date', 'time', 'temp', 'applied_compensation']
    }

for filename in os.listdir(location):
    if filename in dict:
        f  = open(os.path.join(location, filename), "r")
        log = f.read().splitlines()
        log = [line.split() for line in log]
        f = open((filename + '.csv'), 'w')
        writer = csv.writer(f)
        writer.writerow(dict[filename])
        for line in log:
            if len(line) == len(dict[filename]):
                writer.writerow(line)