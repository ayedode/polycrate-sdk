from typing import Literal

ApiV1DomainsDnsrecordsUpdateTtlErrorComponentAttr = Literal["ttl"]

API_V1_DOMAINS_DNSRECORDS_UPDATE_TTL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsUpdateTtlErrorComponentAttr
] = {
    "ttl",
}


def check_api_v1_domains_dnsrecords_update_ttl_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsUpdateTtlErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_UPDATE_TTL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_UPDATE_TTL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
