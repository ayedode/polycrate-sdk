from typing import Literal

ApiV1OrganizationsChoicesListKindItem = Literal["generic"]

API_V1_ORGANIZATIONS_CHOICES_LIST_KIND_ITEM_VALUES: set[ApiV1OrganizationsChoicesListKindItem] = {
    "generic",
}


def check_api_v1_organizations_choices_list_kind_item(value: str) -> ApiV1OrganizationsChoicesListKindItem:
    if value in API_V1_ORGANIZATIONS_CHOICES_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CHOICES_LIST_KIND_ITEM_VALUES!r}"
    )
