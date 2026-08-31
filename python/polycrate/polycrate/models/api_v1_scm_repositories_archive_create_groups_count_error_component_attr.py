from typing import Literal

ApiV1ScmRepositoriesArchiveCreateGroupsCountErrorComponentAttr = Literal["groups_count"]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_GROUPS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreateGroupsCountErrorComponentAttr
] = {
    "groups_count",
}


def check_api_v1_scm_repositories_archive_create_groups_count_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreateGroupsCountErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_GROUPS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_GROUPS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
