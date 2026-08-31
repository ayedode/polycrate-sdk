from typing import Literal

ApiV1DomainsDnsrecordsListCreatedAtErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DNSRECORDS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsListCreatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_dnsrecords_list_created_at_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsListCreatedAtErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
