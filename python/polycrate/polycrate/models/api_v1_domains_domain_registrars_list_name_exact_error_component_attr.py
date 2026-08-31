from typing import Literal

ApiV1DomainsDomainRegistrarsListNameExactErrorComponentAttr = Literal["name_exact"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsListNameExactErrorComponentAttr
] = {
    "name_exact",
}


def check_api_v1_domains_domain_registrars_list_name_exact_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsListNameExactErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
