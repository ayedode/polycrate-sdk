from typing import Literal

ApiV1DomainsDomainRegistrarsListNameErrorComponentAttr = Literal["name"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsListNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_domains_domain_registrars_list_name_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsListNameErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
