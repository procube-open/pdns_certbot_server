# swagger_client.GetCertificateApi

All URIs are relative to *http://localhost:61003/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_certificate**](GetCertificateApi.md#get_certificate) | **GET** /get/{fqdn} | サーバ証明書を取得するAPIである。

# **get_certificate**
> Certificate get_certificate(fqdn)

サーバ証明書を取得するAPIである。

fqdn で指定されたドメインのサーバ証明書 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetCertificateApi()
fqdn = 'fqdn_example' # str | 取得する証明書の FQDN

try:
    # サーバ証明書を取得するAPIである。
    api_response = api_instance.get_certificate(fqdn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetCertificateApi->get_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| 取得する証明書の FQDN | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

