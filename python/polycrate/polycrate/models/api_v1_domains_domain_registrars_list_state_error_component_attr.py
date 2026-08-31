from typing import Literal

ApiV1DomainsDomainRegistrarsListStateErrorComponentAttr = Literal["state"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_domains_domain_registrars_list_state_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsListStateErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
