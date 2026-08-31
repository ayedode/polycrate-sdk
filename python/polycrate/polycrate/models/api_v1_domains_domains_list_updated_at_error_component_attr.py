from typing import Literal

ApiV1DomainsDomainsListUpdatedAtErrorComponentAttr = Literal["updated_at"]

API_V1_DOMAINS_DOMAINS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsListUpdatedAtErrorComponentAttr
] = {
    "updated_at",
}


def check_api_v1_domains_domains_list_updated_at_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsListUpdatedAtErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
