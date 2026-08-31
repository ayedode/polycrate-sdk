from typing import Literal

ApiV1DomainsDomainsListNameExactErrorComponentAttr = Literal["name_exact"]

API_V1_DOMAINS_DOMAINS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsListNameExactErrorComponentAttr
] = {
    "name_exact",
}


def check_api_v1_domains_domains_list_name_exact_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsListNameExactErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
