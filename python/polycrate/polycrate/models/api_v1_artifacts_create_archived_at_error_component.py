from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_v1_artifacts_create_archived_at_error_component_attr import (
    ApiV1ArtifactsCreateArchivedAtErrorComponentAttr,
    check_api_v1_artifacts_create_archived_at_error_component_attr,
)
from ..models.api_v1_artifacts_create_archived_at_error_component_code import (
    ApiV1ArtifactsCreateArchivedAtErrorComponentCode,
    check_api_v1_artifacts_create_archived_at_error_component_code,
)

T = TypeVar("T", bound="ApiV1ArtifactsCreateArchivedAtErrorComponent")


@_attrs_define
class ApiV1ArtifactsCreateArchivedAtErrorComponent:
    """
    Attributes:
        attr (ApiV1ArtifactsCreateArchivedAtErrorComponentAttr): * `archived_at` - archived_at
        code (ApiV1ArtifactsCreateArchivedAtErrorComponentCode): * `date` - date
            * `invalid` - invalid
            * `make_aware` - make_aware
            * `overflow` - overflow
        detail (str):
    """

    attr: ApiV1ArtifactsCreateArchivedAtErrorComponentAttr
    code: ApiV1ArtifactsCreateArchivedAtErrorComponentCode
    detail: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attr: str = self.attr

        code: str = self.code

        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attr": attr,
                "code": code,
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attr = check_api_v1_artifacts_create_archived_at_error_component_attr(d.pop("attr"))

        code = check_api_v1_artifacts_create_archived_at_error_component_code(d.pop("code"))

        detail = d.pop("detail")

        api_v1_artifacts_create_archived_at_error_component = cls(
            attr=attr,
            code=code,
            detail=detail,
        )

        api_v1_artifacts_create_archived_at_error_component.additional_properties = d
        return api_v1_artifacts_create_archived_at_error_component

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
