from typing import Literal

ApiV1ScmRepositoriesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_SCM_REPOSITORIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_scm_repositories_create_annotations_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
