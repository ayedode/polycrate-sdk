from typing import Literal

ApiV1PrefixesListCreatedByUsersErrorComponentAttr = Literal["created_by_users"]

API_V1_PREFIXES_LIST_CREATED_BY_USERS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesListCreatedByUsersErrorComponentAttr
] = {
    "created_by_users",
}


def check_api_v1_prefixes_list_created_by_users_error_component_attr(
    value: str,
) -> ApiV1PrefixesListCreatedByUsersErrorComponentAttr:
    if value in API_V1_PREFIXES_LIST_CREATED_BY_USERS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_LIST_CREATED_BY_USERS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
