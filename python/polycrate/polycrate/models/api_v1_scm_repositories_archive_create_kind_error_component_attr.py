from typing import Literal

ApiV1ScmRepositoriesArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_scm_repositories_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreateKindErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
