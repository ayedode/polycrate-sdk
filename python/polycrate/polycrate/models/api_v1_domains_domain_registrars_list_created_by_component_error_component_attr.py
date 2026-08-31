from typing import Literal

ApiV1DomainsDomainRegistrarsListCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsListCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_domains_domain_registrars_list_created_by_component_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsListCreatedByComponentErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
