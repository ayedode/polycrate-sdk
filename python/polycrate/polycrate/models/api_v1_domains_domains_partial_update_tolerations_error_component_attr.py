from typing import Literal

ApiV1DomainsDomainsPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_domains_domains_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
