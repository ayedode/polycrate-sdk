from typing import Literal

ApiV1DomainsDnsrecordsListCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_DOMAINS_DNSRECORDS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsListCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_domains_dnsrecords_list_created_by_component_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsListCreatedByComponentErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
