from typing import Literal

ApiV1DomainsDnszonesPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_domains_dnszones_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
