from typing import Literal

ApiV1DomainsDnsrecordsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_DOMAINS_DNSRECORDS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_domains_dnsrecords_create_provider_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsCreateProviderErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
