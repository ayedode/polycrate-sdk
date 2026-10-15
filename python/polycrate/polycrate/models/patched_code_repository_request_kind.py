from typing import Literal

PatchedCodeRepositoryRequestKind = Literal["forgejo", "generic", "gitea", "gitlab"]

PATCHED_CODE_REPOSITORY_REQUEST_KIND_VALUES: set[PatchedCodeRepositoryRequestKind] = {
    "forgejo",
    "generic",
    "gitea",
    "gitlab",
}


def check_patched_code_repository_request_kind(value: str) -> PatchedCodeRepositoryRequestKind:
    if value in PATCHED_CODE_REPOSITORY_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_CODE_REPOSITORY_REQUEST_KIND_VALUES!r}")
