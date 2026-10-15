from typing import Literal

ProviderAccountDetailRequestCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

PROVIDER_ACCOUNT_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[
    ProviderAccountDetailRequestCreatedByComponentType1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_provider_account_detail_request_created_by_component_type_1(
    value: str,
) -> ProviderAccountDetailRequestCreatedByComponentType1:
    if value in PROVIDER_ACCOUNT_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROVIDER_ACCOUNT_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
