from typing import Literal

ApiV1DomainsDnsrecordsCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_DOMAINS_DNSRECORDS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_domains_dnsrecords_create_labels_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsCreateLabelsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
