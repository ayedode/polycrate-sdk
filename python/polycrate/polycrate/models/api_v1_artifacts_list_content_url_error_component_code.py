from typing import Literal

ApiV1ArtifactsListContentUrlErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_ARTIFACTS_LIST_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ArtifactsListContentUrlErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_artifacts_list_content_url_error_component_code(
    value: str,
) -> ApiV1ArtifactsListContentUrlErrorComponentCode:
    if value in API_V1_ARTIFACTS_LIST_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_LIST_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
