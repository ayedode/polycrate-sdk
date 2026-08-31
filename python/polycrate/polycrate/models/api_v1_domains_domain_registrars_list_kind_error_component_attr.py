from typing import Literal

ApiV1DomainsDomainRegistrarsListKindErrorComponentAttr = Literal["kind"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_domains_domain_registrars_list_kind_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsListKindErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
