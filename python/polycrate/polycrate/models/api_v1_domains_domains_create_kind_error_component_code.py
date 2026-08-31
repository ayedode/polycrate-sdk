from typing import Literal

ApiV1DomainsDomainsCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOMAINS_DOMAINS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DomainsDomainsCreateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_domains_domains_create_kind_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsCreateKindErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
