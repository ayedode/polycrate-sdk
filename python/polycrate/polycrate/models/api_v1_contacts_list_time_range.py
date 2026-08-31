from typing import Literal

ApiV1ContactsListTimeRange = Literal["12h", "1h", "24h", "30d", "6h", "7d", "90d"]

API_V1_CONTACTS_LIST_TIME_RANGE_VALUES: set[ApiV1ContactsListTimeRange] = {
    "12h",
    "1h",
    "24h",
    "30d",
    "6h",
    "7d",
    "90d",
}


def check_api_v1_contacts_list_time_range(value: str) -> ApiV1ContactsListTimeRange:
    if value in API_V1_CONTACTS_LIST_TIME_RANGE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_LIST_TIME_RANGE_VALUES!r}")
