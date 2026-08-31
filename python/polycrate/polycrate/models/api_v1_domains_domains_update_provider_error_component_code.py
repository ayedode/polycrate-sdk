from typing import Literal

ApiV1DomainsDomainsUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOMAINS_DOMAINS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_domains_domains_update_provider_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsUpdateProviderErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
