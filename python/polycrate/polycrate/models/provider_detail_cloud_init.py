from typing import Literal

ProviderDetailCloudInit = Literal["", "no", "planned", "yes"]

PROVIDER_DETAIL_CLOUD_INIT_VALUES: set[ProviderDetailCloudInit] = {
    "",
    "no",
    "planned",
    "yes",
}


def check_provider_detail_cloud_init(value: str) -> ProviderDetailCloudInit:
    if value in PROVIDER_DETAIL_CLOUD_INIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_CLOUD_INIT_VALUES!r}")
