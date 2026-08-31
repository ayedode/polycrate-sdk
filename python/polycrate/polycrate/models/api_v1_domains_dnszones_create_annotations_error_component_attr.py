from typing import Literal

ApiV1DomainsDnszonesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DOMAINS_DNSZONES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_domains_dnszones_create_annotations_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
