from typing import Literal

ApiV1DomainsDnsrecordsPartialUpdateTtlErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_TTL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsPartialUpdateTtlErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_domains_dnsrecords_partial_update_ttl_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsPartialUpdateTtlErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_TTL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_TTL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
