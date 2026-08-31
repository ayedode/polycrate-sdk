from typing import Literal

ApiV1OrganizationsListKindItem = Literal["generic"]

API_V1_ORGANIZATIONS_LIST_KIND_ITEM_VALUES: set[ApiV1OrganizationsListKindItem] = {
    "generic",
}


def check_api_v1_organizations_list_kind_item(value: str) -> ApiV1OrganizationsListKindItem:
    if value in API_V1_ORGANIZATIONS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_LIST_KIND_ITEM_VALUES!r}")
