from typing import Literal

ApiV1WorkspacesReloadCreateOnPremiseErrorComponentAttr = Literal["on_premise"]

API_V1_WORKSPACES_RELOAD_CREATE_ON_PREMISE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReloadCreateOnPremiseErrorComponentAttr
] = {
    "on_premise",
}


def check_api_v1_workspaces_reload_create_on_premise_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReloadCreateOnPremiseErrorComponentAttr:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_ON_PREMISE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_ON_PREMISE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
