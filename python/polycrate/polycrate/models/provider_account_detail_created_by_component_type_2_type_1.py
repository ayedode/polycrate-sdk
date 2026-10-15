from typing import Literal

ProviderAccountDetailCreatedByComponentType2Type1 = Literal["", "api", "cli", "operator"]

PROVIDER_ACCOUNT_DETAIL_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES: set[
    ProviderAccountDetailCreatedByComponentType2Type1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_provider_account_detail_created_by_component_type_2_type_1(
    value: str,
) -> ProviderAccountDetailCreatedByComponentType2Type1:
    if value in PROVIDER_ACCOUNT_DETAIL_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROVIDER_ACCOUNT_DETAIL_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES!r}"
    )
