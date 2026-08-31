from typing import Literal

ApiV1OrganizationsUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ORGANIZATIONS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_organizations_update_labels_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateLabelsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
