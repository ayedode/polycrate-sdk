from typing import Literal

ApiV1DomainsDomainsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DOMAINS_DOMAINS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_domains_domains_create_annotations_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
