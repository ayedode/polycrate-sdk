from typing import Literal

ApiV1WorkspacesCheckCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_WORKSPACES_CHECK_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_workspaces_check_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreateSloTargetErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
