from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_domains_domain_registrars_update_created_by_component_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateCreatedByComponentErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
