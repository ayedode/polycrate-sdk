from typing import Literal

ApiV1DomainsDnsrecordsCreateTtlErrorComponentAttr = Literal["ttl"]

API_V1_DOMAINS_DNSRECORDS_CREATE_TTL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsCreateTtlErrorComponentAttr
] = {
    "ttl",
}


def check_api_v1_domains_dnsrecords_create_ttl_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsCreateTtlErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_CREATE_TTL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_CREATE_TTL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
