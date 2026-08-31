from typing import Literal

ApiV1OrganizationsDiscoverCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsDiscoverCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_organizations_discover_create_annotations_error_component_code(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateAnnotationsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
