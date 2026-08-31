from typing import Literal

ApiV1ScmRepositoriesCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_SCM_REPOSITORIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_scm_repositories_create_annotations_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesCreateAnnotationsErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
