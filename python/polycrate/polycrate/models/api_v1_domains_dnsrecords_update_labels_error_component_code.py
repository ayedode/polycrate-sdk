from typing import Literal

ApiV1DomainsDnsrecordsUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DNSRECORDS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_dnsrecords_update_labels_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsUpdateLabelsErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
