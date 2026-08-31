from typing import Literal

ApiV1DomainsDnsrecordsArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_DOMAINS_DNSRECORDS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_domains_dnsrecords_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
