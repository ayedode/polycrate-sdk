from typing import Literal

ApiV1DomainsDomainsListRegistrarErrorComponentAttr = Literal["registrar"]

API_V1_DOMAINS_DOMAINS_LIST_REGISTRAR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsListRegistrarErrorComponentAttr
] = {
    "registrar",
}


def check_api_v1_domains_domains_list_registrar_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsListRegistrarErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_LIST_REGISTRAR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_LIST_REGISTRAR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
