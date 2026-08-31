from typing import Literal

ApiV1DomainsDnsrecordsCreatePriorityErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_DOMAINS_DNSRECORDS_CREATE_PRIORITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsCreatePriorityErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_domains_dnsrecords_create_priority_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsCreatePriorityErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_CREATE_PRIORITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_CREATE_PRIORITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
