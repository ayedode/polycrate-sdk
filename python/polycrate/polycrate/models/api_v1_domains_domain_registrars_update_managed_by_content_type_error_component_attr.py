from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateManagedByContentTypeErrorComponentAttr = Literal["managed_by_content_type"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateManagedByContentTypeErrorComponentAttr
] = {
    "managed_by_content_type",
}


def check_api_v1_domains_domain_registrars_update_managed_by_content_type_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateManagedByContentTypeErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
