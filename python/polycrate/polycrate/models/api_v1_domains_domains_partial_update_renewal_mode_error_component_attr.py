from typing import Literal

ApiV1DomainsDomainsPartialUpdateRenewalModeErrorComponentAttr = Literal["renewal_mode"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_RENEWAL_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateRenewalModeErrorComponentAttr
] = {
    "renewal_mode",
}


def check_api_v1_domains_domains_partial_update_renewal_mode_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateRenewalModeErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_RENEWAL_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_RENEWAL_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
