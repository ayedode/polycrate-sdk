from typing import Literal

ApiV1ScmRepositoriesArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_scm_repositories_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
