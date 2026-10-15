from typing import Literal

ProviderDetailRequestDedicatedAvailable = Literal["", "no", "planned", "yes"]

PROVIDER_DETAIL_REQUEST_DEDICATED_AVAILABLE_VALUES: set[ProviderDetailRequestDedicatedAvailable] = {
    "",
    "no",
    "planned",
    "yes",
}


def check_provider_detail_request_dedicated_available(value: str) -> ProviderDetailRequestDedicatedAvailable:
    if value in PROVIDER_DETAIL_REQUEST_DEDICATED_AVAILABLE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_DEDICATED_AVAILABLE_VALUES!r}"
    )
