from typing import Literal

ApiV1OrganizationsDiscoverCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsDiscoverCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_organizations_discover_create_labels_error_component_code(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateLabelsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
