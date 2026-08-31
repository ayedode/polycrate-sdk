from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateManagedByObjectIdErrorComponentAttr = Literal["managed_by_object_id"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateManagedByObjectIdErrorComponentAttr
] = {
    "managed_by_object_id",
}


def check_api_v1_domains_domain_registrars_archive_create_managed_by_object_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateManagedByObjectIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
