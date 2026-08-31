from typing import Literal

ApiV1ScmRepositoriesListTimeRangeErrorComponentCode = Literal["invalid_choice"]

API_V1_SCM_REPOSITORIES_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesListTimeRangeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_scm_repositories_list_time_range_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesListTimeRangeErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
