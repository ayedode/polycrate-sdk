from typing import Literal

ApiV1ScmRepositoriesUpdateGroupsCountErrorComponentAttr = Literal["groups_count"]

API_V1_SCM_REPOSITORIES_UPDATE_GROUPS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesUpdateGroupsCountErrorComponentAttr
] = {
    "groups_count",
}


def check_api_v1_scm_repositories_update_groups_count_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesUpdateGroupsCountErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_UPDATE_GROUPS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_UPDATE_GROUPS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
