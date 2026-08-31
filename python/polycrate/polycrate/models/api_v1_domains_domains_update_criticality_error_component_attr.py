from typing import Literal

ApiV1DomainsDomainsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_DOMAINS_DOMAINS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_domains_domains_update_criticality_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
