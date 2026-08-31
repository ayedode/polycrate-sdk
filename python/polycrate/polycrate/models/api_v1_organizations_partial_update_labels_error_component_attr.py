from typing import Literal

ApiV1OrganizationsPartialUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_organizations_partial_update_labels_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateLabelsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
