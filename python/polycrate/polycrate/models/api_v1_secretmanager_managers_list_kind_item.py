from typing import Literal

ApiV1SecretmanagerManagersListKindItem = Literal["vault"]

API_V1_SECRETMANAGER_MANAGERS_LIST_KIND_ITEM_VALUES: set[ApiV1SecretmanagerManagersListKindItem] = {
    "vault",
}


def check_api_v1_secretmanager_managers_list_kind_item(value: str) -> ApiV1SecretmanagerManagersListKindItem:
    if value in API_V1_SECRETMANAGER_MANAGERS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_LIST_KIND_ITEM_VALUES!r}"
    )
