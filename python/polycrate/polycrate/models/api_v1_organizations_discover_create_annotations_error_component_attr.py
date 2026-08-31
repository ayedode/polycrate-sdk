from typing import Literal

ApiV1OrganizationsDiscoverCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_organizations_discover_create_annotations_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateAnnotationsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
