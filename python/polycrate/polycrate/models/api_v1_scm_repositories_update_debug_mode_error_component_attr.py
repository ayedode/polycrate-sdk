from typing import Literal

ApiV1ScmRepositoriesUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_SCM_REPOSITORIES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesUpdateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_scm_repositories_update_debug_mode_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesUpdateDebugModeErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
