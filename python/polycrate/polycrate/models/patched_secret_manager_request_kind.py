from typing import Literal

PatchedSecretManagerRequestKind = Literal["vault"]

PATCHED_SECRET_MANAGER_REQUEST_KIND_VALUES: set[PatchedSecretManagerRequestKind] = {
    "vault",
}


def check_patched_secret_manager_request_kind(value: str) -> PatchedSecretManagerRequestKind:
    if value in PATCHED_SECRET_MANAGER_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_SECRET_MANAGER_REQUEST_KIND_VALUES!r}")
