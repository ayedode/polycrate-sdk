from typing import Literal

ApiV1DomainsDomainsUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_DOMAINS_DOMAINS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_domains_domains_update_criticality_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsUpdateCriticalityErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
