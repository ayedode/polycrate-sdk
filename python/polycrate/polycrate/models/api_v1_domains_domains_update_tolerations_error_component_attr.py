from typing import Literal

ApiV1DomainsDomainsUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_DOMAINS_DOMAINS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_domains_domains_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsUpdateTolerationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
