from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="S3RegionList")


@_attrs_define
class S3RegionList:
    """
    Attributes:
        id (UUID): workspaces.Region UUID — pass this as `region` in POST /api/v1/s3/buckets/.
        region (None | str):
        endpoint (str): $HOSTNAME (without protocol://)
        name (str):
        display_name (None | str):
        url (None | str):
    """

    id: UUID
    region: None | str
    endpoint: str
    name: str
    display_name: None | str
    url: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        region: None | str
        region = self.region

        endpoint = self.endpoint

        name = self.name

        display_name: None | str
        display_name = self.display_name

        url: None | str
        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "region": region,
                "endpoint": endpoint,
                "name": name,
                "display_name": display_name,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_region(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        region = _parse_region(d.pop("region"))

        endpoint = d.pop("endpoint")

        name = d.pop("name")

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("display_name"))

        def _parse_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url = _parse_url(d.pop("url"))

        s3_region_list = cls(
            id=id,
            region=region,
            endpoint=endpoint,
            name=name,
            display_name=display_name,
            url=url,
        )

        s3_region_list.additional_properties = d
        return s3_region_list

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
