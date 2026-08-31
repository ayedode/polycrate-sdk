from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_domain_registrars_archive_create_labels_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateLabelsErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
