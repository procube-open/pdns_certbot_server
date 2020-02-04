# swagger_client.GetCertificateApi

All URIs are relative to *http://localhost:61003/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_certificate**](GetCertificateApi.md#get_certificate) | **GET** /get/{fqdn} | API that get server certificate.

# **get_certificate**
> Certificate get_certificate(fqdn)

API that get server certificate.

server certificate of domain that specified in fqdn

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetCertificateApi()
fqdn = 'fqdn_example' # str | FQDN of certificate to get

try:
    # API that gets server certificate.
    api_response = api_instance.get_certificate(fqdn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetCertificateApi->get_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| FQDN of certificate to get | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

