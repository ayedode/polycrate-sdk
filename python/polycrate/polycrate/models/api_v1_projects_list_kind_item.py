from typing import Literal

ApiV1ProjectsListKindItem = Literal["offboarding", "onboarding", "ongoing"]

API_V1_PROJECTS_LIST_KIND_ITEM_VALUES: set[ApiV1ProjectsListKindItem] = {
    "offboarding",
    "onboarding",
    "ongoing",
}


def check_api_v1_projects_list_kind_item(value: str) -> ApiV1ProjectsListKindItem:
    if value in API_V1_PROJECTS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_LIST_KIND_ITEM_VALUES!r}")
