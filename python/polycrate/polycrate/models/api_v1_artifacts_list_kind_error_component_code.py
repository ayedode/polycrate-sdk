from typing import Literal

ApiV1ArtifactsListKindErrorComponentCode = Literal["invalid_choice"]

API_V1_ARTIFACTS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ArtifactsListKindErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_artifacts_list_kind_error_component_code(value: str) -> ApiV1ArtifactsListKindErrorComponentCode:
    if value in API_V1_ARTIFACTS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
