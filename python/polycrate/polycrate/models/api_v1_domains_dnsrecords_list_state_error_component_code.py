from typing import Literal

ApiV1DomainsDnsrecordsListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_DOMAINS_DNSRECORDS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsListStateErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_domains_dnsrecords_list_state_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsListStateErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
