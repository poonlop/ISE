from OpenSSL import crypto 
import pem

def verify(target_cert_path, int_cert_path):
    with open(target_cert_path, 'r') as cert_file:
        cert = cert_file.read()

    with open(int_cert_path, 'r') as int_cert_file: 
        int_cert = int_cert_file.read()

    pems=pem.parse_file('./ca-certificates.crt'); trusted_certs = []
    for mypem in pems:
        trusted_certs.append(str(mypem))

    trusted_certs.append(int_cert)
    verified = verify_chain_of_trust(cert, trusted_certs)
    if verified:
        print('Certificate verified')

def verify_chain_of_trust(cert_pem, trusted_cert_pems):

    certificate = crypto.load_certificate(crypto.FILETYPE_PEM, cert_pem)

    # Create and fill a X509Store with trusted certs 
    store = crypto.X509Store()
    for trusted_cert_pem in trusted_cert_pems:
        trusted_cert = crypto.load_certificate(crypto.FILETYPE_PEM, trusted_cert_pem)
        store.add_cert(trusted_cert)

    # Create a X590StoreContext with the cert and trusted certs 
    # and verify the the chain of trust
    store_ctx = crypto.X509StoreContext(store, certificate)
# Returns None if certificate can be validated
    
    result = store_ctx.verify_certificate()
    if result is None: 
        return True
    else: 
        return False

#twitter certs
twitter_cert = './twitter.com.cer'
int_twt_cert = './intermediate_twt.cer'
print('\nVerify twitter certs: ')
verify(twitter_cert, int_twt_cert)

#google certs
google_cert = './google.com.cer'
int_google_cert = './intermediate_google.cer'
print('\nVerify google certs: ')
verify(google_cert, int_google_cert)

# #cu certs
chula_cert = './chula.ac.th.cer'
int_cu_cert = './intermediate_cu.cer'
print('\nVerify chula.ac.th certs: ')
verify(chula_cert, int_cu_cert)

#ClassDeeDee certs
cdd_cert = './classdeedee.cer'
int_cdd_cert = './intermediate_cdd.cer'
print('\nVerify classdeedee certs: ')
verify(cdd_cert, int_cdd_cert)
