from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_domains_domain_registrars_archive_create_kind_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateKindErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
