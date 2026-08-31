from typing import Literal

ApiV1DomainsDomainsCreateRenewalModeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOMAINS_DOMAINS_CREATE_RENEWAL_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsCreateRenewalModeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_domains_domains_create_renewal_mode_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsCreateRenewalModeErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_RENEWAL_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_RENEWAL_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
