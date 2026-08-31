from typing import Literal

ApiV1DomainsDomainsUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOMAINS_DOMAINS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DomainsDomainsUpdateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_domains_domains_update_kind_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsUpdateKindErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
