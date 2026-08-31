from typing import Literal

ApiV1DomainsDnsrecordsPartialUpdateTtlErrorComponentAttr = Literal["ttl"]

API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_TTL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsPartialUpdateTtlErrorComponentAttr
] = {
    "ttl",
}


def check_api_v1_domains_dnsrecords_partial_update_ttl_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsPartialUpdateTtlErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_TTL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_TTL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
