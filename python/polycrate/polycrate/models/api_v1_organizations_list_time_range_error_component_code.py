from typing import Literal

ApiV1OrganizationsListTimeRangeErrorComponentCode = Literal["invalid_choice"]

API_V1_ORGANIZATIONS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsListTimeRangeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_organizations_list_time_range_error_component_code(
    value: str,
) -> ApiV1OrganizationsListTimeRangeErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
