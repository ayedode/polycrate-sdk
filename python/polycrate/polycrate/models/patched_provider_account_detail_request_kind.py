from typing import Literal

PatchedProviderAccountDetailRequestKind = Literal["generic"]

PATCHED_PROVIDER_ACCOUNT_DETAIL_REQUEST_KIND_VALUES: set[PatchedProviderAccountDetailRequestKind] = {
    "generic",
}


def check_patched_provider_account_detail_request_kind(value: str) -> PatchedProviderAccountDetailRequestKind:
    if value in PATCHED_PROVIDER_ACCOUNT_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_ACCOUNT_DETAIL_REQUEST_KIND_VALUES!r}"
    )
