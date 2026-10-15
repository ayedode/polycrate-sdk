from typing import Literal

ProviderDetailRequestCloudInit = Literal["", "no", "planned", "yes"]

PROVIDER_DETAIL_REQUEST_CLOUD_INIT_VALUES: set[ProviderDetailRequestCloudInit] = {
    "",
    "no",
    "planned",
    "yes",
}


def check_provider_detail_request_cloud_init(value: str) -> ProviderDetailRequestCloudInit:
    if value in PROVIDER_DETAIL_REQUEST_CLOUD_INIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_CLOUD_INIT_VALUES!r}")
