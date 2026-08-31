from typing import Literal

ApiV1DomainsDnsrecordsUpdateTtlErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_DOMAINS_DNSRECORDS_UPDATE_TTL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsUpdateTtlErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_domains_dnsrecords_update_ttl_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsUpdateTtlErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_UPDATE_TTL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_UPDATE_TTL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
