from typing import Literal

ApiV1DomainsDomainsListStateErrorComponentAttr = Literal["state"]

API_V1_DOMAINS_DOMAINS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DomainsDomainsListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_domains_domains_list_state_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsListStateErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
