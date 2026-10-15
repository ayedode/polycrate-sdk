from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lbi_v2_route_match_request_headers import LbiV2RouteMatchRequestHeaders


T = TypeVar("T", bound="LbiV2RouteMatchRequest")


@_attrs_define
class LbiV2RouteMatchRequest:
    """
    Attributes:
        hostnames (list[str] | Unset):
        path (None | str | Unset):
        headers (LbiV2RouteMatchRequestHeaders | Unset):
    """

    hostnames: list[str] | Unset = UNSET
    path: None | str | Unset = UNSET
    headers: LbiV2RouteMatchRequestHeaders | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostnames: list[str] | Unset = UNSET
        if not isinstance(self.hostnames, Unset):
            hostnames = self.hostnames

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hostnames is not UNSET:
            field_dict["hostnames"] = hostnames
        if path is not UNSET:
            field_dict["path"] = path
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lbi_v2_route_match_request_headers import LbiV2RouteMatchRequestHeaders  # noqa: PLC0415

        d = dict(src_dict)
        hostnames = cast(list[str], d.pop("hostnames", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        _headers = d.pop("headers", UNSET)
        headers: LbiV2RouteMatchRequestHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = LbiV2RouteMatchRequestHeaders.from_dict(_headers)

        lbi_v2_route_match_request = cls(
            hostnames=hostnames,
            path=path,
            headers=headers,
        )

        lbi_v2_route_match_request.additional_properties = d
        return lbi_v2_route_match_request

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
