from typing import Literal

ApiV1DomainsDomainsPartialUpdateNameserversErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_NAMESERVERS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateNameserversErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_domains_partial_update_nameservers_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateNameserversErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_NAMESERVERS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_NAMESERVERS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
