from typing import Literal

ApiV1DomainsDnsrecordsUpdatePriorityErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_DOMAINS_DNSRECORDS_UPDATE_PRIORITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsUpdatePriorityErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_domains_dnsrecords_update_priority_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsUpdatePriorityErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_UPDATE_PRIORITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_UPDATE_PRIORITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
