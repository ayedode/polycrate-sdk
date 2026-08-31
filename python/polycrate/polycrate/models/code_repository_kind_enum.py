from typing import Literal

CodeRepositoryKindEnum = Literal["forgejo", "generic", "gitea", "gitlab"]

CODE_REPOSITORY_KIND_ENUM_VALUES: set[CodeRepositoryKindEnum] = {
    "forgejo",
    "generic",
    "gitea",
    "gitlab",
}


def check_code_repository_kind_enum(value: str) -> CodeRepositoryKindEnum:
    if value in CODE_REPOSITORY_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CODE_REPOSITORY_KIND_ENUM_VALUES!r}")
