from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreateArchivedReasonErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreateArchivedReasonErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_archived_reason_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreateArchivedReasonErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
