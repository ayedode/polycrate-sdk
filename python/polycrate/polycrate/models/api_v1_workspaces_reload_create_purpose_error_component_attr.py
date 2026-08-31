from typing import Literal

ApiV1WorkspacesReloadCreatePurposeErrorComponentAttr = Literal["purpose"]

API_V1_WORKSPACES_RELOAD_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReloadCreatePurposeErrorComponentAttr
] = {
    "purpose",
}


def check_api_v1_workspaces_reload_create_purpose_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReloadCreatePurposeErrorComponentAttr:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
