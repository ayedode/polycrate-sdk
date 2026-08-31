from typing import Literal

ApiV1DomainsDomainRegistrarsListCreatedAtErrorComponentAttr = Literal["created_at"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsListCreatedAtErrorComponentAttr
] = {
    "created_at",
}


def check_api_v1_domains_domain_registrars_list_created_at_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsListCreatedAtErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
