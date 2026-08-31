from typing import Literal

ApiV1OrganizationsUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ORGANIZATIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_organizations_update_annotations_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateAnnotationsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
