from typing import Literal

ApiV1DomainsDnsrecordsUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DNSRECORDS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_dnsrecords_update_annotations_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsUpdateAnnotationsErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
