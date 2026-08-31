from typing import Literal

ApiV1WorkspacesCheckCreatePurposeErrorComponentAttr = Literal["purpose"]

API_V1_WORKSPACES_CHECK_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreatePurposeErrorComponentAttr
] = {
    "purpose",
}


def check_api_v1_workspaces_check_create_purpose_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreatePurposeErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
