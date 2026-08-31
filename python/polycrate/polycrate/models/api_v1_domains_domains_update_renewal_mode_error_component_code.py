from typing import Literal

ApiV1DomainsDomainsUpdateRenewalModeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOMAINS_DOMAINS_UPDATE_RENEWAL_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsUpdateRenewalModeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_domains_domains_update_renewal_mode_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsUpdateRenewalModeErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_RENEWAL_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_RENEWAL_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
