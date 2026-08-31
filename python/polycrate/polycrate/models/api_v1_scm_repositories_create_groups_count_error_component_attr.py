from typing import Literal

ApiV1ScmRepositoriesCreateGroupsCountErrorComponentAttr = Literal["groups_count"]

API_V1_SCM_REPOSITORIES_CREATE_GROUPS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesCreateGroupsCountErrorComponentAttr
] = {
    "groups_count",
}


def check_api_v1_scm_repositories_create_groups_count_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesCreateGroupsCountErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_CREATE_GROUPS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_CREATE_GROUPS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
