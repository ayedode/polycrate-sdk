from typing import Literal

ApiV1DomainsDomainsPartialUpdateNameserversErrorComponentAttr = Literal["nameservers"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_NAMESERVERS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateNameserversErrorComponentAttr
] = {
    "nameservers",
}


def check_api_v1_domains_domains_partial_update_nameservers_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateNameserversErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_NAMESERVERS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_NAMESERVERS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
