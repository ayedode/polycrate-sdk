from typing import Literal

ApiV1ScmRepositoriesArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_scm_repositories_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
