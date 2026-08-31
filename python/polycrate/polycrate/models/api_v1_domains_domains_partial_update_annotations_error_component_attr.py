from typing import Literal

ApiV1DomainsDomainsPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_domains_domains_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
