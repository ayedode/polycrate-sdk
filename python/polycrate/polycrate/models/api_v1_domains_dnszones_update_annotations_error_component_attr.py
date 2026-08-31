from typing import Literal

ApiV1DomainsDnszonesUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DOMAINS_DNSZONES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_domains_dnszones_update_annotations_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
