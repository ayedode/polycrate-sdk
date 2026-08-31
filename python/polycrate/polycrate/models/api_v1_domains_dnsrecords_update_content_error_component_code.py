from typing import Literal

ApiV1DomainsDnsrecordsUpdateContentErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_DOMAINS_DNSRECORDS_UPDATE_CONTENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsUpdateContentErrorComponentCode
] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_domains_dnsrecords_update_content_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsUpdateContentErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_UPDATE_CONTENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_UPDATE_CONTENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
