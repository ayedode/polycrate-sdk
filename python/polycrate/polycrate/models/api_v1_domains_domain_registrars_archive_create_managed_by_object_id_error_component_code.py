from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateManagedByObjectIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateManagedByObjectIdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_domains_domain_registrars_archive_create_managed_by_object_id_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateManagedByObjectIdErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
