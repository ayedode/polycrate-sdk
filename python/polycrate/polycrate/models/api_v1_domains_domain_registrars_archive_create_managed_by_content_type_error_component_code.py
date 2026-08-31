from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateManagedByContentTypeErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type"
]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateManagedByContentTypeErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_domains_domain_registrars_archive_create_managed_by_content_type_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateManagedByContentTypeErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
