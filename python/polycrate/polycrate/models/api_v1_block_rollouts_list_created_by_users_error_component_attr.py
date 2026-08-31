from typing import Literal

ApiV1BlockRolloutsListCreatedByUsersErrorComponentAttr = Literal["created_by_users"]

API_V1_BLOCK_ROLLOUTS_LIST_CREATED_BY_USERS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsListCreatedByUsersErrorComponentAttr
] = {
    "created_by_users",
}


def check_api_v1_block_rollouts_list_created_by_users_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsListCreatedByUsersErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_LIST_CREATED_BY_USERS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_LIST_CREATED_BY_USERS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
