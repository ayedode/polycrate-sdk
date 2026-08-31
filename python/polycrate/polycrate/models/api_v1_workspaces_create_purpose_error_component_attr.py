from typing import Literal

ApiV1WorkspacesCreatePurposeErrorComponentAttr = Literal["purpose"]

API_V1_WORKSPACES_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1WorkspacesCreatePurposeErrorComponentAttr] = {
    "purpose",
}


def check_api_v1_workspaces_create_purpose_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCreatePurposeErrorComponentAttr:
    if value in API_V1_WORKSPACES_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
