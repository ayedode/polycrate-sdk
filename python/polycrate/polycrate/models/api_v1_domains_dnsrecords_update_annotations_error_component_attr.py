from typing import Literal

ApiV1DomainsDnsrecordsUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DOMAINS_DNSRECORDS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_domains_dnsrecords_update_annotations_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
