from typing import Literal

ApiV1DomainsDnsrecordsCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DNSRECORDS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_dnsrecords_create_labels_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsCreateLabelsErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
