from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_domains_domain_registrars_archive_create_criticality_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateCriticalityErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
