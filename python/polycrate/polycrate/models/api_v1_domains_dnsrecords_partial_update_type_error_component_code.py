from typing import Literal

ApiV1DomainsDnsrecordsPartialUpdateTypeErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsPartialUpdateTypeErrorComponentCode
] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_domains_dnsrecords_partial_update_type_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsPartialUpdateTypeErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
