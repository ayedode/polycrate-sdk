from typing import Literal

ApiV1ScmRepositoriesCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_SCM_REPOSITORIES_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_scm_repositories_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesCreateDebugModeErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
