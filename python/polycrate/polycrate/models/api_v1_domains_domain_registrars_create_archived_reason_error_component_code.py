from typing import Literal

ApiV1DomainsDomainRegistrarsCreateArchivedReasonErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateArchivedReasonErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_domains_domain_registrars_create_archived_reason_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateArchivedReasonErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
