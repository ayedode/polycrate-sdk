from typing import Literal

ApiV1IncidentsListKindItem = Literal[
    "account-compromise",
    "availability",
    "data-breach",
    "data-leak",
    "integrity",
    "malware",
    "network-attack",
    "other",
    "phishing",
    "physical",
    "policy-violation",
    "security-control",
    "supply-chain",
    "unauthorized-access",
    "upstream-provider",
]

API_V1_INCIDENTS_LIST_KIND_ITEM_VALUES: set[ApiV1IncidentsListKindItem] = {
    "account-compromise",
    "availability",
    "data-breach",
    "data-leak",
    "integrity",
    "malware",
    "network-attack",
    "other",
    "phishing",
    "physical",
    "policy-violation",
    "security-control",
    "supply-chain",
    "unauthorized-access",
    "upstream-provider",
}


def check_api_v1_incidents_list_kind_item(value: str) -> ApiV1IncidentsListKindItem:
    if value in API_V1_INCIDENTS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_LIST_KIND_ITEM_VALUES!r}")
