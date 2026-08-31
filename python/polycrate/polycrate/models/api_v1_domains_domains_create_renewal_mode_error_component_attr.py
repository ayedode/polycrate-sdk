from typing import Literal

ApiV1DomainsDomainsCreateRenewalModeErrorComponentAttr = Literal["renewal_mode"]

API_V1_DOMAINS_DOMAINS_CREATE_RENEWAL_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsCreateRenewalModeErrorComponentAttr
] = {
    "renewal_mode",
}


def check_api_v1_domains_domains_create_renewal_mode_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsCreateRenewalModeErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_RENEWAL_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_RENEWAL_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
