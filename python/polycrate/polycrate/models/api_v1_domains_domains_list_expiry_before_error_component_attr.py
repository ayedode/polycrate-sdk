from typing import Literal

ApiV1DomainsDomainsListExpiryBeforeErrorComponentAttr = Literal["expiry_before"]

API_V1_DOMAINS_DOMAINS_LIST_EXPIRY_BEFORE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsListExpiryBeforeErrorComponentAttr
] = {
    "expiry_before",
}


def check_api_v1_domains_domains_list_expiry_before_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsListExpiryBeforeErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_LIST_EXPIRY_BEFORE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_LIST_EXPIRY_BEFORE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
