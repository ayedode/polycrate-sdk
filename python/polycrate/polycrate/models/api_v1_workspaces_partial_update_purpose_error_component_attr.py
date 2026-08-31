from typing import Literal

ApiV1WorkspacesPartialUpdatePurposeErrorComponentAttr = Literal["purpose"]

API_V1_WORKSPACES_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesPartialUpdatePurposeErrorComponentAttr
] = {
    "purpose",
}


def check_api_v1_workspaces_partial_update_purpose_error_component_attr(
    value: str,
) -> ApiV1WorkspacesPartialUpdatePurposeErrorComponentAttr:
    if value in API_V1_WORKSPACES_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
