from typing import Literal

ApiV1ArtifactsListAppVersionErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_ARTIFACTS_LIST_APP_VERSION_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ArtifactsListAppVersionErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_artifacts_list_app_version_error_component_code(
    value: str,
) -> ApiV1ArtifactsListAppVersionErrorComponentCode:
    if value in API_V1_ARTIFACTS_LIST_APP_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_LIST_APP_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
