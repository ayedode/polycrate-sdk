from typing import Literal

ApiV1OrganizationsDiscoverCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_organizations_discover_create_labels_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateLabelsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
