from subprocess import call, check_output

cmd = 'openssl crl2pkcs7 -nocrl -certfile /Users/wleelaket/Documents/ICE/"Year4 Sem2"/SysSecurity/ca-certificates.crt | openssl pkcs7 -print_certs -noout'
run_ssl = call(cmd, shell=True)
# print(run_ssl)
# list_cert = str(run_ssl).split('\\n\\n')
# msg = 'Number of certificates: '
# print(msg, len(list_cert) - 1) #minus the last member in list


