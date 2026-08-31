from typing import Literal

ApiV1DomainsDomainRegistrarsCreateManagedByObjectIdErrorComponentAttr = Literal["managed_by_object_id"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateManagedByObjectIdErrorComponentAttr
] = {
    "managed_by_object_id",
}


def check_api_v1_domains_domain_registrars_create_managed_by_object_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateManagedByObjectIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
