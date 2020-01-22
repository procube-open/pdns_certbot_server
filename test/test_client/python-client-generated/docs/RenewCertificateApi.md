# swagger_client.RenewCertificateApi

All URIs are relative to *http://localhost:61003/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**renew**](RenewCertificateApi.md#renew) | **POST** /renew | サーバ証明書を更新する

# **renew**
> renew()

サーバ証明書を更新する

取得済みの証明書の期限切れをチェックし、期限切れが 近いものを更新するAPIである。クロックデーモンにより、 定期的に呼び出されることを前提としている。 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RenewCertificateApi()

try:
    # サーバ証明書を更新する
    api_instance.renew()
except ApiException as e:
    print("Exception when calling RenewCertificateApi->renew: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

