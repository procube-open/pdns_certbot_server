"""Certbot main public entry point."""
from certbot._internal import main as internal_main
import os


def main(cli_args=None):
    """Command line argument parsing and main script execution.

    :returns: result of requested command

    :raises errors.Error: OS errors triggered by wrong permissions
    :raises errors.Error: error if plugin command is not supported

    """

    fqdn = 'test.sakura.ne.jp'
    os.makedirs('/etc/letsencrypt/live/' + fqdn, exist_ok = True)

    with open('/etc/letsencrypt/live/' + fqdn + '/cert.pem', 'w', newline="\n") as cert_file:
        cert_file.write('-----BEGIN CERTIFICATE-----\n'\
                        'MIIJqzCCCJOgAwIBAgIQVIhihZkFDxismyB1t2pm+jANBgkqhkiG9w0BAQsFADCB\n'\
                        'gjELMAkGA1UEBhMCSlAxDjAMBgNVBAgTBVRva3lvMRMwEQYDVQQHEwpDaGl5b2Rh\n'\
                        'LWt1MRQwEgYDVQQKEwtHZWhpcm4gSW5jLjE4MDYGA1UEAxMvR2VoaXJuIE1hbmFn\n'\
                        'ZWQgQ2VydGlmaWNhdGlvbiBBdXRob3JpdHkgLSBSU0EgRFYwHhcNMTgwNjI4MDAw\n'\
                        'MDAwWhcNMjAwNjI3MjM1OTU5WjA8MSEwHwYDVQQLExhEb21haW4gQ29udHJvbCBW\n'\
                        'YWxpZGF0ZWQxFzAVBgNVBAMMDiouc2FrdXJhLm5lLmpwMIIBIjANBgkqhkiG9w0B\n'\
                        'AQEFAAOCAQ8AMIIBCgKCAQEA5Q7v6Ba4yS7NGTG535yVZBR82oO6XZXzi/PJV4hh\n'\
                        'qivpVtMGWvEHwS9qQaK+jq70bwjvoSgb6Or6MOax8lgS1h9kVG6/kc+OBkZ0nUr+\n'\
                        '3RBaHlci6ixU9wFtuWZaFe7/gUv23vjb70LDbhwOqktISJyWqchfnmeQcbcpuaXh\n'\
                        '5P5sUAiyprYMbqjiM6+RhRKS5BA4GxGwYWdFMKTyx8wrvYPbjLWUtsdYnyw+rutn\n'\
                        'BoKgM5OSuh7vnRJ9BZUzb2csRIajHdvxmfsRpNt0PuxvUEQtke/a/fwsipF/XHls\n'\
                        'FhTtMzk+qsbLiEZYaYmeXNoQeU9XlDwBHxalpwtTcyYTsQIDAQABo4IGYDCCBlww\n'\
                        'HwYDVR0jBBgwFoAUEuZqJYZx7cyOaQxZGcAHvByorUswHQYDVR0OBBYEFGqEaygH\n'\
                        'q4zhSo5jT6fgrtrit50CMA4GA1UdDwEB/wQEAwIFoDAMBgNVHRMBAf8EAjAAMB0G\n'\
                        'A1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjBLBgNVHSAERDBCMDYGCysGAQQB\n'\
                        'sjEBAgI8MCcwJQYIKwYBBQUHAgEWGWh0dHBzOi8vY3BzLnVzZXJ0cnVzdC5jb20w\n'\
                        'CAYGZ4EMAQIBMFYGA1UdHwRPME0wS6BJoEeGRWh0dHA6Ly9jcmwudXNlcnRydXN0\n'\
                        'LmNvbS9HZWhpcm5NYW5hZ2VkQ2VydGlmaWNhdGlvbkF1dGhvcml0eVJTQURWLmNy\n'\
                        'bDCBiAYIKwYBBQUHAQEEfDB6MFEGCCsGAQUFBzAChkVodHRwOi8vY3J0LnVzZXJ0\n'\
                        'cnVzdC5jb20vR2VoaXJuTWFuYWdlZENlcnRpZmljYXRpb25BdXRob3JpdHlSU0FE\n'\
                        'Vi5jcnQwJQYIKwYBBQUHMAGGGWh0dHA6Ly9vY3NwLnVzZXJ0cnVzdC5jb20wggMq\n'\
                        'BgNVHREEggMhMIIDHYIOKi5zYWt1cmEubmUuanCCCiouMTgwci5jb22CCCouMi1k\n'\
                        'LmpwggoqLmFjaG9vLmpwgg0qLmFtYXJldHRvLmpwggkqLmJvbmEuanCCCSouY2hl\n'\
                        'dy5qcIIJKi5jcmFwLmpwgg0qLmRheW5pZ2h0LmpwggoqLmRla284LmpwggsqLmRv\n'\
                        'amluLmNvbYIIKi5lZWsuanCCCSouZmxvcC5qcIIJKi5mcm9tLnR2gg0qLmZ1YnVr\n'\
                        'aS5pbmZvgg0qLmdva3Vqb3UuYml6ggoqLmdyYXRzLmpwggkqLmdycnIuanCCDSou\n'\
                        'aGFsZm1vb24uanCCDSouaXZvcnkubmUuanCCCSouamVlei5qcIIJKi5qcG4ub3Jn\n'\
                        'ggsqLmtpcmFyYS5zdIILKi5rb2thZ2UuY2OCECoubWFpbC1ib3gubmUuanCCCyou\n'\
                        'bWF0cml4LmpwggsqLm1pbW96YS5qcIINKi5taW50cy5uZS5qcIIPKi5tb2t1cmVu\n'\
                        'Lm5lLmpwggkqLm5hem8uY2OCDioubmV0Z2FtZXJzLmpwggkqLm5vb2IuanCCCyou\n'\
                        'bnlhbnRhLmpwggkqLm8wbzAuanCCDCoub3BhbC5uZS5qcIIJKi5yYXNoLmpwggoq\n'\
                        'LnJhem9yLmpwgggqLnJkeS5qcIIIKi5yZ3IuanCCCSoucm9qby5qcIIKKi5yb3Nz\n'\
                        'YS5jY4IKKi5ydWxlei5qcIIJKi5ydXNrLnRvgg0qLnNhaWt5b3UuYml6ggsqLnNh\n'\
                        'a3VyYS50doIPKi5zYWt1cmF0YW4uY29tgg8qLnNha3VyYXdlYi5jb22CCyouc2Fs\n'\
                        'b29uLmpwggkqLnNpbGsudG+CCCouc2tyLmpwggoqLnNwYXduLmpwgg0qLnNxdWFy\n'\
                        'ZXMubmV0gg4qLnN1bW9tby5uZS5qcIIJKi50YW5rLmpwggoqLnRoeW1lLmpwgg0q\n'\
                        'LnRvcGF6Lm5lLmpwggoqLnVoLW9oLmpwggkqLnVuZG8uanCCDSoud2Vic296YWku\n'\
                        'anCCCSoud2hvYS5qcIIIKi54MC5jb22CByoueDAudG+CCCoueGlpLmpwMIIBfQYK\n'\
                        'KwYBBAHWeQIEAgSCAW0EggFpAWcAdgDuS723dc5guuFCaR+r4Z5mow9+X7By2IMA\n'\
                        'xHuJeqj9ywAAAWREex2WAAAEAwBHMEUCIHEbhtYPC2HmaSI+VKvoho0aKZb7dv9e\n'\
                        'uQAFx620tfL1AiEAk3+PvH35stHXo9jhEjLyotlUV/5Bfzsv3uBZQQjyPtQAdgBe\n'\
                        'p3P531bA57U2SH3QSeAyepGaDIShEhKEGHWWgXFFWAAAAWREex3aAAAEAwBHMEUC\n'\
                        'IEsUHzvzvEXOJRlghqlcIJR9BKkKYNiAxrGKB6ADqLGfAiEA8nzKg99hFTzImtpG\n'\
                        '5jJ1pJIrPu7lm3+099GIWTAepu8AdQBVgdTCFpA2AUrqC5tXPFPwwOQ4eHAlCBcv\n'\
                        'o6odBxPTDAAAAWREex26AAAEAwBGMEQCIAa/nHlcXPjyQhcnnkddqzH9+KMdSGgx\n'\
                        'd2KF7r/Kwi+nAiBFTggil1fhKxm0hYWptOQJjzF1MX1p3ncv/A1idBqg3TANBgkq\n'\
                        'hkiG9w0BAQsFAAOCAQEALKhm1hC3mkllUw3C4lv1igtYRLTmEx1XoCYAGrJK5Aap\n'\
                        'QMwTakzmRl+U41XoQcamk0pAGFaewwplae2kqsMe/tRSuQmrPM08TyVfJGS1nB4m\n'\
                        'Zow3fYajj4zwu84TQhbQxIweGT7BEMlfowxNS92vtoAcSOP8JGjQc9KTOIlSBh3e\n'\
                        'CZLgwz8n+p3q9GaLrOsoqM2KzIXjPNHfxnEVqnadLl1FCgcIxO/dTQTXZ7EfBDXR\n'\
                        'mlQjTkNT1AQfMMga98nW7EMnUk8QuKpEWQKVAFkqhkIJtbYsph5NkCN18lY4gGJB\n'\
                        '28tMCgf8kEjX2H/aS8p/lLftS3UKeapBSFQR/TRSyQ==\n'\
                        '-----END CERTIFICATE-----')

    with open('/etc/letsencrypt/live/' + fqdn + '/fullchain.pem', 'w', newline="\n") as fullchain_file:  
        fullchain_file.write('-----BEGIN CERTIFICATE-----\n'\
                             'MIIGKDCCBRCgAwIBAgISA5FY/8zZgI3QbaUi3wSpgtMJMA0GCSqGSIb3DQEBCwUA\n'\
                             'MEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\n'\
                             'ExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODEwMDUxMDM4MjRaFw0x\n'\
                             'OTAxMDMxMDM4MjRaMCoxKDAmBgNVBAMTH3BvcnRhbC5taWMtdGVzdC5wcm9jdWJl\n'\
                             'LWRlbW8uanAwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCrNahcIILd\n'\
                             'gyEMcwveA7CYC+ZnmDW2jbE2AwXO6b3G4/lMX8YDeq5FXLdC5Qrcs6jBSu02uUKQ\n'\
                             'o5uHaEaCXynR2Xo1L1kvKYFivKM+GWs3KY/pT/1lCaP6xCVtED/Tepy1K0lgfj5e\n'\
                             '-----END CERTIFICATE-----')

    with open('/etc/letsencrypt/live/' + fqdn + '/key.pem', 'w', newline="\n") as key_file:  
        key_file.write('-----BEGIN KEY-----\n'\
                       'MIIGKDCCBRCgAwIBAgISA5FY/8zZgI3QbaUi3wSpgtMJMA0GCSqGSIb3DQEBCwUA\n'\
                       'MEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\n'\
                       'ExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODEwMDUxMDM4MjRaFw0x\n'\
                       'OTAxMDMxMDM4MjRaMCoxKDAmBgNVBAMTH3BvcnRhbC5taWMtdGVzdC5wcm9jdWJl\n'\
                       'LWRlbW8uanAwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCrNahcIILd\n'\
                       'gyEMcwveA7CYC+ZnmDW2jbE2AwXO6b3G4/lMX8YDeq5FXLdC5Qrcs6jBSu02uUKQ\n'\
                       'o5uHaEaCXynR2Xo1L1kvKYFivKM+GWs3KY/pT/1lCaP6xCVtED/Tepy1K0lgfj5e\n'\
                       '-----END KEY-----')

    with open('/etc/letsencrypt/live/' + fqdn + '/privkey.pem', 'w', newline="\n") as privkey_file:
        privkey_file.write('-----BEGIN PRIVATE KEY-----\n'\
                           'MIIGKDCCBRCgAwIBAgISA5FY/8zZgI3QbaUi3wSpgtMJMA0GCSqGSIb3DQEBCwUA\n'\
                           'MEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\n'\
                           'ExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xODEwMDUxMDM4MjRaFw0x\n'\
                           'OTAxMDMxMDM4MjRaMCoxKDAmBgNVBAMTH3BvcnRhbC5taWMtdGVzdC5wcm9jdWJl\n'\
                           'LWRlbW8uanAwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCrNahcIILd\n'\
                           'gyEMcwveA7CYC+ZnmDW2jbE2AwXO6b3G4/lMX8YDeq5FXLdC5Qrcs6jBSu02uUKQ\n'\
                           'o5uHaEaCXynR2Xo1L1kvKYFivKM+GWs3KY/pT/1lCaP6xCVtED/Tepy1K0lgfj5e\n'\
                           '-----END PRIVATE KEY-----')

    return None
    # return internal_main.main(cli_args)
